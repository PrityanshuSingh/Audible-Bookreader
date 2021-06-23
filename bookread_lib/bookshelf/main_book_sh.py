# Making book shelf
from bookread_lib.voices.main_v import *
import os

def directory():
    # taking out all the files frm the given folder path or directory
    path=r'C:\Users\prity\PycharmProjects\BOOKREADER- PS\available_books'
    lst=os.listdir(path)
    lst_store=[]
    for filename in lst:
        store=os.path.splitext(filename) # splitting the filenames and their extensions
        lst_store.append(store) # and then storing the splitted items them in a list

    # splitting out .pdf extension files from the folder
    #print(lst_store)
    dic_pdf={}
    count=0
    for j in lst_store:
        if j[1] == ".pdf":   # separating .pdf files from lst_store and storing them in a dictionary dic_pdf
            count+=1
            dic_pdf[count]=j[0]
        elif j[1]=="":       # separating files with no ext (i.e folders) from lst_store
            pass
        else:
            pass

    # separating book number and book name from dictionary dic_pdf nd storing them in sep lists
    #print(dic_pdf)
    b_number=[]
    b_name=[]
    for i in dic_pdf:
        b_number.append(i)
        b_name.append(dic_pdf[i])

    #print(b_number)
    #print(b_name)

    return b_number,b_name,dic_pdf
    

# ALL THE PRINTING STUFF NOTHING MORE
def bookshelf(voice,b_number,b_name,dic_pdf):
    print("\033[4m" +"".center(180)+ "\033[0m")
    print("\033[1m" +"| YOUR BOOKSHELF |".center(180)+ "\033[0m")
    voice("THIS IS YOUR BOOKSHELF.")
    print("\033[4m" +"".center(180)+ "\033[0m")
    print()
    for i in b_number:
        print("\t"*18,end="")
        print(i," ","\t"*3,"- ","\t"*3,end="")
        print(b_name[i-1])

    print("\033[4m" +"".center(180)+ "\033[0m")
    print("\033[1m" +"| SELECT THE NUMBER OF THE BOOK YOU WANT TO READ |".center(185)+ "\033[0m")
    voice("| SELECT THE NUMBER OF THE BOOK YOU WANT TO READ |")
    ask_num_b=int(input("".center(90)))
    print("\033[1m" +"".center(78)+"| YOU CHOSE "+dic_pdf[ask_num_b]+" |"+ "\033[0m")
    voice("| YOU CHOSE "+dic_pdf[ask_num_b]+" |")
    print("\033[4m" +"".center(180)+ "\033[0m")
    book_name=dic_pdf[ask_num_b]

    return book_name

#bookshelf()
