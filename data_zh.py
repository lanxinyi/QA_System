# -*- coding: utf-8 -*-
from data import *
import jieba

def Seg_Chinese_In_Sentence(data_line):
    if not data_line:
        return None

    line = data_line.strip()
    line = line.replace(' ', '')
    line = line.replace('\t', '')
    seg_list = jieba.cut(line, cut_all=False)
    sentence = " ".join(seg_list)
    return sentence


def Seg_Chinese_In_File(data_file):
    IO_Date.file_exit(data_file)
    outputfile = IO_Date.get_temp_file_name() + "_seg.txt"
    with open(data_file, 'r', encoding='utf-8') as in_f:
        with open(outputfile, 'w', encoding='utf-8') as out_f:
            cnt = 0
            while True:
                line = in_f.readline()
                if not line:
                    break
                line = line.strip()
                line = line.replace(' ', '')
                line = line.replace('\t', '')
                seg_list = jieba.cut(line, cut_all=False)
                sentence = " ".join(seg_list)
                out_f.write(sentence + '\n')
                cnt += 1
                if cnt % 100000 == 0:
                    print("processed %d lines" % cnt)
