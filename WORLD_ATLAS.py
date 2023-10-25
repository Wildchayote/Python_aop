import time, json
import time


def escape():
    print("[!] Okay bye",user,"(:\n")
    exit()
print()
user=input("[prompt:]  Enter username: ")
print()

with open('dictionary.txt', 'r') as file:
    world_atlas = json.load(file)

while True:
    nation=input("[prompt:]  Enter name of country: ").lower()
    for i in range(3):
        if nation in world_atlas:
            print("[output:] ",nation.upper(),"|",world_atlas[nation])
            print()

            if i==2:
                esc=input("""Would you like to exit app?...
Enter yes to exit and otherwise to stay:
""").lower()
                print()
                if esc=="yes":
                    escape()
                else:
                    pass
                    #nation=input("Enter name of country: ").lower()
            else:
                nation=input("Enter name of country: ").lower()
        else:
            print("[error:] "+nation.title()+" not found! Enter correct spelling\n")
            esc=input("""Would you like to exit app?...
Enter yes to exit and otherwise to stay:
""").lower()
            print()
            if esc=="yes":
                escape()
            else:
                nation=input("Enter name of country: ").lower()
