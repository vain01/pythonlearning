import os, glob
from dive_into import humansize
# import humansize

print(os.path.join('a', 'b'))
print(os.getcwd())
# os.chdir('xx\yy')
print(os.path.expanduser('~'))

pub_key = os.path.join(os.path.expanduser('~'), '.ssh', 'id_rsa.pub')
print(pub_key)
dir_name, file_name = os.path.split(pub_key)
print(dir_name)
print(file_name)
short_name, extension = os.path.splitext(file_name)
print(short_name)
print(extension)

os.chdir('D:\\github\\pythonlearning\\dive_into')
print(os.getcwd())
print(glob.glob('*.py'))
print([os.path.realpath(f) for f in glob.glob('*.py')])
print([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')])
print([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py') if os.stat(f).st_size < 1000])
print([(humansize.approximate_size(os.stat(f).st_size), os.path.realpath(f)) for f in glob.glob('*.py') if os.stat(f).st_size < 1000])
