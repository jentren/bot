with open('settings.txt', 'r', encoding='utf-8') as f:


	mas__ = []

	for line in f:
		x1,y1 = map(int, line.split())
		mas__.append({"x": x1, "y": y1})



areainfo1=mas__[0]
areainfo2=mas__[1]
areaitem1=mas__[2]
areaitem2=mas__[3]
sky=mas__[4]
ground=mas__[5]
winitem=mas__[6]
winstone=mas__[7]
buttom=mas__[8]
