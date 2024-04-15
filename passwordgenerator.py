import random,string
pass_length=int(input("Enter the Lenth of the Password:"))
includeAlphabets=input("Do You want to Include Alphabets: ")
includeSymbols=input("Do You want to Include Symbols: ")

def rand_pass(size):
    if includeSymbols=='yes' and includeAlphabets=='yes':
        symbols='#$&*%'
        generate_pass=''.join([random.choice(string.ascii_uppercase+string.ascii_uppercase+string.digits+string.punctuation)for n in range(size)])
    elif includeAlphabets=='yes' and includeSymbols!='yes':
        generate_pass=''.join([random.choice(string.ascii_uppercase+string.ascii_uppercase+string.digits)for n in range(size)])
    else:
        generate_pass=''.join([random.choice(string.digits)for n in range(size)])

    return generate_pass

password=rand_pass(pass_length)
print("Password = ",end=" ")
print(password)