# -*- coding: utf-8 -*-

import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print(globals()['__doc__'] % locals())
        sys.exit(1)

    inp, outp1, outp2 = sys.argv[1:4]

    model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5, workers=multiprocessing.cpu_count())
    # 1、sg=1 是skip-gram算法，对低频词敏感；默认sg=0为CBOW算法
    # 2、size是输出词向量的维度，值太小会导致词映射因为冲突而影响结果，值太大则会耗内存并使算法计算变慢，一般取值为100到200之间
    # 3、window是句子中当前词与目标词之间的最大距离
    # 4、min_count是对词进行过滤，频率小于min-count的单词则会被忽视，默认值为5
    # 5、negative和sample可根据训练结果进行微调，sample表示更高频率的词被随机下采样到所设置的阈值，默认值为1e-3
    # 6、hs=1表示层级softmax将会被使用，默认hs=0且negative不为0，则负采样将会被选择使用
    # 7、workers控制训练的并行，此参数只有在安装看Cpython后才有效

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(outp1)  # save model
    model.wv.save_word2vec_format(outp2, binary=False)
