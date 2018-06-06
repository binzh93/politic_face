#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import re

os.chdir("/Users/bin/Desktop/")

file1 = os.path.join("json", "中纪委_gamma_0.0.1-resume_conv.json")
file2 = os.path.join("json", "中纪委_gamma_0.0.1-resume_conv_2.json")
file3 = os.path.join("json", "zjsjw_aaa-resume_conv.json")
file4 = os.path.join("json", "zjsjw_aaa-resume_conv_2.json")

def load1(file):
    a = []
    invalid_nums = 0
    invalid_str = ''
    with open(file, 'r') as f:
        for line in f:
            #print type(line)
            #print eval(line.strip())
            #name = eval(line.strip())['result']['resume'].split(' ')[0].split('简历')[0]
            #print(line.strip())
            name = eval(line.strip())['result']['resume']
            #name = re.split(r"\s|:\s|:\s\s|：|：\s\s|：\s|,\s|:\n", name)
            #print name
            name = re.split(r"\s|:\s|:\s|：|：\s|,\s|:", name)
            temp = name[0].split("个人简历")
            temp = temp[0].split("简历")
            #if len(temp)==0 | len(temp)>3:
            #print name[1]
            if len(temp) == 0:
                temp = name[1].split("，")[0]
            #print type(temp)
            if len(temp[0]) == 0:
                invalid_nums += 1
                invalid_str += line.strip()

            a.append(temp)

    #c = set()
    for i in a:
        print i[0]
        #c.add(i[0])
    print invalid_nums
    print invalid_str
    print len(a)
    #print len(c)
    a = [i[0] for i in a]
    return list(a)



def load2(file):
    a = []
    with open(file, 'r') as f:
        for line in f:
            #name = eval(line.strip())['result']['resume'].split(' ')[0].split('简历')[0]
            #print(line.strip())
            name = eval(line.strip())['result']['resume']
            #name = re.split(r"\s|:\s|:\s\s|：|：\s\s|：\s|,\s|:\n", name)
            print name
            name = re.split(r"\s|:\s|:\s|：|：\s|,\s|:", name)
            temp = name[0].split("个人简历")
            temp = temp[0].split("简历")
            #if len(temp)==0 | len(temp)>3:
            #print name[1]
            if len(temp) == 0:
                temp = name[1].split("，")[0]

            a.append(temp)

    for i in a:
        print i[0]

if __name__ == '__main__':
    load1(file4)

