# -*- coding: utf-8 -*-
import os
import requests
from getNameList import load1
from downOnePic import getOnePic


def main(basepath, file, isHaveErr=True):
    name_list = load1(file)
    duplicate_name = dict()

    nums = 0

    for keyword in name_list:
        print '--------%s---------' % nums
        nums += 1
        duplicate_name = getOnePic(keyword, 30, duplicate_name, basepath)


if __name__ =="__main__":
    file1 = os.path.join("json", "中纪委_gamma_0.0.1-resume_conv.json")
    file2 = os.path.join("json", "中纪委_gamma_0.0.1-resume_conv_2.json")
    file3 = os.path.join("json", "zjsjw_aaa-resume_conv.json")
    file4 = os.path.join("json", "zjsjw_aaa-resume_conv_2.json")
    #basepath = "/Users/bin/Desktop/politic/中纪委2/"
    basepath = '/Users/bin/Desktop/kk/'

    main(basepath, file2)
    print 'well done'
