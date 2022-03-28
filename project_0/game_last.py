import numpy as np

def random_predict(number:int=1) -> int:
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
    count_ls = []
    random_array = np.random.randint(1, 101, size =(1))  
    for number in random_array:
        count_ls.append(random_predict(number))
     
    score = int(np.mean(count_ls))
    print(score) 
    return(score)

    
if __name__ == '__main__':
    score_game(random_predict)
    



