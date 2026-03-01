# create a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

input_string = "hello world"
result_list = []
words = input_string.split()
for word in words:
    result_list.append(tuple(word))
    
print(result_list)