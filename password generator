import string,random

# password length
length = int(input("Enter password length: "))

print("Choose character set for password from these : \n1. Digits\n2. Letters\n3. Special characters\n4. Exit")

characterList = ""

# character set for password
while(True):
	choice = int(input("Select a number : "))

	if(choice == 1):
		# Adding letters 
		characterList += string.ascii_letters

	elif(choice == 2):
		# Adding digits
		characterList += string.digits

	elif(choice == 3):
		# Adding special characters 
		characterList += string.punctuation

	elif(choice == 4):
		break

	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	#random number
	randomchar = random.choice(characterList)
	
	# appending 
	password.append(randomchar)

#password 
print("The random password is " + "".join(password))