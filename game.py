"""Игра угадай число"""
import numpy as np
number = np.random.randint(1,101) #загадываем число
number_2 = np.random.randint(1,101) #загадываем число
count = 0
count_2 = 0
while True:
    count+=1
    predict_nubmer = int(input("Наташа угадай число от 1 до 100: "))
    if predict_nubmer > number:
        print("Число должно быть меньше")
    elif predict_nubmer < number:
        print("Число должно быть больше")    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры если угадали
    
while True:
    count_2+=1
    predict_nubmer_2 = int(input("Андрей угадай число от 1 до 100: "))
    if predict_nubmer_2 > number_2:
        print("Число должно быть меньше")
    elif predict_nubmer_2 < number_2:
        print("Число должно быть больше")    
    else:
        print(f"Вы угадали число! Это число = {number_2}, за {count_2} попыток")
        break #конец игры если угадали
    
if count > count_2:
    print("Мастер игры победил!")
elif count < count_2:
    print("Победил Зайчик Мастера игры победил!")
else:
    print("Победила дружба Мастера игры и Зайчика Мастера игры")
    

    
    