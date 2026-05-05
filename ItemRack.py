import pandas as pd
import numpy as np
import sqlite3 as sql
from InventoryItem import InventoryItem, blank_item
import pickle

class ItemRack:
    def __init__(self, rack_file_name):
        self.items = pd.DataFrame(np.full((3, 3), blank_item))
        self.rack_file_name = rack_file_name

    def save(self):
        for i in range(3):
            for j in range(3):
                self.items.iloc[i, j] = pickle.dumps(self.items.iloc[i, j])
        connect = sql.connect(self.rack_file_name)
        self.items.to_sql("ItemRack", connect, if_exists='replace', index=False)
        connect.close()

    def load(self):
        connect = sql.connect(self.rack_file_name)
        self.items = pd.read_sql_query("SELECT * FROM ItemRack", connect)
        connect.close()
        for i in range(3):
            for j in range(3):
                self.items.iloc[i, j] = pickle.loads(self.items.iloc[i, j])

    def print_contents(self):
        for i in range(3):
            for j in range(3):
                print(f"{self.items.iloc[i, j].get_name():^10}", end="")
            print()

    def get_item(self, row, column):
        return self.items.iloc[row, column]

    def get_item_by_name(self, name):
        for i in range(3):
            for j in range(3):
                if self.items.iloc[i, j].get_name() == name:
                    return self.items.iloc[i, j]
        return None

    def set_item(self, row, column, item):
        self.items.iloc[row, column] = item

    def remove_item(self, row, column):
        self.items.iloc[row, column] = blank_item

    def remove_item_by_name(self, name):
        for i in range(3):
            for j in range(3):
                if self.items.iloc[i, j].get_name() == name:
                    self.items.iloc[i, j] = blank_item

    def clear_item_rack(self):
        self.items = pd.DataFrame(np.full((3, 3), blank_item))

    def check_empty(self):
        for i in range(3):
            for j in range(3):
                if self.items.iloc[i, j].get_name() != "Empty":
                    return False
        return True

    def check_full(self):
        for i in range(3):
            for j in range(3):
                if self.items.iloc[i, j].get_name() == "Empty":
                    return False
        return True

if __name__ == '__main__':
    item_rack = ItemRack("Profile1ItemRack.db")
    item_rack.set_item(0, 1, InventoryItem("Ball"))
    #item_rack.clear_item_rack()
    item_rack.print_contents()
    #item_rack.save()