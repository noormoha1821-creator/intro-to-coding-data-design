# the second Exercise 
# by Noor Muaydh
high_temp = None
low_temp = None
high_city = ""
low_city = ""
while True :
    city = input("Please enter the name the cities :")
    if city == "exit" :
        break
    temp_f = float(input("Enter the the current temperature in farenheit in "+ city +" :"))
    temp_c = float((temp_f - 32 )* 5/9 )
    word = None
    if  temp_c == 0 :
        word = "equals"
    elif  temp_c < 0 :
        word = "below"
    else : 
        word = "above"
    print("The temperature in "+ city +" is " + word +" the freezing point")
    print( city + "'s Temperature in Celsius :", temp_c) 
    if low_temp > temp_c :
        low_temp = temp_c
        low_city = city
    if high_temp < temp_c :
        high_temp = temp_c
        high_city = city
print("summery :- ")
print("--------------------------------------------------------------------")
print("The highest temperature is " , high_temp , " in "+high_city+" .")
print(".The lowest temperature is " , low_temp , " in "+low_city+" .")
print("--------------------------------------------------------------------")