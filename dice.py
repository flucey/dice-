from random import choices
nrolls=10000
total=0
ndice=20
for i in range(nrolls):
    dice=choices(range(1,7),k=ndice)
    dice.sort(reverse=True)
    total=total+dice[0]+dice[1]
print("Average roll=", total/nrolls)