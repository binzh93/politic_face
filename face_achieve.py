# -*- coding:utf-8 -*-
import re
import os
import requests



def dowmloadPic(basepath, html, keyword, duplicate_name):

    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    if keyword not in duplicate_name:
        duplicate_name[keyword] = 0
        os.makedirs(basepath + keyword)
        temppath = os.path.join(basepath, keyword)
    else:
        duplicate_name[keyword] += 1
        os.makedirs(basepath + keyword + str(duplicate_name[keyword]))
        temppath = os.path.join(basepath, keyword + str(duplicate_name[keyword]))


    #temppath = os.path.join(basepath, keyword)
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=200)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        dir = os.path.join(temppath, keyword + '_' + str(i) + '.jpg')
        #print dir
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        if i>50:
            break
    return duplicate_name



if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text, word)
