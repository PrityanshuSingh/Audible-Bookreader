from bookread_lib.bookshelf.main_book_sh import *
import PyPDF2
# Taking book and page name
def book(voice,name):
    print()
    line = ("I am glad I will be your narrator.")
    print(name+line)
    voice(line)

    b_number,b_name,dic_pdf=directory()
    book_name=bookshelf(voice,b_number,b_name,dic_pdf)

    book_path=r"C:\Users\prity\PycharmProjects\BOOKREADER- PS\available_books"
    slash="\\"

    pdfFileObj = open(book_path+slash+book_name+".pdf", 'rb')  # 'rb' for read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    n = pdfReader.numPages

    print()
    line = ("Enter the page number (out of "+str(n)+" pages in "+book_name +") from where you want to continue your book.")
    print(name+line)
    voice(line)

    page = input("=> ")

    line = ("Wait! Opening " + book_name)
    print(name+line)
    voice(line)

    return book_name,page,name

#book(voice=richard,name="richard")
