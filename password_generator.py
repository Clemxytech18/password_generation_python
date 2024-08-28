import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

generated_password = []

print("Welcome to the PyPassword Generator!")

#Generate random letters
nr_letters = int(input("How many letters would you like in your password?\n"))
generated_letters = ""

for letter in range(0, nr_letters):
    generated_letters = generated_letters + random.choice(letters)
    generated_password.append(random.choice(letters))

#Generate random symbols
nr_symbols = int(input(f"How many symbols would you like?\n"))
generated_symbols = ""
for symbol in range(0, nr_symbols):
    generated_symbols = generated_symbols + random.choice(symbols)
    generated_password.append(random.choice(symbols))

#Generate random numbers
nr_numbers = int(input(f"How many numbers would you like?\n"))
generated_number = ""
for number in range(0, nr_numbers):
    generated_number = generated_number + random.choice(numbers)
    generated_password.append(random.choice(numbers))


#Generate Easy password
#Combine all into a list and shuffle
print("Easy Password:")
generated = [generated_letters, generated_symbols, generated_number]
random.shuffle(generated)
easy_password = ""
for password in generated:
    easy_password += password
print(easy_password)

print("Hard Password")
random.shuffle(generated_password) #shuffle generated list
hard_password = ""
for hard in generated_password:
    hard_password += hard
print(hard_password)
