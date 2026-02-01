"""
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )
* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and post on the forum ;)
"""

from pprint import pprint
import requests

def fetch_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()
    return response["value"]
  
def fetch_rhyming_word(word):
    url = f"https://api.datamuse.com/words?rel_rhy={word}"
    response = requests.get(url).json()
    if response:
        return response[0]["word"]
    return None
  
poem_lines = []
for _ in range(5):
    joke = fetch_chuck_norris_joke()
    last_word = joke.split()[-1].strip('.,!?;"\'').lower()
    rhyme_word = fetch_rhyming_word(last_word)
    
    if rhyme_word:
        poem_lines.append(f"{joke} ... {rhyme_word}")
    else:
        poem_lines.append(joke)
        
print("Avant-Garde Chuck Norris Poem:\n")
for line in poem_lines:
    print(line)
    
print("\nEnjoy your avant-garde poem!")