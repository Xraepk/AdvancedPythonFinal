
class Interactable:
    def __init__(self, name, needs_tool=False, message="You interacted with"):
        self.name = name
        self.needs_tool = needs_tool
        self.message = message

    def interact(self, tool=None):
        if self.needs_tool:
            tool_name = tool.get_name()
            if tool_name == "Empty":
                tool_name = "nothing"
            input(f"{self.message} {self.name} using {tool_name}! (Enter): ")
        else:
            input(f"{self.message} {self.name}! (Enter): ")

    def get_name(self):
        return self.name

    def get_info(self):
        return [self.needs_tool]

    def set_info(self, info):
        self.needs_tool = info[0]