"""
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.
In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals
# """
# import requests, json
# from pprint import pprint

# response=requests.get("https://restcountries.com/v3.1/all").text
# # response=requests.get("https://restcountries.com/v3.1/all")
# response=json.loads(response)
# for each in response:
#     name=each["name"]["common"]
#     area=each["area"]
#     population=each["population"]
#     # print(f"{name} have {area} km2 and {population/1000000} millions people")
#     if name=="India":
#         currency=each["currencies"]
#         print(f"The currency of {name} is {currency}. The population is {population/1000000} millions people")
#     if name=="France":
#         currency=each["currencies"]
#         print(f"The currency of {name} is {currency}. The population is {population/1000000} millions people")
#     if name=="Costa Rica":
#         currency=each["currencies"]
#         print(f"The currency of {name} is {currency}. The population is {population/1000000} millions people")


## Updated code

import requests, json
from pprint import pprint


def get_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url).text
    data = json.loads(response)[0]

    native_names = data["name"]["nativeName"]
    native_name = list(native_names.values())[0]["common"]

    country_info = {
        "name": data["name"]["common"],
        "native_name": native_name,
        "capital": data["capital"][0],
        "population": data["population"],
        "area": data["area"]
    }

    return country_info

home_country = get_country_data("India")
current_country = get_country_data("Japan")

print("\nHome country data:")
pprint(home_country)

print("\nCurrent country data:")
pprint(current_country)

if home_country["population"] > current_country["population"]:
    larger_population = home_country["name"]
else:
    larger_population = current_country["name"]


area_difference = abs(home_country["area"] - current_country["area"])


print("\nComparison Results:")
print(f"- {larger_population} has the larger population.")
print(f"- Area difference: {area_difference:.2f} km²")

print("\nAdditional Information:")
print(f"{home_country['name']} native name: {home_country['native_name']}, capital: {home_country['capital']}")
print(f"{current_country['name']} native name: {current_country['native_name']}, capital: {current_country['capital']}")