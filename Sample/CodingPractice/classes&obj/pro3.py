class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        
    def display_info(self):
        return f"Author: {self.name}, Birth Year: {self.birth_year}"

class Book():
    def __init__(self, title, publication_year, author):
        self.title = title
        self.publication_year = publication_year
        self.author = author
        
    def display_info(self):
        author_info = self.author.display_info()
        return f"Book: {self.title}, Publication Year: {self.publication_year}\n{author_info}"

# Create an instance of Author
author = Author("Jane Austen", 1775)

# Create an instance of Book with the Author instance
book = Book("Pride and Prejudice", 1813, author)

# Display book and author information
print(book.display_info())