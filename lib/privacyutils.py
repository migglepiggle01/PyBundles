import sys
import keyboard
import getpass

class GetPass:
    @staticmethod
    def get_hidden_pass(prompt="Enter your password: "):
        """Securely gets password input while displaying asterisks (*) in the correct place."""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        password = ""

        while True:
            key = keyboard.read_event(suppress=True)  # Read keypress

            if key.event_type == "down":  # Only register key presses
                if key.name == "enter":
                    print()  # Move to new line after pressing enter
                    break
                elif key.name == "backspace":
                    if password:
                        password = password[:-1]
                        sys.stdout.write("\b \b")  # Erase last '*'
                        sys.stdout.flush()
                elif len(key.name) == 1 and not key.name.startswith("shift"):  # Ignore shift keys
                    password += key.name
                    sys.stdout.write("*")
                    sys.stdout.flush()

        return password

        
    @staticmethod
    def get_fully_hidden_pass(prompt="Enter your password: "):
        user_input = getpass.getpass(prompt)
        return user_input
