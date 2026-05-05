from Profile import Profile
import pandas as pd
import sqlite3 as sql

class ProfileManager:
    def __init__(self, profile_list=None, loaded_profile=None):
        if profile_list is None:
            profile_list = [Profile(1), Profile(2), Profile(3)]
        self.profile_list = profile_list
        self.loaded_profile = loaded_profile

    def load_profile(self, file_identifier):
        for profile in self.profile_list:
            if str(profile.get_id()) == file_identifier or profile.get_name() == file_identifier:
                self.loaded_profile = profile
                return True
        return False

    def delete_profile(self, name):
        for i, profile in enumerate(self.profile_list):
            if profile.get_name() == name:
                self.profile_list[i].clear()
                return True
        return False

    def create_profile(self, name, slot_num):
        for profile in self.profile_list:
            if profile.get_name() == name:
                input("File name already exists. (Enter): ")
                return
        if self.profile_list[slot_num - 1].get_name() == "Empty":
            self.profile_list[slot_num - 1] = Profile(slot_num, name)
            self.profile_list[slot_num - 1].ground.clear_ground()
        else:
            overwrite_command = None
            while overwrite_command != "Y" and overwrite_command != "N":
                overwrite_command = input(f"Overwrite file {self.profile_list[slot_num - 1].get_name()}? "
                                          f"This cannot be undone. (Y/N): ").upper().strip()
            if overwrite_command == "Y":
                self.profile_list[slot_num - 1] = Profile(slot_num, name)

    def print_profiles(self):
        print("Profiles:\n")
        for i, profile in enumerate(self.profile_list):
            print(f"\tProfile #{i + 1}: {profile.get_name()}")

    def save(self):
        for profile in self.profile_list:
            profile.save()
        profile_name_list = [profile.get_name() for profile in self.profile_list]
        profile_name_list = pd.DataFrame(profile_name_list, columns=["Profile"])
        connect = sql.connect("ProfileManager.db")
        profile_name_list.to_sql("ProfileName", connect, if_exists='replace', index=False)
        connect.close()

    def load(self):
        try:
            for profile in self.profile_list:
                profile.load()
            connect = sql.connect("ProfileManager.db")
            name_list = pd.read_sql_query("SELECT * FROM ProfileName", connect)
            connect.close()
            for i in range(len(name_list)):
                self.profile_list[i].set_name(name_list.iloc[i, 0])
        except pd.errors.DatabaseError:
            self.save()
            self.load()
