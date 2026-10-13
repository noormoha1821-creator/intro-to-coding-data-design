# the first Exercise 
# by Noor Muaydh
cities = {}
temp = 0
while True :
    city = input("Please enter the name the city :").strip().lower()
    if city == "exit" :
        break
    city_infos = {}
    temp_typ = input("Would you like to enter the temperature in Fahrenheit or Celsius ? -").strip().lower()
    if temp_typ == "fahrenheit".strip().lower():
        temp = int (temp_f)
        temp_c = False
        typ= "fahrenheit"
    else : 
        temp = int (temp_c)
        temp_f = False
        typ= "celsius"
    temp = float(input("Enter the the current temperature in " + temp_typ +" in "+ city +" :"))
    city_infos ["temp"] = str(temp)  + " " + typ
    word = None
    if temp == 32 and temp_c == False or temp == 0 and temp_f == False:
        word = "equals"
    elif  temp < 32 and temp_c == None or temp < 0 and temp_f == None:
        word = "below"
    else : 
        word = "above"
    city_infos ["sentence"] = word + " freezing point"
    rain = input("Is it raining in "+ city +"? (yes/no) -").strip().lower()
    if rain == "yes" :
        city_infos ["wether"] = " its reiny"
    else : 
        city_infos ["wether"] = " its not reiny"  
    sunny = input("Is the sun shining in "+ city +"? (yes/no) -").strip().lower()
    if sunny == "yes":
        city_infos ["wether"] += " and its sunny"
    else : 
        city_infos ["wether"] += " and its not sunny" 
    cities[city] = city_infos
print("summery :- ")
print("--------------------------------------------------------------------")
print (cities)
