from InteractionManager import InteractionManager
from ProfileManager import ProfileManager
from TextFormats import clear_screen
from InteractionManager import InteractionManager

class GameManager:
    def __init__(self):
        self.profile_manager = ProfileManager()
        self.interaction_manager = InteractionManager()

    def get_loaded(self):
        return self.profile_manager.loaded_profile

    def save(self):
        self.profile_manager.save()
        self.interaction_manager.save()

    def inspect_loaded_file(self):
        profile = self.get_loaded()
        clear_screen()
        if profile.get_name() != "Empty":
            print(f"{profile.get_name()}:\n")
            file_action = input("Key:\n\n"
                                "\tA - Open File\n"
                                "\tB - Delete File\n"
                                "\nEnter: ").upper().strip()
            if file_action == "A":
                return True
            elif file_action == "B":
                clear_screen()
                failsafe = input(f"Are you sure you want to delete "
                                 f"\"{profile.get_name()}\"?"
                                 f"\nThis action cannot be undone. (Y/N):").upper().strip()
                if failsafe == "Y":
                    self.profile_manager.delete_profile(profile.get_name())
                    self.save()
                    return False
                else:
                    return False
            else:
                input("Invalid action. (Enter): ")
                return False
        else:
            new_game = input("Begin new game? (Y/N): ").strip().upper()
            if new_game == "Y":
                while True:
                    try:
                        clear_screen()
                        file_name = input("Enter new file name: ")
                        if file_name == "Empty" or file_name.upper() == "QUIT" or file_name.strip() == '':
                            raise ValueError("Invalid file name")
                        self.profile_manager.create_profile(file_name, self.profile_manager.loaded_profile.get_id())
                        self.get_loaded().ground.clear_ground()
                        self.save()
                        return False
                    except ValueError as e:
                        input(f"{e} (Enter): ")
            else:
                return False

    def start_game(self):
        self.profile_manager.load()
        input("Welcome to Milton's Hotel Inventory Test Edition! (Enter): ")
        file_loaded = False
        while not file_loaded:
            try:
                clear_screen()
                self.profile_manager.print_profiles()
                file_identifier = input("\nEnter slot number or file name to inspect or \"QUIT\" to quit: ")
                if file_identifier == "QUIT":
                    exit()
                if file_identifier != "Empty":
                    if not self.profile_manager.load_profile(file_identifier):
                        raise ValueError("Invalid slot number or file name")
                else:
                    raise ValueError("Invalid slot number or file name")
                if self.inspect_loaded_file():
                    self.get_loaded().load()
                    self.interaction_manager.set_slot(self.get_loaded().slot_num)
                    self.interaction_manager.load()
                    file_loaded = True
            except ValueError as e:
                input(f"\n{e} (Enter): ")

    def ground_add(self):
        profile = self.get_loaded()
        if profile.check_empty_inventory():
            input("No objects in inventory. (Enter): ")
        else:
            adding_item = True
            while adding_item:
                clear_screen()
                profile.print_inventory()
                add_item = input("\nEnter slot number to add to ground."
                                 "\nEnter RETURN to return to ground menu."
                                 "\n\nEnter: ")
                if add_item == "RETURN":
                    adding_item = False
                else:
                    try:
                        add_item = int(add_item)
                        if not 1 <= add_item <= 4:
                            raise IndexError("Invalid slot number.")
                        if profile.inventory[add_item - 1].get_name() == "Empty":
                            raise IndexError("Slot cannot be empty.")
                        profile.ground_inventory_swap(add_item)
                        adding_item = False
                        input(f"{profile.ground.items[-1].get_name()} added to ground. (Enter): ")
                    except ValueError:
                        input("Invalid slot number. (Enter): ")
                    except IndexError as e:
                        input(f"{e} (Enter): ")

    def ground_take(self):
        profile = self.get_loaded()
        if profile.check_full_inventory():
            input("Inventory is full. (Enter): ")
        else:
            taking_item = True
            while taking_item:
                try:
                    clear_screen()
                    profile.print_ground()
                    take_item = input("\nEnter item name to take from ground."
                                      "\nEnter RETURN to return to ground menu."
                                      "\n\nEnter: ")
                    if take_item.strip().upper() == "RETURN":
                        taking_item = False
                    elif profile.ground.get_item(take_item) is None:
                        raise ValueError("Invalid item name.")
                    else:
                        slot_num = profile.find_free_inventory_slot() + 1
                        profile.ground_inventory_swap(slot_num, take_item)
                        taking_item = False
                        input(f"{take_item} added to inventory. (Enter): ")
                except ValueError as e:
                    input(f"{e} (Enter): ")

    def inspect_ground(self):
        inspecting_ground = True
        while inspecting_ground:
            if self.get_loaded().print_ground():
                command = input("\nTAKE - add item to inventory from ground"
                                "\nADD - add item to ground from inventory"
                                "\nRETURN - return to main menu"
                                "\n\nEnter: ").strip().upper()
                if command == "TAKE":
                    self.ground_take()
                elif command == "ADD":
                    self.ground_add()
                elif command == "RETURN":
                    inspecting_ground = False
            else:
                command = input("\nADD - add item to ground from inventory"
                                "\nRETURN - return to main menu"
                                "\n\nEnter: ").strip().upper()
                if command == "ADD":
                    self.ground_add()
                elif command == "RETURN":
                    inspecting_ground = False
            clear_screen()

    def item_rack_add(self):
        profile = self.get_loaded()
        if profile.check_empty_inventory():
            input("No objects in inventory. (Enter): ")
        elif profile.check_full_item_rack():
            input("Item rack is full. (Enter): ")
        else:
            adding_item = True
            while adding_item:
                clear_screen()
                profile.print_inventory()
                add_item = input("\nEnter slot number to add to item rack."
                                 "\nEnter RETURN to return to item rack menu."
                                 "\n\nEnter: ")
                if add_item == "RETURN":
                    adding_item = False
                else:
                    try:
                        add_item = int(add_item)
                        if not 1 <= add_item <= 4:
                            raise IndexError("Invalid slot number.")
                        if profile.inventory[add_item - 1].get_name() == "Empty":
                            raise IndexError("Slot cannot be empty.")
                        add_item_name = profile.inventory[add_item - 1].get_name()
                        profile.item_rack_inventory_swap(add_item)
                        adding_item = False
                        input(f"{add_item_name} added to ground. (Enter): ")
                        adding_item = False
                    except ValueError:
                        input("Invalid slot number. (Enter): ")
                    except IndexError as e:
                        input(f"{e} (Enter): ")

    def item_rack_take(self):
        profile = self.get_loaded()
        if profile.check_full_inventory():
            input("Inventory is full. (Enter): ")
        else:
            taking_item = True
            while taking_item:
                try:
                    clear_screen()
                    profile.print_item_rack()
                    take_item = input("\nEnter item name to take from item rack."
                                      "\nEnter RETURN to return to item rack menu."
                                      "\n\nEnter: ")
                    if take_item.strip().upper() == "RETURN":
                        taking_item = False
                    elif take_item == "Empty":
                        raise ValueError("Slot cannot be empty.")
                    elif profile.item_rack.get_item_by_name(take_item) is None:
                        raise ValueError("Invalid item name.")
                    else:
                        input(2)
                        slot_num = profile.find_free_inventory_slot() + 1
                        input(3)
                        profile.item_rack_inventory_swap(slot_num, take_item)
                        taking_item = False
                        input(4)
                        input(f"{take_item} added to inventory. (Enter): ")
                except ValueError as e:
                    input(f"{e} (Enter): ")

    def inspect_item_rack(self):
        inspecting_item_rack = True
        while inspecting_item_rack:
            self.get_loaded().print_item_rack()
            if not self.get_loaded().check_empty_item_rack():
                command = input("\nTAKE - add item to inventory from item rack"
                                "\nADD - add item to ground from inventory"
                                "\nRETURN - return to main menu"
                                "\n\nEnter: ").strip().upper()
                if command == "TAKE":
                    self.item_rack_take()
                elif command == "ADD":
                    self.item_rack_add()
                elif command == "RETURN":
                    inspecting_item_rack = False
            else:
                command = input("\nADD - add item to ground from inventory"
                                "\nRETURN - return to main menu"
                                "\n\nEnter: ").strip().upper()
                if command == "ADD":
                    self.item_rack_add()
                elif command == "RETURN":
                    inspecting_item_rack = False
            clear_screen()

    def world_interaction(self):
        interacting = True
        while interacting:
            self.interaction_manager.print_items()
            command = input("Enter item name to interact."
                            "\nEnter RETURN to return to main menu."
                            "\n\nEnter: ").strip()
            if command.upper() == "RETURN":
                interacting = False
            else:
                try:
                    item_exists = False
                    for item in self.interaction_manager.interactable_list:
                        if item.get_name() == command:
                            item_exists = True
                    if not item_exists:
                        raise ValueError("Invalid world item name.")
                    if self.interaction_manager.get_item(command).needs_tool:
                        self.get_loaded().print_inventory()
                        tool_name = input("Enter inventory item name to use: ")
                        tool = None
                        for item in self.get_loaded().inventory:
                            if item.get_name() == tool_name:
                                tool = item
                                break
                        if tool is None:
                            raise ValueError("Invalid inventory item name.")
                        if tool.get_name() == "Empty":
                            raise ValueError("Slot cannot be empty.")
                    else:
                        tool = None
                    if not self.interaction_manager.interact(command, tool):
                        input("Invalid item. (Enter): ")
                except ValueError as e:
                    input(f"{e} (Enter): ")
            clear_screen()

    def play(self):
        profile = self.profile_manager.loaded_profile
        clear_screen()
        playing = True
        while playing:
            game_command = input("Enter \"HELP\" to see commands."
                                 "\nEnter: ").strip().upper()
            clear_screen()
            if game_command == "HELP":
                print("HELP - see commands"
                      "\nGROUND - inspect ground"
                      "\nITEM RACK - inspect item rack"
                      "\nINVENTORY - inspect inventory"
                      "\nWORLD - interact with world objects"
                      "\nSAVE - save game"
                      "\nQUIT - quit the game"
                      "\n")
            elif game_command == "GROUND":
                self.inspect_ground()
            elif game_command == "ITEM RACK":
                self.inspect_item_rack()
            elif game_command == "INVENTORY":
                profile.print_inventory()
            elif game_command == "WORLD":
                self.world_interaction()
            elif game_command == "SAVE":
                self.save()
                print("Game saved.")
            elif game_command == "QUIT":
                playing = False
                print("Quitting...")

