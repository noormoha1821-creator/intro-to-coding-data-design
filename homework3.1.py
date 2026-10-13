# the first Exercise 
# by Noor Muaydh
while True :
    city = input("Please enter the name the cities :") 
    if city == "exit" :
        print("bye")
        break
    temp_f = float(input("Enter the the current temperature in farenheit in "+ city +" :"))
    temp_c = float((temp_f - 32 )* 5/9 )
    if  temp_c <= 0 :
        print("Alert!: The temperature in "+ city +" is below freezing point")
    else : 
        print("The temperature in "+ city +" is above the freezing point")
        print( city + "'s Temperature in Celsius :", temp_c)