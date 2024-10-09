listt = list(range(1,100))
print(list)



def generators (list = listt, adjacent_digit = 2): 
    for i in range(len(list) - adjacent_digit + 1): 
        digits = listt[i:i +adjacent_digit] 
        sum = 1
        for digit in digits: 
            sum += int(digit)
        final_sum = sum 
        print(final_sum)
   
generators()


def generator(list = listt, adjacent_digit = 1): 
    for i in range(len(list) - adjacent_digit + 1): 
        digits = listt[i:i + adjacent_digit]
        for digit in digits: 
            sum = listt[i] + digit
        return sum

generator ()



listt = list(range(1,100))
result = []
s = 0 

for i in listt: 
    s=+ i 
    result.append(s)

print(result)

