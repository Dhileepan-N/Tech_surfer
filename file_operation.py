file = open('C:\\Users\Patterns\Downloads\PKG_DLY_COLL_PROCESS.pck','r')
path = 'C:\\Users\Patterns\Downloads\\'
filename = input("Enter the Package Name : ")
extension = '.pck'
# try:
#     file = open(path + str(filename) + extension, 'r')
# except:
#     print('File not Found')
lines = file.readlines()
from_tables = []
insert_tables = []
update_tables = []
delete_tables = []

for line in lines:
    if line.find('DELETE FROM ') != -1:
        words = line.split('DELETE FROM ')
        word = words[1].split(' ')
        delete_tables.append(word[0])
print(delete_tables)

for line in lines:
    i = 0
    if line.find(' FROM '.casefold()) != -1 :
        print(i)
        words = line.split(' FROM ')
        word = words[1].split(' ')
        from_tables.append(word[0])
        i = i+1;
from_tables_final = [x for x in from_tables if x not in delete_tables]
print(from_tables)
print(from_tables_final)
for line in lines:
    if line.find('INSERT INTO ') != -1:
        words = line.split('INSERT INTO ')
        word = words[1].split('(')
        insert_tables.append(word[0])
print(insert_tables)

for line in lines:
    if line.find('UPDATE ') != -1:
        words = line.split('UPDATE ')
        word = words[1].split(' ')
        update_tables.append(word[0])
print(update_tables)

