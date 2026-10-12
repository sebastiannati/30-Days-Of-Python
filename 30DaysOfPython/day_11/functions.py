print("\n", "-" * 30, "Exercice: Level 1", "-" * 30, "\n")


def add_two_numbers(num1, num2):
    return num1 + num2


def area_of_circle(radius):
    return 3.141592653589793 * radius ** 2


def add_all_nums(*args):
    total = 0
    for num in args:
        if type(num) not in (int, float):
            return f"Invalid argument: {num!r} is not a number"
        total += num
    return total


def convert_celsius_tofahrenheit(temp):
    return temp * (9 / 5) + 32


def check_season(month):
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]

    month = month.strip().capitalize()
    if month in autumn:
        return "Autumn"
    elif month in winter:
        return "Winter"
    elif month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    return "Not a month"


def calculate_slope(a):
    """For a line y = ax + b, its slope is a."""
    return a


def solve_quadratic_eqn(a, b, c):
    """Return the tuple of real solutions of ax² + bx + c = 0."""
    if a == 0:
        if b == 0:
            return "Infinite solutions" if c == 0 else "No solution"
        return (-c / b,)

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return ()  # No real solutions
    elif delta == 0:
        return (-b / (2 * a),)

    sol_1 = (-b - delta ** 0.5) / (2 * a)
    sol_2 = (-b + delta ** 0.5) / (2 * a)
    return sol_1, sol_2


def print_list(liste):
    for elem in liste:
        print(f"  \t {elem}")


def reverse_list(liste):
    liste_2 = []
    for i in range(1, len(liste) + 1):
        liste_2.append(liste[-i])
    return liste_2


def capitalize_list_items(liste):
    liste_2 = []
    for elem in liste:
        if not isinstance(elem, str):
            return "Can't capitalize list: all elements must be strings"
        liste_2.append(elem.capitalize())
    return liste_2


def add_item(liste, item):
    liste_2 = liste.copy()
    liste_2.append(item)
    return liste_2


def remove_item(liste, item):
    liste_2 = liste.copy()
    if item in liste_2:
        liste_2.remove(item)
    return liste_2


def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total


def sum_of_odds(num):
    total = 0
    for i in range(num + 1):
        if i % 2 != 0:
            total += i
    return total


