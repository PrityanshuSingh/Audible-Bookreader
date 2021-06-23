import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# ITS HAPPENING TOO SLOW SO REAL TYPE FEELING IS NOT COMING BETTER USE SIMPLE PRINT STATEMENT ONE
'''lst=[]
msg = "Let's see who is gonna win, well well well!, no worries i am pro at this."
a=msg.split()
for i in msg.split():
    lst.append(i)
for char in a:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.00000000000009)
    richard(char)'''

'''                 **************************************** CHARACTERS IN THE GAME ********************************************                      '''


# index 0 is for DAVID (narrator MALE)
# index 1 is for RICHARD (narrator MALE)
# index 2 is for MARK (narrator MALE)
# index 3 is for LINDA (narrator FEMALE)
# index 4 is for ZIRA (narrator FEMALE)

# MALE NARRATOR DAVID
def david(line):
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)  
    engine.say(line)
    engine.runAndWait()


# MALE NARRATOR RICHARD
def richard(line):
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)  
    engine.say(line)
    engine.runAndWait()


# FEMALE NARRATOR ZIRA
def zira(line):
    engine.setProperty('voice', voices[4].id)
    engine.setProperty('rate', 150)
    engine.say(line)
    engine.runAndWait()


# MALE NARRATOR MARK
def mark(line):
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)  
    engine.say(line)
    engine.runAndWait()


# FEMALE NARRATOR LINDA
def linda(line):
    engine.setProperty('voice', voices[3].id)
    engine.setProperty('rate', 150)
    engine.say(line)
    engine.runAndWait()
