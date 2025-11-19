from cryptography.fernet import Fernet

def coder_message(message: str, key: bytes = None) -> tuple[bytes, bytes]:
    if key is None:
        key = Fernet.generate_key()
    fernet = Fernet(key)
    message_chiffre = fernet.encrypt(message.encode())
    return message_chiffre, key

if __name__ == "__main__":
    message = input("Écris ton message : ")

    message_chiffre, cle = coder_message(message)

    print("\n--- Résultat ---")
    print("Message chiffré :", message_chiffre)
    print("Clé utilisée pour le déchiffrement :", cle)
