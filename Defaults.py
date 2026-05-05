from Key import Key
from InventoryItem import InventoryItem
from Interactable import Interactable
from Door import Door
from Person import Person

new_game_item_list_ground = [
    InventoryItem("Cheese Burger"),
    Key("Red Key", 1),
    InventoryItem("Spaghetti"),
    Key("Blue Key", 2),
    InventoryItem("Lemon"),
    Key("Green Key", 3),
    InventoryItem("Pavlova"),
    InventoryItem("Popsicle"),
    Key("Purple Key", 4),
    InventoryItem("Chicken Nugget")
]
new_game_interactable_item_list = [
    Person("Devin", "Cheese Burger"),
    Door("Red Door", 1),
    Interactable("Tree", message="You ate the"),
    Person("Jenessa", "Pavlova"),
    Interactable("Dog", message="You were bit by the"),
    Door("Blue Door", 2),
    Interactable("Wall", message="You ran into the"),
    Door("Green Door", 3),
    Person("Olaf", "Chicken Nugget"),
    Door("Purple Door", 4),
    Interactable("Lamp", message="You were lit on fire by the"),
    Person("Xander", "Spaghetti")
]