from time import sleep
print(1)
print(1)
a = 1
b = 1
c = a + b
while True:
	print(c)
	b = a
	a = c
	c = a + b
	sleep(0.1)
