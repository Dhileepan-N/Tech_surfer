import xlwt
import cx_Oracle
import datetime
table_name = input()
try:
    con = cx_Oracle.connect('CSBMARVP_FEE/CSBMARVP_FEE@localhost:1521/orcl')
    cur = con.cursor()
    cur.execute('select count(*) from ' + table_name )
    records_cnt = cur.fetchall()
    records_count = records_cnt[0][0]
    cur.execute('select * from ' + table_name)
    column_name = cur.description
    column_count = len(column_name)
    records = cur.fetchmany(records_cnt[0][0])
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Products')
    date_style = xlwt.easyxf(num_format_str='DD/MM/YY')
    for i in range(column_count):
        sheet.write(0, i, column_name[i][0])
        workbook.save('C:\\Users\Patterns\Desktop\Table_Records.xls')
    for i in range(records_count):
        for j in range(column_count):
            if i <= records_count:
                if isinstance(records[i][j], datetime.datetime):
                    sheet.write(i + 1, j, records[i][j], date_style)
                else:
                    sheet.write(i+1, j, records[i][j])
                    workbook.save('C:\\Users\Patterns\Desktop\Table_Records.xls')

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)


