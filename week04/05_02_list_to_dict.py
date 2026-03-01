# Exercise

# Write a Python program to convert the nested list to a list of dictionaries

# Sample lists: [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]

# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
#                   {'color_name': 'Red', 'color_code': '#FF0000'},
#                   {'color_name': 'Maroon', 'color_code': '#800000'},
#                   {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# use a for-loop

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result_list = []
for i in range(len(color_names)):
    result_list.append({
        "color_name": color_names[i],
        "color_code": color_codes[i]
    })

print(result_list)