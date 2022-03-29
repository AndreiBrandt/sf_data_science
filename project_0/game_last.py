import numpy as np

def random_predict(number:int=1) -> int:
    #The function tries to guess the guessed number  on the segment from 1 to 100.
    #Where number is the guessed number, min_number is the lower bound. max_number - upper bound, count - number of attempts.
    #At each step of the loop if the number is not guessed, the average value between the boundaries is searched,
    #which changes the lower or upper bound by itself, depending on whether the guessed number is greater or less.
    #At the end of the function, the number of attempts from which it turned out to guess the guessed number is returned.
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
    #The function creates a random_array list with 1000 random values ​​from 1 to 100.
    #And stored with whatever reversed number is in the count_ls variable.
    #When finished, it returns a variable grade that stores the average of all grades
    count_ls = []
    random_array = np.random.randint(1, 101, size =(1000))  
    for number in random_array:
        count_ls.append(random_predict(number))
     
    score = int(np.mean(count_ls))
    print(f'Программа угадывает загаданное число в среднем за {score} попыток.') 
    return(score)

    
if __name__ == '__main__':
    score_game(random_predict)
    



