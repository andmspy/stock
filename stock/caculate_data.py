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


def get_pe(csv):
    file = pandas.read_csv(csv)
    pe = file['per']
    return pe.median()

def get_turnoverratio(csv):
    file = pandas.read_csv(csv)
    turnoverratio = file['turnoverratio']
    return turnoverratio.median()


def get_changepercent_ratio(csv):
    file = pandas.read_csv(csv)
    percent_list = file['changepercent'].tolist()
    up = []
    none = []
    low = []
    for i in percent_list:
        if i > 0:
            up.append(i)
        elif i < 0:
            low.append(i)
        else:
            none.append(i)
    if len(percent_list) == len(up)+len(none)+len(low):
        pass
    else:
        print('统计数量不一致')
        os._exit(0)
    up_percent = '%.2f%%' % (len(up)/len(percent_list)*100)
    none_percent = '%.2f%%' % (len(none)/len(percent_list)*100)
    low_percent = '%.2f%%' % (len(low)/len(percent_list)*100)
    print(up_percent, ':', none_percent, ':', low_percent)

if __name__ == '__main__':
    file = r'./history_data/2019/excel/'
    file_list = os.listdir(file)
    print('低于比率：')
    print('    日期    低净率   整盈率  整手率           二八现象')
    print('-------------------------------------------------------------------------')
    for i in file_list:
        print('|', i[1:9], end=' | ')
        print(get_csv_file(file+i), end=' | ')
        print('%.2f%%' % get_pe(file+i), end=' |  ')
        print('%.2f%%' % get_turnoverratio(file+i), end=' | ')
        get_changepercent_ratio(file+i)

