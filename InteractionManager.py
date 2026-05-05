import pandas.errors

from Defaults import new_game_interactable_item_list
import sqlite3 as sql
import pandas as pd
import pickle

class InteractionManager:
    def __init__(self, slot_num=1):
        self.interactable_list = new_game_interactable_item_list
        self.slot_num = slot_num

    def interact(self, name, tool):
        for item in self.interactable_list:
            if item.get_name() == name:
                item.interact(tool)
                return True
        return False

    def print_items(self):
        print("World Items:\n")
        for item in self.interactable_list:
            print(f"\t{item.get_name()}")
        print()

    def get_item(self, name):
        for item in self.interactable_list:
            if item.get_name() == name:
                return item
        return False

    def save(self):
        interacted_list = []
        for item in self.interactable_list:
            interacted_list.append(pickle.dumps(item.get_info()))
        connect = sql.connect("Interactable_list" + str(self.slot_num) + ".db")
        interacted_df = pd.DataFrame(interacted_list)
        interacted_df.to_sql("Interactable", connect, if_exists='replace', index=False)
        connect.close()

    def load(self):
        try:
            connect = sql.connect("Interactable_list" + str(self.slot_num) + ".db")
            interacted_df = pd.read_sql("SELECT * FROM Interactable", connect)
            for item in range(len(self.interactable_list)):
                self.interactable_list[item].set_info(pickle.loads(interacted_df.iloc[item, 0]))
            connect.close()
        except pandas.errors.DatabaseError:
            self.save()
            self.load()

    def set_slot(self, slot_num):
        self.slot_num = slot_num