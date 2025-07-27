import actions as act
import time
import sys

# Чтение аргумента
number = int(sys.argv[1])


time.sleep(2)
for i in range(1,number):
	act.change(i)