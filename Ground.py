import pickle
import sqlite3 as sql
import pandas as pd
from InventoryItem import InventoryItem
from Key import Key
from Defaults import new_game_item_list_ground

class Ground:
    def __init__(self, ground_file_name, items=None):
        if items is None:
            items = []
        self.items = items
        self.ground_file_name = ground_file_name

    def remove_item(self, name):
        for item in self.items:
            if item.get_name() == name:
                self.items.remove(item)
                return True
        return False

    def add_item(self, item):
        self.items.append(item)

    def get_item(self, name):
        for item in self.items:
            if item.get_name() == name:
                return item
        return None

    def save(self):
        items_list = self.items[:]
        for item in range(len(self.items)):
            items_list[item] = pickle.dumps(items_list[item])
        connect = sql.connect(self.ground_file_name)
        items_db = pd.DataFrame(items_list, columns=['Item'])
        items_db.to_sql("Ground", connect, if_exists='replace', index=False)
        connect.close()

    def load(self):
        try:
            connect = sql.connect(self.ground_file_name)
            items_list = pd.read_sql_query("SELECT * FROM Ground", connect)
            connect.close()
            self.items = []
            for item in range(len(items_list)):
                items_list.iloc[item, 0] = pickle.loads(items_list.iloc[item, 0])
                self.items.append(items_list.iloc[item, 0])

        except (pd.errors.DatabaseError, IndexError, ValueError) as e:
            self.items = []

    def print_ground(self):
        if self.items:
            print("Ground:\n")
            for item in range(len(self.items)):
                print(f"\t#{item + 1}: ", self.items[item].get_name())
            return True
        else:
            print("No items on ground")
            return False

    def clear_ground(self):
        self.items = new_game_item_list_ground