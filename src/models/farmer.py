from src.models.user import User 

class Farmer(User):
    """Farmer class inherits from user"""
    def __init__(self, name, phone, location, pin):
        super().__init__(name, phone, location, pin)

    def get_role(self):
        return "Farmer"
    
    @classmethod 
    def from_dict(cls, data):
        farmer = cls(
            name = data["name"],
            phone = data["phone"],
            location = data["locationi"],
            pin = data["pin"]
        )
        farmer.user_id = data["user_id"]
        return Farmer 
    
