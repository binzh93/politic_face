# -*- coding: utf-8 -*-
import os
import requests
from test1 import load1
from face_achieve import dowmloadPic


def main(basepath, file):

    name_list = load1(file)

    duplicate_name = dict()

    for word in name_list:
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
        result = requests.get(url)
        duplicate_name = dowmloadPic(basepath, result.text, word, duplicate_name)


if __name__ =="__main__":
    file1 = os.path.join("json", "中纪委_gamma_0.0.1-resume_conv.json")
    file2 = os.path.join("json", "中纪委_gamma_0.0.1-resume_conv_2.json")
    file3 = os.path.join("json", "zjsjw_aaa-resume_conv.json")
    file4 = os.path.join("json", "zjsjw_aaa-resume_conv_2.json")
    basepath = "/Users/bin/Desktop/politic/zjsjw2/"

    main(basepath, file4)
    print 'well done'
