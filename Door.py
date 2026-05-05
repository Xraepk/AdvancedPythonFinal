from Interactable import Interactable
from Key import Key

class Door(Interactable):
    def __init__(self, name, door_id, locked=True):
        Interactable.__init__(self, name, True)
        self.door_id = door_id
        self.locked = locked

    def interact(self, tool=None):
        if self.locked:
            if type(tool) != Key:
                input("This is a door! Try using a key. (Enter): ")
            else:
                print("Door is locked")
                command = input("Unlock door? (Y/N): ").upper().strip()
                if tool.door_id != self.door_id:
                    input("This door needs a different key! (Enter): ")
                elif command == "Y":
                    self.needs_tool = False
                    self.locked = False
                    input("Door unlocked (Enter): ")
        else:
            input("Door is unlocked (Enter) :")

    def get_info(self):
        return [self.needs_tool, self.locked]

    def set_info(self, info):
        self.needs_tool = info[0]
        self.locked = info[1]