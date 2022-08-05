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
			r = input("Try agian(y/n): ")
	if status:
		i += 1
		continue
	print(i)
	i += 1
print('Code ended')