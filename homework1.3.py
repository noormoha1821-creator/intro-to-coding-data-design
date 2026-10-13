# the third Exercise 
# by Noor Muaydh
city1 = input("Hello User . Please enter the name of the first city :")
city2 = input("Now enter the name of the second city :")
temp1 = float(input("Enter the the current temperature in Celsius in "+ city1 +" :"))
temp2 = float(input("Enter the the current temperature in Celsius in "+ city2 +" :"))
temp3 = (temp1 - temp2)
print("The average temperature between "+ city1 ,"and " + city2 ,"is" , + temp3 )
temp_f = ( temp3 * 9/5 + 32)
print("Temperature in Fahrenheit :", temp_f)