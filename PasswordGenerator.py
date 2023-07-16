import random
import string

letters = string.ascii_letters
numbers = string.digits
characters = string.punctuation
allChars = letters + numbers + characters
noNumbers = letters + characters
noCharacters = letters + numbers


def StandardGen():
    password = ''
    for x in range(16):
        password += random.choice(allChars)

    print("Your password is:", password)


def NoNumberGen():
    password = ''
    for x in range(16):
        password += random.choice(noNumbers)

    print("\nYour password is:", password)


def NoCharacterGen():
    password = ''
    for x in range(16):
        password += random.choice(noCharacters)

    print("\nYour password is:", password)


def OnlyLettersGen():
    password = ''
    for x in range(16):
        password += random.choice(letters)

    print("\nYour password is:", password)


print("\nThe total characters available are: ", allChars)

modifyChars = input("\nWould you like to remove a section of the characters listed above from your password (e.g no "
                    "numbers, no special characters or both)? [Yes/No] ")

if modifyChars.lower() == 'yes':

    removeCharChoice = input("What would you like to remove? [numbers, characters or both] ")

    if removeCharChoice.lower() == 'numbers':
        NoNumberGen()
    elif removeCharChoice.lower() == 'characters':
        NoCharacterGen()
    elif removeCharChoice.lower() == 'both':
        OnlyLettersGen()
    else:
        print("That is not a valid option")

elif modifyChars.lower() == 'no':
    StandardGen()

else:
    print("That is not a valid option")