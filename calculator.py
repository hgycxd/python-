#coding=utf-8
"""
written by master_yee in python3.5.2

date is 2018-09-28
"""

import math,sys

def calculator(item):
	item=item.replace(' ','')
	item=item.replace('^','**')
	item=item.replace('=','')
	item=item.replace('?','')
	#item=item.replace('%','/100')
	item=item.replace('rad','radians')
	item=item.replace('mod','%')
	functions=['sin','cos','tan','cosh','sinh','tanh','sqrt','pi','radians','e']
	item=item.lower()
	for func in functions:
		if func in item:
			withmath='math.'+func
			item=item.replace(func,withmath)
	try:
		item=eval(item)
	except ZeroDivisionError:
		print("\ncan't divide by 0. please try again")
	except NameError:
		print("invalid input.please try again")
	except AttributeError:
		print("please check usage method and try again")
	return item
def result(item):
	print("\nthe result is:\n\n"+"\033[5;31;43m{0}\033[0m".format(str(calculator(item)))+"\n")
def main():
	while True:
		k=input("--please input formula,or 'quit' to exit:\n")
		if k=="quit":
			break
		result(k)
if __name__=="__main__":
	main()

