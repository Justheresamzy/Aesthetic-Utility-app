print()
print("Student Login")
print()


new_use = input("Enter a new Username: ")
new_pas = input("Enter a new Password: ")

print("All set!")

log_use = input("Enter Your Username: ")
log_pas = input("Enter Your Password: ")

while not log_use == new_use and log_pas == new_pas:
    print("wrong username, try again!")
    log_use = input("Enter Your Username: ")
while not log_pas == new_pas:
        print("wrong password, try again!")
        log_pas = input("Enter Your Password: ")

print()
print("You are logged in!")

print()
print("quiz")

score = 0

q1= input("What is 2+2 : ")
print()
q2 = input("What is 3x3 = : ")
print()
q3 = input("What is 4x2 = : ")
print()

if q1 == "4" :
    score += 1
if q2 == "9" :
    score += 1
if q3 == "8":
    score += 1
print(f"Your final score is {score} / 3")