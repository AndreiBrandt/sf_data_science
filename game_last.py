"""Игра угадай число"""
import numpy as np

def random_predict(number:int=1) -> int:
    
    count = 0
    min = 1 
    max = 101
    predict_number = 50
    while True:
        
        count+=1
        #predict_number = np.random.randint(min, max)
        
        if number == predict_number:
            break
        elif number > predict_number:
            min = predict_number
            predict_number = int(min + len(range(min,max+1))/2)
            print(f'Загаданное число больше {predict_number}')
        elif number < predict_number:
            max = predict_number
            predict_number = int(max - len(range(min,max+1))/2)
            
            
            print(f'Загаданное число меньше {predict_number}')
   
    return (count)
        
def score_game (random_predict):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size =(2))  
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(score) 
    return(score)
    
    
if __name__ == '__main__':
    score_game(random_predict)
    



