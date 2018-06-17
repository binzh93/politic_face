# -*- coding: utf-8 -*-
import os
import json
import numpy as np
import cv2

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def get_name(name_unique):
    num_list = [str(k) for k in xrange(10)]
    name = name_unique
    for i in num_list:
        name = name.split(i)[0]
    return name

#os.chdir("/Users/bin/Desktop/中纪委的副本2/")
basepath = "/Users/bin/Desktop/downfile/result/1/facex_api_response_#180611-133309/"
basepath2 = "/Users/bin/Desktop/downfile/result/2/facex_api_response_#180611-230432/"
basepath3 = "/Users/bin/Desktop/downfile/result/3/facex_api_response_#180611-140025/"
basepath4 = "/Users/bin/Desktop/downfile/result/4/facex_api_response_#180611-140515/"
basepath5 = "/Users/bin/Desktop/downfile/result/5/facex_api_response_#180611-230518/"
basepath6 = "/Users/bin/Desktop/downfile/result/6/facex_api_response_#180611-153634/"
basepath7 = "/Users/bin/Desktop/downfile/result/7/facex_api_response_#180611-230651/"
basepath8 = "/Users/bin/Desktop/downfile/result/8/facex_api_response_#180611-173530/"
basepath9 = "/Users/bin/Desktop/downfile/result/9/facex_api_response_#180611-182033/"
basepath10 = "/Users/bin/Desktop/downfile/result/10/facex_api_response_#180611-230748/"

#path = "/Users/bin/Desktop/api-det2/311facex-api-test-master2/ava-version-python-little-endian/facex_api_response_#180611-120717"
#os.chdir(path)
filename1 = basepath10 + "facex_attr_req_data_list.json"
filename2 = basepath10 + "facex_det_req_data_list.json"
filename3 = basepath10 + "facex_det_resp_list.json"
filename4 = basepath10 + "facex_feature_resp_list.json"

f = open(filename4, 'rb')
value_dict = json.load(f)
#i = 0

for value in value_dict:
    # if i < 1000:
    name_unique = value['feat_npy'].split('/')[-1].split('.')[0]    # 丁么明1_0
    name_dir = get_name(name_unique)
    pic_name = name_unique.split("_")[0] + ".jpg"
    x1_ = value['pts'][0][0]
    x2_ = value['pts'][1][0]
    y1_ = value['pts'][0][1]
    y2_ = value['pts'][2][1]

    x_center = (x1_ + x2_)/2
    y_center = (y1_ + y2_)/2
    face_w = (x2_ - x1_ + 1)/2*2   # turn the face width and height to even
    face_h = (y2_ - y1_ + 1)/2*2


    if not os.path.exists("/Users/bin/Desktop/face/" + name_dir):
        os.makedirs("/Users/bin/Desktop/face/" + name_dir)

    pic_path = "/Users/bin/Desktop/中纪委的副本2/" + name_dir + "/" + pic_name
    print pic_path

    #"""
    img = cv2.imread(pic_path)
    if img is not None:
        w_img = img.shape[1]
        h_img = img.shape[0]

        x1 = max(0, x_center - face_w) / 2 * 2
        x2 = min(w_img, x_center + face_w) / 2 * 2
        y1 = max(0, y_center - face_h) / 2 * 2
        y2 = min(h_img, y_center + face_h) / 2 * 2

        x_b = face_w - (x2 - x1) / 2
        y_b = face_h - (y2 - y1) / 2

        new_img = np.zeros((2 * face_h, 2 * face_w, 3))
        new_img[y_b: y_b + (y2 - y1), x_b: x_b + (x2 - x1), :] = img[y1: y2, x1: x2, :]

        cv2.imwrite("/Users/bin/Desktop/face/" + name_dir + "/" + name_unique + ".jpg", new_img)

        #"""

        #print name_unique, pic_name, name_dir, value['pts'], value['feat_npy']#, url.split("/")[-1].split('.')[0]


        #print value
    #i += 1
print "---------done--------"







