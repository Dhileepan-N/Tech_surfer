import xlrd
import json
from test import *

class eXcelToJson():

    def __init__(self, filename):
        self.filename = filename

    def cnvrtxl2json(self):

        file_path = 'C:\\Users\Patterns\Desktop\\'
        try:
            wb = xlrd.open_workbook(file_path + str(self.filename) + '.xls')
            sheet = wb.sheet_by_index(0)
            temp_json = {}
            json_content = {}

            for i in range(sheet.nrows):
                for j in range(sheet.ncols):
                    if i > 0:
                        temp_json[sheet.cell_value(0, j)] = sheet.cell_value(i, j)
                        json_content[i] = temp_json.copy()
            print(json_content)
            json_file = json.dumps(json_content)
            with open(file_path + filename + '.json', "w") as outfile:
                outfile.write(json_file)
        except FileNotFoundError:
            print("Wrong file or file path")


if __name__ == '__main__':
    filename = input("Enter the Filename without extention : ")
    excel2jsonobject = eXcelToJson(filename)
    # name = excel2jsonobject.getfilename()
    excel2jsonobject.cnvrtxl2json()
