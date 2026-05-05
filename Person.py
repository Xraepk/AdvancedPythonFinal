from Interactable import Interactable

class Person(Interactable):
    def __init__(self, name, snack):
        Interactable.__init__(self, name, True)
        self.snack = snack

    def interact(self, tool=None):
        if self.needs_tool:
            print("I'm Hungry!")
            command = input(f"Feed {self.name}? (Y/N): ").upper().strip()
            if tool.get_name() != self.snack:
                input(f"I DON'T WANT TO EAT A {tool.get_name().upper()} I WANT {self.snack.upper()} (Enter): ")
            elif command == "Y":
                self.needs_tool = False
                input(f"YAAAAAY MY {self.snack.upper()}!!! (Enter): ")
        else:
            input(f"{self.name} is full. (Enter) :")

    def get_info(self):
        return [self.needs_tool]

    def set_info(self, info):
        self.needs_tool = info[0]