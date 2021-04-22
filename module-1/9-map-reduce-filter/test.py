from functools import reduce

def solution(digits):
    num_ini = int(reduce(lambda a,b: a if a>b else b , str(digits)))
    num_fin = num_ini + 3
    return digits[num_ini:num_fin]
        
print(solution('19265'))
