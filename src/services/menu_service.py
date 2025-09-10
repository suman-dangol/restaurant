from src.models.menu_item import MenuItem
from src.utils.file_manager import FileManager
from src.utils.exceptions import FileError, ValidationError, NotFoundError
from src.utils.validators import validate_price, validate_id

class MenuService:
    def __init__(self, menu_file_path="src/data/menu.txt"):
        self.menu_file_path = menu_file_path
        self.menu_items = self.load_menu()

    def load_menu(self):
        """Loads menu items from the menu file."""
        try:
            lines = FileManager.read_file(self.menu_file_path)
            menu_items = []
          
            for line in lines:
                item_data = line.strip().split("|")
                if len(item_data) == 4:
                    item_id, name, category, price = item_data
                    try:
                        item_id = int(item_id)  # Convert item_id to integer
                        item_id = validate_id(item_id)
                        price = validate_price(price)
                        menu_item = MenuItem(item_id, name, category, price)
                        menu_items.append(menu_item)
                    except ValidationError as e:
                        print(f"Validation error loading menu item: {e}")
                        continue # Skip invalid menu items
                    except ValueError:
                        print(f"Invalid item_id format. Skipping item. Line: {line}") # Print the line
                        continue
                else:
                    print(f"Skipping line due to incorrect format (expected 4 parts). Line: {line}") # Print the line
                    continue
            return menu_items
        except FileError as e:
            print(f"Error loading menu: {e}")
            return []

    def get_menu_items_by_category(self, category):
        """Returns a list of menu items for a given category."""
        return [item for item in self.menu_items if item.category.lower() == category.lower()]

    def get_menu_item_by_id(self, item_id):
        """Returns a menu item with the given ID, or None if not found."""
        for item in self.menu_items:
            if item.item_id == item_id:
                return item
        return None

    def add_menu_item(self, name, category, price):
        """Adds a new menu item to the menu."""
        try:
            # Generate a new item ID (you might want to use a better strategy)
            new_id = max([item.item_id for item in self.menu_items], default=0) + 1
            price = validate_price(price)
            new_item = MenuItem(new_id, name, category, price)
            
            # Append to file
            FileManager.append_file(self.menu_file_path, f"{new_item.item_id}|{new_item.name}|{new_item.category}|{new_item.price}")
            
            # Update in-memory menu
            self.menu_items.append(new_item)
            return True
        except FileError as e:
            print(f"Error adding menu item: {e}")
            return False
        except ValidationError as e:
            print(f"Validation error: {e}")
            return False

    def update_menu_item(self, item_id, name=None, category=None, price=None):
        """Updates an existing menu item."""
        try:
            item_id = validate_id(item_id)
            item = self.get_menu_item_by_id(item_id)
            if not item:
                raise NotFoundError(f"Menu item with ID {item_id} not found.")

            if name:
                item.name = name
            if category:
                item.category = category
            if price:
                item.price = validate_price(price)

            self._save_menu_to_file() # Save changes to file
            return True
        except FileError as e:
            print(f"Error updating menu item: {e}")
            return False
        except ValidationError as e:
            print(f"Validation error: {e}")
            return False
        except NotFoundError as e:
            print(f"{e}")
            return False

    def delete_menu_item(self, item_id):
        """Deletes a menu item from the menu."""
        try:
            item_id = validate_id(item_id)
            item = self.get_menu_item_by_id(item_id)
            if not item:
                raise NotFoundError(f"Menu item with ID {item_id} not found.")

            self.menu_items = [i for i in self.menu_items if i.item_id != item_id]
            self._save_menu_to_file()
            return True
        except FileError as e:
            print(f"Error deleting menu item: {e}")
            return False
        except ValidationError as e:
            print(f"Validation error: {e}")
            return False
        except NotFoundError as e:
            print(f"{e}")
            return False

    def _save_menu_to_file(self):
         """Saves the current menu items to the file."""
         try:
             lines = [f"{item.item_id}|{item.name}|{item.category}|{item.price}" for item in self.menu_items]
             FileManager.write_file(self.menu_file_path, lines)
         except FileError as e:             print(f"Error saving menu to file: {e}")