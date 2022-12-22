# student library system  using oops where student can borrow a book from the list of books, by creating a separate library and sudent class .your program must be menu driven .you are free to choose methods and atributes of your choice to implement this functionality #

class Library:
    def __init__(self,listOfBooks):
         self.books=listOfBooks
    def displayAvailableBooks(self):
        print("the books present in this library are: ")
        for book in self.books:
            
            print( "\t"+book)
            
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}.Please return it safely within 2 months")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry,this book has already been issued by someone else.Please wait until the book returns")
            return False
        
    def returnBook(self, bookName):
            self.books.append(bookName)
            print("thanks for returning this book. hope you emjoyed it")
class Student:
    
        def requestBook(self):
            self.book=input("enter the name of the book you want to borrow")
            return self.book
        
        def returnBook(self):
            self.book=input("enter the name of the book you want to return ")
            return self.book

if __name__=="__main__":
    centralLibrary = Library(["algo","django","clrs","python notes"])
    student= Student()
    centralLibrary.displayAvailableBooks()
    
    while(True):
        welcomeMSG=''' ====Welcome to central library====
        please choose an option:
        1- listing all the books
        2-request a book
        3-return a book
        4-exit library
        '''
        print(welcomeMSG)
        
        a=int(input("enter your choice: "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("thanks for using this central library.")
            exit()
        else:
            print("invalid choice!")
            









