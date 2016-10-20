import math 
def _sum (_list):
	_sum_ = _list[0]
	for i in range(1,len(_list)):
		_sum_ = _sum_ + _list[i] 
	return _sum_

def product (_list):
    prod = 1
    if len(_list) == 1:
    	for i in range(1,_list[0]+1):
    		prod *= i
    	return prod	
    else:
    	for i in _list:
    		prod *= i
    	return prod 

def reverse (_list):
	return _list[::-1]

def max (_list):
    result = _list[0]
    for i in range(1,len(_list)):
    	if _list[i] > result:
    	    result = _list[i]
    return result	    	

def min (_list):
    result = _list[0]
    for i in range(1,len(_list)):
    	if _list[i] < result:
    	    result = _list[i]
    return result

def cumulative_pro (_list):
    prod = 1
    new_list = []
    for i in _list:
    	prod *= i
    	new_list.append(prod)
    return new_list     

def cumulative_sum (_list):
    _sum = 0
    new_list = []
    for i in _list:
    	_sum += i
    	new_list.append(_sum)
    return new_list  

def unique (_list):
	_list.sort()
	new_list = []
	new_list.append(_list[0])
	for i in range(1,len(_list)):
		if _list[i] != _list[i-1]:
			new_list.append(_list[i])
	return new_list		

def dups (_list):
	_list.sort()
	new_list = []
	if _list.count(_list[0]) > 1:
		new_list.append(_list[0])
	for i in range(1,len(_list)):
		if (_list[i] != _list[i-1]) and (_list.count(_list[i]) > 1):
			new_list.append(_list[i])
	return new_list	


def group (_list, div):
	#div = ord(div) - ord("0")
	new_list = []
	shift = math.ceil(len(_list)/div)
	print (shift)
	n = 0
	for i in range (0,div):
		if n+shift > len(_list)-1:
			new_list.extend([_list[n:]])
			print("Hmmmmm")
			return new_list
		else:
			new_list.extend([_list[n:n+shift]])
			n += shift  
			print ("zxc")	


_list = [1,2,3,4,5,6]
print(group(_list,3))		


