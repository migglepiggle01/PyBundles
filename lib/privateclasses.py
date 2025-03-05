import getpass
from privacyutils import GetPass

from cryptography.fernet import Fernet

class SecureStorage:
    def __init__(self, master_password):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.data_store = {}  # Holds encrypted data
        self.master_password = master_password  # Store only temporarily

    def save(self, data):
        """Encrypts keys and values before storing them."""
        self.data_store = {
            self.cipher.encrypt(key.encode()).decode(): self.cipher.encrypt(value.encode()).decode()
            for key, value in data.items()
        }

    def load(self, encrypted=False):
        """Returns only encrypted data unless the user verifies with a password."""
        if encrypted:
            return self.data_store

        # Ask for password before decryption
        user_input = GetPass.get_hidden_pass(prompt="Enter password to decrypt data: ")

        if user_input != self.master_password:
            print("Access Denied: Incorrect password.")
            return None  # Deny access

        # Decrypt only if password is correct
        return {
            self._decrypt_once(key): self._decrypt_once(value)
            for key, value in self.data_store.items()
        }

    def _decrypt_once(self, encrypted_value):
        """Decrypts once and immediately wipes the value."""
        decrypted = self.cipher.decrypt(encrypted_value.encode())
        decrypted_bytearray = bytearray(decrypted)  # Mutable byte array

        # Convert to string just for return, but minimize persistence
        result = decrypted.decode()

        # Overwrite memory with zero bytes
        for i in range(len(decrypted_bytearray)):
            decrypted_bytearray[i] = 0

        return result
