""" # Demonstrating the ord() function.
char_1 = 'A'
char_2 = ' '  # space

print(ord(char_1))  #print the ASCII codepoint of A 65
print(ord(char_2))

# Demonstrating the chr() function.
print(chr(97))      #print the character of the codepoint
print(chr(945))

aa=chr(ord('a')) == 'a'
bb=ord(chr(945)) == 945
print(aa)
print(bb) 

# Demonstrating the list() function:
print(list("abcabc"))
"""

# Indexing through a string.
from random import choice
world_atlas = {"nigeria": "ABUJA", "togo": "LOME", "uk": "LONDON","scotland": "EDINBURG","wales": "CARDIFF","germany": "BERLIN", "benin": "PORT-NOVO"}
keys = list(world_atlas)
country = choice(keys)
for i in range(len(country)):

    print(country[i],end='  ')

print()

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Demonstrating the index() method:

print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))



# Demonstrating the capitalize() method:
print('aBcD'.capitalize())



# Demonstrating the center() method:
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
# Demonstrating the 2nd variant center() method:
print('[' + 'gamma'.center(20, '*') + ']')



# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))    #Returns the index of the substring if found -returns -1 if not found
print('kappa'.find('a', 2))  #Specifics search 2 args
print('kappa'.find('a', 1, 4)) # 3 args
print('kappa'.find('a', 1, 4))
# Demonstrating the rfind() method: searches from the end of the strings (r- right; from the right)
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)



# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")



# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())           #Returns true is string contains digits and strings -returns false if otherwise.
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())             #checks only alphabets
# Example 1: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())         #checks only digits



# Example: Demonstrating the islower() method:
print("Moooo".islower())            #checks only lower-cases -returns true; false if not lowercase
print('moooo'.islower())
# Example: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())   #output:i KNOW THAT i KNOW NOTHING.
# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())    #Capitalizes the first xter of every word. tai pei= Tai Pei



# Example: Demonstrating the isspace() method:
print(' \n '.isspace())             #checks only whitespaces -returns true; false if not whitespace
print(" ".isspace())
print("mooo mooo mooo".isspace())



# Demonstrating the join() method:
print("*".join(["omicron", "pi", "rho"]))       #output: omicon*pi*rho
a=["omicron", "pi", "rho"]                      #output: omicon# pi# rho
print("# ".join(a))
# Demonstrating the split() method:
print("phi      \tchi\npsi".split())                 #Returns a list ['phi','chi','psi']



# Demonstrating the parameterless lstrip() method:
print("[" + "            tau".lstrip() + "]")   #removes all whitespaces leading to the string
# Demonstrating the lstrip() method with parameter:
print("www.cisco.com".lstrip("w."))             #removes all leading whitespaces and xters enlisted in the arg to the string; cisco.com
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")           #removes all whitespaces leading and trailing the string


# Demonstrating the 2 parameter replace() method:
print("www.netacad.com".replace("www.netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))       #output: Thare are it
print("Apple juice".replace("juice", ""))
# Demonstrating the 3 parameter replace() method:
print("This is it!".replace("is", "are", 1))    #3rd parameter is the limit output: Thare is it
print("This is it!".replace("is", "are", 3))                                #output: Thare are it











        
