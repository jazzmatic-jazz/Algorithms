#Fizz Buzz algorithm
# Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively.
# multiple of 3 AND 5, the number is replaced with "fizz buzz."
import numbers


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = []

for i in number:
    if i%3 ==0 and i%5==0 :
        # print("fizz buzz")
        a.append('fizz buzz')
    
    elif i%3 == 0:
        # print("fizz")
        a.append('fizz')

    elif i%5 == 0:
        # print("buzz")
        a.append('buzz')

    else:
        # print(i)
        a.append(i)

print(a)
