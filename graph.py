import matplotlib.pyplot as plt

y1 = [] # count marage
y2 = [] # middle count


with open("данные.txt", "r", encoding="utf-8") as file:
	numbers = [int(line.strip()) for line in file]

all = 0
last = 0


for i in numbers:
    all+=1
    last+=1
    if i == 3:
        y1.append(last)
        y2.append(all/len(y1))
        last = 0


plt.plot(y1)
plt.plot(y2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("График")
plt.grid(True)
plt.show()