def sum_of_evens(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return total


print(f"1.\t Sum of 3 and 5 : {add_two_numbers(3, 5)}")
print(f"2.\t Area of a circle (radius = 4) : {area_of_circle(4):.2f}")
print(f"3.\t Sum of 2, 4 and 6 : {add_all_nums(2, 4, 6)}")
print(f"  \t Invalid arguments : {add_all_nums(2, 'A', 6)}")
print(f"4.\t 25°C in Fahrenheit : {convert_celsius_tofahrenheit(25)}°F")
print(f"5.\t Season of October : {check_season('October')}")
print(f"6.\t Slope of y = 3x + 2 : {calculate_slope(3)}")
print(f"7.\t Solutions of x² - 3x + 2 = 0 : {solve_quadratic_eqn(1, -3, 2)}")
print("8.\t Elements of the list :")
print_list(["Apple", "Banana", "Mango"])
print(f"9.\t Reversed list : {reverse_list([1, 2, 3, 4, 5])}")
print(f"  \t Reversed letters : {reverse_list(['A', 'B', 'C'])}")
food_stuff = ["Potato", "Tomato", "Mango", "Milk"]
numbers = [2, 3, 7, 9]
print(f"10.\t Capitalized items : {capitalize_list_items(['potato', 'tomato', 'mango'])}")
print(f"11.\t Added food item : {add_item(food_stuff, 'Meat')}")
print(f"  \t Added number : {add_item(numbers, 5)}")
print(f"12.\t Removed food item : {remove_item(food_stuff, 'Mango')}")
print(f"  \t Removed number : {remove_item(numbers, 3)}")
print(f"13.\t Sum of numbers from 0 to 5 : {sum_of_numbers(5)}")
print(f"  \t From 0 to 10 : {sum_of_numbers(10)}")
print(f"  \t From 0 to 100 : {sum_of_numbers(100)}")
print(f"14.\t Sum of odd numbers from 0 to 10 : {sum_of_odds(10)}")
print(f"15.\t Sum of even numbers from 0 to 10 : {sum_of_evens(10)}")


print("\n", "-" * 30, "Exercice: Level 2", "-" * 30, "\n")


def evens_and_odds(num):
    total_evens = 0
    total_odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total_evens += 1
        else:
            total_odds += 1
    return total_evens, total_odds


def factorial(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("Factorial requires a non-negative integer")
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


def is_empty(arg):
    return len(arg) == 0


def calculate_mean(liste):
    if not liste:
        raise ValueError("The list cannot be empty")
    total = 0
    for i in liste:
        total += i
    return total / len(liste)


def calculate_median(liste):
    if not liste:
        raise ValueError("The list cannot be empty")
    liste = sorted(liste)
    middle = len(liste) // 2
    if len(liste) % 2 == 0:
        return (liste[middle - 1] + liste[middle]) / 2
    return liste[middle]


def calculate_mode(liste):
    if not liste:
        raise ValueError("The list cannot be empty")
    count = {}
    for i in liste:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    maximum = max(count.values())
    return [value for value, number in count.items() if number == maximum]


def calculate_range(liste):
    if not liste:
        raise ValueError("The list cannot be empty")
    return max(liste) - min(liste)


def calculate_variance(liste):
    mean = calculate_mean(liste)
    ecarts = 0
    for i in liste:
        ecarts += (i - mean) ** 2
    return ecarts / len(liste)  # Population variance


def calculate_std(liste):
    return calculate_variance(liste) ** 0.5


def greet(name="Guest"):
    print(f"Hello, {name}!")


def show_args(**args):
    text = ", ".join(f"{k}: {v}" for k, v in args.items())
    print(f"Received: {text}")


evens, odds = evens_and_odds(100)
print(f"1.\t The number of odds are {odds}.")
print(f"  \t The number of evens are {evens}.")
print(f"2.\t Factorial of 5 : {factorial(5)}")
print(f"3.\t Is the list empty : {is_empty([])}")
liste = [2, 4, 4, 4, 5, 5, 7, 9]
print(f"4.\t Mean : {calculate_mean(liste)}")
print(f"  \t Median : {calculate_median(liste)}")
print(f"  \t Mode(s) : {calculate_mode(liste)}")
print(f"  \t Range : {calculate_range(liste)}")
print(f"  \t Variance : {calculate_variance(liste)}")
print(f"  \t Standard deviation : {calculate_std(liste):.2f}")
print("5.\t ", end="")
greet()
print("  \t ", end="")
greet("Alice")
print("6.\t ", end="")
show_args(name="Alice", age=30, city="New York")
print("  \t ", end="")
show_args(name="Bob", pet="Fluffy, the bunny")


print("\n", "-" * 30, "Exercice: Level 3", "-" * 30, "\n")


def is_prime(num):
    if not isinstance(num, int) or num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_unique(liste):
    return len(liste) == len(set(liste))


def all_data_types(liste):
    if not liste:
        return True
    type_l = type(liste[0])
    for i in range(1, len(liste)):
        if type(liste[i]) != type_l:
            return False
    return True


def is_variable(name):
    keywords = [
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else", "except",
        "finally", "for", "from", "global", "if", "import", "in", "is",
        "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
        "try", "while", "with", "yield"
    ]
    return isinstance(name, str) and name.isidentifier() and name not in keywords


# Données des pays intégrées directement : aucun import nécessaire.
list_data = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": [
            "Arabic"
        ],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar"
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    },
    {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "languages": [
            "Catalan"
        ],
        "population": 78014,
        "flag": "https://restcountries.eu/data/and.svg",
        "currency": "Euro"
    },
    {
        "name": "Angola",
        "capital": "Luanda",
        "languages": [
            "Portuguese"
        ],
        "population": 25868000,
        "flag": "https://restcountries.eu/data/ago.svg",
        "currency": "Angolan kwanza"
    },
    {
        "name": "Anguilla",
        "capital": "The Valley",
        "languages": [
            "English"
        ],
        "population": 13452,
        "flag": "https://restcountries.eu/data/aia.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Antarctica",
        "capital": "",
        "languages": [
            "English",
            "Russian"
        ],
        "population": 1000,
        "flag": "https://restcountries.eu/data/ata.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Antigua and Barbuda",
        "capital": "Saint John's",
        "languages": [
            "English"
        ],
        "population": 86295,
        "flag": "https://restcountries.eu/data/atg.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Argentina",
        "capital": "Buenos Aires",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 43590400,
        "flag": "https://restcountries.eu/data/arg.svg",
        "currency": "Argentine peso"
    },
    {
        "name": "Armenia",
        "capital": "Yerevan",
        "languages": [
            "Armenian",
            "Russian"
        ],
        "population": 2994400,
        "flag": "https://restcountries.eu/data/arm.svg",
        "currency": "Armenian dram"
    },
    {
        "name": "Aruba",
        "capital": "Oranjestad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi"
        ],
        "population": 107394,
        "flag": "https://restcountries.eu/data/abw.svg",
        "currency": "Aruban florin"
    },
    {
        "name": "Australia",
        "capital": "Canberra",
        "languages": [
            "English"
        ],
        "population": 24117360,
        "flag": "https://restcountries.eu/data/aus.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Austria",
        "capital": "Vienna",
        "languages": [
            "German"
        ],
        "population": 8725931,
        "flag": "https://restcountries.eu/data/aut.svg",
        "currency": "Euro"
    },
    {
        "name": "Azerbaijan",
        "capital": "Baku",
        "languages": [
            "Azerbaijani"
        ],
        "population": 9730500,
        "flag": "https://restcountries.eu/data/aze.svg",
        "currency": "Azerbaijani manat"
    },
    {
        "name": "Bahamas",
        "capital": "Nassau",
        "languages": [
            "English"
        ],
        "population": 378040,
        "flag": "https://restcountries.eu/data/bhs.svg",
        "currency": "Bahamian dollar"
    },
    {
        "name": "Bahrain",
        "capital": "Manama",
        "languages": [
            "Arabic"
        ],
        "population": 1404900,
        "flag": "https://restcountries.eu/data/bhr.svg",
        "currency": "Bahraini dinar"
    },
    {
        "name": "Bangladesh",
        "capital": "Dhaka",
        "languages": [
            "Bengali"
        ],
        "population": 161006790,
        "flag": "https://restcountries.eu/data/bgd.svg",
        "currency": "Bangladeshi taka"
    },
    {
        "name": "Barbados",
        "capital": "Bridgetown",
        "languages": [
            "English"
        ],
        "population": 285000,
        "flag": "https://restcountries.eu/data/brb.svg",
        "currency": "Barbadian dollar"
    },
    {
        "name": "Belarus",
        "capital": "Minsk",
        "languages": [
            "Belarusian",
            "Russian"
        ],
        "population": 9498700,
        "flag": "https://restcountries.eu/data/blr.svg",
        "currency": "New Belarusian ruble"
    },
    {
        "name": "Belgium",
        "capital": "Brussels",
        "languages": [
            "Dutch",
            "French",
            "German"
        ],
        "population": 11319511,
        "flag": "https://restcountries.eu/data/bel.svg",
        "currency": "Euro"
    },
    {
        "name": "Belize",
        "capital": "Belmopan",
        "languages": [
            "English",
            "Spanish"
        ],
        "population": 370300,
        "flag": "https://restcountries.eu/data/blz.svg",
        "currency": "Belize dollar"
    },
    {
        "name": "Benin",
        "capital": "Porto-Novo",
        "languages": [
            "French"
        ],
        "population": 10653654,
        "flag": "https://restcountries.eu/data/ben.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Bermuda",
        "capital": "Hamilton",
        "languages": [
            "English"
        ],
        "population": 61954,
        "flag": "https://restcountries.eu/data/bmu.svg",
        "currency": "Bermudian dollar"
    },
    {
        "name": "Bhutan",
        "capital": "Thimphu",
        "languages": [
            "Dzongkha"
        ],
        "population": 775620,
        "flag": "https://restcountries.eu/data/btn.svg",
        "currency": "Bhutanese ngultrum"
    },
    {
        "name": "Bolivia (Plurinational State of)",
        "capital": "Sucre",
        "languages": [
            "Spanish",
            "Aymara",
            "Quechua"
        ],
        "population": 10985059,
        "flag": "https://restcountries.eu/data/bol.svg",
        "currency": "Bolivian boliviano"
    },
    {
        "name": "Bonaire, Sint Eustatius and Saba",
        "capital": "Kralendijk",
        "languages": [
            "Dutch"
        ],
        "population": 17408,
        "flag": "https://restcountries.eu/data/bes.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Bosnia and Herzegovina",
        "capital": "Sarajevo",
        "languages": [
            "Bosnian",
            "Croatian",
            "Serbian"
        ],
        "population": 3531159,
        "flag": "https://restcountries.eu/data/bih.svg",
        "currency": "Bosnia and Herzegovina convertible mark"
    },
    {
        "name": "Botswana",
        "capital": "Gaborone",
        "languages": [
            "English",
            "Tswana"
        ],
        "population": 2141206,
        "flag": "https://restcountries.eu/data/bwa.svg",
        "currency": "Botswana pula"
    },
    {
        "name": "Bouvet Island",
        "capital": "",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/bvt.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Brazil",
        "capital": "Brasília",
        "languages": [
            "Portuguese"
        ],
        "population": 206135893,
        "flag": "https://restcountries.eu/data/bra.svg",
        "currency": "Brazilian real"
    },
    {
        "name": "British Indian Ocean Territory",
        "capital": "Diego Garcia",
        "languages": [
            "English"
        ],
        "population": 3000,
        "flag": "https://restcountries.eu/data/iot.svg",
        "currency": "United States dollar"
    },
    {
        "name": "United States Minor Outlying Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 300,
        "flag": "https://restcountries.eu/data/umi.svg",
        "currency": "United States Dollar"
    },
    {
        "name": "Virgin Islands (British)",
        "capital": "Road Town",
        "languages": [
            "English"
        ],
        "population": 28514,
        "flag": "https://restcountries.eu/data/vgb.svg",
        "currency": "[D]"
    },
    {
        "name": "Virgin Islands (U.S.)",
        "capital": "Charlotte Amalie",
        "languages": [
            "English"
        ],
        "population": 114743,
        "flag": "https://restcountries.eu/data/vir.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Brunei Darussalam",
        "capital": "Bandar Seri Begawan",
        "languages": [
            "Malay"
        ],
        "population": 411900,
        "flag": "https://restcountries.eu/data/brn.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Bulgaria",
        "capital": "Sofia",
        "languages": [
            "Bulgarian"
        ],
        "population": 7153784,
        "flag": "https://restcountries.eu/data/bgr.svg",
        "currency": "Bulgarian lev"
    },
    {
        "name": "Burkina Faso",
        "capital": "Ouagadougou",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 19034397,
        "flag": "https://restcountries.eu/data/bfa.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Burundi",
        "capital": "Bujumbura",
        "languages": [
            "French",
            "Kirundi"
        ],
        "population": 10114505,
        "flag": "https://restcountries.eu/data/bdi.svg",
        "currency": "Burundian franc"
    },
    {
        "name": "Cambodia",
        "capital": "Phnom Penh",
        "languages": [
            "Khmer"
        ],
        "population": 15626444,
        "flag": "https://restcountries.eu/data/khm.svg",
        "currency": "Cambodian riel"
    },
    {
        "name": "Cameroon",
        "capital": "Yaoundé",
        "languages": [
            "English",
            "French"
        ],
        "population": 22709892,
        "flag": "https://restcountries.eu/data/cmr.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Canada",
        "capital": "Ottawa",
        "languages": [
            "English",
            "French"
        ],
        "population": 36155487,
        "flag": "https://restcountries.eu/data/can.svg",
        "currency": "Canadian dollar"
    },
    {
        "name": "Cabo Verde",
        "capital": "Praia",
        "languages": [
            "Portuguese"
        ],
        "population": 531239,
        "flag": "https://restcountries.eu/data/cpv.svg",
        "currency": "Cape Verdean escudo"
    },
    {
        "name": "Cayman Islands",
        "capital": "George Town",
        "languages": [
            "English"
        ],
        "population": 58238,
        "flag": "https://restcountries.eu/data/cym.svg",
        "currency": "Cayman Islands dollar"
    },
    {
        "name": "Central African Republic",
        "capital": "Bangui",
        "languages": [
            "French",
            "Sango"
        ],
        "population": 4998000,
        "flag": "https://restcountries.eu/data/caf.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chad",
        "capital": "N'Djamena",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 14497000,
        "flag": "https://restcountries.eu/data/tcd.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chile",
        "capital": "Santiago",
        "languages": [
            "Spanish"
        ],
        "population": 18191900,
        "flag": "https://restcountries.eu/data/chl.svg",
        "currency": "Chilean peso"
    },
    {
        "name": "China",
        "capital": "Beijing",
        "languages": [
            "Chinese"
        ],
        "population": 1377422166,
        "flag": "https://restcountries.eu/data/chn.svg",
        "currency": "Chinese yuan"
    },
    {
        "name": "Christmas Island",
        "capital": "Flying Fish Cove",
        "languages": [
            "English"
        ],
        "population": 2072,
        "flag": "https://restcountries.eu/data/cxr.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Cocos (Keeling) Islands",
        "capital": "West Island",
        "languages": [
            "English"
        ],
        "population": 550,
        "flag": "https://restcountries.eu/data/cck.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Colombia",
        "capital": "Bogotá",
        "languages": [
            "Spanish"
        ],
        "population": 48759958,
        "flag": "https://restcountries.eu/data/col.svg",
        "currency": "Colombian peso"
    },
    {
        "name": "Comoros",
        "capital": "Moroni",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 806153,
        "flag": "https://restcountries.eu/data/com.svg",
        "currency": "Comorian franc"
    },
    {
        "name": "Congo",
        "capital": "Brazzaville",
        "languages": [
            "French",
            "Lingala"
        ],
        "population": 4741000,
        "flag": "https://restcountries.eu/data/cog.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Congo (Democratic Republic of the)",
        "capital": "Kinshasa",
        "languages": [
            "French",
            "Lingala",
            "Kongo",
            "Swahili",
            "Luba-Katanga"
        ],
        "population": 85026000,
        "flag": "https://restcountries.eu/data/cod.svg",
        "currency": "Congolese franc"
    },
    {
        "name": "Cook Islands",
        "capital": "Avarua",
        "languages": [
            "English"
        ],
        "population": 18100,
        "flag": "https://restcountries.eu/data/cok.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Costa Rica",
        "capital": "San José",
        "languages": [
            "Spanish"
        ],
        "population": 4890379,
        "flag": "https://restcountries.eu/data/cri.svg",
        "currency": "Costa Rican colón"
    },
    {
        "name": "Croatia",
        "capital": "Zagreb",
        "languages": [
            "Croatian"
        ],
        "population": 4190669,
        "flag": "https://restcountries.eu/data/hrv.svg",
        "currency": "Croatian kuna"
    },
    {
        "name": "Cuba",
        "capital": "Havana",
        "languages": [
            "Spanish"
        ],
        "population": 11239004,
        "flag": "https://restcountries.eu/data/cub.svg",
        "currency": "Cuban convertible peso"
    },
    {
        "name": "Curaçao",
        "capital": "Willemstad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi",
            "English"
        ],
        "population": 154843,
        "flag": "https://restcountries.eu/data/cuw.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Cyprus",
        "capital": "Nicosia",
        "languages": [
            "Greek (modern)",
            "Turkish",
            "Armenian"
        ],
        "population": 847000,
        "flag": "https://restcountries.eu/data/cyp.svg",
        "currency": "Euro"
    },
    {
        "name": "Czech Republic",
        "capital": "Prague",
        "languages": [
            "Czech",
            "Slovak"
        ],
        "population": 10558524,
        "flag": "https://restcountries.eu/data/cze.svg",
        "currency": "Czech koruna"
    },
    {
        "name": "Denmark",
        "capital": "Copenhagen",
        "languages": [
            "Danish"
        ],
        "population": 5717014,
        "flag": "https://restcountries.eu/data/dnk.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Djibouti",
        "capital": "Djibouti",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 900000,
        "flag": "https://restcountries.eu/data/dji.svg",
        "currency": "Djiboutian franc"
    },
    {
        "name": "Dominica",
        "capital": "Roseau",
        "languages": [
            "English"
        ],
        "population": 71293,
        "flag": "https://restcountries.eu/data/dma.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Dominican Republic",
        "capital": "Santo Domingo",
        "languages": [
            "Spanish"
        ],
        "population": 10075045,
        "flag": "https://restcountries.eu/data/dom.svg",
        "currency": "Dominican peso"
    },
    {
        "name": "Ecuador",
        "capital": "Quito",
        "languages": [
            "Spanish"
        ],
        "population": 16545799,
        "flag": "https://restcountries.eu/data/ecu.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Egypt",
        "capital": "Cairo",
        "languages": [
            "Arabic"
        ],
        "population": 91290000,
        "flag": "https://restcountries.eu/data/egy.svg",
        "currency": "Egyptian pound"
    },
    {
        "name": "El Salvador",
        "capital": "San Salvador",
        "languages": [
            "Spanish"
        ],
        "population": 6520675,
        "flag": "https://restcountries.eu/data/slv.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Equatorial Guinea",
        "capital": "Malabo",
        "languages": [
            "Spanish",
            "French"
        ],
        "population": 1222442,
        "flag": "https://restcountries.eu/data/gnq.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Eritrea",
        "capital": "Asmara",
        "languages": [
            "Tigrinya",
            "Arabic",
            "English"
        ],
        "population": 5352000,
        "flag": "https://restcountries.eu/data/eri.svg",
        "currency": "Eritrean nakfa"
    },
    {
        "name": "Estonia",
        "capital": "Tallinn",
        "languages": [
            "Estonian"
        ],
        "population": 1315944,
        "flag": "https://restcountries.eu/data/est.svg",
        "currency": "Euro"
    },
    {
        "name": "Ethiopia",
        "capital": "Addis Ababa",
        "languages": [
            "Amharic"
        ],
        "population": 92206005,
        "flag": "https://restcountries.eu/data/eth.svg",
        "currency": "Ethiopian birr"
    },
    {
        "name": "Falkland Islands (Malvinas)",
        "capital": "Stanley",
        "languages": [
            "English"
        ],
        "population": 2563,
        "flag": "https://restcountries.eu/data/flk.svg",
        "currency": "Falkland Islands pound"
    },
    {
        "name": "Faroe Islands",
        "capital": "Tórshavn",
        "languages": [
            "Faroese"
        ],
        "population": 49376,
        "flag": "https://restcountries.eu/data/fro.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Fiji",
        "capital": "Suva",
        "languages": [
            "English",
            "Fijian",
            "Hindi",
            "Urdu"
        ],
        "population": 867000,
        "flag": "https://restcountries.eu/data/fji.svg",
        "currency": "Fijian dollar"
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": [
            "Finnish",
            "Swedish"
        ],
        "population": 5491817,
        "flag": "https://restcountries.eu/data/fin.svg",
        "currency": "Euro"
    },
    {
        "name": "France",
        "capital": "Paris",
        "languages": [
            "French"
        ],
        "population": 66710000,
        "flag": "https://restcountries.eu/data/fra.svg",
        "currency": "Euro"
    },
    {
        "name": "French Guiana",
        "capital": "Cayenne",
        "languages": [
            "French"
        ],
        "population": 254541,
        "flag": "https://restcountries.eu/data/guf.svg",
        "currency": "Euro"
    },
    {
        "name": "French Polynesia",
        "capital": "Papeetē",
        "languages": [
            "French"
        ],
        "population": 271800,
        "flag": "https://restcountries.eu/data/pyf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "French Southern Territories",
        "capital": "Port-aux-Français",
        "languages": [
            "French"
        ],
        "population": 140,
        "flag": "https://restcountries.eu/data/atf.svg",
        "currency": "Euro"
    },
    {
        "name": "Gabon",
        "capital": "Libreville",
        "languages": [
            "French"
        ],
        "population": 1802278,
        "flag": "https://restcountries.eu/data/gab.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Gambia",
        "capital": "Banjul",
        "languages": [
            "English"
        ],
        "population": 1882450,
        "flag": "https://restcountries.eu/data/gmb.svg",
        "currency": "Gambian dalasi"
    },
    {
        "name": "Georgia",
        "capital": "Tbilisi",
        "languages": [
            "Georgian"
        ],
        "population": 3720400,
        "flag": "https://restcountries.eu/data/geo.svg",
        "currency": "Georgian Lari"
    },
    {
        "name": "Germany",
        "capital": "Berlin",
        "languages": [
            "German"
        ],
        "population": 81770900,
        "flag": "https://restcountries.eu/data/deu.svg",
        "currency": "Euro"
    },
    {
        "name": "Ghana",
        "capital": "Accra",
        "languages": [
            "English"
        ],
        "population": 27670174,
        "flag": "https://restcountries.eu/data/gha.svg",
        "currency": "Ghanaian cedi"
    },
    {
        "name": "Gibraltar",
        "capital": "Gibraltar",
        "languages": [
            "English"
        ],
        "population": 33140,
        "flag": "https://restcountries.eu/data/gib.svg",
        "currency": "Gibraltar pound"
    },
    {
        "name": "Greece",
        "capital": "Athens",
        "languages": [
            "Greek (modern)"
        ],
        "population": 10858018,
        "flag": "https://restcountries.eu/data/grc.svg",
        "currency": "Euro"
    },
    {
        "name": "Greenland",
        "capital": "Nuuk",
        "languages": [
            "Kalaallisut"
        ],
        "population": 55847,
        "flag": "https://restcountries.eu/data/grl.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Grenada",
        "capital": "St. George's",
        "languages": [
            "English"
        ],
        "population": 103328,
        "flag": "https://restcountries.eu/data/grd.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Guadeloupe",
        "capital": "Basse-Terre",
        "languages": [
            "French"
        ],
        "population": 400132,
        "flag": "https://restcountries.eu/data/glp.svg",
        "currency": "Euro"
    },
    {
        "name": "Guam",
        "capital": "Hagåtña",
        "languages": [
            "English",
            "Chamorro",
            "Spanish"
        ],
        "population": 184200,
        "flag": "https://restcountries.eu/data/gum.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Guatemala",
        "capital": "Guatemala City",
        "languages": [
            "Spanish"
        ],
        "population": 16176133,
        "flag": "https://restcountries.eu/data/gtm.svg",
        "currency": "Guatemalan quetzal"
    },
    {
        "name": "Guernsey",
        "capital": "St. Peter Port",
        "languages": [
            "English",
            "French"
        ],
        "population": 62999,
        "flag": "https://restcountries.eu/data/ggy.svg",
        "currency": "British pound"
    },
    {
        "name": "Guinea",
        "capital": "Conakry",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 12947000,
        "flag": "https://restcountries.eu/data/gin.svg",
        "currency": "Guinean franc"
    },
    {
        "name": "Guinea-Bissau",
        "capital": "Bissau",
        "languages": [
            "Portuguese"
        ],
        "population": 1547777,
        "flag": "https://restcountries.eu/data/gnb.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Guyana",
        "capital": "Georgetown",
        "languages": [
            "English"
        ],
        "population": 746900,
        "flag": "https://restcountries.eu/data/guy.svg",
        "currency": "Guyanese dollar"
    },
    {
        "name": "Haiti",
        "capital": "Port-au-Prince",
        "languages": [
            "French",
            "Haitian"
        ],
        "population": 11078033,
        "flag": "https://restcountries.eu/data/hti.svg",
        "currency": "Haitian gourde"
    },
    {
        "name": "Heard Island and McDonald Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/hmd.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Holy See",
        "capital": "Rome",
        "languages": [
            "Latin",
            "Italian",
            "French",
            "German"
        ],
        "population": 451,
        "flag": "https://restcountries.eu/data/vat.svg",
        "currency": "Euro"
    },
    {
        "name": "Honduras",
        "capital": "Tegucigalpa",
        "languages": [
            "Spanish"
        ],
        "population": 8576532,
        "flag": "https://restcountries.eu/data/hnd.svg",
        "currency": "Honduran lempira"
    },
    {
        "name": "Hong Kong",
        "capital": "City of Victoria",
        "languages": [
            "English",
            "Chinese"
        ],
        "population": 7324300,
        "flag": "https://restcountries.eu/data/hkg.svg",
        "currency": "Hong Kong dollar"
    },
    {
        "name": "Hungary",
        "capital": "Budapest",
        "languages": [
            "Hungarian"
        ],
        "population": 9823000,
        "flag": "https://restcountries.eu/data/hun.svg",
        "currency": "Hungarian forint"
    },
    {
        "name": "Iceland",
        "capital": "Reykjavík",
        "languages": [
            "Icelandic"
        ],
        "population": 334300,
        "flag": "https://restcountries.eu/data/isl.svg",
        "currency": "Icelandic króna"
    },
    {
        "name": "India",
        "capital": "New Delhi",
        "languages": [
            "Hindi",
            "English"
        ],
        "population": 1295210000,
        "flag": "https://restcountries.eu/data/ind.svg",
        "currency": "Indian rupee"
    },
    {
        "name": "Indonesia",
        "capital": "Jakarta",
        "languages": [
            "Indonesian"
        ],
        "population": 258705000,
        "flag": "https://restcountries.eu/data/idn.svg",
        "currency": "Indonesian rupiah"
    },
    {
        "name": "Côte d'Ivoire",
        "capital": "Yamoussoukro",
        "languages": [
            "French"
        ],
        "population": 22671331,
        "flag": "https://restcountries.eu/data/civ.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Iran (Islamic Republic of)",
        "capital": "Tehran",
        "languages": [
            "Persian (Farsi)"
        ],
        "population": 79369900,
        "flag": "https://restcountries.eu/data/irn.svg",
        "currency": "Iranian rial"
    },
    {
        "name": "Iraq",
        "capital": "Baghdad",
        "languages": [
            "Arabic",
            "Kurdish"
        ],
        "population": 37883543,
        "flag": "https://restcountries.eu/data/irq.svg",
        "currency": "Iraqi dinar"
    },
    {
        "name": "Ireland",
        "capital": "Dublin",
        "languages": [
            "Irish",
            "English"
        ],
        "population": 6378000,
        "flag": "https://restcountries.eu/data/irl.svg",
        "currency": "Euro"
    },
    {
        "name": "Isle of Man",
        "capital": "Douglas",
        "languages": [
            "English",
            "Manx"
        ],
        "population": 84497,
        "flag": "https://restcountries.eu/data/imn.svg",
        "currency": "British pound"
    },
    {
        "name": "Israel",
        "capital": "Jerusalem",
        "languages": [
            "Hebrew (modern)",
            "Arabic"
        ],
        "population": 8527400,
        "flag": "https://restcountries.eu/data/isr.svg",
        "currency": "Israeli new shekel"
    },
    {
        "name": "Italy",
        "capital": "Rome",
        "languages": [
            "Italian"
        ],
        "population": 60665551,
        "flag": "https://restcountries.eu/data/ita.svg",
        "currency": "Euro"
    },
    {
        "name": "Jamaica",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2723246,
        "flag": "https://restcountries.eu/data/jam.svg",
        "currency": "Jamaican dollar"
    },
    {
        "name": "Japan",
        "capital": "Tokyo",
        "languages": [
            "Japanese"
        ],
        "population": 126960000,
        "flag": "https://restcountries.eu/data/jpn.svg",
        "currency": "Japanese yen"
    },
    {
        "name": "Jersey",
        "capital": "Saint Helier",
        "languages": [
            "English",
            "French"
        ],
        "population": 100800,
        "flag": "https://restcountries.eu/data/jey.svg",
        "currency": "British pound"
    },
    {
        "name": "Jordan",
        "capital": "Amman",
        "languages": [
            "Arabic"
        ],
        "population": 9531712,
        "flag": "https://restcountries.eu/data/jor.svg",
        "currency": "Jordanian dinar"
    },
    {
        "name": "Kazakhstan",
        "capital": "Astana",
        "languages": [
            "Kazakh",
            "Russian"
        ],
        "population": 17753200,
        "flag": "https://restcountries.eu/data/kaz.svg",
        "currency": "Kazakhstani tenge"
    },
    {
        "name": "Kenya",
        "capital": "Nairobi",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 47251000,
        "flag": "https://restcountries.eu/data/ken.svg",
        "currency": "Kenyan shilling"
    },
    {
        "name": "Kiribati",
        "capital": "South Tarawa",
        "languages": [
            "English"
        ],
        "population": 113400,
        "flag": "https://restcountries.eu/data/kir.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Kuwait",
        "capital": "Kuwait City",
        "languages": [
            "Arabic"
        ],
        "population": 4183658,
        "flag": "https://restcountries.eu/data/kwt.svg",
        "currency": "Kuwaiti dinar"
    },
    {
        "name": "Kyrgyzstan",
        "capital": "Bishkek",
        "languages": [
            "Kyrgyz",
            "Russian"
        ],
        "population": 6047800,
        "flag": "https://restcountries.eu/data/kgz.svg",
        "currency": "Kyrgyzstani som"
    },
    {
        "name": "Lao People's Democratic Republic",
        "capital": "Vientiane",
        "languages": [
            "Lao"
        ],
        "population": 6492400,
        "flag": "https://restcountries.eu/data/lao.svg",
        "currency": "Lao kip"
    },
    {
        "name": "Latvia",
        "capital": "Riga",
        "languages": [
            "Latvian"
        ],
        "population": 1961600,
        "flag": "https://restcountries.eu/data/lva.svg",
        "currency": "Euro"
    },
    {
        "name": "Lebanon",
        "capital": "Beirut",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 5988000,
        "flag": "https://restcountries.eu/data/lbn.svg",
        "currency": "Lebanese pound"
    },
    {
        "name": "Lesotho",
        "capital": "Maseru",
        "languages": [
            "English",
            "Southern Sotho"
        ],
        "population": 1894194,
        "flag": "https://restcountries.eu/data/lso.svg",
        "currency": "Lesotho loti"
    },
    {
        "name": "Liberia",
        "capital": "Monrovia",
        "languages": [
            "English"
        ],
        "population": 4615000,
        "flag": "https://restcountries.eu/data/lbr.svg",
        "currency": "Liberian dollar"
    },
    {
        "name": "Libya",
        "capital": "Tripoli",
        "languages": [
            "Arabic"
        ],
        "population": 6385000,
        "flag": "https://restcountries.eu/data/lby.svg",
        "currency": "Libyan dinar"
    },
    {
        "name": "Liechtenstein",
        "capital": "Vaduz",
        "languages": [
            "German"
        ],
        "population": 37623,
        "flag": "https://restcountries.eu/data/lie.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Lithuania",
        "capital": "Vilnius",
        "languages": [
            "Lithuanian"
        ],
        "population": 2872294,
        "flag": "https://restcountries.eu/data/ltu.svg",
        "currency": "Euro"
    },
    {
        "name": "Luxembourg",
        "capital": "Luxembourg",
        "languages": [
            "French",
            "German",
            "Luxembourgish"
        ],
        "population": 576200,
        "flag": "https://restcountries.eu/data/lux.svg",
        "currency": "Euro"
    },
    {
        "name": "Macao",
        "capital": "",
        "languages": [
            "Chinese",
            "Portuguese"
        ],
        "population": 649100,
        "flag": "https://restcountries.eu/data/mac.svg",
        "currency": "Macanese pataca"
    },
    {
        "name": "Macedonia (the former Yugoslav Republic of)",
        "capital": "Skopje",
        "languages": [
            "Macedonian"
        ],
        "population": 2058539,
        "flag": "https://restcountries.eu/data/mkd.svg",
        "currency": "Macedonian denar"
    },
    {
        "name": "Madagascar",
        "capital": "Antananarivo",
        "languages": [
            "French",
            "Malagasy"
        ],
        "population": 22434363,
        "flag": "https://restcountries.eu/data/mdg.svg",
        "currency": "Malagasy ariary"
    },
    {
        "name": "Malawi",
        "capital": "Lilongwe",
        "languages": [
            "English",
            "Chichewa"
        ],
        "population": 16832910,
        "flag": "https://restcountries.eu/data/mwi.svg",
        "currency": "Malawian kwacha"
    },
    {
        "name": "Malaysia",
        "capital": "Kuala Lumpur",
        "languages": [
            "Malaysian"
        ],
        "population": 31405416,
        "flag": "https://restcountries.eu/data/mys.svg",
        "currency": "Malaysian ringgit"
    },
    {
        "name": "Maldives",
        "capital": "Malé",
        "languages": [
            "Divehi"
        ],
        "population": 344023,
        "flag": "https://restcountries.eu/data/mdv.svg",
        "currency": "Maldivian rufiyaa"
    },
    {
        "name": "Mali",
        "capital": "Bamako",
        "languages": [
            "French"
        ],
        "population": 18135000,
        "flag": "https://restcountries.eu/data/mli.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Malta",
        "capital": "Valletta",
        "languages": [
            "Maltese",
            "English"
        ],
        "population": 425384,
        "flag": "https://restcountries.eu/data/mlt.svg",
        "currency": "Euro"
    },
    {
        "name": "Marshall Islands",
        "capital": "Majuro",
        "languages": [
            "English",
            "Marshallese"
        ],
        "population": 54880,
        "flag": "https://restcountries.eu/data/mhl.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Martinique",
        "capital": "Fort-de-France",
        "languages": [
            "French"
        ],
        "population": 378243,
        "flag": "https://restcountries.eu/data/mtq.svg",
        "currency": "Euro"
    },
    {
        "name": "Mauritania",
        "capital": "Nouakchott",
        "languages": [
            "Arabic"
        ],
        "population": 3718678,
        "flag": "https://restcountries.eu/data/mrt.svg",
        "currency": "Mauritanian ouguiya"
    },
    {
        "name": "Mauritius",
        "capital": "Port Louis",
        "languages": [
            "English"
        ],
        "population": 1262879,
        "flag": "https://restcountries.eu/data/mus.svg",
        "currency": "Mauritian rupee"
    },
    {
        "name": "Mayotte",
        "capital": "Mamoudzou",
        "languages": [
            "French"
        ],
        "population": 226915,
        "flag": "https://restcountries.eu/data/myt.svg",
        "currency": "Euro"
    },
    {
        "name": "Mexico",
        "capital": "Mexico City",
        "languages": [
            "Spanish"
        ],
        "population": 122273473,
        "flag": "https://restcountries.eu/data/mex.svg",
        "currency": "Mexican peso"
    },
    {
        "name": "Micronesia (Federated States of)",
        "capital": "Palikir",
        "languages": [
            "English"
        ],
        "population": 102800,
        "flag": "https://restcountries.eu/data/fsm.svg",
        "currency": "[D]"
    },
    {
        "name": "Moldova (Republic of)",
        "capital": "Chișinău",
        "languages": [
            "Romanian"
        ],
        "population": 3553100,
        "flag": "https://restcountries.eu/data/mda.svg",
        "currency": "Moldovan leu"
    },
    {
        "name": "Monaco",
        "capital": "Monaco",
        "languages": [
            "French"
        ],
        "population": 38400,
        "flag": "https://restcountries.eu/data/mco.svg",
        "currency": "Euro"
    },
    {
        "name": "Mongolia",
        "capital": "Ulan Bator",
        "languages": [
            "Mongolian"
        ],
        "population": 3093100,
        "flag": "https://restcountries.eu/data/mng.svg",
        "currency": "Mongolian tögrög"
    },
    {
        "name": "Montenegro",
        "capital": "Podgorica",
        "languages": [
            "Serbian",
            "Bosnian",
            "Albanian",
            "Croatian"
        ],
        "population": 621810,
        "flag": "https://restcountries.eu/data/mne.svg",
        "currency": "Euro"
    },
    {
        "name": "Montserrat",
        "capital": "Plymouth",
        "languages": [
            "English"
        ],
        "population": 4922,
        "flag": "https://restcountries.eu/data/msr.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Morocco",
        "capital": "Rabat",
        "languages": [
            "Arabic"
        ],
        "population": 33337529,
        "flag": "https://restcountries.eu/data/mar.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Mozambique",
        "capital": "Maputo",
        "languages": [
            "Portuguese"
        ],
        "population": 26423700,
        "flag": "https://restcountries.eu/data/moz.svg",
        "currency": "Mozambican metical"
    },
    {
        "name": "Myanmar",
        "capital": "Naypyidaw",
        "languages": [
            "Burmese"
        ],
        "population": 51419420,
        "flag": "https://restcountries.eu/data/mmr.svg",
        "currency": "Burmese kyat"
    },
    {
        "name": "Namibia",
        "capital": "Windhoek",
        "languages": [
            "English",
            "Afrikaans"
        ],
        "population": 2324388,
        "flag": "https://restcountries.eu/data/nam.svg",
        "currency": "Namibian dollar"
    },
    {
        "name": "Nauru",
        "capital": "Yaren",
        "languages": [
            "English",
            "Nauruan"
        ],
        "population": 10084,
        "flag": "https://restcountries.eu/data/nru.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Nepal",
        "capital": "Kathmandu",
        "languages": [
            "Nepali"
        ],
        "population": 28431500,
        "flag": "https://restcountries.eu/data/npl.svg",
        "currency": "Nepalese rupee"
    },
    {
        "name": "Netherlands",
        "capital": "Amsterdam",
        "languages": [
            "Dutch"
        ],
        "population": 17019800,
        "flag": "https://restcountries.eu/data/nld.svg",
        "currency": "Euro"
    },
    {
        "name": "New Caledonia",
        "capital": "Nouméa",
        "languages": [
            "French"
        ],
        "population": 268767,
        "flag": "https://restcountries.eu/data/ncl.svg",
        "currency": "CFP franc"
    },
    {
        "name": "New Zealand",
        "capital": "Wellington",
        "languages": [
            "English",
            "Māori"
        ],
        "population": 4697854,
        "flag": "https://restcountries.eu/data/nzl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Nicaragua",
        "capital": "Managua",
        "languages": [
            "Spanish"
        ],
        "population": 6262703,
        "flag": "https://restcountries.eu/data/nic.svg",
        "currency": "Nicaraguan córdoba"
    },
    {
        "name": "Niger",
        "capital": "Niamey",
        "languages": [
            "French"
        ],
        "population": 20715000,
        "flag": "https://restcountries.eu/data/ner.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Nigeria",
        "capital": "Abuja",
        "languages": [
            "English"
        ],
        "population": 186988000,
        "flag": "https://restcountries.eu/data/nga.svg",
        "currency": "Nigerian naira"
    },
    {
        "name": "Niue",
        "capital": "Alofi",
        "languages": [
            "English"
        ],
        "population": 1470,
        "flag": "https://restcountries.eu/data/niu.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Norfolk Island",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2302,
        "flag": "https://restcountries.eu/data/nfk.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Korea (Democratic People's Republic of)",
        "capital": "Pyongyang",
        "languages": [
            "Korean"
        ],
        "population": 25281000,
        "flag": "https://restcountries.eu/data/prk.svg",
        "currency": "North Korean won"
    },
    {
        "name": "Northern Mariana Islands",
        "capital": "Saipan",
        "languages": [
            "English",
            "Chamorro"
        ],
        "population": 56940,
        "flag": "https://restcountries.eu/data/mnp.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Norway",
        "capital": "Oslo",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 5223256,
        "flag": "https://restcountries.eu/data/nor.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Oman",
        "capital": "Muscat",
        "languages": [
            "Arabic"
        ],
        "population": 4420133,
        "flag": "https://restcountries.eu/data/omn.svg",
        "currency": "Omani rial"
    },
    {
        "name": "Pakistan",
        "capital": "Islamabad",
        "languages": [
            "English",
            "Urdu"
        ],
        "population": 194125062,
        "flag": "https://restcountries.eu/data/pak.svg",
        "currency": "Pakistani rupee"
    },
    {
        "name": "Palau",
        "capital": "Ngerulmud",
        "languages": [
            "English"
        ],
        "population": 17950,
        "flag": "https://restcountries.eu/data/plw.svg",
        "currency": "[E]"
    },
    {
        "name": "Palestine, State of",
        "capital": "Ramallah",
        "languages": [
            "Arabic"
        ],
        "population": 4682467,
        "flag": "https://restcountries.eu/data/pse.svg",
        "currency": "Israeli new sheqel"
    },
    {
        "name": "Panama",
        "capital": "Panama City",
        "languages": [
            "Spanish"
        ],
        "population": 3814672,
        "flag": "https://restcountries.eu/data/pan.svg",
        "currency": "Panamanian balboa"
    },
    {
        "name": "Papua New Guinea",
        "capital": "Port Moresby",
        "languages": [
            "English"
        ],
        "population": 8083700,
        "flag": "https://restcountries.eu/data/png.svg",
        "currency": "Papua New Guinean kina"
    },
    {
        "name": "Paraguay",
        "capital": "Asunción",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 6854536,
        "flag": "https://restcountries.eu/data/pry.svg",
        "currency": "Paraguayan guaraní"
    },
    {
        "name": "Peru",
        "capital": "Lima",
        "languages": [
            "Spanish"
        ],
        "population": 31488700,
        "flag": "https://restcountries.eu/data/per.svg",
        "currency": "Peruvian sol"
    },
    {
        "name": "Philippines",
        "capital": "Manila",
        "languages": [
            "English"
        ],
        "population": 103279800,
        "flag": "https://restcountries.eu/data/phl.svg",
        "currency": "Philippine peso"
    },
    {
        "name": "Pitcairn",
        "capital": "Adamstown",
        "languages": [
            "English"
        ],
        "population": 56,
        "flag": "https://restcountries.eu/data/pcn.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Poland",
        "capital": "Warsaw",
        "languages": [
            "Polish"
        ],
        "population": 38437239,
        "flag": "https://restcountries.eu/data/pol.svg",
        "currency": "Polish złoty"
    },
    {
        "name": "Portugal",
        "capital": "Lisbon",
        "languages": [
            "Portuguese"
        ],
        "population": 10374822,
        "flag": "https://restcountries.eu/data/prt.svg",
        "currency": "Euro"
    },
    {
        "name": "Puerto Rico",
        "capital": "San Juan",
        "languages": [
            "Spanish",
            "English"
        ],
        "population": 3474182,
        "flag": "https://restcountries.eu/data/pri.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Qatar",
        "capital": "Doha",
        "languages": [
            "Arabic"
        ],
        "population": 2587564,
        "flag": "https://restcountries.eu/data/qat.svg",
        "currency": "Qatari riyal"
    },
    {
        "name": "Republic of Kosovo",
        "capital": "Pristina",
        "languages": [
            "Albanian",
            "Serbian"
        ],
        "population": 1733842,
        "flag": "https://restcountries.eu/data/kos.svg",
        "currency": "Euro"
    },
    {
        "name": "Réunion",
        "capital": "Saint-Denis",
        "languages": [
            "French"
        ],
        "population": 840974,
        "flag": "https://restcountries.eu/data/reu.svg",
        "currency": "Euro"
    },
    {
        "name": "Romania",
        "capital": "Bucharest",
        "languages": [
            "Romanian"
        ],
        "population": 19861408,
        "flag": "https://restcountries.eu/data/rou.svg",
        "currency": "Romanian leu"
    },
    {
        "name": "Russian Federation",
        "capital": "Moscow",
        "languages": [
            "Russian"
        ],
        "population": 146599183,
        "flag": "https://restcountries.eu/data/rus.svg",
        "currency": "Russian ruble"
    },
    {
        "name": "Rwanda",
        "capital": "Kigali",
        "languages": [
            "Kinyarwanda",
            "English",
            "French"
        ],
        "population": 11553188,
        "flag": "https://restcountries.eu/data/rwa.svg",
        "currency": "Rwandan franc"
    },
    {
        "name": "Saint Barthélemy",
        "capital": "Gustavia",
        "languages": [
            "French"
        ],
        "population": 9417,
        "flag": "https://restcountries.eu/data/blm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "capital": "Jamestown",
        "languages": [
            "English"
        ],
        "population": 4255,
        "flag": "https://restcountries.eu/data/shn.svg",
        "currency": "Saint Helena pound"
    },
    {
        "name": "Saint Kitts and Nevis",
        "capital": "Basseterre",
        "languages": [
            "English"
        ],
        "population": 46204,
        "flag": "https://restcountries.eu/data/kna.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Lucia",
        "capital": "Castries",
        "languages": [
            "English"
        ],
        "population": 186000,
        "flag": "https://restcountries.eu/data/lca.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Martin (French part)",
        "capital": "Marigot",
        "languages": [
            "English",
            "French",
            "Dutch"
        ],
        "population": 36979,
        "flag": "https://restcountries.eu/data/maf.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Pierre and Miquelon",
        "capital": "Saint-Pierre",
        "languages": [
            "French"
        ],
        "population": 6069,
        "flag": "https://restcountries.eu/data/spm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Vincent and the Grenadines",
        "capital": "Kingstown",
        "languages": [
            "English"
        ],
        "population": 109991,
        "flag": "https://restcountries.eu/data/vct.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Samoa",
        "capital": "Apia",
        "languages": [
            "Samoan",
            "English"
        ],
        "population": 194899,
        "flag": "https://restcountries.eu/data/wsm.svg",
        "currency": "Samoan tālā"
    },
    {
        "name": "San Marino",
        "capital": "City of San Marino",
        "languages": [
            "Italian"
        ],
        "population": 33005,
        "flag": "https://restcountries.eu/data/smr.svg",
        "currency": "Euro"
    },
    {
        "name": "Sao Tome and Principe",
        "capital": "São Tomé",
        "languages": [
            "Portuguese"
        ],
        "population": 187356,
        "flag": "https://restcountries.eu/data/stp.svg",
        "currency": "São Tomé and Príncipe dobra"
    },
    {
        "name": "Saudi Arabia",
        "capital": "Riyadh",
        "languages": [
            "Arabic"
        ],
        "population": 32248200,
        "flag": "https://restcountries.eu/data/sau.svg",
        "currency": "Saudi riyal"
    },
    {
        "name": "Senegal",
        "capital": "Dakar",
        "languages": [
            "French"
        ],
        "population": 14799859,
        "flag": "https://restcountries.eu/data/sen.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Serbia",
        "capital": "Belgrade",
        "languages": [
            "Serbian"
        ],
        "population": 7076372,
        "flag": "https://restcountries.eu/data/srb.svg",
        "currency": "Serbian dinar"
    },
    {
        "name": "Seychelles",
        "capital": "Victoria",
        "languages": [
            "French",
            "English"
        ],
        "population": 91400,
        "flag": "https://restcountries.eu/data/syc.svg",
        "currency": "Seychellois rupee"
    },
    {
        "name": "Sierra Leone",
        "capital": "Freetown",
        "languages": [
            "English"
        ],
        "population": 7075641,
        "flag": "https://restcountries.eu/data/sle.svg",
        "currency": "Sierra Leonean leone"
    },
    {
        "name": "Singapore",
        "capital": "Singapore",
        "languages": [
            "English",
            "Malay",
            "Tamil",
            "Chinese"
        ],
        "population": 5535000,
        "flag": "https://restcountries.eu/data/sgp.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Sint Maarten (Dutch part)",
        "capital": "Philipsburg",
        "languages": [
            "Dutch",
            "English"
        ],
        "population": 38247,
        "flag": "https://restcountries.eu/data/sxm.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Slovakia",
        "capital": "Bratislava",
        "languages": [
            "Slovak"
        ],
        "population": 5426252,
        "flag": "https://restcountries.eu/data/svk.svg",
        "currency": "Euro"
    },
    {
        "name": "Slovenia",
        "capital": "Ljubljana",
        "languages": [
            "Slovene"
        ],
        "population": 2064188,
        "flag": "https://restcountries.eu/data/svn.svg",
        "currency": "Euro"
    },
    {
        "name": "Solomon Islands",
        "capital": "Honiara",
        "languages": [
            "English"
        ],
        "population": 642000,
        "flag": "https://restcountries.eu/data/slb.svg",
        "currency": "Solomon Islands dollar"
    },
    {
        "name": "Somalia",
        "capital": "Mogadishu",
        "languages": [
            "Somali",
            "Arabic"
        ],
        "population": 11079000,
        "flag": "https://restcountries.eu/data/som.svg",
        "currency": "Somali shilling"
    },
    {
        "name": "South Africa",
        "capital": "Pretoria",
        "languages": [
            "Afrikaans",
            "English",
            "Southern Ndebele",
            "Southern Sotho",
            "Swati",
            "Tswana",
            "Tsonga",
            "Venda",
            "Xhosa",
            "Zulu"
        ],
        "population": 55653654,
        "flag": "https://restcountries.eu/data/zaf.svg",
        "currency": "South African rand"
    },
    {
        "name": "South Georgia and the South Sandwich Islands",
        "capital": "King Edward Point",
        "languages": [
            "English"
        ],
        "population": 30,
        "flag": "https://restcountries.eu/data/sgs.svg",
        "currency": "British pound"
    },
    {
        "name": "Korea (Republic of)",
        "capital": "Seoul",
        "languages": [
            "Korean"
        ],
        "population": 50801405,
        "flag": "https://restcountries.eu/data/kor.svg",
        "currency": "South Korean won"
    },
    {
        "name": "South Sudan",
        "capital": "Juba",
        "languages": [
            "English"
        ],
        "population": 12131000,
        "flag": "https://restcountries.eu/data/ssd.svg",
        "currency": "South Sudanese pound"
    },
    {
        "name": "Spain",
        "capital": "Madrid",
        "languages": [
            "Spanish"
        ],
        "population": 46438422,
        "flag": "https://restcountries.eu/data/esp.svg",
        "currency": "Euro"
    },
    {
        "name": "Sri Lanka",
        "capital": "Colombo",
        "languages": [
            "Sinhalese",
            "Tamil"
        ],
        "population": 20966000,
        "flag": "https://restcountries.eu/data/lka.svg",
        "currency": "Sri Lankan rupee"
    },
    {
        "name": "Sudan",
        "capital": "Khartoum",
        "languages": [
            "Arabic",
            "English"
        ],
        "population": 39598700,
        "flag": "https://restcountries.eu/data/sdn.svg",
        "currency": "Sudanese pound"
    },
    {
        "name": "Suriname",
        "capital": "Paramaribo",
        "languages": [
            "Dutch"
        ],
        "population": 541638,
        "flag": "https://restcountries.eu/data/sur.svg",
        "currency": "Surinamese dollar"
    },
    {
        "name": "Svalbard and Jan Mayen",
        "capital": "Longyearbyen",
        "languages": [
            "Norwegian"
        ],
        "population": 2562,
        "flag": "https://restcountries.eu/data/sjm.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Swaziland",
        "capital": "Lobamba",
        "languages": [
            "English",
            "Swati"
        ],
        "population": 1132657,
        "flag": "https://restcountries.eu/data/swz.svg",
        "currency": "Swazi lilangeni"
    },
    {
        "name": "Sweden",
        "capital": "Stockholm",
        "languages": [
            "Swedish"
        ],
        "population": 9894888,
        "flag": "https://restcountries.eu/data/swe.svg",
        "currency": "Swedish krona"
    },
    {
        "name": "Switzerland",
        "capital": "Bern",
        "languages": [
            "German",
            "French",
            "Italian"
        ],
        "population": 8341600,
        "flag": "https://restcountries.eu/data/che.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Syrian Arab Republic",
        "capital": "Damascus",
        "languages": [
            "Arabic"
        ],
        "population": 18564000,
        "flag": "https://restcountries.eu/data/syr.svg",
        "currency": "Syrian pound"
    },
    {
        "name": "Taiwan",
        "capital": "Taipei",
        "languages": [
            "Chinese"
        ],
        "population": 23503349,
        "flag": "https://restcountries.eu/data/twn.svg",
        "currency": "New Taiwan dollar"
    },
    {
        "name": "Tajikistan",
        "capital": "Dushanbe",
        "languages": [
            "Tajik",
            "Russian"
        ],
        "population": 8593600,
        "flag": "https://restcountries.eu/data/tjk.svg",
        "currency": "Tajikistani somoni"
    },
    {
        "name": "Tanzania, United Republic of",
        "capital": "Dodoma",
        "languages": [
            "Swahili",
            "English"
        ],
        "population": 55155000,
        "flag": "https://restcountries.eu/data/tza.svg",
        "currency": "Tanzanian shilling"
    },
    {
        "name": "Thailand",
        "capital": "Bangkok",
        "languages": [
            "Thai"
        ],
        "population": 65327652,
        "flag": "https://restcountries.eu/data/tha.svg",
        "currency": "Thai baht"
    },
    {
        "name": "Timor-Leste",
        "capital": "Dili",
        "languages": [
            "Portuguese"
        ],
        "population": 1167242,
        "flag": "https://restcountries.eu/data/tls.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Togo",
        "capital": "Lomé",
        "languages": [
            "French"
        ],
        "population": 7143000,
        "flag": "https://restcountries.eu/data/tgo.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Tokelau",
        "capital": "Fakaofo",
        "languages": [
            "English"
        ],
        "population": 1411,
        "flag": "https://restcountries.eu/data/tkl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Tonga",
        "capital": "Nuku'alofa",
        "languages": [
            "English",
            "Tonga (Tonga Islands)"
        ],
        "population": 103252,
        "flag": "https://restcountries.eu/data/ton.svg",
        "currency": "Tongan paʻanga"
    },
    {
        "name": "Trinidad and Tobago",
        "capital": "Port of Spain",
        "languages": [
            "English"
        ],
        "population": 1349667,
        "flag": "https://restcountries.eu/data/tto.svg",
        "currency": "Trinidad and Tobago dollar"
    },
    {
        "name": "Tunisia",
        "capital": "Tunis",
        "languages": [
            "Arabic"
        ],
        "population": 11154400,
        "flag": "https://restcountries.eu/data/tun.svg",
        "currency": "Tunisian dinar"
    },
    {
        "name": "Turkey",
        "capital": "Ankara",
        "languages": [
            "Turkish"
        ],
        "population": 78741053,
        "flag": "https://restcountries.eu/data/tur.svg",
        "currency": "Turkish lira"
    },
    {
        "name": "Turkmenistan",
        "capital": "Ashgabat",
        "languages": [
            "Turkmen",
            "Russian"
        ],
        "population": 4751120,
        "flag": "https://restcountries.eu/data/tkm.svg",
        "currency": "Turkmenistan manat"
    },
    {
        "name": "Turks and Caicos Islands",
        "capital": "Cockburn Town",
        "languages": [
            "English"
        ],
        "population": 31458,
        "flag": "https://restcountries.eu/data/tca.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Tuvalu",
        "capital": "Funafuti",
        "languages": [
            "English"
        ],
        "population": 10640,
        "flag": "https://restcountries.eu/data/tuv.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Uganda",
        "capital": "Kampala",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 33860700,
        "flag": "https://restcountries.eu/data/uga.svg",
        "currency": "Ugandan shilling"
    },
    {
        "name": "Ukraine",
        "capital": "Kiev",
        "languages": [
            "Ukrainian"
        ],
        "population": 42692393,
        "flag": "https://restcountries.eu/data/ukr.svg",
        "currency": "Ukrainian hryvnia"
    },
    {
        "name": "United Arab Emirates",
        "capital": "Abu Dhabi",
        "languages": [
            "Arabic"
        ],
        "population": 9856000,
        "flag": "https://restcountries.eu/data/are.svg",
        "currency": "United Arab Emirates dirham"
    },
    {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "capital": "London",
        "languages": [
            "English"
        ],
        "population": 65110000,
        "flag": "https://restcountries.eu/data/gbr.svg",
        "currency": "British pound"
    },
    {
        "name": "United States of America",
        "capital": "Washington, D.C.",
        "languages": [
            "English"
        ],
        "population": 323947000,
        "flag": "https://restcountries.eu/data/usa.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Uruguay",
        "capital": "Montevideo",
        "languages": [
            "Spanish"
        ],
        "population": 3480222,
        "flag": "https://restcountries.eu/data/ury.svg",
        "currency": "Uruguayan peso"
    },
    {
        "name": "Uzbekistan",
        "capital": "Tashkent",
        "languages": [
            "Uzbek",
            "Russian"
        ],
        "population": 31576400,
        "flag": "https://restcountries.eu/data/uzb.svg",
        "currency": "Uzbekistani so'm"
    },
    {
        "name": "Vanuatu",
        "capital": "Port Vila",
        "languages": [
            "Bislama",
            "English",
            "French"
        ],
        "population": 277500,
        "flag": "https://restcountries.eu/data/vut.svg",
        "currency": "Vanuatu vatu"
    },
    {
        "name": "Venezuela (Bolivarian Republic of)",
        "capital": "Caracas",
        "languages": [
            "Spanish"
        ],
        "population": 31028700,
        "flag": "https://restcountries.eu/data/ven.svg",
        "currency": "Venezuelan bolívar"
    },
    {
        "name": "Viet Nam",
        "capital": "Hanoi",
        "languages": [
            "Vietnamese"
        ],
        "population": 92700000,
        "flag": "https://restcountries.eu/data/vnm.svg",
        "currency": "Vietnamese đồng"
    },
    {
        "name": "Wallis and Futuna",
        "capital": "Mata-Utu",
        "languages": [
            "French"
        ],
        "population": 11750,
        "flag": "https://restcountries.eu/data/wlf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "Western Sahara",
        "capital": "El Aaiún",
        "languages": [
            "Spanish"
        ],
        "population": 510713,
        "flag": "https://restcountries.eu/data/esh.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Yemen",
        "capital": "Sana'a",
        "languages": [
            "Arabic"
        ],
        "population": 27478000,
        "flag": "https://restcountries.eu/data/yem.svg",
        "currency": "Yemeni rial"
    },
    {
        "name": "Zambia",
        "capital": "Lusaka",
        "languages": [
            "English"
        ],
        "population": 15933883,
        "flag": "https://restcountries.eu/data/zmb.svg",
        "currency": "Zambian kwacha"
    },
    {
        "name": "Zimbabwe",
        "capital": "Harare",
        "languages": [
            "English",
            "Shona",
            "Northern Ndebele"
        ],
        "population": 14240168,
        "flag": "https://restcountries.eu/data/zwe.svg",
        "currency": "Botswana pula"
    }
]


