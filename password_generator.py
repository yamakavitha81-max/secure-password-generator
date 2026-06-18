import random
import string
import re
#for generating password
def generate_password(length):
    if length < 6:
        return None, "Password should be at least 6 characters."
    upper=random.choice(string.ascii_uppercase)
    lower=random.choice(string.ascii_lowercase)
    digit=random.choice(string.digits)
    symbol=random.choice(string.punctuation)
    all_chars=string.ascii_letters+string.digits+string.punctuation
    remaining = [random.choice(all_chars) for _ in range(length - 4)]
    password_list=[upper,lower,digit,symbol]+remaining
    random.shuffle(password_list)
    password="".join(password_list)
    return password,"success"
#for checking strength of password
def check_strength(password):
    score=0
    if len(password)>=8:
        score=score+1
    if re.search(r"[A-Z]",password):
        score=score+1
    if re.search(r"[a-z]",password):
        score=score+1
    if re.search(r"[0-9]",password):
        score=score+1
    if re.search(r"[!@#$%^&*(),.?\:{}|<>]",password):
        score=score+1
    if score<=2:
        return "Weak"
    elif score==3 or score==4:
        return "Medium"
    else:
        return "Strong"
#saving file
def save_password(password):
    with open("passwords.txt","a")as file:
        file.write(password+"\n")
def main():
    print("\n======PASSWORD GENERATOR=====")
    while True:
        print("\n 1.Generate Password")
        print("2.Exit")
        choice=input("Enter choice:")
        if choice=="1":
            length=int(input("Enter Password Length:"))
            password,msg=generate_password(length)
            if password is None:
                print(msg)
                continue
            strength=check_strength(password)
            print("\nGenerated Password:",password)
            print("Strength:",strength)
            
            save=input("Save Password?(y/n):")
            if save.lower()=="y":
                save_password(password)
                print("Saved Successfully!")
        elif choice=="2":
            print("Exiting Program....")
            break
        else:
            print("Invalid choice.Try again.")
if __name__=="__main__":
    main()