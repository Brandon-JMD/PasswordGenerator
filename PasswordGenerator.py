import string
import secrets

letters = string.ascii_letters
numbers = string.digits
characters = string.punctuation
allChars = letters + numbers + characters
noNumbers = letters + characters
noChars = letters + numbers


def StandardGen():
    password = ''.join(secrets.choice(allChars) for x in range(16))
    print("Your password is:", password)


def NoNumberGen():
    password = ''.join(secrets.choice(noNumbers) for x in range(16))
    print("\nYour password is:", password)


def NoCharacterGen():
    password = ''.join(secrets.choice(noChars) for x in range(16))
    print("\nYour password is:", password)


def OnlyLettersGen():
    password = ''.join(secrets.choice(letters) for x in range(16))
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