print("-"*30,"Exercise","-"*30,"\n")

concat1 = ['Thirty', 'Days', 'Of', 'Python']
concat2 = ['Coding', 'For' , 'All']

print("1.\t concat1enated sting : {}".format(' '.join(concat1)))
print("2.\t concat1enated sting : {}".format(' '.join(concat2)))

company = ' '.join(concat2)
print("3.\t Company sting : {}".format(company))
print("4.\t Company sting : {}".format(company))
print("5.\t Company sting length: {}".format(len(company)))
print("6.\t Company UPPERCASE sting : {}".format(company.upper()))
print("7.\t Company LOWERCASE sting : {}".format(company.lower()))
print("8.\t Company Title, Capitalize, Swapcase stings : {}, {}, {}".format(company.title(),company.capitalize(),company.swapcase()))
print("9.\t Company Cut first word sting : {}".format(company[5:]))

substring = 'Coding'

print("10.\t 'Coding' in company sting : {}, {}".format(company.index(substring),company.find(substring)))
print("11.\t Replacing 'coding' in company sting : {}".format(company.replace('Coding','Cooking')))
print("12.\t Replacing 'Everyone' by 'All' in 'Python for Everyone'sting : {}".format('Python for Everyone'.replace('Everyone','All')))
print("13.\t Splitting 'Python for All' sting : {}".format('Python for All'.split(' ')))
print("14.\t Splitting 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' sting by comma : {}".format('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(',')))
print("15.\t Character 0 in 'Coding for All' sting : {}".format('Coding for All'[0]))
print("16.\t Last character in 'Coding for All' sting : {}".format('Coding for All'[-1]))
print("17.\t Character 10 in 'Coding for All' sting : {}".format('Coding for All'[10]))
print("18.\t Acronym for 'Python For Everyone' sting : {}".format('Python For Everyone'[::4]))
print("19.\t Acronym for 'Coding For All' sting : {}".format('Coding For All'[::2]))
print("20.\t First occurence of 'C' in 'Coding For All' sting : {}".format('Coding For All'.index('C')))
print("21.\t First occurence of 'F' in 'Coding For All' sting : {}".format('Coding For All'.index('F')))
print("22.\t Last occurence of 'l' in 'Coding For All' sting : {}".format('Coding For All'.rindex('l')))
print("23.\t First occurence of 'because' in 'You cannot end a sentence with because because because is a conjunction' string : {}".format('You cannot end a sentence with because because because is a conjunction'.find('because')))
print("24.\t Last occurence of 'because' in 'You cannot end a sentence with because because because is a conjunction' string : {}".format('You cannot end a sentence with because because because is a conjunction'.rfind('because')))
print("25.\t Slicing out 'because because because' form 'You cannot end a sentence with because because because is a conjunction' sting : {}".format('You cannot end a sentence with because because because is a conjunction'[31:54]))
print("28.\t 'Coding For All' sting starting with 'Coding': {}".format("Coding For All".startswith("Coding")))
print("29.\t 'Coding For All' sting starting with 'Coding': {}".format("Coding For All".endswith("coding")))
print("30.\t Removing spaces in '   Coding For All      ' sting : {}".format('   Coding For All      '.strip()))
print("31.\t Which of those strings '30DaysOfPython', 'thity_days_of_python' returns True with method isidentifier() : {}, {}".format("30DaysOfPython".isidentifier(),"thirty_days_of_python".isidentifier()))
print("32.\t Joining '['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']' with a hash and a space : {}".format( "# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])))
print("33.\t Separing sentences using line escape : {}".format("I am enjoying this challenge.\n\nI just wonder what is next."))
print("34.\t Using string format to display this : \n\t\t{}\n\t\t{}\n\t\t{}".format("radius = 10","area = 3.14 * radius ** 2","The area of a circle with radius 10 is 314 meters square."))
print("35.\t Using string format to display this ; \n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}\n\t\t{}".format("8 + 6 = 14",
                                                                                                                    "8 - 6 = 2",
                                                                                                                    "8 * 6 = 48",
                                                                                                                    "8 / 6 = 1.33",
                                                                                                                    "8 % 6 = 2",
                                                                                                                    "8 // 6 = 1",
                                                                                                                    "8 ** 6 = 262144"))