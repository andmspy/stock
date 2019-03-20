import os
import pandas as pd
file_list = os.listdir(r'./history_data\2019\excel')

def get_describe(file_name):
    today = pd.read_csv(file_name, encoding='utf-8')
    changepercent = today['changepercent']

    up_list = []
    down_list = []
    up_stop = []
    down_stop = []
    for i in changepercent:
        if i < 0:
            down_list.append(i)
        elif i < -9.97:
            down_stop.append(i)
        elif i > 0:
            up_list.append(i)
        elif i > 9.97:
            up_stop.append(i)

    print('样本：', changepercent.count(), end='   |   ')
    print('众数：', changepercent.mode()[0], end='   |   ')
    print('中位数：', changepercent.median().round(2), end='   |   ')
    print('均值：', changepercent.mean().round(2), end='   |   ')
    print('下跌：', len(down_list), end='   |   ')
    print('跌停：', len(down_stop), end='   |   ')
    print('上涨：', len(up_list), end='   |   ')
    print('涨停：', len(up_stop))
    print('================================================================================================')




path = os.path.abspath(os.path.dirname(__file__))


for i in file_list:
    # print(i, file_list.index(i))
    file_path = path+'\\'+'history_data'+'\\'+'2019'+'\\'+'excel'+'\\'+i
    get_describe(file_path)



#涨跌停无法筛选！！！！
# 获取down_stop,down,up,up_stop



