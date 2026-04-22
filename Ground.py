class Ground:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)