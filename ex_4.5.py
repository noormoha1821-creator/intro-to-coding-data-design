# fifth Exercise 
# by Noor Muaydh
numbers = []
while True :
    num = (input("enter a number ( type exit if not ) : ")).strip()
    if num == "exit".strip() :
        break
    num = int(num)
    numbers.append(num)
if numbers :
    high_num = numbers[0]
    low_num = numbers[0]
    for num in numbers:
        if num < low_num:
            low_num = num
        if num > high_num:
            high_num = num
print("--------------------------------------------------------------------")
print(numbers)
print("The highest number is " , high_num , " .")
print("The lowest number is " , low_num , " .")
print("--------------------------------------------------------------------")