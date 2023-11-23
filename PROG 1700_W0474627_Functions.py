def greet():
    print("Hello, welcome to the Python functions lessons!")

# call with an argument
def great_user(username):
    print(f"Hello {username}!")

great_user("John")

# multiplies two numbers
def multiply (a, b):
    return a*b

print(f"My agae is {multiply(6, 4)}!")

life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': '',
        'emus': '',
        },
    'plants': '',
    'other': ''
    }

def print_keys(dic):
    for key, value in life.items():
        print(key)
        if isinstance(value, dict):
            print_keys(value)