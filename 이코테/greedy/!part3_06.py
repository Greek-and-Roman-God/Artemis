def solution(food_times, k):
    answer = 0
    time = 0
    i = 0
    
    while time < k :
        if food_times[i] == 0 :
            i += 1
            if food_times.count(0) == len(food_times) :
                answer = -1
                break
            if i == len(food_times) :
                i = 0
            continue
        food_times[i] -= 1
        time += 1
        i += 1
        if i == len(food_times) :
            i = 0
    
    answer = i + 1
    
    if food_times.count(0) == len(food_times) :
        answer = -1
        
    return answer