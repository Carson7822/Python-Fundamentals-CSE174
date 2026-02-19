#Demostration of how one program can be broken into multiple functions

def startBox():
    print("*****")
    print("*****")
    print("*****")

def startTriangle():
    print("*****")
    print("****")
    print("***")
    print("**")
    print("*")

def main():
    startTriangle()
    print("Hi Everyone")
    startBox()
    print("goodbye")
    startBox()
    startTriangle()

if __name__ == "__main__":
    main()

