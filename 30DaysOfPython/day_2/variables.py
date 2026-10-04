print("\n","-"*30,"Level 1","-"*30,"\n")

print("\n1.\t","Comment : # Day 2: 30 Days of python programming")

firstname = "Sebastian"
print("2.\t variable 'firstname' : ",firstname)

lastname = "NATI"
print("3.\t variable 'lastname' : ",lastname)

fullname = "Sebastian NATI"
print("4.\t variable 'fullname' : ",fullname)

country = "France"
print("5.\t variable 'country' : ", country)

city = "Champigny-sur-marne"
print("6.\t variable 'city' : ", city)

age = 24
print("7.\t variable 'age' : ", age)

year = 2026
print("8.\t variable 'year' : ", year)

is_married = False
print("9.\t variable 'is_married' : ", is_married)

is_true = True 
print("10.\t variable 'is_true' : ", is_true)

is_light_on = True
print("11.\t variable 'is_light_on' : ", is_light_on)

degree, speciality = "Engineer" , "Mathematics applied and computer science"
print("12.\t varibles 'degree, speciality' : ", degree, speciality)

print("\n","-"*30,"Level 2", "-"*30,"\n")

print("1.\t type of all variables : ", type(firstname),
      type(lastname),
      type(fullname),
      type(country),
      type(city),
      type(age),
      type(year),
      type(is_married),
      type(is_true),
      type(is_light_on),
      type(degree),
      type(speciality))

print("2.\t length of 'firstname' : ", len(firstname))

print("3.\t length of 'lastname' : ", len(lastname))

num_one, num_two = 5, 4
print(f"4.\t 'num_one' : {num_one}, num_two : {num_two}")

total = num_one + num_two
print(f"5.\t Adding 'num_one' and 'num_two' : {total}")

diff = num_one - num_two
print(f"6.\t Substracting 'num_two' to 'num_one' : {diff}")

product = num_two*num_one
print(f"7.\t Multiplying 'num_two' to 'num_one' : {product}")

division = num_one/num_two
print(f"8.\t Dividing 'num_one' by 'num_two' : {division}")

remainder = num_two%num_one
print(f"9.\t Using modulus to divide 'num_two' by 'num_one' : {remainder}")

exp = num_one ** num_two
print(f"10.\t 'num_one' to power 'num_two' : {exp}")

floor_division = num_one//num_two
print(f"11.\t Floor division of 'num_one' by 'num_two' : {floor_division}")

radius = 30
area_of_circle = 3.14 * radius**2
circum_of_circle = 2*radius*3.14
print("12.\t Circle of radius 30 meters :")
print(f"\ta.\t Area of circle : {area_of_circle}")
print(f"\tb.\t Circum of circle : {circum_of_circle}")
custom_radius = input("\tc.\t Choose the radius of your own circle :")
custom_area = 3.14 * int(custom_radius)**2
print(f"\t\t\t Area of your circle : {custom_area}")

res = input("Enter your first name, last name, country and age : ")
list_res = res.split(" ")
firstname,lastname,country,age = list_res[0], list_res[1], list_res[2], list_res[3]
print(f"13.\t Hello {firstname} {lastname} {country} {age}")

print("14.\t Help function of reserved words :")
help('keywords')