"""
В этом задании вам нужно создать интерфейс для работы с файлами. Класс File должен поддерживать несколько необычных операций.

Класс инициализируется полным путем.

obj = File('/tmp/file.txt')

Класс должен поддерживать метод write.

obj.write('line\n')

Объекты типа File должны поддерживать сложение.


first = File('/tmp/first')
second = File('/tmp/second')
new_obj = first + second
В этом случае создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.

Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.


for line in File('/tmp/file.txt'):
  ...
И наконец, при выводе файла с помощью функции print должен печататься его полный путь, переданный при инициализации.


obj = File('/tmp/file.txt')
print(obj)
'/tmp/file.txt'
Опишите свой класс в скрипте и загрузите на платформу.
"""

import os
import tempfile


class File:
	def __init__(self, file_path):
		self.file_path = file_path
		self.lines = ''

		if os.path.exists(self.file_path):
			with open(self.file_path) as file:
				self.file_data = file.read()
			
			self.lines = self.file_data.split('\n')


	def write(self, new_line):
		try:
			with open(self.file_path, 'w') as file:
				file.write(new_line)
		except IOError:
			print('File does not exists, path:', self.file_path)

	def __add__(self, other):
		# https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir
		temp_path = os.path.join(tempfile.gettempdir(), 'tmp.txt')
		temp = File(temp_path)

		with open(self.file_path, 'r') as file:
			file1 = file.read()

		with open(other.file_path, 'r') as file:
			file2 = file.read()

		temp.write(file1 + file2)

		return temp

	def __str__(self):
		return self.file_path

	def __iter__(self):
		self.iter = 0
		return self

	def __next__(self):
		if self.iter >= len(self.lines):
			raise StopIteration

		result = self.lines[self.iter]
		self.iter += 1

		return result

# obj = File('/tmp/file.txt')
# print(obj)