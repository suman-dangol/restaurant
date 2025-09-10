class MenuItem:
    def __init__(self, item_id, name,description,price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        
    def __repr__(self):
        return f"MenuItem(item_id={self.item_id}, name={self.name}, description={self.description}, price={self.price})"
    
    def __str__(self):
        return f"{self.item_id}|{self.name}|{self.description}|{self.price}"