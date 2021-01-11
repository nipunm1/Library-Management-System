class Library:
    books = []
    
    def addBook(self):
        name = input("Enter books name : ")
        self.books.append(name)        
        print("New Book Added.")

    def display(self):
        print("Books present in the library -:")
        for book in self.books:
            print(book)
        if(len(self.books) == 0):
            print("There is no book present in the library. List is Emplty.")    

    def issueBook(self,bookName):
        count=-1
        if(bookName in self.books):
            for b in self.books:
                try:
                    count = count+1
                    if(b == bookName):
                        studentName = input("Enter Student Name: ")
                        enroll = int(input("Enter Enroll number: "))
                        semester = int(input("Enter semester: "))
                        section = int(input("Enter section: "))
                        s = Student()
                        s.issueBookStudent(studentName,semester,section,bookName,enroll)
                        self.books.pop(count)
                        break
                except ValueError:
                    print("Please enter valid input.")
            return bookName    
        else:
            print(f"There is no book with name '{bookName}' present in the library.")
            return False

    def addBackBook(self,bookName):
        self.books.append(bookName)
        print("Book added back to library successfully")

class Student:
    name = []
    section = []
    semester = []
    enrollno = []
    borrowedBook = []

    def issueBookStudent(self,name,semester,section,bookName,enrollno):
        self.name.append(name)
        self.section.append(section)
        self.semester.append(semester)
        self.borrowedBook.append(bookName)
        self.enrollno.append(enrollno)
        print(f"Book '{bookName}' issued to student {name} with enrollno. {enrollno}")

    def displayBorrowedBooksDetails(self,name):
        count=-1
        if(name in self.borrowedBook):
            for n in self.borrowedBook:
                count=count+1
                if(n == name):
                    print(f"Book '{name}' borrowed by-:")
                    print(f"Student name = {self.name[count]}")
                    print(f"Section = {self.section[count]}")
                    print(f"Semester = {self.semester[count]}")
                    print(f"Enroll no. = {self.enrollno[count]}")
        else:
            print(f"There is no book borrowed with the name '{name}'")

    def returnBorrowedBook(self,name,enrollno):
        count=-1
        flag=0
        if(name in self.borrowedBook):
            for e in self.enrollno:
                count=count+1
                if(e == enrollno):
                    flag=1
                    if(self.borrowedBook[count] == name):
                        l = Library()
                        self.borrowedBook.pop(count)
                        self.name.pop(count)
                        self.section.pop(count)
                        self.semester.pop(count)
                        self.enrollno.pop(count)
                        l.addBackBook(name)
                        print("Thanks for returning back the book")
                    else:
                        print(f"There is no book with name '{name}' borrowed by student with enroll no. {enrollno}")
                        return False    
            if(flag == 0):    
                print(f"No student with enroll no. {enrollno} borrowed a book")
                return False    
        else:
            print(f"There is no book borrowed with the name '{name}'")
            return False

def mainSart():
    while(True):
        print("----------------------------------------------")
        print("0. Exit")
        print("1. Add new book.")
        print("2. Issue a book.")
        print("3. Add-back borrowed book.")
        print("4. Search Borrowed book details.")
        print("5. Display All Books present in the library.")
        try:
            choice = int(input("Enter your choice: "))
            if(choice == 0):
                break
            elif(choice == 1):
                l = Library()
                l.addBook()
            elif(choice == 2):
                l = Library()
                name = input("Enter Book name to issue: ")
                b = l.issueBook(name)
                if(b==False):
                    continue
            elif(choice == 3):
                try:
                    s = Student()
                    bookName = input("Enter book name : ")
                    enroll = int(input("Enter enroll no. : "))
                    b = s.returnBorrowedBook(bookName,enroll)
                    if(b==False):
                        continue
                except ValueError:
                    print("Please enter valid inputs.")
                except Exception:
                    print("Some Exception occured.")        
            elif(choice == 4):
                s = Student()
                name = input("Enter book name to search: ")
                s.displayBorrowedBooksDetails(name)
            elif(choice == 5):
                l = Library()
                l.display()
            else:
                print("Please enter valid input.")    
        except ValueError:
            print("Please enter valid input.")
        except Exception as e:
            print(f"Some exception occured : {e}")
        print("----------------------------------------------")

mainSart()