import sys
from ConversationalShell import ConversationalShell

class TerminalBridge:
    """
    CLI-based interface for interacting with Builder Core in real-time.
    Connects user input to ConversationalShell and prints responses.
    """
    def __init__(self):
        self.shell = ConversationalShell()

    def start(self):
        print("\n🤖 Builder Core CLI active. Type 'exit' to quit.\n")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting Builder Core CLI.")
                break
            response = self.shell.receive_message(user_input)
            print(f"Builder: {response}\n")