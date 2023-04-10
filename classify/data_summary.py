import os
import shutil

# class
# 0 : smoke
# 1 : fire
# none : neutral

# read all the files in the folder and then read the lines of files in the folder
def get_directory(path):
    files = []
    for file in os.listdir(path):
        files.append(file)
    return files

# readline the files in the folder and then write the name of the files at each class
# the class is determined by the first word of the line in the file
def get_txt(path, mode):
    files = get_directory(path)
    for file in files:
        file_path = path + '/' + file
        with open(file_path, 'r') as f:
            lines = f.readlines()
        if len(lines) == 0:
            with open(f'D:/bongkj/Dataset/230331_Fire_Dataset/new/Kaggle_D-Fire/{mode}_neutral.txt', 'a') as f:
                f.write(path + '/' + file + '\n')
        else:
            with open(f'D:/bongkj/Dataset/230331_Fire_Dataset/new/Kaggle_D-Fire/{mode}_fire.txt', 'a') as f:
                f.write(path + '/' + file + '\n')


get_txt('D:/bongkj/Dataset/230331_Fire_Dataset/new/Kaggle_D-Fire/D-Fire/train/labels', 'train')
get_txt('D:/bongkj/Dataset/230331_Fire_Dataset/new/Kaggle_D-Fire/D-Fire/test/labels', 'test')

# readline each txt file and then copy/paste the file(from line) to the corresponding class
def get_txt(mode, class_):
    with open(f'D:/bongkj/Dataset/230331_Fire_Dataset/new/Kaggle_D-Fire/{mode}_{class_}.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        line_ = line.replace('labels', 'images')
        line_ = line_.replace('txt', 'jpg')
        try:
            shutil.copy2(line_.split('\n')[0], f'C:/Dataset/Kaggle_D-Fire/{mode}/{class_}/')
        except:
            continue


get_txt('train', 'fire')
get_txt('train', 'neutral')
get_txt('test', 'fire')
get_txt('test', 'neutral')