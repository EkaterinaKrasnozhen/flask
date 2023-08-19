# Задание №5
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.
import os
from multiprocessing import Process, Pool
import time


def readfile(folder, file):
    filename = os.path.join(folder, file)
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    count = len(content.split())
    print(f'Количество сло в файле {file} {count}. Посчитано за {time.time()- start_time:.2f} сек.')
    
    
folder = 'thread'    
processes = []
start_time = time.time()


if __name__ == '__main__':
    files = os.listdir(folder)
    for file in files:
        process = Process(target=readfile, args=(folder, file,))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()