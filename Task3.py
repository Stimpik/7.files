import os

files = os.listdir()
txt = [file for file in files if file.endswith('.txt')]
all_files = []
for files in txt:
    temp = []
    file = open(files, 'r', encoding='utf-8')
    temp.append(file.name + '\n')
    temp.append(str(len(file.read().split('\n'))) + '\n')
    file = open(files, 'r', encoding='utf-8')
    temp.append(file.read() + '\n')
    all_files.append(temp)


def func_for_sort(file):
    return int(file[1][0])


result = open('Result/result.txt', 'a', encoding='utf-8')

for file in sorted(all_files, key=func_for_sort):
    result.writelines(file)
