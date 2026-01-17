"""
create a library class
# Attributes
title
author
publisher
price

# Methods
book information (to get the information for the current book, use print())

Define a constructor used to initialize the attributes of the method with values entered by the user.
"""

class Library:
    def __init__(self):
        self.title = input("Enter the book title: ")
        self.author = input("Enter the author's name: ")
        self.publisher = input("Enter the publisher: ")
        while True:
            try:
                self.price = float(input("Enter the price of the book: "))
                break
            except ValueError:
                print("Please enter a valid number for the price.")
                
                
        
    def book_information(self):
            print("\nBook Information:")
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Publisher: {self.publisher}")
            print(f"Price: ${self.price:.2f}")
        
if __name__ == "__main__":
    book = Library()
    book.book_information()