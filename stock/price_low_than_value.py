import pandas
import time
import os

name = 't' + time.strftime("%Y%m%d", time.localtime())
path = './history_data/2019/excel/'


def get_csv_file(csv):
    file = pandas.read_csv(csv)
    trade = file['trade']
    pb = file['pb']
    file['pb_value'] = trade/pb
    file['upper'] = file['trade'] > file['pb_value']
    b = file['upper'].value_counts()
    file_B = file[file['upper'] == False] #筛选为False的值，即低于净资产的Dataframe
    return (b[0]/b[1]).round(3)


if __name__ == '__main__':
    file = r'./history_data/2019/excel/'
    file_list = os.listdir(file)
    print('低于比率：')
    for i in file_list:
        print(get_csv_file(file+i), end=' | ')