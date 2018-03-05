import os
import time
import zipfile

# 创建文件（如果文件不存在的话先创建文件 ）
file_source = 'dir.txt'
file_creation_command = 'if exist ' + file_source + ' (echo ' + file_source + ' is existed.) else (dir>' + file_source + ')'
os.system(file_creation_command)
# 设定压缩文件存放的文件夹
backup_folder = 'backup' + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)
# 设定压缩文件名
backup_file_name = backup_folder + os.sep + time.strftime('%H%M%S') + '.zip'
# 设定压缩文件命令
with zipfile.ZipFile(backup_file_name, 'w') as myzip:
    myzip.write(file_source)
