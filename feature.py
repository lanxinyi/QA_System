# -*- coding: utf-8 -*-
from data_zh import *
import math

class Basic_Feature(object):
    def __init__(self):
        self.desc = ""

    def set_desc(self, desc, o):
        self.desc = "%s - %s" % (desc, o.__class__)
        print(self.desc)

    def printme(self):
        print(self.desc)

    def sim(self, q, r):
        raise NotImplementedError


class IF_IDF(Basic_Feature):
    def __init__(self, document_file):
        super(self.__class__, self).__init__()
        self.set_desc("tf-idf", self)
        self.word_idf_list = self.word_idf(document_file)

    def word_idf(self, document_file):
        IO_Date.file_exist(document_file)
        word_idf_list = {}
        length = 0.0
        with open(document_file, 'r', encoding='utf-8') as i_file:
            while True:
                sentence = i_file.readline()
                if not sentence:
                    break
                length += 1
                seg_sen = Seg_Chinese_In_Sentence(sentence.strip())
                word_list = seg_sen.split(' ')
                word_list = list(set(word_list))
                for word in word_list:
                    if word in word_idf_list:
                        word_idf_list[word] += 1
                    else:
                        word_idf_list[word] = 1

        for k in word_idf_list:
            #print(length, k, word_idf_list[k])
            word_idf_list[k] = math.log(length / word_idf_list[k])

        #print(word_idf_list)
        return word_idf_list

    def sim(self, q, r):
        q_seg = Seg_Chinese_In_Sentence(q.strip())
        r_seg = Seg_Chinese_In_Sentence(r.strip())

        q_word_list = q_seg.split(' ')
        r_word_list = r_seg.split(' ')
        r_length = len(r_word_list)
        score = 0.0
        r_word_req = {}
        for r_word in r_word_list:
            if r_word in r_word_req:
                r_word_req[r_word] += 1
            else:
                r_word_req[r_word] = 1

        for q_word in q_word_list:
            if not q_word in r_word_req:
                continue
            else:
                score += float(r_word_req[q_word]) / r_length * self.word_idf_list[q_word]
                #print(float(r_word_req[q_word]), r_length, self.word_idf_list[q_word])

        return score


class Overlap(Basic_Feature):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.set_desc("Overlap", self)

    def sim(self, q, r):
        q_seg = Seg_Chinese_In_Sentence(q.strip())
        r_seg = Seg_Chinese_In_Sentence(r.strip())

        q_word_list = q_seg.split(' ')
        r_word_list = r_seg.split(' ')
        q_word_set = set(q_word_list)
        r_word_set = set(r_word_list)

        if not q_word_set and not r_word_set:
            return 0.0

        score = float(len(q_word_set & r_word_set)) / len(q_word_set | r_word_set)
        return score


class BM25(Basic_Feature):
    def __init__(self, document_file):
        super(self.__class__, self).__init__()
        self.set_desc("BM25", self)
        self.weight_Rel_word_doc, self.avg_doc_length = self.Weight_Relation_word_document(document_file)
        self.k1 = 2.0
        self.b = 0.75

    def Weight_Relation_word_document(self, document_file):
        IO_Date.file_exist(document_file)
        Weight_Rel_word_doc = {}
        doc_length = 0.0
        avg_doc_length = 0.0
        with open(document_file, 'r', encoding='utf-8') as i_file:
            while True:
                sentence = i_file.readline()
                if not sentence:
                    break
                doc_length += 1
                seg_sen = Seg_Chinese_In_Sentence(sentence.strip())
                word_list = seg_sen.split(' ')
                avg_doc_length += len(word_list)
                word_list = list(set(word_list))
                for word in word_list:
                    if word in Weight_Rel_word_doc:
                        Weight_Rel_word_doc[word] += 1
                    else:
                        Weight_Rel_word_doc[word] = 1

        for k in Weight_Rel_word_doc:
            if doc_length - Weight_Rel_word_doc[k] < Weight_Rel_word_doc[k]:
                Weight_Rel_word_doc[k] = math.log((doc_length + 0.5) / (Weight_Rel_word_doc[k] + 0.5))
            else:
                Weight_Rel_word_doc[k] = math.log((doc_length - Weight_Rel_word_doc[k] + 0.5) / (Weight_Rel_word_doc[k] + 0.5))

        avg_doc_length /= doc_length

        return Weight_Rel_word_doc, avg_doc_length

    def sim(self, q, r):
        q_seg = Seg_Chinese_In_Sentence(q.strip())
        r_seg = Seg_Chinese_In_Sentence(r.strip())

        q_word_list = q_seg.split(' ')
        r_word_list = r_seg.split(' ')
        r_length = len(r_word_list)
        K_val = self.k1 * (1 - self.b + self.b * (r_length / self.avg_doc_length))

        score = 0.0
        r_word_req = {}
        for r_word in r_word_list:
            if r_word in r_word_req:
                r_word_req[r_word] += 1
            else:
                r_word_req[r_word] = 1

        for q_word in q_word_list:
            if not q_word in r_word_req:
                continue
            else:
                score += r_word_req[q_word] * (self.k1 + 1) / (r_word_req[q_word] + K_val) \
                         * self.weight_Rel_word_doc[q_word]

        return score


class LM(Basic_Feature):
    def __init__(self, document_file):
        super(self.__class__, self).__init__()
        self.set_desc("LM", self)
        self.lamda = 0.5
        self.word_freq_in_doc = self.Word_Freq_In_Doc(document_file)

    def Word_Freq_In_Doc(self, document_file):
        IO_Date.file_exist(document_file)
        word_freq_in_doc = {}
        total_word_num = 0.0
        with open(document_file, 'r', encoding='utf-8') as i_file:
            while True:
                sentence = i_file.readline()
                if not sentence:
                    break
                seg_sen = Seg_Chinese_In_Sentence(sentence.strip())
                word_list = seg_sen.split(' ')
                total_word_num += len(word_list)
                for word in word_list:
                    if word in word_freq_in_doc:
                        word_freq_in_doc[word] += 1
                    else:
                        word_freq_in_doc[word] = 1

        for k in word_freq_in_doc:
            word_freq_in_doc[k] = word_freq_in_doc[k] / total_word_num

        return word_freq_in_doc

    def sim(self, q, r):
        q_seg = Seg_Chinese_In_Sentence(q.strip())
        r_seg = Seg_Chinese_In_Sentence(r.strip())

        q_word_list = q_seg.split(' ')
        r_word_list = r_seg.split(' ')
        r_length = len(r_word_list)

        score = 1.0
        r_word_req = {}
        for r_word in r_word_list:
            if r_word in r_word_req:
                r_word_req[r_word] += 1
            else:
                r_word_req[r_word] = 1

        for q_word in q_word_list:
            if not q_word in r_word_req:
                continue
            else:
                score *= (1.0 - self.lamda) * r_word_req[q_word] / r_length + self.lamda * self.word_freq_in_doc[q_word]

        return score





