

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Human-readable string (no extra spaces)
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Code-like string (no extra spaces inside quotes or commas)
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Proper deletion message without extra spaces
        print(f"Deleting {self.title}")

