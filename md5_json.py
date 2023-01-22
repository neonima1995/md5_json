import hashlib
import os
from datetime import datetime
import json


def check_sum():
    svn_version = input('Введи SVN_VERSION: ')
    while True:
        folder = input('Path/Exit: ')
        
        if folder.lower() == 'exit':
            return
        
        try:
            file = os.listdir(folder)
        
        except:
            print('Папки не существует :(')
        
        else:
            if file:
                md5_list = {
                    "files":[],
                    "svn_version": svn_version,
                    "git_version": "175bed51520de09c6020d19bcaecc21834fcd51b"
                }
                
                for files in file:
                    if '.' in files:
                        with open(folder+'/'+files, 'rb') as get_file:
                            byte_size = get_file.read()
                            
                        get_file.close()

                        md5_list['files'].append({
                            "size":len(byte_size),
                            "name":get_file.name,
                            "md5":str(hashlib.md5(byte_size).hexdigest())
                        })
                        
                with open('file_'+svn_version+'_'+str(datetime.now().strftime('%y.%m.%d(%H-%M-%S)'))+'.json', 'w') as json_file:
                    json_file.write(json.dumps(md5_list))
                    json_file.close()
            
            else:
                print('Данная папка пуста!')
        
if __name__ == '__main__':
    check_sum()
    print('***BYE***')