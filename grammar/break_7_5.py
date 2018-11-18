while True:
    cmd = input('$:')
    if cmd == 'exit':
        break
    elif cmd == 'dir':
        ret = '''
        2018/11/18  20:44    <DIR>          Links
        2018/11/04  12:21    <DIR>          Music
        2018/11/04  12:21    <DIR>          Pictures
        2018/11/04  12:21    <DIR>          Saved Games
        2018/11/04  12:21    <DIR>          Searches
        2018/11/04  12:21    <DIR>          Videos
                       1 个文件            327 字节
                      19 个目录 76,136,419,328 可用字节
        '''
        print('执行{0}完成.'.format(ret))
    else:
        print("'{0}' 不是内部或外部命令，也不是可运行的程序或批处理文件。".format(cmd))
