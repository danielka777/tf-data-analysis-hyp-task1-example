import pandas as pd
import numpy as np

from statsmodels.stats.proportion import proportions_ztest

chat_id = 1050115025 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    z_stat, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative="smaller")
    
    return p_value <= alpha # Ваш ответ, True или False
