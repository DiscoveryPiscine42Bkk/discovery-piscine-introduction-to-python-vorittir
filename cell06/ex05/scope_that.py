ef add_one(x):
    x = x + 1
    print("Inside add_one:", x)

if __name__ == "__main__":
    number = 5
    print("Before add_one:", number)
    add_one(number)
    print("After add_one:", number)