from ItemRack import ItemRack

class Profile:
    def __init__(self, name, slot_num, inventory=None, item_rack=None):
        self.name = name
        self.id_num = slot_num
        if inventory is None:
            self.inventory = [None, None, None, None]
        self.inventory = inventory
        self.item_rack = ItemRack("ItemRack" + slot_num + "db")

    def set_slot(self, slot_num, item):
        if self.inventory[slot_num - 1] is None:
            self.inventory[slot_num - 1] = item

    def swap_inventory_slot(self, slot_num1, slot_num2,):
        temp_item = self.inventory[slot_num1]
        self.inventory[slot_num1] = slot_num2
        self.inventory[slot_num2] = temp_item

    def add_item(self, item):
        slot_assigned = False
        for slot in self.inventory:
            if self.inventory[slot] is None:
                self.inventory[slot] = item
                slot_assigned = True
                break
        if not slot_assigned:
            print("Inventory Full")