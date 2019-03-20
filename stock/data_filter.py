import pandas as pd
import time
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot
import os
import sqlite3


class gernarate_pic:

    def __init__(self):
        self.name = 't' + time.strftime("%Y%m%d", time.localtime())
        self.today = pd.read_csv('./history_data/2019/excel/%s.csv' % self.name, encoding='utf-8')
        self.changepercent = self.today['changepercent'].round(0)
        self.count = self.changepercent.value_counts()
        self.sort = self.count.sort_index()
        self.sortList = self.sort.values.tolist()
        self.percent = self.sort.index.tolist()


    def delete_new(self):
        for i in self.percent:
            if i > 11:
                self.percent.remove(i)
                self.sortList.pop()


    def check_data_quility(self):
        if self.percent[10] == -0.0:
            print(self.percent[10])
            self.percent[10] = '0.0'
            print(self.percent[10])
        else:
            print('haha')

        if len(self.sortList) == len(self.percent):
            print(self.sortList)
            print(self.percent)
            print('数据一致！')
        else:
            print('请检查数据')
            os._exit(0)



    def chart(self):
        bar = Bar("ebooking")
        bar.add("60客户", self.percent, self.sortList, is_stack=True)
        bar.render()
        make_a_snapshot('render.html', './pic/%s.png' % self.name)


    def main(self):
        self.delete_new()
        self.check_data_quility()
        self.chart()


    def import_after_filter(self):
        tableName = 'Normal'
        database_name = time.strftime("%Y", time.localtime())
        conn = sqlite3.connect(r'./history_data/2019/{}.db'.format(database_name))
        try:
            conn.execute('''create table if not exists %s('DATE' TEXT,'-10.0' TEXT,'-9.0' TEXT,'-8.0' TEXT,'-7.0' TEXT,'-6.0' TEXT,'-5.0' TEXT,'-4.0' TEXT,'-3.0' TEXT,'-2.0' TEXT,'-1.0' TEXT,'0.0' TEXT,'1.0' TEXT,'2.0' TEXT,'3.0' TEXT,'4.0' TEXT,'5.0' TEXT,'6.0' TEXT,'7.0' TEXT,'8.0' TEXT,'9.0' TEXT,'10.0' TEXT);''' % tableName)
        except:
            print('数据库出错，请检查。')
            os._exit(0)
        DATE = time.strftime("%Y%m%d", time.localtime())
        conn.execute('''insert into %s ('DATE') values ('%s');''' % (tableName, DATE))
        for i in range(len(self.percent)):
            conn.execute('''update %s set '%s'='%s' where DATE='%s' ;''' % (tableName, self.percent[i], self.sortList[i], DATE))
        conn.commit()
        conn.close()





if __name__ == '__main__':
    main = gernarate_pic()
    main.main()
    main.import_after_filter()

