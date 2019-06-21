import os


def walk_files(directory_path):
    for name in os.listdir(directory_path):
        path = os.path.join(directory_path, name)

        if os.path.isdir(path):
            print(path)
            walk_files(path)
        else:
            print(path)


path = '.'
walk_files(path)
