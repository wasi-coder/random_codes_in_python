def hello ():
    print("Welcome to the game")
name= input("Enter your name: ")

def main ():
    if(name=="wasi"):
        print("You are a great player")
    else:
        print("You are a bad player")

name=name.strip().capitalize()

print("Hello",name)
hello() 


main()
