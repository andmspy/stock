import sqlite3
import time
import os
import tushare as ts
import data_filter


class database_import:

    def __init__(self):
        self.name = 't' + time.strftime("%Y%m%d", time.localtime())
        print('当前下载数据的日期：', self.name)


    # 检查数据库是否存在
    def check_database_path(self):
        path = r'.\history_data\2019\2019.db'
        if os.path.exists(path):
            print('数据库已存在，不用创建')
        else:
            database_name = time.strftime("%Y", time.localtime())
            conn = sqlite3.connect(r'./history_data/2019/{}.db'.format(database_name))
            print('找不到数据库，已重新创建')

    def create_date_table(self):
        table = sqlite3.connect(r'.\history_data\2019\2019.db')
        try:
            table.execute('''create table %s(
                      "code" TEXT,
                      "name" TEXT,
                      "changepercent" INT,
                      "trade" INT,
                      "open" INT,
                      "high" INT,
                      "low" INT,
                      "settlement" INT,
                      "volume" INT,
                      "turnoverratio" INT,
                      "amount" INT,
                      "per" INT,
                      "pb" INT,
                      "mktcap" INT,
                      "nmc" INT
                    );''' % self.name)
            print('已创建当前日期表。')
        except:
            print('表已存在，无法创建。')
            os._exit(0)
        with open('.\SQL\csv_to_sqlite.sql', 'w+') as f:
            f.write(
                '.open C:\\\\Users\\\\Administrator\\\\Desktop\\\\eCom\\\\easyship_view\\\\stock\\\\history_data\\\\2019\\\\2019.db\n')
            f.write('.separator \',\'\n')
            f.write(
                '.import C:\\\\Users\\\\Administrator\\\\Desktop\\\\eCom\\\\easyship_view\\\\stock\\\\history_data\\\\2019\\\\excel\\\\%s.csv %s' % (self.name, self.name))
            f.close()
            os.system('sqlite3 contact.db<.\SQL\csv_to_sqlite.sql')
            print('done')

    # 下载当天数据
    def get_today_data(self):
        today = ts.get_today_all()
        today.to_csv(r'.\history_data\2019\excel\%s.csv' % self.name, index=False, encoding='utf_8_sig')


    def main(self):
        self.check_database_path()
        self.get_today_data()
        self.create_date_table()


if __name__ == '__main__':
    main = database_import()
    main.main()




