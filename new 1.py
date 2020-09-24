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
    dictionary = gensim.corpora.Dictionary([str1,str2])
    corpus = [dictionary.doc2bow(text) for text in (str1,str2)]
    #tf = gensim.models.TfidfModel(corpus)
    #corpus_tf = tf[corpus]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    org_corpus = dictionary.doc2bow(str1)
    #new_vec_tf = tf[new_vec]
    sim = similarity[org_corpus][1]
    return sim

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
    print("文章相似度: %.4f"%similarity)
    file = open(out_path, 'w', encoding="utf-8")
    file.write("文章相似度: %.4f"%similarity)
    file.close()