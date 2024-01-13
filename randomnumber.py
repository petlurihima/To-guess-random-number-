import random
a=random.randint(0,100)
guessno=a+1
while(a!=guessno):
  guessno=int(input("Enter Guessing number:"))
  if(guessno<=0):
    print("You are quitting")
    break;
  elif(guessno>a):
    print("Number is too large!Try again")
  elif(guessno<a):
    print("Number is too small!Try again")
else:
  print("Your guess is correct,Congratulations")