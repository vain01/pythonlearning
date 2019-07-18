import os

cmd = 'ls -l'
fp = os.cpu_count()
print(fp)
fp = os.popen(cmd)
print(fp)
for line in fp:
    print(line, '')
fp.close()
