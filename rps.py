import random
print'                   welcome to the Game!'
print'                 Rock,Paper and Scissor!'
r=1
p=2
s=3
print'select your choice as r,p or s for Rock,Paper and Scissor respectively.'
while True:
    a=input('\n Enter your choice:')
    print'Hope for Your luck...'
    b=random.randint(1,3)
    if a==b:
        print'ohh! Its a Tie!'
    elif a==1 and b==3:
        print'Congratulations! You won the game'
    elif a==1 and b==2:
        print'Sorry..You lost the game.'
    elif a==2 and b==1:
        print'Congratulations! You won the game'
    elif a==2 and b==3:
        print'Sorry..You lost the game.'
    elif a==3 and b==1:
        print'Sorry..You lost the game.'
    elif a==3 and b==2:
        print'Congratulations! You won the game'

