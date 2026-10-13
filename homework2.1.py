# the first Exercise 
# by Noor Muaydh
city1 = input("Hello User . Please enter the name of the first city :")
temp_f = float(input("Enter the the current temperature in Farenheit in "+ city1 +" :"))
temp_c = ((temp_f - 32 )* 5/9 )
if temp_c <= 0 :
    print("Alert!: The temperature is below freezing point")
else : 
    print("The temperature is above the freezing point")
print("Temperature in Celsius :", temp_c)