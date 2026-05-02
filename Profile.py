from ItemRack import ItemRack
from InventoryItem import InventoryItem, blank_item
from Ground import Ground
import pandas as pd

class Profile:

    def __init__(self, slot_num, display_name="Empty"):
        self.display_name = display_name
        self.inventory = [blank_item, blank_item, blank_item, blank_item]
        self.slot_num = slot_num
        self.item_rack = ItemRack("ItemRack" + str(slot_num) + ".db")
        self.ground = Ground("Ground" + str(slot_num) + ".db")

    def get_name(self):
        return self.display_name

    def set_name(self, name):
        self.display_name = name

    def get_id(self):
        return self.slot_num

    def swap_inventory_slots(self, slot_num1, slot_num2):
        temp_item = self.inventory[slot_num1 - 1]
        self.inventory[slot_num1 - 1] = self.inventory[slot_num2 - 1]
        self.inventory[slot_num2 - 1] = temp_item

    def add_inventory_item(self, item):
        slot_assigned = False
        for slot in range(len(self.inventory)):
            if self.inventory[slot].get_name() == "Empty":
                self.inventory[slot] = item
                slot_assigned = True
                break
        if not slot_assigned:
            print("Inventory Full")

    def item_rack_inventory_swap(self, inventory_slot, rack_row, rack_col):
        temp_item = self.inventory[inventory_slot - 1]
        self.inventory[inventory_slot - 1] = self.item_rack.get_item(rack_row, rack_col)
        self.item_rack.set_item(rack_row, rack_col, temp_item)

    def ground_inventory_swap(self, inventory_slot, item_name):
        temp_item = self.ground.get_item(item_name)
        if self.ground.remove_item(item_name):
            if self.inventory[inventory_slot].get_name() != "Empty":
                self.ground.add_item(self.inventory[inventory_slot - 1])
            self.inventory[inventory_slot - 1] = temp_item

    def print_inventory(self):
        for slot in range(len(self.inventory)):
            print(f"#{slot + 1}: ", end='')
            if type(self.inventory[slot]) == InventoryItem:
                print(self.inventory[slot].get_name())
            else:
                print("Empty")

    def print_item_rack(self):
        self.item_rack.print_contents()

    def print_ground(self):
        self.ground.print_ground()

    def print_info(self):
        self.print_inventory()
        self.print_item_rack()
        self.print_ground()

    def save(self):
        self.item_rack.save()
        self.ground.save()

    def load(self):
        loaded = False
        while not loaded:
            try:
                self.item_rack.load()
                self.ground.load()
                loaded = True
            except pd.errors.DatabaseError:
                self.item_rack.save()

    def clear(self):
        self.ground.clear_ground()
        self.item_rack.clear_item_rack()
        self.inventory = [blank_item, blank_item, blank_item, blank_item]
        self.set_name("Empty")


if __name__ == "__main__":
    pass