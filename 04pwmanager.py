master_pwd = input("What is the master password? : ")

def view():
    with open("04password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip("\n")
            user, passw = data.split(" | ")
            print("User:", user, ", Password:", passw)

def add():
    name = input("User name: ")
    pwd = input("Passwod: ")
    with open("04password.txt", "a") as f:
        f.write(name + " | " + pwd + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing password (add,view) or press 'q' to quit? : ".lower())
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode")
