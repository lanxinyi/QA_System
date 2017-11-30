import gensim
from data_zh import *
from tool import *

class AveragCosineSimilarity():
    def __init__(self, modelfile):
        IO_Date.file_exist(modelfile)
        self.model = gensim.models.Word2Vec.load(modelfile)



    def sim(self, q, r):
        q_seg = Seg_Chinese_In_Sentence(q)
        r_seg = Seg_Chinese_In_Sentence(r)

        q_vec = np.zeros(200)
        q_len = 0
        for q_word in q_seg.split(' '):
            q_vec += self.model[q_word]
            q_len += 1

        if q_len == 0:
            raise "Error, the length of q is zero"
        q_vec = q_vec / q_len

        r_vec = np.zeros(200)
        r_len = 0
        for r_word in r_seg.split(' '):
            r_vec += self.model[r_word]
            r_len += 1

        if r_len == 0:
            raise "Error, the length of r is zero"
        r_vec = r_vec / r_len

        return tool.cosine(q_vec, r_vec)
