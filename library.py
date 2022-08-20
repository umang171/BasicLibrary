class Library:
    def __init__(self,books,nm):
        self.books=books
        self.nm=nm
        self.lendlist = {}
    def display(self):
        i=1
        print("List of books:")
        for item in self.books:
            print("book",i,":",item)
            i+=1
    def lend(self,name,bnm):
       if bnm not in self.lendlist.keys():
            self.lendlist.update({bnm:name})
            print(f"{name},you got your {bnm}")
       else:
           print("book is already taken by",self.lendlist[bnm])
    def add(self,book):
        self.books.append(book)
        print("book is added")
    def retur(self,bnm):
        self.lendlist.pop(bnm)
        print(f"you successfully returned {bnm}")


if __name__ == '__main__':
    umang = Library(["cpp", "php", "asp", "c#", "java", "python", "android", "cl"], "Umang libray")
    while True:
        choice=int(input("1 for display\n2 for lend \n3 for add\n4 for return\n"
                         "0 to quit\nEnter your choice:"))
        if choice==1:
            umang.display()
        elif choice==2:
            name=input("Enter your name:")
            bnm=input("Enter your book name:")
            umang.lend(name,bnm)
        elif choice==3:
            booknm=input("your book name:")
            umang.add(booknm)
        elif choice==4:
            bnm=input("Enter your book name:")
            umang.retur(bnm)
        elif choice==0:
            exit()
        else:
            print("invalid choice")
