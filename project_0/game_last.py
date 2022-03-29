import numpy as np

def random_predict(number:int=1) -> int:
    #Функция пытается угадать загаданное на отрезке от 1 до 100.  
    #Где number - загаданное число, min_number - нижняя граница. max_number - верхняя граница, count - кол-во попыток.
    #На каждом шаге цикла, если число не угадано, ищется среднее значение между границами,
    #которое изменяет нижнюю или верхнюю границу собой, в зависимости от того больше или меньше загаданное число. 
    #При завершении функции возвращается количество попыток с которого получилось угадать загаданное число.
    count = 0
    min_number = 1 
    max_number = 100
    predict_number = int((min_number+max_number)/2)
    while True:
        count += 1
        if number > predict_number:
            min_number = predict_number
            predict_number = round((min_number+max_number)/2)
        elif number < predict_number:
            max_number = predict_number
            predict_number = int((min_number+max_number)/2)
        else:
            break
    return (count)
        
def score_game (random_predict):
    #Функция создает список random_array с 1000 рендомными значениями от 1 до 100.
    #И сохраняет с какой попытки было угадано число в переменную count_ls. 
    #По окончанию возвращает переменную score, в которой храниться среднее значение всех попыток. 
    count_ls = []
    random_array = np.random.randint(1, 101, size =(1000))  
    for number in random_array:
        count_ls.append(random_predict(number))
     
    score = int(np.mean(count_ls))
    print(f'Программа угадывает загаданное число в среднем за {score} попыток.') 
    return(score)

    
if __name__ == '__main__':
    score_game(random_predict)
    



