import os
file_path = 'E:\\test-2'
destination_path = 'E:\\test-1'
for file in os.listdir(file_path):
    if len(os.listdir(file_path + '\\' +file)) == 3:
        os.replace(file_path + '\\' +file, destination_path+ '\\' +file)
