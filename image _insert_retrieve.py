import cx_Oracle
import base64
from datetime import date
import img2pdf
filename = 'assassins'
# img = cv2.imread('C:\\Users\Patterns\Desktop\assasins.jpeg')
# with open(r'C:\\Users\Patterns\Desktop\Assasins.jpg', 'rb') as image_file:
#     blob = base64.b64encode(image_file.read())
    # data = [filename, blob]
try:
    # con = cx_Oracle.connect('CSBMARVP_FEE/CSBMARVP_FEE@localhost:1521/orcl')
    data = [
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',1000,'',101,'0','0','','0','0','F',10000,200,1000,500,100,''),
('1017700006728','514256','Collerctor3','','',9999.06,'',101,'0','0','','0','0','F',10000,200,1000,500,100,'')
]
    con = cx_Oracle.connect('csbmarvp/csbmarvp@192.168.1.91:1521/oracsbdb')
    cur = con.cursor()
    # insert_query = ('insert into IMAGEUPLOAD (filename,image)' 'values(:filename, :blob)')
    insert_query = ('insert into CBS_STG_PAYMENT (SZLEGACYAGREEMENTNUM,SZLEGACYCUSTOMERNUM,SZCOLLECTORCODE,DTBUSIDATE,DTACTIVITY,FAMOUNT,DTRECEIPTDATE,IRECEIPTNO,SZINSTRUMENTTYPE,SZCHECKNO,DTINSTRUMENTDATE,SZBANK,SZBANKBRANCH,FSTATUS,FEMIODC,FCC,FPRNCOLLECTED,FINTCOLLECTED,FPENALCHARGES,DTUPDTIMESTAMP)' 'values(:SZLEGACYAGREEMENTNUM,:SZLEGACYCUSTOMERNUM,:SZCOLLECTORCODE,:DTBUSIDATE,:DTACTIVITY,:FAMOUNT,:DTRECEIPTDATE,:IRECEIPTNO,:SZINSTRUMENTTYPE,:SZCHECKNO,:DTINSTRUMENTDATE,:SZBANK,:SZBANKBRANCH,:FSTATUS,:FEMIODC,:FCC,:FPRNCOLLECTED,:FINTCOLLECTED,:FPENALCHARGES,:DTUPDTIMESTAMP)')
    select_query = ('select IMAGE from  IMAGEUPLOAD')
    cur.executemany(insert_query, data)
    con.commit()
    print('Insertion Complete')
    # cur.execute(select_query)
    # records = cur.fetchone()
    # retrived_blob = records[0]
    # out_imagefile = open(r'C:\\Users\Patterns\Desktop\new.jpg' , 'wb')
    # out_imagefile.write(base64.b64decode(retrived_blob.read()))
    # out_pdffile = open(r'C:\\Users\Patterns\Desktop\image.pdf' , 'wb')
    # out_pdffile.write(base64.b64decode(retrived_blob.read()))
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)