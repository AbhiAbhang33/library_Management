"""
Author:- Abhi
Discription:- This code is written for manage the library using python.
Date:- Jan 24, 2024.
"""

try:
    
    class Library:
        def __init__(self, listOfBooks):
            self.books = [book.lower() for book in listOfBooks]     # Convert all book names to lowercase
            self.issued_books = {}      # Dictionary to store issued books and corresponding students

        def displayAvailableBooks(self):
            print("Books present in this library are: ")
            for book in self.books:
                print(" * " + book.capitalize())    # Capitalize the first letter of each book name

        def borrowBook(self, bookName, studentName):
            bookName = bookName.lower()     # Convert the input book name to lowercase
            if bookName in self.books:
                if bookName in self.issued_books:
                    print(f"Sorry,{studentName} '{bookName}' is already issued to {self.issued_books[bookName]}")
                    return False
                else:
                    self.issued_books[bookName] = studentName
                    print(f"{studentName} You have been issued '{bookName}' Book. Please keep it safe and return it within 30 days.")
                    self.books.remove(bookName)
                    return True
            else:
                print(f"Sorry, {studentName} This book is either not available in the library.")
                return False

        def returnBook(self, bookName):
            bookName = bookName.lower()         # Convert the input book name to lowercase
            if bookName in self.issued_books:
                self.books.append(bookName)
                print(f"Thanks {studentName} for returning this {bookName} Book! Hope you enjoyed reading it. Have a great day a head!")
                del self.issued_books[bookName]  # Remove the book from the issued_books dictionary
            else:
                print(f"{studentName} This is not the book you borrowed from here.")
            
    studentName = input('Enter Your Name: ')

    class Student:
        def requestBook(self):        
            self.book = input("Enter the name of the book you want to borrow: ")
            self.book = self.book.lower()
            return self.book 

        def returnBook(self):        
            self.book = input("Enter the name of the book you want to return: ")
            self.book = self.book.lower()
            return self.book

    if __name__ == "__main__":
        aspirantsLibrary = Library(["Python Notes", "Django", "HTML", "SQL", "Algorithms"])
        student = Student()
        
        while True:
            welcomeMsg = '''\n ====== Welcome to Aspirants Library ======
            Please choose an option:
            1. List all the books
            2. Request a book
            3. Return a book
            4. Exit
            '''
            print(welcomeMsg)
            a = int(input("Enter a choice: "))
            if a == 1:
                aspirantsLibrary.displayAvailableBooks()            
            elif a == 2:
                book_to_borrow = student.requestBook()
                studentName = studentName     # Assuming student name is for simplicity
                aspirantsLibrary.borrowBook(book_to_borrow, studentName)
            elif a == 3:
                book_to_return = student.returnBook()
                aspirantsLibrary.returnBook(book_to_return)
            elif a == 4:
                print(f"Thanks {studentName} for choosing Aspirants Library. Have a great day a head!")
                exit()
            else:
                print("Invalid Choice!")

except Exception as e:
    print(f"Error Occured = {e}")

finally:
    print('Visit Again...')