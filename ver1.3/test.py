import unittest,main

class test(unittest.TestCase):
    def test_orig_copy(self):
        print("orig.txt与orig_copy.txt的相似度为：")
        origText_path = r"F:\py\test\orig.txt"
        testText_path = r"F:\py\test\orig_copy.txt"
        out_path = r"F:\py\test\ans.txt"
        str1 = main.Leading_in(origText_path)
        str2 = main.Leading_in(testText_path)
        str1 = main.clean_txt(str1)
        str2 = main.clean_txt(str2)
        str1 = main.spilt_txt(str1)
        str2 = main.spilt_txt(str2)
        similarity = main.Similarity(str1, str2)
        print("文本相似度为: %.2f%%"%(similarity*100))

    def test_orig_add(self):
        print("orig.txt与orig_0.8_add.txt的相似度为：")
        origText_path = r"F:\py\test\orig.txt"
        testText_path = r"F:\py\test\orig_0.8_add.txt"
        out_path = r"F:\py\test\ans.txt"
        str1 = main.Leading_in(origText_path)
        str2 = main.Leading_in(testText_path)
        str1 = main.clean_txt(str1)
        str2 = main.clean_txt(str2)
        str1 = main.spilt_txt(str1)
        str2 = main.spilt_txt(str2)
        similarity = main.Similarity(str1, str2)
        print("文本相似度为: %.2f%%"%(similarity*100))
    
    def test_orig_del(self):
        print("orig.txt与orig_0.8_del.txt的相似度为：")
        origText_path = r"F:\py\test\orig.txt"
        testText_path = r"F:\py\test\orig_0.8_del.txt"
        out_path = r"F:\py\test\ans.txt"
        str1 = main.Leading_in(origText_path)
        str2 = main.Leading_in(testText_path)
        str1 = main.clean_txt(str1)
        str2 = main.clean_txt(str2)
        str1 = main.spilt_txt(str1)
        str2 = main.spilt_txt(str2)
        similarity = main.Similarity(str1, str2)
        print("文本相似度为: %.2f%%"%(similarity*100))
    def test_orig_dis_1(self):
        print("orig.txt与orig_0.8_dis_1.txt的相似度为：")
        origText_path = r"F:\py\test\orig.txt"
        testText_path = r"F:\py\test\orig_0.8_dis_1.txt"
        out_path = r"F:\py\test\ans.txt"
        str1 = main.Leading_in(origText_path)
        str2 = main.Leading_in(testText_path)
        str1 = main.clean_txt(str1)
        str2 = main.clean_txt(str2)
        str1 = main.spilt_txt(str1)
        str2 = main.spilt_txt(str2)
        similarity = main.Similarity(str1, str2)
        print("文本相似度为: %.2f%%"%(similarity*100))
    
    def test_orig_dis_10(self):
        print("orig.txt与orig_0.8_dis_10.txt的相似度为：")
        origText_path = r"F:\py\test\orig.txt"
        testText_path = r"F:\py\test\orig_0.8_dis_10.txt"
        out_path = r"F:\py\test\ans.txt"
        str1 = main.Leading_in(origText_path)
        str2 = main.Leading_in(testText_path)
        str1 = main.clean_txt(str1)
        str2 = main.clean_txt(str2)
        str1 = main.spilt_txt(str1)
        str2 = main.spilt_txt(str2)
        similarity = main.Similarity(str1, str2)
        print("文本相似度为: %.2f%%"%(similarity*100))

    def test_orig_dis_15(self):
        print("orig.txt与orig_0.8_dis_15.txt的相似度为：")
        origText_path = r"F:\py\test\orig.txt"
        testText_path = r"F:\py\test\orig_0.8_dis_15.txt"
        out_path = r"F:\py\test\ans.txt"
        str1 = main.Leading_in(origText_path)
        str2 = main.Leading_in(testText_path)
        str1 = main.clean_txt(str1)
        str2 = main.clean_txt(str2)
        str1 = main.spilt_txt(str1)
        str2 = main.spilt_txt(str2)
        similarity = main.Similarity(str1, str2)
        print("文本相似度为: %.2f%%"%(similarity*100))

if __name__ == '__main__':
    unittest.main()
