import time
import random


def run(d, i):

	n = [3,4,5,6,7,8,9,11,12]

	for i in range(i):
		x = n[random.randint(0, len(n)-1)]
		y = n[random.randint(0, len(n)-1)]

		if not x*y in d:
			d[x*y] = [0, 0, 0]

		right = True
		start = time.time()
		
		ans = int(input("{} x {} = ".format(x,y)))

		while ans != x*y:
			ans = int(input("{} x {} = ".format(x,y)))
			right = False

		end = time.time()

		if right:
			d[x*y][0] += 1

		d[x*y][1] += end-start
		d[x*y][2] += 1

	return d



d = {}

while True:
	x = input("Rounds: ")
	if x == "q":
		break
	else:
		d = run(d, int(x))



for each in d:
	print(each, d[each][0]/d[each][2], d[each][1]/d[each][2])

print(d)

