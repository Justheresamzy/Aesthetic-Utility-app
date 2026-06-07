print("Flag Quiz")
print()
print()
name = input("What is your name?: ")
aw = input(f"Are you ready {name} (Y/N): ").lower()
score = 0

if aw == "n":
    print("Sorry for disturbing!")
    quit()
elif aw == "y":
    print("Let's start!")
print()

print()





print("Question 1")
print()

print("A: Saudi Arabia")
print("B: Oman")
print("C: UAE")

q1 = input("What is this flag 🇦🇪 : ").lower()

if q1 == "c":
    print("CORRECT! 🥳")
    score += 1
elif not q1 == "c":
    print("Incorrect 🕊️")


print()
print (f"Your score so far is {score}/5")
print()





print("Question 2")
print()


print("A: Germany")
print("B: Belgium")
print("C: Russia")


q2 = input("What is this flag 🇩🇪:").lower()


if q2 == "a":
    print("CORRECT! 🥳")
    score += 1
elif not q2 == "a":
        print("Incorrect 🕊️")


print()
print (f"Your score so far is {score}/5")



print()
print("Question 3")
print()


print("A: Ireland")
print("B: India")
print("C: France")

q3 = input("What is this flag 🇮🇪:").lower()


if q3 == "a":
    print("CORRECT! 🥳")
    score += 1
if not q3 == "a":
        print("Incorrect 🕊️")


print()
print (f"Your score so far is {score}/5")
print()




print("Question 4")
print()

print("A: Pakistan")
print("B: Algeria")
print("C: India")

q4 = input("What is this flag 🇩🇿:").lower()


if q4 == "b":
    print("CORRECT! 🥳")
    score += 1
if not q4 == "b":
        print("Incorrect 🕊️")


print()
print (f"Your score so far is {score}/5")
print()





print("Question 5")
print()

print("A: Nigeria")
print("B: Argentina")
print("C: Somalia")

q5 = input("What is this flag 🇦🇷:").lower()


if q5 == "b":
    print("CORRECT! 🥳")
    score += 1
if not q5 == "b":
        print("Incorrect 🕊️")



print()
print(f"Your score is {score}/5")
print()





if score > 3:
    print("YOU DID SO WELL!")
else:
    print("Yay Good job")
