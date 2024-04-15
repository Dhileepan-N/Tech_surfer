import os
import shutil
# Folder Should be in following format
#     Module Name
#       -->BO
#       -->MANAGER
#       -->LOCAL
#       -->VAL
#       -->CTL
#       -->JSP
#       -->JASPER
#       -->COMMOON
#         -->HELP_STATEMENT
#         -->SQL_STATEMENT
#         -->FACES_CONFIG
#         -->LABEL_MESSAGES
#         -->JNDI_NAMES
#         -->SCRIPTS
input_Path = 'C:\\Users\\Patterns\\Downloads\\Phase4'
module_name = [x[0]  for x in os.walk(input_Path)][1].split("\\")[-1]

jsp_input_path = input_Path + '\\' + module_name + '\\' + 'JSP'+'\\'
ctl_input_path = input_Path + '\\' + module_name + '\\' + 'CTL'+'\\'
val_input_path = input_Path + '\\' + module_name + '\\' + 'VAL'+'\\'
manager_input_path = input_Path + '\\' + module_name + '\\' + 'MANAGER'+'\\'
bo_input_path = input_Path + '\\' + module_name + '\\' + 'BO'+'\\'
local_input_path = input_Path + '\\' + module_name + '\\' + 'LOCAL'+'\\'
jasper_input_path = input_Path + '\\' + module_name + '\\' + 'JASPER'+'\\'
faces_config_input_file = input_Path + '\\' + module_name + '\\' + 'COMMON'+'\\' + 'FACES_CONFIG.txt'
label_msg_input_file = input_Path + '\\' + module_name + '\\' + 'COMMON'+'\\' + 'LABEL_MESSAGES.txt'
jndi_names_input_file = input_Path + '\\' + module_name + '\\' + 'COMMON'+'\\' + 'JNDI_NAMES.txt'
help_statement_input_file = input_Path + '\\' + module_name + '\\' + 'COMMON'+'\\' + 'HELP_STATEMENT.txt'
sql_statement_input_file = input_Path + '\\' + module_name + '\\' + 'COMMON'+'\\' + 'SQL_STATEMENT.txt'

jsp_workspace_path = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\Panaceaweb\\WebContent' + '\\' + module_name.upper()
ctl_workspace_path = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\Panaceaweb\\src\\panacea'+module_name.upper()+'web\\'+ module_name+'Ctlbean'
val_workspace_path = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\PanaceaValidate\\src\\panacea\\'+module_name.upper()+'action'
local_workspace_path = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\PanaceaEJBClient\\ejbModule\\panacea\\ejb\\view\\' + module_name.upper()
bo_workspace_path = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\PanaceaEJB\\ejbModule\\panacea\\'+ module_name.upper() +'\\ejb'
manager_workspace_path = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\PanaceaUpdate\\src\\panacea\\'+module_name.upper()+'\\Update'
jasper_workspace_path = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\Panaceaweb\\WebContent\\'+module_name.upper()+'\\Reports\\'
faces_config_destination_file = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\Panaceaweb\\WebContent\\ADV\\faces-config.xml'
label_message_destination_file = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\Panaceaweb\\src\\panaceaADVweb\\advMsg\\LabelMsg.properties'
jndi_destination_file = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\panaceaUtils\\src\\panacea\\common\\JNDINames.java'
help_destination_file = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\Panaceaweb\\src\\panaceaweb\\utility\\HelpStmtManager.java'
sql_statement_destination_file = 'E:\\Priya\\TechUpgrade\\Repo\\csbcm-rebase\\panaceaUtils\\src\\panacea\\common\\SQLStmtManager.java'
faces_phrase = '<faces-config>'
jndi_phrase = 'private JNDINames() {};	'
help_statement_phrase = 'private void load'+ module_name.capitalize() +'HelpSQL()'
sql_statement_phrase = 'private void load'+ module_name.upper() +'SQL()'

def isJspFolderHasValidFile():
    global jspErrorMsg
    jspErrorMsg = ''
    if not os.path.exists(jsp_input_path):
        jspErrorMsg = 'File Path does not exists - Jsp'
    elif os.listdir(jsp_input_path) == []:
        jspErrorMsg = 'File not found in Path Given - Jsp'
    if jspErrorMsg == '':
        jsp_files = os.listdir(jsp_input_path)
        for file in jsp_files:
            if not file.endswith('.jsp'):
                jspErrorMsg = 'Inavalid File Format Found in Jsp Folder'
            else:
                jspErrorMsg = ''
