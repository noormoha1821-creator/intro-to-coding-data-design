# the second Exercise 
# by Noor Muaydh
city1 = input("Hello User . Please enter the name of the first city :")
city2 = input("Now enter the name of the second city :")
temp_f1 = float(input("Enter the the current temperature in farenheit in "+ city1 +" :"))
temp_f2 = float(input("Enter the the current temperature in farenheit in "+ city2 +" :"))
temp_c1 = float((temp_f1 - 32 )* 5/9 )
temp_c2 = float((temp_f2 - 32 )* 5/9 )
if temp_c1 <= 0 and temp_c2 <= 0 :
    print("Alert!: The temperature in both cities is below freezing point")
elif temp_c1 <= 0 or temp_c2 <= 0 :
    print("The temperature in one of the cities is below freezing point.")
else : 
    print("The temperature in both cities is above the freezing point")

print( city1 + "'s Temperature in Celsius :", temp_c1)
print( city2 + "'s Temperature in Celsius :", temp_c2)