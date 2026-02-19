#Reading a txt file in a python program

def read():
    #IDK why this isn't working but whatevs
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
    file.close()

if __name__ == "__main__":
    read()
