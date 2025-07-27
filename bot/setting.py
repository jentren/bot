import pyautogui
import keyboard

# Открытие файла для записи координат
with open("settings.txt", "w") as file:
    
    # Переменная для подсчёта количества записанных координат
    count = 0
    first_two_recorded = False  # Флаг для записи первых двух координат как области

    areainfo1 =""
    areainfo2 =""
    areaitem1=""
    areaitem2=""
    sky=""
    ground=""
    winitem=""
    winstone=""
    buttom=""


    print("Нажмите 'X', чтобы записать координаты мыши.")
    while count < 9:
        if keyboard.is_pressed('z'):
            x, y = pyautogui.position()  # Получение координат мыши
            print(1)
            match count:
                case 0:
                    areainfo1+=f"{x} {y} "
                    file.write(areainfo1+"\n")

                case 1:
                    areainfo2+=f"{x} {y}"
                    file.write(areainfo2+"\n")
                case 2:
                    areaitem1+=f"{x} {y} "
                    file.write(areaitem1+"\n")
                case 3:
                    areaitem2+=f"{x} {y}"
                    file.write(areaitem2+"\n")
                case 4:
                    sky+=f"{x} {y}"
                    file.write(sky+"\n")
                case 5:
                    ground+=f"{x} {y}"
                    file.write(ground+"\n")
                case 6:
                    winitem+=f"{x} {y}"
                    file.write(winitem+"\n")
                case 7:
                    winstone+=f"{x} {y}"
                    file.write(winstone+"\n")
                case 8:
                    buttom+=f"{x} {y}" 
                    file.write(buttom+"\n")
            count += 1
            while keyboard.is_pressed('z'):  # Ожидание отпускания клавиши Z
                pass
