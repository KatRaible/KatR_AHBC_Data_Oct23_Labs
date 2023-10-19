def apt_search1(city, max_rent, min_beds, pets_allowed):
    search_criteria = f"Searching for apartments in {city} with a maximum rent of ${max_rent}, at least {min_beds} bedrooms"
    if pets_allowed:
        search_criteria += " that allow pets."
    else:
        search_criteria += " with no pets allowed."
    return search_criteria

city = "Metropolis"
max_rent = 2200
min_beds = 2
pets_allowed = True

search_result = apt_search1(city, max_rent, min_beds, pets_allowed)
print(search_result)

def apt_search2(city, max_rent, min_beds=1, pets_allowed=True):
    search_criteria = f"Searching for apartments in {city} with a maximum rent of ${max_rent}, at least {min_beds} bedrooms"
    if pets_allowed:
        search_criteria += " that allow pets."
    else:
        search_criteria += " with no pets allowed."
    return search_criteria

result1 = apt_search2("Metropolis", 1700)
print(result1)

result2 = apt_search2("Star City", 1500, min_beds=3)
print(result2)

result3 = apt_search2("Central City", 1200, pets_allowed=False)
print(result3)

plus_one_hundred = lambda x: x + 100
square_num = lambda x: x ** 2
concatenate = lambda s: "- " + s
divide_by_three = lambda x: x / 3

city = "Gotham City"
max_rent = 950

result4 = apt_search2(city, max_rent)
print("Result of first search:", result4)

num = 50
string = "Hello"

result5 = plus_one_hundred(num)
result6 = square_num(num)
result7 = concatenate(string)
result8 = divide_by_three(num)

print(plus_one_hundred(30))  
print(square_num(4)) 
print(concatenate('Hello'))  
print(divide_by_three(9))
