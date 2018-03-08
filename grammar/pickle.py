# 本程序在Win10x64环境下python3.6运行失败，报错：
#   File "D:/github/pythonlearning/grammar/pickle.py", line 1, in <module>    import pickleFile "D:/github/pythonlearning/grammar/pickle.py", line 1, in < module >
# import pickle

import pickle

shoplist_file = 'shotlist.txt'
shoplist = ['Mango', 'Apple', 'Pear']

file = open(shoplist_file, 'wb')
pickle.dump(shoplist, file)
file.close()

del shoplist

file = open(shoplist_file, 'rb')
shoplist_load = pickle.load(shoplist_file)
file.close()

print(shoplist_load)
