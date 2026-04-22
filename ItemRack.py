import pandas as pd
import numpy as np
import sqlite3 as sql
from InventoryItem import InventoryItem
import pickle
import os

class ItemRack:
    def __init__(self, rack_file_name=None):
        if type(rack_file_name) == str and os.path.exists(rack_file_name):
            connect = sql.connect(rack_file_name)
            self.items = pd.read_sql_query("SELECT * FROM ItemRack", connect)
            connect.close()
            for i in range(3):
                for j in range(3):
                    self.items.iloc[i, j] = pickle.loads(self.items.iloc[i, j])
        elif type(rack_file_name) == str:
            self.items = pd.DataFrame(np.full((3, 3), InventoryItem("None")))
        else:
            raise FileNotFoundError("Item Rack file not given properly")

        self.rack_file_name = rack_file_name

    def save(self):
        for i in range(3):
            for j in range(3):
                self.items.iloc[i, j] = pickle.dumps(self.items.iloc[i, j])
        connect = sql.connect(self.rack_file_name)
        self.items.to_sql("ItemRack", connect, if_exists='replace', index=False)

    def print_contents(self):
        for i in range(3):
            for j in range(3):
                print(self.items.iloc[i, j].name, end=" ")
            print()

    def set_item(self, row, column, item):
        self.items.iloc[row, column] = item

    def remove_item(self, row, column):
        self.items.iloc[row, column] = InventoryItem("None")

    def clear_item_rack(self):
        self.items = pd.DataFrame(np.full((3, 3), InventoryItem("None")))

if __name__ == '__main__':
    item_rack = ItemRack("Profile1ItemRack.db")
    item_rack.set_item(0, 1, InventoryItem("Ball"))
    #item_rack.clear_item_rack()
    item_rack.print_contents()
    #item_rack.save()