def most_spoken_languages(liste, number=10):
    """Count countries listing each language (not the number of speakers)."""
    counter = {}
    for country in liste:
        for lang in country.get("languages", []):
            if lang not in counter:
                counter[lang] = 1
            else:
                counter[lang] += 1
    sorted_counter = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return sorted_counter[:number]


def most_populated_countries(liste, number=10):
    sorted_pop = sorted(liste, key=lambda country: country.get("population", 0), reverse=True)
    return [(country["name"], country["population"]) for country in sorted_pop[:number]]


print(f"1.\t Is 17 a prime number : {is_prime(17)}")
print(f"  \t Is 18 a prime number : {is_prime(18)}")
print(f"2.\t Are the elements unique : {all_unique([1, 2, 3, 4])}")
print(f"  \t Are the elements unique : {all_unique([1, 2, 2, 4])}")
print(f"3.\t Are all items of the same type : {all_data_types([1, 2, 3])}")
print(f"  \t Are all items of the same type : {all_data_types([1, '2', 3])}")
print(f"4.\t Is 'my_variable' a valid variable name : {is_variable('my_variable')}")
print(f"  \t Is 'for' a valid variable name : {is_variable('for')}")
print("5.\t Countries data :")
print("  a. Ten most commonly listed languages (number of countries) :")
for language, count in most_spoken_languages(list_data, 10):
    print(f"  \t {language}: {count}")
print("  b. Ten most populated countries :")
for country, population in most_populated_countries(list_data, 10):
    print(f"  \t {country}: {population:,}")


