import csv
import os
import sys
import numpy as np
import random
import requests
# name of data file
# 数据集名称
birth_weight_file = 'birth_weight.csv'


#mypath = sys.argv[1]
mypath = '/Users/zhuzhichao/Documents/data_analysis'



if not os.path.exists(mypath):
    print ("The path %s does not exist!")
    sys.exit(2)

for f in [s for s in os.listdir(mypath) if os.path.splitext(s)[1] == ".csta"]:
    outputName  = f + ".csv"
    fd          = open(os.path.join(mypath, f), 'rb')
    outputFd    = open(os.path.join(mypath, outputName), 'w')


# download data and create data file if file does not exist in current directory
# 如果当前文件夹下没有birth_weight.csv数据集则下载dat文件并生成csv文件
if not os.path.exists(birth_weight_file):
    birthdata_url = 'https://github.com/nfmcclure/tensorflow_cookbook/raw/master/01_Introduction/07_Working_with_Data_Sources/birthweight_data/birthweight.dat'
    birth_file = requests.get(birthdata_url)
    birth_data = birth_file.text.split('\r\n')
    # split分割函数,以一行作为分割函数，windows中换行符号为'\r\n',每一行后面都有一个'\r\n'符号。
    birth_header = birth_data[0].split('\t')
    # 每一列的标题，标在第一行，即是birth_data的第一个数据。并使用制表符作为划分。
    birth_data = [[float(x) for x in y.split('\t') if len(x) >= 1] for y in birth_data[1:] if len(y) >= 1]
    print(np.array(birth_data).shape)
    # (189, 9)
    # 此为list数据形式不是numpy数组不能使用np,shape函数,但是我们可以使用np.array函数将list对象转化为numpy数组后使用shape属性进行查看。
    with open(birth_weight_file, "w", newline='') as f:
    # with open(birth_weight_file, "w") as f:
        writer = csv.writer(f)
        writer.writerows([birth_header])
        writer.writerows(birth_data)
        f.close()