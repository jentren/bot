from check_luck import check
from load import *
from actions import *
from time import sleep
import keyboard
stategy =[1,1,1,2,2,3] # 1- мираж , 2- небеска , 3 -подземка 
goal = int(input("целевая ")) # целевая заточка
items = int(input("предметов "))     # количество предметов ( максимум 32)
s = int(input("небесок ")) # количество небесных камней 
m = int(input("Миражей ")) # количество миражей
g = int(input("подземок ")) # количество подземок

accept = True

done = int(input("готово "))
actstone = 1 #1 - без ,2-небеска ,3-подземка 
sleep(5)
while done < items and accept:
    if keyboard.is_pressed(('y', 'u', 'i', 'o', 'h', 'j', 'k', 'l', 'b', 'n', 'm')):
            print("Цикл остановлен.")
            break
    change(done+1)
    gear = 0
    while gear<goal and accept:
        if s < 1 or m < 1 or g < 1:
            accept = False
            break
        if stategy[gear] == 1:
            #клик без камня
            if stategy[gear] is not actstone:
                pullout()
                actstone = 1
            click()
        if stategy[gear] == 2:
            #клик небеска
            if stategy[gear] is not actstone:
                insky()
                actstone = 2
            s-=1    
            click()
        if stategy[gear] == 3:
            #клик земля
            if stategy[gear] is not actstone:
                inground()
                actstone = 3
            g-=1
            click()
        m-=1
        sleep(1.5)
        if check():
            gear+=1
        elif actstone == 3:
            gear-=1
        else:
            gear=0

        print(gear)
    done+=1
     # - игра не моментально даёт результат
        
input("нажмите для закрытия ")