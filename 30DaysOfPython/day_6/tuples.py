print("\n","-"*30,"Exercice: Level 1", "-"*30,"\n")

empty_tuple = ()
brothers = ('Bogdan', 'Adrian')
sisters = ('Bogdana','Adriana')
siblings = brothers + sisters 
family_members = list(siblings) + ['Florin','Ana']
family_members = tuple(family_members)
print(f"1.\t Empty tuple : {empty_tuple}")
print(f"2.\t Siblings tuples : {brothers}, {sisters}")
print(f"3.\t Joined tuples : {siblings}")
print(f"4.\t Number of siblings : {len(siblings)}")
print(f"5.\t Family members : {family_members}")

print("\n","-"*30,"Exercice: Level 2", "-"*30,"\n")

parents, siblings = family_members[0:2],family_members[2:]
print(f"1.\t Unpacked parents and siblings : {parents}, {siblings}")

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animals = ('horse', 'cat', 'dog')

fruit_stuff_tp = fruits + vegetables + animals
fruit_stuff_list = list(fruit_stuff_tp)
print(f"2.\t Joining fruits,vegetables and animals tuples : {fruit_stuff_tp}")
print(f"3.\t Change to list : {fruit_stuff_list}")
print(f"4.\t Middle items of the list : {fruit_stuff_list[len(fruit_stuff_list)//2:len(fruit_stuff_list)//2+1] 
                                                if len(fruit_stuff_list)%2 !=0 
                                                else fruit_stuff_list[len(fruit_stuff_list)//2]}"
                                                )

print(f"5.\t First 3 items and last 3 items : {fruit_stuff_list[:3]}, {fruit_stuff_list[-3:]}")

del fruit_stuff_tp

print("6.\t Food stuff tuple deleted")

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(f"7.\t Is 'Estonia' and 'Iceland' nordic countries : { 'Estonia' in nordic_countries}, {'Iceland' in nordic_countries}")