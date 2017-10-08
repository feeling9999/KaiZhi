import numpy as np

if __name__=='__main__':
    m = 0 # 均值
    seg = 1#标准差
    valueList = np.random.normal(m,seg,100)
    valueList[valueList > 0] = 0
    print(valueList)
