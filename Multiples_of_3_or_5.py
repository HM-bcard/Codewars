def solution(number):
    pass
    sum = 0
    if number <0:
       return 0
    else:
        for n in range (1,number):
            if n % 3 == 0:
                sum += n
            elif n % 5 ==0:
                sum  += n
            else:
                continue
    return sum


    
