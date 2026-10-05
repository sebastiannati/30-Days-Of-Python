print("-"*30, "Exercise", "-"*30)

age = 24
height = 1.75
complex_number = 1+1j

print("\n1.\t variable 'age' : ",age)
print("2.\t variable 'height' : ", height)
print("3.\t complex number : ", complex_number)

base = float(input("\t Enter base : "))
height = float(input("\t Enter height : "))
triangle_area = 0.5*base*height
print("4.\t Area of your triangle : ", triangle_area)

a = float(input("\tEnter side a : "))
b = float(input("\tEnter side b : "))
c = float(input("\tEnter side c : "))
perimeter = a+b+c
print("5.\t Perimeter of your triangle : ", perimeter)

length = float(input("\tEnter a length : "))
width = float(input("\tEnter a width : "))
area = length*width
perimeter = 2*(length+width)
print("6.\t Area and perimeter of rectangle : ", area, perimeter)

radius = float(input("\tEnter a radius : "))
area = 3.14*radius**2
circum = 2*3.14*radius
print("7.\t Radius and circumference of circle : ", area, circum)

slope1 = (0+2)/1
x_intercept = (1,0)
y_intercept = (0,-2)
print("8.\t For 'y = 2x -2', slope, x-intercept, y-intercept : ", slope1, x_intercept, y_intercept)

slope2 = (6-2)/(10-2)
euc_dist = ((6-2)**2+(10-2)**2)**1/2
print("9.\t Slope and euclidean distance bewteen points (2,2) and (6,10) : ", slope2, euc_dist)

print("10.\t Is slope of 'y=2x -2' bigger than slope between points (2,2) and (6,10) : ", slope1>slope2)

value1 = -1**2 -6 + 9
value2 = 9
value3 = 1 + 7 + 9
delta = 6**2 -4*1*9
solution = (-6 + delta**1/2)/2
print("11.\t Values of 'y=x² + 6x + 9' for x = [-1,0,1], solution for 'y=0' : ", value1,value2,value3,solution)

python = 'python'
dragon = 'dragon'
print("12.\t Is lenght of 'python' superior to 'dragon' : ", len(python)>len(dragon))

print("13.\t Is 'on' in both 'python' and 'dragon' : ", 'on' in python and 'on' in dragon)

sentence = "I hope this course is not full of jargon."
print("14.\t Is 'jargon' in the sentence 'I hope this course is not full of jargon.' : ", 'jargon' in sentence)

print("15.\t Is there no 'on' in 'python' and 'dragon' : ", 'on' not in python and 'on' not in dragon)

print(f"16.\t Length of 'python' : {len(python)}, in float : {float(len(python))}, in sting : {str(len(python))}")

print("17.\t To check if a number 'x' is even we can verify that 'x%2 == 0' in python")

converted_int = int(2.7)
floor_div = 7//3
print(f"18.\t Check if the floor division of 7 by 3 : {floor_div} is equal to the int converted value of 2.7. {converted_int} : ", floor_div == converted_int)

print("19.\t Check if type of '10' is equal to type of 10 : ", type('10') == type(10))

print("20.\t Check if int('9.8') is equal to 10 : ", int(9.8) == 10)

hours = float(input("\t Enter number of hours : "))
rate = float(input("\t Enter rate per hour : "))

print("21.\t Your weekly earning is : ", hours*rate)

years = float(input("\t Enter number of years you have lived : "))

seconds = years*365*24*60*60
print(f"22.\t You have lived for {seconds} seconds")


def write_table(n):
    print("23. The following table : \n")
    for i in range(n):
        # * sur un generateur comme une compréhension de liste est l'operateur unpacking il unpack un itérable (set,liste,tuple,string...)
        print("\t", i+1, *[(i+1)**j for j in range(n)])

write_table(5)