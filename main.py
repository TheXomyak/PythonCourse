import os
import shutil
from datetime import datetime

# print(os.getcwd())
# os.chdir("test")
# print(os.getcwd())

#
# dir1 = os.listdir()
# print(dir1)
# dir1 = os.listdir('..')
# print(dir1)

# dir_name = 'test2'
# os.mkdir(dir_name)
# dir_name2 = 'test3/test4'
# os.mkdir(dir_name2)
# dir_name3 = 'test3/test4'
# os.makedirs(dir_name3)
#
# obj = os.walk(os.getcwd())
# print(obj)
# # for elem in obj:
# #     print(elem)
# print(obj.__next__())

# os.rmdir('test')
# os.removedirs('test3/test4')


# os.remove('test.py')

# os.rename('app.py', 'new_app.py')
# os.rename('test2', 'new_test')

# status = os.stat('new_test')
# print(datetime.fromtimestamp(status.st_mtime))

# name = os.path.basename(r'C:\PythonProjects\AiogramBotWeatherProject\main.py')
# print(name)

# name = os.path.dirname(r'C:\PythonProjects\AiogramBotWeatherProject')
# print(name)
#
# print(os.path.isdir('new_test'))
# print(os.path.isfile('main.py'))

# shutil.copy2('main.py', 'main2.py')


dir = 'new_test'
file = 'main2.py'
shutil.move(file, dir)