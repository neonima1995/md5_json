import hashlib
import os
import json


def check_sum():
    svn_version = input('SVN_VERSION: ')
    path = input('Folder: ')
    file_json = input('Output JSON Name: ')
    
    while True:
        check_del = input(f'Deleted Start Path "{path}/"? -- y/n: ')
        
        if check_del.lower() == 'y' or check_del.lower() == 'n' or check_del.lower() == 'yes' or check_del.lower() == 'no':
            break

    md5_list = {
        "files":[],
        "svn_version": svn_version,
        "git_version": "175bed51520de09c6020d19bcaecc21834fcd51b"
    }

    print(f'Start Make JSON: "{file_json}.json"')
    
    for rootdir, dirs, files in os.walk(path):
        for file in files:       
            # print (os.path.join(rootdir, file))
            
            with open(os.path.join(rootdir, file), 'rb') as get_file:
                byte_size = get_file.read()
                            
                get_file.close()

                if check_del.lower() == 'y' or check_del.lower() == 'yes':
                    md5_list['files'].append({
                        "size":len(byte_size),
                        "name":str(os.path.join(rootdir, file)).replace('\\', '/').lstrip(f'{path}/'),
                        "md5":str(hashlib.md5(byte_size).hexdigest())
                    })
                    
                else:
                    md5_list['files'].append({
                        "size":len(byte_size),
                        "name":str(os.path.join(rootdir, file)).replace('\\', '/'),
                        "md5":str(hashlib.md5(byte_size).hexdigest())
                    })
                            
        with open(file_json+'.json', 'w') as json_file:
            json_file.write(json.dumps(md5_list))
            json_file.close()
        
if __name__ == '__main__':
    check_sum()
    print('Done!')