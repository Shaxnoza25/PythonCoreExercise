try:
    with open("example.txt", "r") as fie:
        content=fie.read()
        print(content)
except FileNotFoundError:
    print("The file doesnt exist")