def isCtlFolderHasValidFile():
    global  ctlErrorMsg
    ctlErrorMsg = ''
    if not os.path.exists(ctl_input_path):
        ctlErrorMsg = 'File Path does not exists - Ctl'
    elif os.listdir(ctl_input_path) == []:
        ctlErrorMsg = 'File not found in Path Given - Ctl'
    if ctlErrorMsg == '':
        ctl_files = os.listdir(ctl_input_path)
        for file in ctl_files:
            if not file.endswith('.java'):
                ctlErrorMsg = 'Inavalid File Format Found in Ctl Folder'
            else:
                ctlErrorMsg = ''
def isValFolderHasValidFile():
    global valErrorMsg
    valErrorMsg =''
    if not os.path.exists(val_input_path):
        valErrorMsg = 'File Path does not exists - Val'
    elif os.listdir(val_input_path) == []:
        valErrorMsg = 'File not found in Path Given - Val'
    if valErrorMsg == '':
        val_files = os.listdir(val_input_path)
        for file in val_files:
            if not file.endswith('.java'):
                valErrorMsg = 'Inavalid File Format Found in Val Folder'
            else:
                valErrorMsg = ''
def isLocalFolderHasValidFile():
    global localErrorMsg
    localErrorMsg = ''
    if not os.path.exists(local_input_path):
        localErrorMsg = 'File Path does not exists - Local'
    elif os.listdir(local_input_path) == []:
        localErrorMsg = 'File not found in Path Given - Local'
    if localErrorMsg == '':
        local_files = os.listdir(local_input_path)
        for file in local_files:
            if not file.endswith('.java'):
                localErrorMsg = 'Inavalid File Format Found in Local Folder'
            else:
                localErrorMsg = ''
def isB0FolderHasValidFile():
    global boErrorMsg
    boErrorMsg = ''
    if not os.path.exists(bo_input_path):
        boErrorMsg = 'File Path does not exists - BO'
    elif os.listdir(bo_input_path) == []:
        boErrorMsg = 'File not found in Path Given - BO'
    if boErrorMsg == '':
        bo_files = os.listdir(bo_input_path)
        for file in bo_files:
            if not file.endswith('.java'):
                boErrorMsg = 'Inavalid File Format Found in BO Folder'
            else:
                boErrorMsg = ''
def isManagerFolderHasValidFile():
    global managerErrorMsg
    managerErrorMsg = ''
    if not os.path.exists(manager_input_path):
        managerErrorMsg = 'File Path does not exists - Manager'
    elif os.listdir(manager_input_path) == []:
        managerErrorMsg = 'File not found in Path Given - Manager'
    if managerErrorMsg == '':
        manager_files = os.listdir(manager_input_path)
        for file in manager_files:
            if not file.endswith('.java'):
                managerErrorMsg = 'Inavalid File Format Found in Manager Folder'
            else:
                managerErrorMsg = ''
def isJasperFolderHasValidFile():
    global jasperErrorMsg
    jasperErrorMsg = ''
    if not os.path.exists(jasper_input_path):
        jasperErrorMsg = 'File Path does not exists - Jasper'
    elif os.listdir(jasper_input_path) == []:
        jasperErrorMsg = 'File not found in Path Given - Jasper'
    if jasperErrorMsg == '':
        jasper_files = os.listdir(jasper_input_path)
        for file in jasper_files:
            if not (file.endswith('.jasper') or file.endswith('.jrxml')):
                jasperErrorMsg = 'Inavalid File Format Found in Jasper Folder'
            else:
                jasperErrorMsg = ''
def moveJspFile():
    isJspFolderHasValidFile()
    if jspErrorMsg == '':
        try:
            for file in os.listdir(jsp_input_path):
                shutil.copy2(jsp_input_path + file,jsp_workspace_path)
                print('Jsp File ' + file +' moved Successfully')
        except Exception as e:
            print(e)
    else:
        print(jspErrorMsg)
def moveManagerFile():
    isManagerFolderHasValidFile()
    if managerErrorMsg == '':
        try:
            for file in os.listdir(manager_input_path):
                shutil.copy2(manager_input_path + file,manager_workspace_path)
                print('Manager File ' + file +' moved Successfully')
        except Exception as e:
            print(e)
    else:
        print(managerErrorMsg)
