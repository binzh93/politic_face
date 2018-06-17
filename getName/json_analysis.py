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

def filter_load(file):
    a = []
    invalid_nums = 0
    invalid_str = []
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
                invalid_str.append(line.strip())

            a.append(temp)

    name_list = []
    for i in a:
        if len(i[0]) >0:
            name_list.append(i[0])
        if len(i[0]) == 0:
            print '123424234234234234'
        else:
            print i[0]

        #c.add(i[0])

    for i in invalid_str:
        print i
    print 'invalid_nums: ', invalid_nums
    #print len(name_list)  # 一次过滤有效name list
    print len(a)

    second_name_list = []
    second_invalid = []
    multi_name_list = []
    multi_str = []
    for i in invalid_str:
        temp = eval(i)['result']['title']  #'', '', '', '', '',
        v_list = ['副市长', '市长', '委员', '主任', '主席', '局长', '区长', '经理', '书记', '校长', '助理','总裁', '政委', '秘书长',
                  '常委', '侦察员', '董事长', '部长', '厅长', '监事长', '规划师', '调研员', '院长', '巡视员', '成员', '行长',
                  '司长', '组长', '理事长', '省长', '纪委', '专员', '检察长', '台长', '州长', '经济师', '会长', '信息官',
                  '处长', '参谋', '干部', '社长', '队长', '司令员', '关长', '被免职', '工程师', '师长', '盟长', '会计师',
                  '县长', '督导员', '督学', '系统', '公司', '对']
        for v in v_list:
            temp = get_split_former_result(temp, v)

        v_last_list = ['开除党籍', '因涉嫌', '因受贿', '因违纪', '被双开', '被\"双开\"', '被“双开”', '被审查', '被撤销',
                       '被留党', '被起诉', '被开除', '被刑拘', '被调查', '接受', '严重', '同志', '涉嫌', '受贿', '被给予',
                       '移送', '受党内', '违纪', '受到', '违反', '立案', '因', '被', '、', '，']

        for v in v_last_list:
            temp = temp.split(v)[0]

        if temp.strip() == '国家监委网站':
            print 'xxxxxxxxxxxxxxxx'
            second_invalid.append(i)
        elif (len(temp.strip()) == 0) | (len(temp.strip()) == 1):
            second_invalid.append(i)
            print 'hhhdhhhhhdhhhhhhhhhhhhhhhh'
        elif '等' in temp:
            temp = temp.split('等')[0]
            multi_name_list.append(temp)
            multi_str.append(i)
            print 'sssss', temp
        else:
            second_name_list.append(temp)
            print temp
    print len(multi_name_list)
    print len(second_name_list)
    print len(second_invalid)
    name_list.extend(second_name_list)
    print len(name_list)

    # write 无法解析和多个人的json文件
    #write_json(second_invalid, multi_str, json_name="中纪委")  # file1
    #write_json(second_invalid, multi_str, json_name="zjw")  # file3





        #print 'ss', temp #.strip()

    #print len(c)
    a = [i[0] for i in a]
    return name_list, multi_name_list

def write_json(invalid_str, multi_str, json_name="中纪委"):
    with open("/Users/bin/Desktop/invalid_json/" + json_name + "无法解析.json", "w") as fw:
        for line in invalid_str:
            new_dict = eval(line)
            json.dump(new_dict, fw, ensure_ascii=False)
            fw.write('\n')
    with open("/Users/bin/Desktop/invalid_json/" + json_name + "多人的.json", "w") as fw:
        for line in multi_str:
            new_dict = eval(line)
            json.dump(new_dict, fw, ensure_ascii=False)
            fw.write('\n')





def get_split_former_result(temp, key):
    temp = temp.split(key)
    if len(temp) > 1:
        temp = temp[1]
    else:
        temp = temp[0]
    return temp




if __name__ == '__main__':
    print 'dasd'
    #filter_load(file3)


