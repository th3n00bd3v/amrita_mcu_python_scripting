"""
Write a function that accepts the following arguments
INPUT:
    name: str
    job : str
    * args: adjectives (str) that describe things (i.e "happy", " sad")
    **args: possessions (str): value (int / float)
Output:
   Form a  nice string that explains everything relevant

example input:
   ('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20)
output:
   "Gilad is a teacher who is happy, amazing, and sooooo cool. Gilad has a bike worth 2000, a house worth 1000, and shoes worth 20"

The string should accomadate any number of *args and **kwargs.
"""

def full_introduction(name, *adjectives, job, **kwargs):
    if len(adjectives) > 1:
        adj_str = ', '.join(adjectives[:-1]) + ', and ' + adjectives[-1] + ' '
    elif adjectives:
        adj_str = adjectives[0] + ' '
    else:
        adj_str = ''

    article = 'an' if (adj_str + job)[0].lower() in 'aeiou' else 'a'

    possessions_list = [f"a {key} worth {value}" for key, value in kwargs.items()]
    if len(possessions_list) > 1:
        possessions = ', '.join(possessions_list[:-1]) + ', and ' + possessions_list[-1]
    elif possessions_list:
        possessions = possessions_list[0]
    else:
        possessions = ''

    intro = f"{name} is {article} {adj_str}{job}"

    if possessions:
        intro += f". {name} has {possessions}"

    return intro
 
print(full_introduction('Gilad', 'happy', 'amazing', 'sooooo cool', job='teacher', smartphone=15000, bike=75000, shoes=1200)) 
print(full_introduction('Alice', 'brilliant', job='engineer', laptop=45000, smartphone=85000)) 
print(full_introduction('Bob', job='artist', painting=500000, sculpture=120000))