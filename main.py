class book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.availible = True
        
    def borrow(self) -> None:
        self.availible = False
        
    def returnBook(self) -> None:
        self.availible = True
        
    def __str__(self) -> str:
        return f'"{self.title}" by {self.author}'

class library:
    def __init__(self, name) -> None:
        self.name = name
        self.contents: dict[str, book] = {}
        ourLibraries[name] = self
        
    def __str__(self) -> str:
        return f'{self.contents}'
 
    
bookCache: dict[str, book] = {
    "The Great Waltz": book("The Great Waltz", "Exx"),
    "A Great Day": book("A Great Day", "Anonymous Author")
}
ourLibraries: dict[str, library] = {}

    
def borrowBook(title: str, library: str) -> book:
    if title == "":
        raise Exception("Title is empty.")
   
    if library == "":
        raise Exception("Specify library name.")
   
    requestedBook: book = bookCache.get(title)
    requestedLib: library = ourLibraries.get(library)
    
    if not requestedBook:
        raise ValueError("Book not found in our database.")
    
    if not requestedLib:
        raise ValueError("Library not found.")
    
    requestedBook.borrow()
    requestedLib.contents[title] = requestedBook
    
    return requestedBook

def returnBook(title: str) -> book:
    if title == "":
        raise Exception("Title is empty.")
    
    for lib in ourLibraries.values():
        requestedBook: book = None
        requestedLib: library = None
        
        if title in lib.contents:
            requestedBook = lib.contents[title]
            requestedLib = lib
            break
    
    if requestedBook and requestedLib:
        requestedBook.returnBook()
        del requestedLib.contents[title]
        
        return requestedBook
        
def searchBook(title: str):
    for bookTitle, book in bookCache.items():
        if bookTitle == title:
            print(book)
            status = "Available" if book.availible else "Not available"
            print(f"Availability: {status}")
            
            