import os

#from cluster_test import *

def cluster_one(videoDir, featureList, picDir, saveDir, eps):
    #parser.add_argument('--videoDir', type=str, required=True, help='Path of features to be clustered')
    #parser.add_argument('--featureList', type=str, required=True, help='Feature list of feature file name')
    #parser.add_argument('--picDir', type=str, required=True, help='Path of pictures to be clustered')
    #parser.add_argument('--saveDir', type=str, required=True, help='Path to save clustered pictures')
    #parser.add_argument('--eps', type=float, required=False, default=None, help='DBSCAN parameter')

    # labelDict = load_label(args['labelDir'])
    # f_score = cluster_and_test_from_video_dir('5ab52c0e28734100076d67b9', labelDict, methodList=['API'])
    # f_score = cluster_and_test_from_video_dir(args['videoDir'], args['picDir'], labelDict, methodList=[args['method']])
    # print f_score
    #eps = 0.4
    if eps is None:
        str_eps = ''
    else:
        str_eps = str(eps)

    saveDir = saveDir + '_' + str_eps
    cluster_from_video_dir(videoDir, featureList, picDir, methodList='DBSCAN',
                           saveResult=True, saveDir=saveDir, eps=eps, nProcess=16)

    os.system("ls -lR {}|grep \"^-\"|wc -l".format(saveDir))
    os.system("ls {}|wc -l".format(saveDir))


def main():
    i = 0
    videoDir = "/Users/bin/Desktop/feature_npy"
    for name_dir in os.listdir("/Users/bin/Desktop/face"):
        if i< 2:
            with open("/Users/bin/Desktop/cluster_result/temp_fea_list.txt", "wb") as f:
                for name_npy in os.listdir("/Users/bin/Desktop/face/" + name_dir):
                    f.write(name_npy + "\n")
                #print name_npy


        featureList = "/Users/bin/Desktop/cluster_result/temp_fea_list.txt"
        picDir = "/Users/bin/Desktop/face/" + name_dir
        saveDir = "/Users/bin/Desktop/cluster_result/" + name_dir
        cluster_one(videoDir, featureList, picDir, saveDir, eps=0.4)
        i += 1


if __name__ == "__main__":
    main()
