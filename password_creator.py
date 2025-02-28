import random
import string


def password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    passw = ""
    i = 1
    while i <= length:
        char = random.choice(alphabet)
        passw += char
        i += 1
    return passw


try:
    length = int(input("Podaj oczekiwaną długość hasła: "))
except ValueError as Err:
    print(Err)
    exit()
generated_pass = password(length)
print(f"Oto twoje nowo wygenerowane hasło: {generated_pass}")
