print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
n1=name1.lower()
n2=name2.lower()
t1=n1.count('t')
t2=n2.count('t')
t=int(t1)+int(t2)
r1=n1.count('r')
r2=n2.count('r')
r=int(r1)+int(r2)
u1=n1.count('u')
u2=n2.count('u')
u=int(u1)+int(u2)
e1=n1.count('e')
e2=n2.count('e')
e=int(e1)+int(e2)
true=str(t+r+u+e)
l1=n1.count('l')
l2=n2.count('l')
l=int(l1)+int(l2)
o1=n1.count('o')
o2=n2.count('o')
o=int(o1)+int(o2)
v1=n1.count('v')
v2=n2.count('v')
v=int(v1)+int(v2)
e1=n1.count('e')
e2=n2.count('e')
e=int(e1)+int(e2)
love=str(l+o+v+e)
score=int(true+love)
if(score<=10 or score>=90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score<40 and score>50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"your score is {score}, made for eachother.")