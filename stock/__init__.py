import data_filter
import data_import

main = data_import.database_import()
main.main()
main2 = data_filter.gernarate_pic()
main2.main()
main2.import_after_filter()


#如数据出错，需要删除3个地方，EXCEL>CSV,2019.db里面的表和Normal里面的数据















