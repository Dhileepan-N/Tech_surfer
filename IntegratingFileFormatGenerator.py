import os
basePath = 'E:\\My ProgramS\\'
filename = 'NEW'
# Label_msg_file_name = 'Label_messages.txt'
# jndi_file_name = 'jndi.txt'
# faces_config_file_name = 'faces_config.txt'
# sql_token_file_name = 'sql_token.txt'
# help_statement_file_name = 'help_statement.txt'
# scripts_file_name = 'scripts.txt'
others_file_name = ['LABEL_MESSAGES.txt','JNDI_NAMES.txt','FACES_CONFIG.txt','c.txt','HELP_STATEMENT.txt','SCRIPTS.txt']
programPath =  basePath + filename + '\\'
others_base_path = programPath + '\\' + 'OTHERS' + '\\'
os.mkdir(programPath)
os.mkdir(programPath + '\\' + 'JSP')
os.mkdir(programPath + '\\' + 'CTL')
os.mkdir(programPath + '\\' + 'VAL')
os.mkdir(programPath + '\\' + 'BO')
os.mkdir(programPath + '\\' + 'LOCAL')
os.mkdir(programPath + '\\' + 'MANAGER')
os.mkdir(programPath + '\\' + 'OTHERS')
os.mkdir(programPath + '\\' + 'JASPER')
for file in others_file_name:
    with open(os.path.join(others_base_path,file),'w'):
        pass