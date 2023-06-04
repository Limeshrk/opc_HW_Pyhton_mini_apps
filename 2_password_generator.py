import string
import secrets

def password_generator():
    length = int(input("Milyen hosszú legyen a jelszó összesen (hány karakter): "))
    
    include_digits = input("Legyenek e benne számok (igen/nem): ")
    include_special_chars = input("Legyenek e benne speciális karakterek (igen/nem): ")
    
    characters = string.ascii_letters # Betűket mindig tartalmaznia kell
    if include_digits.lower() == "igen":
        characters += string.digits # és számokat
    if include_special_chars.lower() == "igen":
        characters += string.punctuation # és speciális karaktereket
    
    password = ""
    for _ in range(length):
      password += secrets.choice(characters) # összeállítja a jelszót

    print(f"\nAz generált jelszó: {password}")

password_generator()