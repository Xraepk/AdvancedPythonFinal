from InventoryItem import InventoryItem

class Key(InventoryItem):
    def __init__(self, name):
        InventoryItem.__init__(self, name)
        door_id = 1