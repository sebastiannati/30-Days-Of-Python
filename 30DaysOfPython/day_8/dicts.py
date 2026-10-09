print("\n","-"*30,"Exercice", "-"*30,"\n")

# sets
dog = {}

print(f"1.\t Empty 'dog' dict : {dog}")

dog['name'] = "Bog"
dog["color"] = "White"
dog['breed'] = 'yorkshire'
dog["age"] = '22'
print(f"2.\t Adding values to 'dog' dict: {dog}")

student = {}
student["first_name"] = "Sebastian"
student["last_name"] = "Nati"
student["gender"] = "M"
student["age"] = 23
student["marital status"] =  False
student["skills"] =  ["Python", "R", "Pytorch"]
student["country"] = "France"
student["city"] = "Paris"

student.get("skills").append("Machine Learning")

print(f"3.\t 'student' dict: {student}")
print(f"4.\t Length of 'student' dict : {len(student)}")
print(f"5.\t Value of skills and data type in 'student' dict : {student.get("skills")},{type(student.get("skills"))}")
print(f"6.\t Adding skills to dict : {student.get("skills")}")
print(f"7.\t The dict's keys : {student.keys()}")
print(f"8.\t The dict's values : {student.values()}")
print(f"9.\t Dict as list of tuples : {student.items()}")

del student["country"]

print(f"10.\t Deleting 'country' from dict : {student}")

del student

print("11.\t Deleted dict")
