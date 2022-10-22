import pandas
from tkinter import *
from tkinter import ttk
import random


class ItemGenerator:
    """Generate items based of type and rarity inputs."""

    def __init__(self):
        self.item_pool = []
        self.selected_item = []
        self.rarities = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        self.types = ['Armor', 'Potion', 'Ring', 'Rod', 'Scroll', 'Staff', 'Wand', 'Weapon', 'Wondrous', 'Any']
        self.text = ""
        self.rarity = ""
        self.type = ""

        # Tkinter GUI Setup
        self.window = Tk()
        self.window.title("Magic Item Generator!")
        self.window.config(height=600, width=800)

        # Label
        self.title = Label()
        self.title.config(text="Magic Item Generator", fg='Black', font=("Birch std", 26, 'bold'))
        self.title.grid(column=0, columnspan=2, row=0, pady=20, padx=50)

        # Canvas
        self.canvas = Canvas(width=100, height=100, highlightthickness=0)
        image = PhotoImage(file='item_image.png')
        self.canvas.create_image(50, 40, image=image)
        self.canvas.grid(column=0, columnspan=2, row=1)

        # Combobox
        self.rare_drop = ttk.Combobox(self.window, values=self.rarities, width=18)
        self.rare_drop.grid(column=0, row=2, pady=10)

        self.type_drop = ttk.Combobox(self.window, values=self.types, width=18)
        self.type_drop.grid(column=1, row=2, pady=10)

        # Button
        self.button = Button()
        self.button.config(text="Generate Items", font=("Birch std", 12, 'italic'), command=self.main_method)
        self.button.grid(column=0, row=3, columnspan=2, pady=10)

        # Mainloop
        self.window.mainloop()

    def main_method(self):
        """Clears previous lists - Calls the methods to select items."""
        self.item_pool.clear()
        self.selected_item.clear()
        self.text = ""
        self.rarity = self.rare_drop.get()
        self.type = self.type_drop.get()
        self.create_item_list()
        self.select_item_from_list()
        self.open_popup()

    def open_popup(self):
        top = Toplevel(self.window)
        top.geometry("750x300")
        top.title("Gem List")
        Label(top, text=f"{self.text}", font=('Papyrus 18 normal')).place(x=100, y=20)

    def create_item_list(self):
        """This method uses the rarity and type inputs create a list of magic items"""
        data = pandas.read_csv("Official Magic Items.csv")
        magic_item_dictionary = data.to_dict('records')
        if self.type == 'Any':
            for magic_item in magic_item_dictionary:
                if magic_item['Rarity']:
                    self.item_pool.append(magic_item)
        else:
            for magic_item in magic_item_dictionary:
                if magic_item['Rarity'] == self.rarity and magic_item['Type'] == self.type:
                    self.item_pool.append(magic_item)

    def select_item_from_list(self):
        """Uses the generated list of magical items to select three at random."""
        for item in range(3):
            item = random.choice(self.item_pool)
            self.text += f"Item: {item['Name']} - {item['Type']} - {item['Rarity']}\n" \
                         f"Source: {item['Source']} Notes: {item['Notes']}\n\n"
            self.selected_item.append(item)


ItemGenerator()
