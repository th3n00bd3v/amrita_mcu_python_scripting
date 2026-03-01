# write code to generate a dictionary where
# each key is:an integer divisible by 3
# each value is: a list containing the even numbers in the range of key

# Take all the numbers divisible by 3 from 1-301
# example output
# {3: [2], 6: [2,4,6], 9:[2,4,6,8].... 300:[2,4,6,...298]}

dict_divisible_by_3 = {}

for n in range(3, 301, 3):
    even_numbers = list(range(2, n + 1, 2))
    dict_divisible_by_3[n] = even_numbers   

for n, even_numbers in dict_divisible_by_3.items():        
    print(f"Key: {n}, Value: {even_numbers}")

