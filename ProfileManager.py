from Profile import Profile
from Exceptions import LengthError

class ProfileManager:
    def __init__(self, profile_list=None, loaded_profile=None):
        if profile_list is None:
            profile_list = [
                Profile("Empty", 1),
                Profile("Empty", 2),
                Profile("Empty", 3)
            ]
        if len(profile_list) != 3:
            raise LengthError("Profile Manager Load Failed: Invalid List Length")
        for profile in profile_list:
            if type(profile) != Profile or not type(profile) is None:
                raise TypeError("Profile Manager Load Failed: Invalid Profile List")

        self.profile_list = profile_list
        self.loaded_profile = loaded_profile

    def load_profile(self, file_identifier):
        for profile in self.profile_list:
            if type(profile) == Profile and profile.name == file_identifier or profile.id_num == file_identifier:
                self.loaded_profile = profile
                break

    def delete_profile(self, file_identifier):
        for i, profile in enumerate(self.profile_list):
            if type(profile) == Profile and profile.name == file_identifier or profile.id_num == file_identifier:
                self.profile_list[i].name = "Empty"

    def save_to_profile(self, name, slot_num, inventory):
        if self.profile_list[slot_num - 1] is None:
            self.profile_list[slot_num] = Profile(name, slot_num, inventory)