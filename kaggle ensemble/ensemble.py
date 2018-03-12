# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from collections import Counter


def invert_dict(d):
    return dict((v,k) for k,v in d.items())


def ensemble(path, CLASSES):
    csv_name = os.listdir(path)
    stacked_list = []
    label_list = []
    for each_csv in csv_name:
        csv_path = path + each_csv
        stacked = pd.read_csv(csv_path)
        number_class = [CLASSES[x] for x in stacked['camera']]
        stacked['camera'] = number_class
        label_list.append(number_class)
        stacked_list.append(stacked)
    sub = pd.DataFrame()
    sub['fname'] = stacked_list[0]['fname']
    label_list = np.array(label_list).T
    new_CLASSES = invert_dict(CLASSES)
    result = []
    for x in label_list:
        result.append(new_CLASSES[(Counter(x).most_common(1))[0][0]])
    sub['camera'] = result
    sub.to_csv('./' + 'ensamble.csv', index=False, float_format='%.0f')


if __name__ == '__main__':
    submission_path = './submission/'
    CLASSES = {'HTC-1-M7': 0,
               'iPhone-6': 1,
               'Motorola-Droid-Maxx': 2,
               'Motorola-X': 3,
               'Samsung-Galaxy-S4': 4,
               'iPhone-4s': 5,
               'LG-Nexus-5x': 6,
               'Motorola-Nexus-6': 7,
               'Samsung-Galaxy-Note3': 8,
               'Sony-NEX-7': 9}
    ensemble(submission_path, CLASSES)

# 参考代码
# from subprocess import check_output
# print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
# def ensemble():
#     stacked_1 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.166586_submission.csv')
#     stacked_2 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.167542_submission.csv')
#     stacked_3 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.167621_submission.csv')
#     stacked_4 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.166586_submission.csv')
#     stacked_5 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.168133_submission.csv')
#     stacked_6 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.170522_submission.csv')
#     stacked_7 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.180278_submission.csv')
#     stacked_8 = pd.read_csv('./pth/kfold/' + 'ResNetLike_0.185876_submission.csv')
#     sub = pd.DataFrame()
#     sub['id'] = stacked_1['id']
#     sub['is_iceberg'] = np.exp(np.mean(
#         [
#             stacked_1['is_iceberg'].apply(lambda x: np.log(x)), \
#             stacked_2['is_iceberg'].apply(lambda x: np.log(x)), \
#             stacked_3['is_iceberg'].apply(lambda x: np.log(x)), \
#             stacked_4['is_iceberg'].apply(lambda x: np.log(x)), \
#             stacked_5['is_iceberg'].apply(lambda x: np.log(x)), \
#             stacked_6['is_iceberg'].apply(lambda x: np.log(x)), \
#             stacked_7['is_iceberg'].apply(lambda x: np.log(x)), \
#             stacked_8['is_iceberg'].apply(lambda x: np.log(x)), \
#             ], axis=0))
#     sub.to_csv('./pth/kfold/' + 'ensamble.csv', index=False, float_format='%.6f')
