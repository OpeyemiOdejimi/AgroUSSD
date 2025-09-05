from src.models.user import User 

class Buyer(User):
    """Buyer class inherits from User"""
    def __init__(self, name, phone, location, pin):
        super().__init__(name, phone, location, pin)

    def get_role(self): 
        return "Buyer"
    
    @classmethod 
    def from_dict(cls, data):
        buyer = cls(
            name = data["name"],
            phone = data["phone"],
            location = data["locationi"],
            pin = data["pin"]
        )
        buyer.user_id = data["user_id"]
        return buyer