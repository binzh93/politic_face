# coding=utf-8
"""根据搜索词下载百度图片"""
import re
import urllib
import requests
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_onepage_urls(onepageurl):
    """获取单个翻页的所有图片的urls+当前翻页的下一翻页的url"""
    if not onepageurl:
        print('已到最后一页, 结束')
        return [], ''
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        fanye_url = ''
        return pic_urls, fanye_url
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    fanye_urls = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
    fanye_url = 'http://image.baidu.com' + fanye_urls[0] if fanye_urls else ''
    return pic_urls, fanye_url




def down_pic(pic_urls, savepath, keyword, max_nums):
    """给出图片链接列表, 下载所有图片"""
    i = 0
    for pic_url in pic_urls:
        i += 1
        try:
            pic = requests.get(pic_url, timeout=15)
            string = savepath + '/' + keyword + str(i) + '.jpg'
            with open(string, 'wb') as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i), str(pic_url)))
            print(e)
            continue

        if i+1 >= max_nums:
            break


def getOnePic(keyword, max_nums, duplicate_name, savepath='/Users/bin/Desktop/pic/ss/'):
    # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&f' \
                     r'm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&hei' \
                     r'ght=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='
    url_init = url_init_first + urllib.quote(keyword, safe='/')
    all_pic_urls = []
    onepage_urls, fanye_url = get_onepage_urls(url_init)
    all_pic_urls.extend(onepage_urls)

    if keyword not in duplicate_name:
        duplicate_name[keyword] = 0
        os.makedirs(savepath + keyword)
        temppath = os.path.join(savepath, str(keyword))
    else:
        duplicate_name[keyword] += 1
        os.makedirs(savepath + keyword + str(duplicate_name[keyword]))
        temppath = os.path.join(savepath, keyword + str(duplicate_name[keyword]))
    print temppath


    down_pic(all_pic_urls, temppath, keyword, max_nums)
    return duplicate_name





if __name__ == '__main__':
    savepath = '/Users/bin/Desktop/pic/ss/'
    #keyword = '刘树琪'
    duplicate_name = dict()
    name_list = ['刘树琪', '刘树琪']
    print
    for keyword in name_list:
        duplicate_name = getOnePic(keyword, 30, duplicate_name)

