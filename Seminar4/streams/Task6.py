# Задание №6
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.

import asyncio
import os
import aiofiles
import time
#pip install aiofiles

async def readfile(folder, file):
    filename = os.path.join(folder, file)
    async with aiofiles.open(filename, 'r', encoding='utf-8') as f:
        content = await f.read()
    count = len(content.split())
    print(f'Количество слов в файле {file} {count}. Посчитано за {time.time()- start_time:.2f} сек.')
    
    
folder = 'thread'    
start_time = time.time()


async def main():
    process = []
    files = os.listdir(folder)
    for file in files:
        proc = asyncio.ensure_future(readfile(folder, file))
        process.append(proc)
    await asyncio.gather(*process)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())