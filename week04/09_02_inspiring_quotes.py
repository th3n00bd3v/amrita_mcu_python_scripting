# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname

famous_quotes = [
    {
        "full_name": "Isaac Asimov",
        "quote": "I do not fear computers. I fear lack of them.",
    },
    {
        "full_name": "Emo Philips",
        "quote": "A computer once beat me at chess, but it was no match for me at "
        "kick boxing.",
    },
    {
        "full_name": "Edsger W. Dijkstra",
        "quote": "Computer Science is no more about computers than astronomy "
        "is about telescopes.",
    },
    {
        "full_name": "Bill Gates",
        "quote": "The computer was born to solve problems that did not exist before.",
    },
    {
        "full_name": "Norman Augustine",
        "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
        "and obeys the Second Law of Thermodynamics; i.e., it always increases.",
    },
    {
        "full_name": "Nathan Myhrvold",
        "quote": "Software is a gas; it expands to fill its container.",
    },
    {
        "full_name": "Alan Bennett",
        "quote": "Standards are always out of date.  That’s what makes them standards.",
    },
    {
        "full_name": "Martin Luther King Jr.",
        "quote": "The computer can't tell you the emotional story. It can give you the exact number of how many times a heart has been broken, but it can't tell you what that feels like.",
    }
]

inspiring_quotes = []

for quote_info in famous_quotes:
    full_name = quote_info["full_name"]
    quote = quote_info["quote"]

    name_parts = full_name.split()
    first_name = name_parts[0]
    last_name = " ".join(name_parts[1:])

    formatted_quote = f'"{quote}" - {last_name}, {first_name}'
    inspiring_quotes.append(formatted_quote)

for quote in inspiring_quotes:
    print(quote)