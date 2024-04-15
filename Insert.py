import ezodf
import os
import cx_Oracle

FilePath = 'E:\\New folder\\'
# FilePath = 'C:\\Users\\patte\\Desktop\\Data\\'
# Replace ODS File Name to Schema Name
# Config = [[ODS File Name and Schema Name should be same,Schema Configuration]]
#Config = [["CSBMWARESERVER","CSBMWARESERVER/CSBMWARESERVER@192.168.1.91:1521/oracsbdb"]]
#Config = [["CSBMWARESERVER","CSBMWARESERVER/CSBMWARESERVER@localhost:1521/xe"]]
#Config = [["shadow","shadow/shadow@192.168.1.91:1521/oracsbdb"]]
#Config = [["csbmarvp","csbmarvp/csbmarvp@192.168.1.91:1521/oracsbdb"]]
Config = [["CSBMARVP_FEE","CSBMARVP_FEE/CSBMARVP_FEE@localhost:1521/orcl"]]
LogEnable = 0


for i in range(len(Config)):
    Directory = FilePath + str(Config[i][0]) + ".ods"
    conn = cx_Oracle.connect(str(Config[i][1]))
    if os.path.exists(Directory):
        doc = ezodf.opendoc(Directory)
        Schema = str(Config[i][0]).upper()
        for j in range(len(doc.sheets)):
            sheet = doc.sheets[j]
            TableName = str(sheet.name)
            TableColumns = []
            datatypes = {}
            if TableName.startswith("Select "):
                TableName = TableName.replace("Select","").replace(" ","").upper()
                if "(" in TableName:
                    TableName = TableName[:TableName.index("(")]
                print(Schema + " - " + TableName + " Starting...")
                TableName_Test = ""
                c = conn.cursor()
                Query = "SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER = '" + str(Schema) + "' AND TABLE_NAME = '" + str(TableName) + "_TEST'"
                c.execute(Query)
                for row in c:
                    TableName_Test = str(row[0])
                if TableName_Test == "":
                    TableName_Test = TableName + "_TEST"
                    c = conn.cursor()
                    Query = "CREATE TABLE " + str(TableName_Test) + " AS SELECT * FROM " + str(TableName)
                    c.execute(Query)
                    conn.commit()
                c = conn.cursor()
                Query = "DELETE FROM " + str(TableName_Test)
                c.execute(Query)
                conn.commit()
                for k, row in enumerate(sheet.rows()):
                    count = 0
                    TableData = ""
                    InsertScript = ""
                    for l, cell in enumerate(row):
                        count = count + 1
                        if count > 1 and sheet.ncols() != count:
                            if k == 0:
                                datatype = ""
                                TableColumns.append(str(cell.value))
                                c = conn.cursor()
                                Query = "SELECT DATA_TYPE FROM ALL_TAB_COLUMNS WHERE OWNER = '" + str(Schema) + "' AND TABLE_NAME = '" + str(TableName) + "' AND COLUMN_NAME = '" + str(cell.value) + "'"
                                c.execute(Query)
                                for row in c:
                                    datatype = str(row[0])
                                if datatype != "":
                                    datatypes[str(count)] = datatype
                                else:
                                    print("DataType doesn't exists.  Schema - " + str(Schema) + " TableName - " + str(TableName) + " ColumnName - " + str(cell.value))
                            else:
                                if type(cell.value) == str:
                                    cellvalue = str(cell.value).encode('ascii', 'ignore').decode('ascii')
                                else:
                                    cellvalue = cell.value
                                if cellvalue == None:
                                    TableData = TableData + "NULL,"
                                else:
                                    if datatypes.get(str(count)) == "NUMBER":
                                        TableData = TableData + str(int(cell.value)) + ","
                                    elif datatypes.get(str(count)) == "CHAR":
                                        TableData = TableData + "'" + str(cellvalue) + "',"
                                    elif datatypes.get(str(count)) == "VARCHAR2":
                                        TableData = TableData + "'" + str(cellvalue).replace("'","''") + "',"
                                    elif datatypes.get(str(count)) == "DATE":
                                        if "T" in cellvalue:
                                            TableData = TableData + "TO_DATE('"+ cellvalue[:10] + " " + cellvalue[11:19] + "','YYYY-MM-DD HH24:MI:SS'),"
                                        else:
                                            TableData = TableData + "TO_DATE('" + str(cellvalue) + "','YYYY-MM-DD'),"
                                    else:
                                        print("DataType doesn't match. - " + str(datatypes.get(str(count))) + " Schema - " + str(Schema) + " TableName - " + str(TableName))
                    if TableData != "":
                        InsertScript = "INSERT INTO " + str(TableName_Test) + "(" + str(",".join(TableColumns)) + ") VALUES (" + str(TableData[:len(TableData)-1].encode('ascii', 'ignore').decode('ascii')) + ")"
                        if TableData.startswith("NULL"):
                            if LogEnable == 1:
                                print(InsertScript)
                        else:
                            c = conn.cursor()
                            Query = InsertScript
                            c.execute(Query)
                conn.commit()
                conn.commit()
                PrimaryKeyColumns = []
                c = conn.cursor()
                Query = "SELECT COLUMN_NAME FROM ALL_CONS_COLUMNS WHERE OWNER = '" + str(Schema) + "' AND CONSTRAINT_NAME = (SELECT CONSTRAINT_NAME FROM USER_CONSTRAINTS WHERE UPPER(TABLE_NAME) = UPPER('" + str(TableName) + "') AND CONSTRAINT_TYPE = 'P')"
                c.execute(Query)
                for row in c:
                    PrimaryKeyColumns.append(str(row[0]))
                c = conn.cursor()
                if len(PrimaryKeyColumns) == 0:
                    print(Schema + " - " + TableName + " No Primary Key for this Table.")
                else:
                    Query = "DELETE FROM " + str(TableName) + " WHERE " + str("||'|'||".join(PrimaryKeyColumns)) + " IN (SELECT " + str("||'|'||".join(PrimaryKeyColumns)) + " FROM " + str(TableName_Test) + ")"
                    c.execute(Query)
                    conn.commit()
                    c = conn.cursor()
                    Query = "INSERT INTO " + str(TableName) + " SELECT * FROM " + str(TableName_Test)
                    c.execute(Query)
                    conn.commit()
                    print(Schema + " - " + TableName + " Done.")
            elif TableName != "SQL":
                print(" Check this table exists - " + str(TableName) + " in this Schema - " + str(Schema))
    else:
        print("File Path doesn't exists - " + str(Directory))
    conn.close()