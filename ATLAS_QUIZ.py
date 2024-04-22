from random import random, choice
import time, openpyxl, json
#import pandas as pd

print()


class Atlas:
    name1 = input('Player1: ')
    name2 = input('Player2: ')

    counter = 0
    player1 = 0
    player2 = 0
    player = [player1, player2]

    def play_again(self):
        play_again = input('Would you like to play again? ')
        if play_again == 'yes':
            Atlas.exception_dial(self)
        else:
            exit()

    
    def Q_and_A(self):
        print("What is the capital of",self.country.upper(),"|")
        answer = input("Answer: ").upper()
        if answer == self.world_atlas[self.country]:
            print(">>\tCorrect!")
            Atlas.player1 += 1
            time.sleep(1)
        else:
            print(">>\tWrong!:", end = '')
            print("\tThe capital of",self.country.title(), "is", self.world_atlas[self.country].title())
            Atlas.player1+=0
            time.sleep(1)

    def exception_dial(self):
        print()
        try:
            questions=int(input("How many questions would you like to try? "))
            print()
        except (KeyboardInterrupt, ValueError):
            print("\n\t[error!] Something went wrong!\n")
            Atlas.exception_dial(self)
        else:
            pass
        
        while True:
            with open('C:\\Users\\labod\\Desktop\\wip\\dictionary.txt', 'r') as file:           #data
                self.world_atlas = json.load(file)
            
            print("Fab!", questions,"questions,...Let's go!")
            for i in range(questions):
                keys = list(self.world_atlas)
                self.country = choice(keys)

                if (Atlas.counter+1)%2 == 0:
                    print("\nQuestion",Atlas.counter+1,": "+Atlas.name2+'\'s turn!')
                    Atlas.Q_and_A(self)
                else:
                    print("\nQuestion",Atlas.counter+1,": "+Atlas.name1+'\'s turn!')
                    Atlas.Q_and_A(self)
                
                

            print()
            print('*** Loading result...')
            time.sleep(2)
            print(Atlas.name1+", you scored ",Atlas.player1)
            print(Atlas.name2+", you scored ",Atlas.player2)
            
            
            for i in Atlas.player:
                score = i / questions
                if i < questions*.5:
                    time.sleep(2)
                    print("\nYou scored",round(score*100,2),"%")
                    print("You failed the quiz!...relaunch app to try again!\n")
                    Atlas.play_again(self)
                else:
                    i>=questions*.5
                    time.sleep(2)
                    self.result = round(score*100,2)
                    print("\nCongratulation!  You passed the quiz!...",self.result,"%\n")
                    Atlas.play_again(self)
                
            


x = Atlas()
print()
x.exception_dial()



















    # def save(self):
    #     self.res = dict(zip(Atlas.name_list, self.ress))
    #     print(self.res)
    #     Atlas.Log(self)
    #     exit()
        
    # def Kounter(self):        
    #     Atlas.name_list.append(name1)
    #     self.ress = [Atlas.result_list1, Atlas.result_list2]
    #     Atlas.counter+=1
    #     if Atlas.counter == self.attempts*2:
    #         Atlas.save(self)
    #     else:
    #         pass
        
    # def Log(self):
    #     start_row = 0
    #     with pd.ExcelWriter("testing.xlsx", engine="openpyxl") as writer:
    #         df = pd.DataFrame(self.res)
    #         df.to_excel(writer, sheet_name = 'Result_Sheet', startrow=start_row, index=True)
    #         writer.save()

#class Round_exce(Atlas):
    
#     def Data_job(self):
#         try:
#             assert name1 and name2 in name
#         except AssertionError:
#             print("Error: Name not registered. Try again!")
#             Round_exce.Data_job(self)
#         else:
#             if name1 == "Bashir":
#                 try:
#                     self.result
#                 except AttributeError:
#                     Atlas.exception_dial(self)
#                 else:
#                     Atlas.result_list1.append(int(self.result))
#                     Atlas.Kounter(self)
#             else:
#                 try:
#                     self.result
#                 except AttributeError:
#                     Atlas.exception_dial(self)
#                 else:
#                     Atlas.result_list2.append(int(self.result))
#                     Atlas.Kounter(self)

    # def rounds(self):
    #     try:
    #         self.attempts=int(input("How many rounds would you like to go? "))
    #         print()
    #     except (KeyboardInterrupt, ValueError):
    #         print("\n\t[error!] Something went wrong!\n")
    #         Round_exce.rounds(self)
    #     else:
    #         # n = self.attempts -1
    #         # r = self.attempts-n
    #         # print('Round: ',r)
    #         pass