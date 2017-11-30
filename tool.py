import numpy as np

class tool():
    def __init__(self):
        pass

    @staticmethod
    def cosine(x, y):  # 一维向量的计算
        if len(x) != len(y):
            raise "x, y length is not equal"

        Lx = np.sqrt(x.dot(x))
        Ly = np.sqrt(y.dot(y))
        cos_angle = x.dot(y) / (Lx * Ly)
        return cos_angle