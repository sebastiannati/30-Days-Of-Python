print("\n","-"*30,"Exercice: Level 1", "-"*30,"\n")

age = int(input("\tEnter your age : "))

if age > 18:
    print("1.\t You are old enough to drive.")
else :
    difference = 18 - age
    print(f"1.\t You need {difference} more years to learn to drive.")


my_age = 24

if my_age > age: 
    print(f"2.\t I am {my_age - age} older than you.")
elif my_age < age:
    print(f"2.\t You are {age-my_age} older than me.")
else:
    print("2.\t We have the same age.")

num_1 = float(input("\t Enter number one : "))
num_2 = float(input("\t Enter number two : "))
if num_1 > num_2:
    print(f"3.\t {num_1} is greater than {num_2}")
elif num_1 < num_2:
    print(f"3.\t {num_2} is smaller than {num_1}")
else:
    print(f"3.\t {num_1} is equal to {num_2}")
    
print("\n","-"*30,"Exercice: Level 2", "-"*30,"\n")

grade = int(input("Enter your grade : "))

if grade > 90:
    print("1.\t A")
elif grade > 80 and grade < 90:
    print("1.\t B")
elif grade > 70 and grade < 80:
    print("1.\t C")
elif grade > 60 and grade < 70:
    print("1.\t D")

elif grade < 0 or grade > 100:
    print("1.\t Not allowed value")

else:
    print("1.\t F")

month = input("Enter a month :")

autumn = ["September", "October","November"]
winter = ["December", "January", "February"]
spring = ["March", "April","May"]
summer = ["June", "July","August"]

if month in autumn:
    print(f"2.\t {month} is in autum")

elif month in winter:
    print(f"2.\t {month} is in winter")
    
elif month in spring:
    print(f"2.\t {month} is in spring")
    
elif month in summer:
    print(f"2.\t {month} is in summer")

else:
    print(f"2.\t {month} is not a month")
    

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit : ")

if fruit in fruits:
    print(f"3.\t {fruit} is in fruits list")
else:
    print(f"3.\t {fruit} is not in fruits list, adding to the list...")
    fruits.append(fruit)
    print(f"  \t\t This is the list updated : {fruits}")

print("\n","-"*30,"Exercice: Level 3", "-"*30,"\n")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }


if person.get("skills"):
    skills = person.get("skills")
    print(f"1.\t Middle skill : {skills[2]}")
    print(f"  \t Is 'Python' in skills list : {"Python" in skills}")
    if skills == ["JavaScript", "React"]:
        print("  \t He is a frontend developer")
    elif skills == ["Node", "Python", "MongoDB"]:
        print("  \t He is a backend developer")
    elif skills == ["React", "Node", "MongoDB"] :
        print("  \t He is a fullstack developer")
    else:
        print("  \t unknown title")
else : 
    print("1.\t No skill section")
    
if person.get("country") == "Finland" and person.get("is_married") == True :
    print(f"  \t{person.get("first_name")} {person.get("last_name")} lives in {person.get("coutry")}. He is married.")
else : 
    print("  \t Don't know where he lives neither if he is married.")