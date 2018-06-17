# -*- coding: utf-8 -*-
import cv2
import os

nums = 0
'''
for name in os.listdir("/Users/bin/Desktop/中纪委的副本2"):  # 中纪委的副本
    for img_name in os.listdir("/Users/bin/Desktop/中纪委的副本2/" + name):
        filename = "/Users/bin/Desktop/中纪委的副本2/" + name + "/" + img_name
        img = cv2.imread(filename)
        if not img:
            print "%s Delete ..." % filename
            os.remove(filename)
'''

for name in os.listdir("/Users/bin/Desktop/中纪委的副本2"):  # 中纪委的副本
    print name
    if name != '.DS_Store':
        for img_name in os.listdir("/Users/bin/Desktop/中纪委的副本2/" + name):
            filename = "/Users/bin/Desktop/中纪委的副本2/" + name + "/" + img_name
            img = cv2.imread(filename)
            if img is None:
                print "%s Delete ..." % filename
                os.remove(filename)


