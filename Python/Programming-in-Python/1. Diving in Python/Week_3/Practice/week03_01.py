"""
Programming assignment: Реализация простого класса для чтения из файла

Первое задание у нас для разогрева. Ваша задача написать Python-модуль solution.py, внутри которого определен класс FileReader.

Инициализатор этого класса принимает аргумент - путь до файла на диске.

У класса должен быть метод read, возвращающий содержимое файла в виде строки.

Еще один момент - внутри метода read вы должны обрабатывать исключение IOError, возникающее, когда файла, с которым был инициализирован класс, на самом деле нет на жестком диске. 
В случае возникновения такой ошибки метод read должен возвращать пустую строку "".

То есть класс должен работать следующим образом:

reader = FileReader("example.txt")
print(reader.read())

"""

class FileReader:

	def __init__(self, filename):
		self._filename = filename

	def read(self):
		try:
			file = open(self._filename, 'r')
			file = file.read()
			return file
		except IOError:
			return ""
		finally:
			file.close()


reader = FileReader("example.txt")
print(reader.read())
