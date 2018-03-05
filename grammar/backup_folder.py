import os
import time

# 创建文件（如果文件不存在的话先创建文件 ）
file_existing = 'if exist dir.txt (echo dir.txt is existed.) else (dir>dir.txt)'
os.system(file_existing)
# 设定压缩文件存放的文件夹
backup_folder = 'backup' + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)
# 设定压缩文件名
backup_file_name = backup_folder + os.sep + time.strftime('%H%M%S') + '.zip'
# 设定压缩文件命令
backup_commond = 'makecab dir.txt ' + backup_file_name
# 备份压缩
if os.system(backup_commond) == 0:
    print('备份成功')
else:
    print('备份失败')
