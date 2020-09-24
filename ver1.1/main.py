#-*-codeing = utf-8 -*-
from jieba import lcut
from re import sub
import gensim
import sys

def Leading_in(path):
	str=""
	file = open(path, 'r', encoding='UTF-8')
	for line in file.readlines():
		str+=line
	file.close()
	return str

def clean_txt(str):
	clean = "[^0-9A-Za-z\u4e00-\u9fa5]"
	return sub(clean, '', str)

def spilt_txt(str):
	str = lcut(str, cut_all=False)
	return str

def Similarity(str1,str2):
    dictionary = gensim.corpora.Dictionary([str1])
    num_features = len(dictionary.token2id)
    corpus = [dictionary.doc2bow(str1)]
    new_vec = dictionary.doc2bow(str2)
    tf = gensim.models.TfidfModel(corpus)
    print(tf)
    corpus_tf = tf[corpus]
    new_vec_tf = tf[new_vec]
    index = gensim.similarities.SparseMatrixSimilarity(corpus_tf, num_features)
    sim = index[new_vec_tf]
    print('\nTF-IDF模型的稀疏向量集：')
    for i in tf[corpus]:
        print(i)
    print('\nTF-IDF模型的keyword稀疏向量：')
    print(tf[new_vec])
    print('\n相似度计算：')
    print(sim)
    return sim[0]

if __name__ == '__main__':
    origText_path = sys.argv[1]
    testText_path = sys.argv[2]
    out_path = sys.argv[3]
    str1 = Leading_in(origText_path)
    str2 = Leading_in(testText_path)
    str1 = clean_txt(str1)
    str2 = clean_txt(str2)
    str1 = spilt_txt(str1)
    str2 = spilt_txt(str2)
    similarity = Similarity(str1, str2)
    print("文本相似度为: %.2f"%similarity)
    file = open(out_path, 'w', encoding="utf-8")
    file.write("文本相似度为: %.2f"%similarity)
    file.close()
