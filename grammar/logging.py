# 此程序不能运行，不能正确载入logging模块
import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), 'test.log')
    print(logging_file)
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
    print(logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filemode='w'
)

logging.debug('Start of the program')
logging.debug('Doing something')
logging.warning('Dying now')
