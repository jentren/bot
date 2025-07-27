import pyautogui
import time
from PIL import Image
import numpy as np
from load import areainfo1, areainfo2

SETTINGS_FILE = 'settings.txt'

# Эталонные цвета для удачи и неудачи
COLOR_SUCCESS = np.array([14, 94, 9])      # Удача (зелёный)
COLOR_FAILURE = np.array([66, 53, 25])     # Неудача (жёлтый)

x1, y1, x2, y2 = 186 ,412 ,420 ,432

def get_average_color(x1, y1, x2, y2):
    """Определяет средний цвет текста в заданной области"""
    img = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    img = img.convert('RGB')
    img_array = np.array(img)
    
    # Получаем средний цвет изображения
    avg_color = np.mean(img_array, axis=(0, 1)).astype(int)
    return avg_color

def get_result_color(avg_color):
    """Определяет, ближе ли цвет к удаче или неудаче"""
    # Считаем расстояние до эталонных цветов
    dist_success = np.linalg.norm(avg_color - COLOR_SUCCESS)
    dist_failure = np.linalg.norm(avg_color - COLOR_FAILURE)
    
    # Определяем, какой цвет ближе
    if dist_success < dist_failure:
        return True
    else:
        return False

def check():   
    avg_color = get_average_color(areainfo1["x"],areainfo1["y"],areainfo2["x"],areainfo2["y"])
    result = get_result_color(avg_color)
    return result

