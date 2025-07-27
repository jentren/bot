from load import *
import pyautogui

def pullout():
	pyautogui.click(winstone["x"], winstone["y"])

def click():
	pyautogui.click(buttom["x"], buttom["y"])

def insky():
	pyautogui.rightClick(sky["x"], sky["y"])

def inground():
	pyautogui.rightClick(ground["x"], ground["y"])
	
def get_cell_center_coordinates(x, y, cell_number):
    # Нумерация cell_number от 1 до 32
    if not (1 <= cell_number <= 96):
        raise ValueError("Номер ячейки должен быть в диапазоне от 1 до 48")

    # Расчет строки и столбца
    row = (cell_number - 1) // 8
    col = (cell_number - 1) % 8

    # Вычисление координат центра ячейки
    center_x = x + col * 35 + 18
    center_y = y + row * 35 + 18

    return center_x, center_y

def change(item):
	pyautogui.rightClick(get_cell_center_coordinates(areaitem1["x"],areaitem1["y"],item))