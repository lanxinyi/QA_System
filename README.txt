代码部分：
arithmetic.py
	arithmetic类：levenshtein()计算first和second字符串的编辑距离，lcs()计算first和second字符串的最大子序列

AveragCosineSimilarity.py
	AveragCosineSimilarity类：sim()根据word2vec得到的模型计算两个句子的平均余弦相似度

data.py
	IO_Date类：file_exist()判断文件是否存在，get_temp_file_name()产生一个带随机数字的文件名称，read_file()将文件读入到一个字符串数组中， write_file()将一个字符串数组写成一个文件

data_zh.py
	Seg_Chinese_In_Sentence()对字符串进行中文分词，Seg_Chinese_In_File()对文件进行中文分词

feature.py
	Basic_Feature基类
	IF_IDF类：初始化需要传入一个训练的文档数据，sim()计算两个字符串的相似度
	Overlap类：sim()计算两个字符串的相似度
	BM25类：初始化需要传入一个训练的文档数据，sim()计算两个字符串的相似度
	LM类：初始化需要传入一个训练的文档数据，sim()计算两个字符串的相似度
	
test.py
	测试函数，可以忽略

tool.py
	cosine()计算一维向量的余弦相似度

train_word2vec_data_process.py
	对word2vec训练的数据进行一下预处理生成数据train_word2vec.txt

train_word2vec_model.py
	训练一个word2vec模型得到dbqa.mode, dbqa.vector

数据部分位于data目录下



