'''
1) Create a code that does
nothing using loops. It must
end at some point
2) Create a code that stops
when the user says stop, bye,
quit, or q
3) Make a program that prints
the numbers from 1 to 10, but
the user can tell the code to
skip a number or not

'''

def num1():
	for i in range(1, 10):
		pass
	print("Code ended")
def num2():
	while True:
		r = input('Say something i\'m givin up on you...  ')
		if r == 'stop':
			break
		elif r == 'bye':
			break
		elif r == 'quit':
			break
		elif r == 'q':
			break
def num3():
	i = 1
	while i <= 10:
		status = False
		r = input('Skip the number(y/n)? ')
		while True:
			if r == 'y':
				status = True
				break
			elif r == 'n':
				break
			else:
				a = input("Try agian(y/n): ")
		if status:
			i += 1
			continue
		print(i)
		i += 1
	print('Code ended')
num1()