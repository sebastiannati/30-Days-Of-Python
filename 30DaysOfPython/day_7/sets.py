print("\n","-"*30,"Exercice: Level 1", "-"*30,"\n")

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"1.\t Length of 'it_companies' set : {len(it_companies)}")
print(f"2.\t Adding 'Twitter' to 'it_companies' set: {it_companies.add('Twitter')}")
print(f"3.\t Multiple companies added at once in the set : {it_companies.update(['OpenAI','Mistral'])}")
print(f"4.\t Removing one of the companies from the set : {it_companies.remove("Facebook")}")
print("5.\t '.remove()' raises errors if the item is not in the given set while '.discard()' don't")

print("\n","-"*30,"Exercice: Level 2", "-"*30,"\n")

join_AB = A.union(B)
join_BA = B.union(A)
inter_AB = A.intersection(B)
print(f"1.\t Joining A and B sets : {join_AB}")
print(f"2.\t Intersection of A and B sets : {inter_AB}")
print(f"3.\t Is A a subset of set B : {A.issubset(B)}")
print(f"4.\t Are A and B disjoint sets : {A.isdisjoint(B)}")
print(f"5.\t Joining A and B and B and A sets : {join_AB}, {join_BA}")
print(f"6.\t Symetric difference of A and B sets : {A.symmetric_difference(B)}")

del A,B

print("7.\t A and B sets deleted")

print("\n","-"*30,"Exercice: Level 3", "-"*30,"\n")

ages_set = set(age)

print(f"1.\t Comparing length of ages list and set : {len(age)}, {len(ages_set)}")
print("2.\t A string is a any type of data witten as text .\n  \t A list is a mutable object containing several variables/values of different data types.\n  \t A tuple is a non mutable object containing several variables/values of different data types.\n  \t A set is a collection of unique elements unordered and un indexed")

sentence = "I am a teacher and I love to inspire and teach people."
list_words = sentence.split(" ")
set_words = set(list_words)

print(f"3.\t In this sentence : 'I am a teacher and I love to inspire and teach people.' there are {len(set_words)} unique words wich are : {set_words}")