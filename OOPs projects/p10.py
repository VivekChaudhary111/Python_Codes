class LibraryBook:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"The book '{self.title}' by {self.author} has been borrowed."
        else:
            return f"The book '{self.title}' by {self.author} is not available for borrowing."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"The book '{self.title}' by {self.author} has been returned."
        else:
            return f"The book '{self.title}' by {self.author} was not borrowed."
book1 = LibraryBook("The Alchemist", "Paulo Coelho")
book2 = LibraryBook("The Da Vinci Code", "Dan Brown")
book3 = LibraryBook("The Catcher in the Rye", "J.D. Salinger")

book1.borrow()
book2.borrow()
book1.return_book()
book3.borrow()
book2.return_book()
book1.borrow()
#end code
g