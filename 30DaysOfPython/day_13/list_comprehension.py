
print("\n","-"*30,"Exercice: Level 1", "-"*30,"\n")


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print(f"1.\t Only positive numbers from list : {[i for i in numbers if i >= 0]}")

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"2.\t Flattened list : {[number for liste in list_of_lists
                                        for number in liste]}")


power_tuples = [(number,1) + tuple([number**pow for pow in range(1,6)]) for number in range(11) ]

print(f"3.\t List of powwer tuples : {power_tuples}")


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

print(f"4.\t Flatten list : {[[country.upper(),country[:3].upper(),city.upper()] for tup in countries for country,city in tup]}")


print(f"5.\t To a list of dictionaries : {[{'country':country.upper(),'city':city.upper()} for tup in countries
                                                                            for country,city in tup] }")

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

print(f"6.\t To a list of concatenated strings : {[first +' '+last for tup in names for first,last in tup]}")

# Calcul du y-intercept
y_intercept = lambda x, y, a: y - a * x

print(f"7.\t Lambda function to find y_intercept of linear functions : {y_intercept(2,-9,3)}")