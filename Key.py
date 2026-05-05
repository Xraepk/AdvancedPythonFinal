from InventoryItem import InventoryItem

class Key(InventoryItem):
    def __init__(self, name, door_id):
        InventoryItem.__init__(self, name)
        self.door_id = door_id