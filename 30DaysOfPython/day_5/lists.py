print("\n","-"*30,"Exercice: Level 1", "-"*30,"\n")

empty_list = []
five_items = [1,2,3,4,5]


print(f"1.\t Empty list : {empty_list}")
print(f"2.\t Five item list : {five_items}")
print(f"3.\t Length of five item list : {len(five_items)}")
print(f"4.\t First, middle, last item of list : {five_items[0]} {five_items[2]} {five_items[-1]}")

mixed_data = ["Sebastian NATI",24, 175, False, "Paris"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

print(f"5.\t 'mixed_data' list : {mixed_data}")
print(f"6.\t 'it_companies' list : {it_companies}")

print(f"7.\t Print the list : {it_companies}")
print(f"8.\t Number of companies in list : {len(it_companies)}")
print(f"9.\t First, middle, last companies in list : {it_companies[0]}, {it_companies[3]}, {it_companies[-1]}")

it_companies[0] = "OpenAI"
print(f"10.\t Modify the list : {it_companies}")

it_companies.append("Antropic")
print(f"11.\t Adding a new company : {it_companies}")

it_companies.insert(4,"Mistral")
print(f"12.\t Insert in middle of the list : {it_companies}")

it_companies[2] = it_companies[2].upper()
print(f"13.\t Company to uppercases in list : {it_companies}")

print(f"14.\t Joining it_companies : {"#; ".join(it_companies)}")
print(f"15.\t 'mc2i' in it_companies : {'mc2i' in it_companies}")

it_companies.sort()

print(f"16.\t Sorted list : {it_companies}")

it_companies.reverse()

print(f"17.\t Reversed list : {it_companies}")
print(f"18.\t 3 first companies from list : {it_companies[:3]}")
print(f"19.\t 3 last companies from list : {it_companies[-3:]}")
print(f"20.\t Middle companies form list : {it_companies[4]}")

it_companies.pop(0)

print(f"21.\t Removing First company from list : {it_companies}")

del it_companies[3:4]

print(f"22.\t Removing middle companies from the list : {it_companies}")

it_companies.pop()

print(f"23.\t Removing last company from the list : {it_companies}")

it_companies.clear()

print(f"24.\t Remove all companies : {it_companies}")

del it_companies

print("25.\t Destroyed 'it_companies' list")

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(f"26.\t Joining front_end and back_end lists : {front_end + back_end}")

full_stack = front_end.copy()
full_stack.extend(back_end)

full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")

print(f"27.\t Full stack extended list : {full_stack}")

print("\n","-"*30,"Exercice: Level 2", "-"*30,"\n")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

print(f"1.\t Sorted list : {ages} , max age : {ages[-1]}, min age : {ages[0]}")

ages.extend([26,19])
ages.sort()

mean = sum(ages)/len(ages)
print(f"2.\t Appened min and max ages to the list : {ages}")
print(f"3.\t Median age is : {(ages[5]+ages[6])/2}")
print(f"4.\t Mean age is : {mean}")
print(f"5.\t Range of ages : {ages[-1]-ages[0]}")
print(f"6.\t Comparing min from averge and max from average : {abs(ages[0]-mean)}; {abs(ages[-1]-mean)}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

print(f"7.\t Middle countries form list are : {countries[len(countries)//2:len(countries)//2+1] 
                                                if len(countries)%2 !=0 
                                                else countries[len(countries)//2]}")

mid = (len(countries) + 1) // 2
countries1 = countries[:mid]
countries2 = countries[mid:]

print(f"8.\t Dividing in two lists : \n\t\t{countries1}, \n\t\t{countries2}")
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,ru,usa,*scandic = countries
print(f"9.\t Unpack countries one by one and rest is scandic countries : {ch}, {ru}, {usa} {scandic}")