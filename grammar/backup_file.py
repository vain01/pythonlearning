import os
import time

# only for windows
source = 'D:' + os.sep + 'mp4'
target = 'D:\\backup\\mp4'
backup_common = 'robocopy {0} {1} /MIR'.format(source, target)
print(backup_common)

# 执行备份
if os.system(backup_common) == 0:
    print('备份成功')
else:
    print('备份失败')
