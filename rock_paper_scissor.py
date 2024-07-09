import random
def result(v,s1,s2):
    l=["r","p","s"]
    c=random.choice(l)
    print("Computer choice : ",c)
    if v==c:
        print("Both did the same try again")
        return s1,s2
    if v=='r':
        if c=='p':
            s2+=1
        else:
            s1+=1
    elif v=='p':
        if c=='s':
            s2+=1
        else:
            s1+=1
    else:
        if c=='r':
            s2+=1
        else:
            s1+=1
    return s1,s2
s1,s2=0,0
winning_score=int(input("Enter the winning score for which you want to play the game: "))
print("Instrucions:\nFor rock type r\nFor paper type p\nFor scissor type s")
while 1:
    if s1==winning_score or s2==winning_score:
        break
    v=input("Player choice : ")
    s1,s2=result(v,s1,s2)
    print(s1,s2)
if s1>s2:
    print("You are the winner !!")
elif s1==s2:
    print("It's a draw")
else:
    print("Computer is the winner !!")
