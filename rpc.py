import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

array = [rock,paper,scissors]
# user
inp = int(input("enter 0 for rock, 1 for paper, 2 for scissors"))
input = array[inp]
print(input)
# computer
rannum = random.randint(0,2)
print(rannum)
computer = array[rannum]
print(computer)
if(inp == rannum):
    print("draw")
elif(inp == 0) and (rannum == 1):
    print("You win")
elif(inp == 1) and(rannum == 2):
    print("You loose")
elif(inp == 1) and (rannum == 0):
    print("You win")
elif(inp == 2) and (rannum == 1):
    print("you win")
elif(inp == 2) and (rannum == 0):
    print("you loose")
elif(inp == 0) and (rannum == 2):
    print("You win")








# print(computer)


