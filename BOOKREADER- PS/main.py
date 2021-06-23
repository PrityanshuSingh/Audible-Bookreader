# NOW I HAVE TO ADD DICTIONARY NAME FROM THE ENTERED NUMBER WHICH WILL THEN COPY TO THE SPCIFIED PATH AD AM DONE


from bookread_lib.midway.main_b import *
from bookread_lib.voices.main_v import *
import PyPDF2, os, time, subprocess

# WELCOME TEXT
print()
print("\033[1m" + "| HELLO |".center(180) + "\033[0m")
print("\033[1m" + "\033[4m" + "| WELCOME TO YOUR PERSONAL BOOK READER |".center(180) + "\033[0m")
print()
print("\033[1m" + "SELECT YOUR TODAY'S NARRATOR".center(180) + "\033[0m")
print()

# Taking user choice for voice
d = "Press d for selecting DAVID (MALE)"
r = "Press r for selecting RICHARD (MALE)"
m = "Press m for selecting MARK (MALE)"
l = "Press l for selecting LINDA (FEMALE)"
z = "Press z for selecting ZIRA (FEMALE)"
for i in [d, r, m, l, z]:
    print("\033[3m" + i.center(180) + "\033[0m")
ch = input("=> ")

# voice choices
if ch in ["d", "D"]:
    voice = david
    book, page, name = book(voice=david, name="David: ")

elif ch in ["r", "R"]:
    voice = richard
    book, page, name = book(voice=richard, name="Richard: ")

elif ch in ["m", "M"]:
    voice = mark
    book, page, name = book(voice=mark, name="Mark: ")

elif ch in ["l", "L"]:
    voice = linda
    book, page, name = book(voice=linda, name="Linda: ")

elif ch in ["z", "Z"]:
    voice = zira
    book, page, name = book(voice=zira, name="Zira: ")

#print(book, page)
# making entered book same as stored pdf file no use rn
'''collect=[]
for i in book:
    if i.isalpha():
        collect.append(i.lower())
call="".join(collect)'''

# converting entered book content to text form

book_path=r"C:\Users\prity\PycharmProjects\BOOKREADER- PS\available_books"
slash="\\"

pdfFileObj = open(book_path+slash+book+".pdf", 'rb')  # 'rb' for read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
n = pdfReader.numPages
#print(n)

# opening entered book pdf file
path = book_path+slash+book+".pdf"
subprocess.Popen([path], shell=True)

time.sleep(1)
# narrator waiting for us to reach to specied number
line = "Waiting for you to go to page number" + str(page)
voice(line)
time.sleep(3)

line = "Ok! Lets continue reading together."
voice(line)

value = True
check=[]
while value == True:
    for i in range(int(page) - 1, n + 1):
        pageObj = pdfReader.getPage(i)
        t = pageObj.extractText()

        '''if i==2:
            lst=t.split()
            print(lst)
            for j in range(26):
                lst.remove(lst[i-2])

            read=" ".join(lst)
            print("PAGE NO: ", i)
            voice("PAGE NUMBER " + str(i))
            print()
            print(read)
            voice(read)'''

        newsplit = []
        split = t.split()
        for j in split:
            store_l = []
            for k in j:  # looping indi letters
                if k != "™":
                    store_l.append(k)
                else:
                    pass

            combine = ''.join(store_l)
            newsplit.append(combine)

        read = " ".join(newsplit)
        print()
        print("PAGE NO: ", i + 1)
        voice("PAGE NUMBER " + str(i + 1))
        print(t)
        voice(read)

        # LATER DO THIS THAT IS CLOSE THE LOOP IF USER SAID NO
        if i + 1 == int(page) + 10:
            line = "Its been so long...Do you want to continue reading? (press y or n)"
            print(name+line)
            voice(line)
            ask = input("=> ")
            if ask in ['y', 'y']:
                pass
            elif ask in ['n', 'N']:
                for k in ["n","N"]:
                    check.append(k)

                break
        else:
            pass

    if check == ["n", "N"]:
        line = "Thanks for reading."
        print(name+line)
        voice(line)
        break
    else:
        pass





