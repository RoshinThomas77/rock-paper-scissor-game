import random
items=["rock","paper","scissor"]
scoreuser=0
scorecomp=0
while scoreuser< 3 and scorecomp <3:
 computer=random.choice(items)
 user=input("\nEnter rock,paper or scissor:").lower()
 if user not in  items:
     print("invalid input")
     continue
 print("computer chose:",computer)
 if user==computer:
    print("\nDraw !!!")
    print("your score:",scoreuser,
          "computer score:",scorecomp)
 elif user=="rock" and computer=="scissor":
    print("\n🏆 you win")
    scoreuser=scoreuser+1
    print("your score:",scoreuser,
          "computer score:",scorecomp)
 elif user=="paper" and computer=="rock":
    print("\n🏆 you win")
    scoreuser=scoreuser+1
    print("your score:",scoreuser,
          "computer score:",scorecomp)
 elif user=="scissor" and computer=="paper":
    print("\n🏆 you win")
    scoreuser=scoreuser+1
    print("your score:",scoreuser,
          "computer score:",scorecomp)
 else:
    print("\n💻Computer win")
    scorecomp=scorecomp+1
    print("your score:",scoreuser,
          "computer score:",scorecomp)
if scoreuser==3:
    print("\n🏆 you win !!!!")
else:
    print("\n💻 computer win !!!!")
input("\npress ENTER to exit........")