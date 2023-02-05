import numpy as np

# Активационная функция
def f(x):
    return np.where(x > 0, 1, 0)
    
def not_xor(x1, x2):

    # Задаем веса
    w1 = np.array([[3/2, -1/2], [-1, 1], [-1, 1]]) 
    w2 = np.array([[3/2], [-1], [-1]])

    # Работа со входными данными
    inputs = np.array([x1, x2])
    inputs = f(np.matmul(np.append([1], inputs), w1)) # Перемножение матриц и вызов функции активации
    inputs = f(np.matmul(np.append([1], inputs), w2)) # Перемножение матриц и вызов функции активации
    # print(inputs)
    return inputs[0]

# Вывод результатов (должны получиться противоположные функции xor результаты) 
print(not_xor(0, 0)) # 1
print(not_xor(0, 1)) # 0
print(not_xor(1, 0)) # 0 
print(not_xor(1, 1)) # 1
