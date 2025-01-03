import random

print("Kockadobás játék")
print("Szabály: az nyer aki nagyobbat dob!\n")

neved = input("Kérlek írd be a neved: ")

print("Az első játékos: gép!")
p1 = random.randint(1,6)
print("A gép dobása: ", p1, "\n")

print(neved, "következik!")
input("Nyomj ENTERt ha mehet...")
p2 = random.randint(1,6)
print(neved,"dobása: ", p2, "\n")

if p1>p2 :
    print("Sajnos most a gép nyert...")
elif p1<p2 :
    print("Gratulálok", neved,"! Te nyertél!!")
else :
    print("Szoros küzdelem... döntetlen!")
