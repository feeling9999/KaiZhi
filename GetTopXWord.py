#coding:utf-8
from collections import Counter

#获取某文档中前X个初现的二元词组
def getTopXWord(filename,X):
    #存储文章所有二元词组
    resultWords = []
    with open(filename, 'r') as file:
        words = file.read()
        wordList = words.split()#去除空格
        for i in range(len(wordList) - 1):
           word1 = wordList[i]
           word2 = wordList[i+1]
           #如果当前词和后一个词的长度为2则定义为二元词组，此时同时也可过滤掉标点符号
           if len(word1)==2 & len(word2)==2:
               resultWords.append(word1 +' '+word2)
        #取前词频最高的前X位
        result = Counter(resultWords).most_common(X)
        return  result


if __name__=='__main__':
    filename ='happiness_seg.txt'
    result = getTopXWord(filename,10)
    for contet in result:
        print(contet)


