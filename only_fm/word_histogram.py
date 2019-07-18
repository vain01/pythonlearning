import os
import string


def get_word_histogram(target_file_path):
    result = {}

    with open(target_file_path, 'r', encoding='UTF-8') as f:
        # 读取每一行
        for line in f:
            # print(line, '')
            # 处理每行单词
            word = ''
            for char in line:
                if char in string.whitespace or char in string.punctuation:
                    result[word] = result.get(word, 0) + 1
                    word = ''
                else:
                    word += char
            if word != '':
                result[word] = result.get(word, 0) + 1
    # 去掉空白单词记录(空白行的时候产生的)
    result.pop('')
    return result


# 显示频率出现最高的7个单词信息
def get_the_highest_frequent_words(result, num):
    print(result[:num])
    for key, freq in result[:num]:
        print(freq, key)


# 获取当前文件路径
FILE_PATH = os.path.abspath(__file__)
# print(FILE_PATH)
# 获取当前目录
BASE_DIR = os.path.dirname(FILE_PATH)
# print(BASE_DIR)
# 获取待处理的文件路径
TARGET_FILE = '43-0.txt'
# print(os.path.abspath(TARGET_FILE))
TARGET_FILE_PATH = BASE_DIR + os.sep + TARGET_FILE

result_dict = get_word_histogram(TARGET_FILE_PATH)
# 排序
result_list = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)

get_the_highest_frequent_words(result_list, 7)