def moveBoFile():
    isB0FolderHasValidFile()
    if boErrorMsg == '':
        try:
            for file in os.listdir(bo_input_path):
                shutil.copy2(bo_input_path + file,bo_workspace_path)
                print('BO File ' + file +' moved Successfully')
        except Exception as e:
            print(e)
    else:
        print(boErrorMsg)
def moveLocalFile():
    isLocalFolderHasValidFile()
    if localErrorMsg == '':
        try:
            for file in os.listdir(local_input_path):
                shutil.copy2(local_input_path + file,local_workspace_path)
                print('Local File ' + file +' moved Successfully')
        except Exception as e:
            print(e)
    else:
        print(localErrorMsg)
def moveCtlFile():
    isCtlFolderHasValidFile()
    if ctlErrorMsg == '':
        try:
            for file in os.listdir(ctl_input_path):
                shutil.copy2(ctl_input_path + file,ctl_workspace_path)
                print('Ctl File ' + file +' moved Successfully')
        except Exception as e:
            print(e)
    else:
        print(ctlErrorMsg)
def moveValFile():
    isValFolderHasValidFile()
    if valErrorMsg == '':
        try:
            for file in os.listdir(val_input_path):
                shutil.copy2(val_input_path + file,val_workspace_path)
                print('Validator File ' + file +' moved Successfully')
        except Exception as e:
            print(e)
    else:
        print(valErrorMsg)
def moveJasperFile():
    isJasperFolderHasValidFile()
    if jasperErrorMsg == '':
        try:
            for file in os.listdir(jasper_input_path):
                shutil.copy2(jasper_input_path + file,jasper_workspace_path)
                print('Jasper File ' + file +' moved Successfully')
        except Exception as e:
            print(e)
    else:
        print(jasperErrorMsg)
def update_faces_config():
    with open(faces_config_input_file, 'r+') as faces:
        faces_input_data = faces.readlines()
        faces_input_data.append('\n')
    with open(faces_config_destination_file, 'r+') as f:
        data = f.readlines()
        for (i, line) in enumerate(data):
            if faces_phrase in line:
                index = i
                break
        data.insert(index + 1, ''.join(faces_input_data))
        f.seek(0)
        f.writelines(data)

def update_label_message():
    with open(label_msg_input_file, 'r+') as labels:
        labels_input_data = labels.readlines()
        labels_input_data.append('\n')
    with open(label_message_destination_file, 'r+') as f:
        data = f.readlines()
        data.insert(0, ''.join(labels_input_data))
        f.seek(0)
        f.writelines(data)
def update_jndi_names():
    with open(jndi_names_input_file, 'r+') as jndi:
        jndi_input_data = jndi.readlines()
        #jndi_input_data.append('\n')
    with open(jndi_destination_file, 'r+') as f:
        data = f.readlines()
        for jndi_record in jndi_input_data:
            if jndi_record in data :
                print('JNDI Record Already exists')
            else:
                for (i, line) in enumerate(data):
                    if jndi_phrase in line:
                        index = i
                        break
                data.insert(index + 1, ''.join(jndi_input_data)+'\n')
                f.seek(0)
                f.writelines(data)

def update_help_statement():
    with open(help_statement_input_file, 'r+') as help_statement:
        help_statement_data = help_statement.readlines()
        #jndi_input_data.append('\n')
    with open(help_destination_file, 'r+') as f:
        data = f.readlines()
        for (i, line) in enumerate(data):
            if help_statement_phrase in line:
                index = i
                break
        data.insert(index + 2, ''.join(help_statement_data)+'\n')
        f.seek(0)
        f.writelines(data)
def update_sql_statement():
    with open(sql_statement_input_file, 'r+') as sql_statement:
        sql_statement_data = sql_statement.readlines()
    with open(sql_statement_destination_file, 'r+') as f:
        data = f.readlines()
        for (i, line) in enumerate(data):
            if sql_statement_phrase in line:
                index = i
                break
        data.insert(index + 2, ''.join(sql_statement_data)+'\n')
        f.seek(0)
        f.writelines(data)
moveJspFile()
moveCtlFile()
moveValFile()
moveLocalFile()
moveBoFile()
moveManagerFile()
moveJasperFile()
update_faces_config()
update_label_message()
update_jndi_names()
update_help_statement()
update_sql_statement()