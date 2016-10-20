import math
import os

def lensort (i_list):
	i_list.sort(key = len)
	
	return i_list

def unique (_list):
	
	new_list = []
	_list[0] = _list[0].lower()
	new_list.append(_list[0])
	for i in range(0,len(_list)):
		_list[i] = _list[i].lower()
	_list.sort()	
	for i in range(1,len(_list)):
		if _list[i] != _list[i-1]:
			new_list.append(_list[i])
	return new_list


def extsort():
	directory = "C:\\Users\\пк\\Desktop\\CS102"
	files = os.listdir(path = directory)
	return files


reverse_file = lambda f: f[::-1]

_list = ['1a','1asd','2','5']
print(lensort(_list))	