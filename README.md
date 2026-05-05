Hello! Welcome to the code for Milton's Hotel Inventory Test Edition!
First before you go explore the code there is one thing I highly recommend that you do first, 
and that is setting up your environment for running as in command line. This makes it so the
screen wont pile up on itself as the program executes.

A short hand guide for the game:

#1 - Create a game file
    Pick a slot, agree to write to it and enter a good file name.
#2 - Open your file
    Enter your file name or the slot to which you assigned it and enter "A" to start your game.
#3 - HELP
    Entering the word "HELP" will give you a list of commands to operate within the game.
#4 - The ground
    This is where all of the objects start out. Put a few in your inventory!
#5 - The Item Rack
    This is a place where you can set down unwanted item. (You can do this with the ground too but it would make more
    sense in a real game scenario where stuff would despawn)
#6 - The world
    This is where all of your interactions lie. Enter the names of all the objects and people you find there!
    Try unlocking doors with weird things! Try feeding mini Xander a Lemon! GO NUTS!
7# - Save & Quit
    Make sure to save if you don't want to lose your progress! Enter QUIT at any time to stop the game.

A short hand guide for fellow devs trying to read my messy work (LOL)

Main is a simple script calling the GameManager class. This class is used to manage all other classes and the
game itself. ProfileManager class is managed by the GameManager class and keeps track of the profiles. 
InteractionManager is managed within GameManager as well and is used to keep track of interactable objects 
and their current state. The Profile class holds classes ItemRack and Ground. InventoryItem class is the base 
class for Key class and it is the central classes used in just about every other class. Interactable is the base 
class for Door class and Person class which are managed by InteractionManager. Defaults file holds the values given
to Ground and InteractionManager at the beginning of a new game. TextFormats file is really just the clear_screen 
function separated for broader use just in case. 

NOTE: I froze the requirements in requirements.txt but when I load in this project from version control it
runs without any install despite using sqlite, pandas and numpy. Might be a sustained .venv or something like that.
Just thought I'd mention it.
