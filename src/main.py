from src.models.farmer import Farmer 
from src.models.buyer import Buyer 
from src.utils.data_handler import save_user 

def create_user():
    print("AgroUSSD User Registration")
    role = input("Enter role (Farmer/Buyer): ").strip().capitalize()

    name = input("Enter name: ").strip().capitalize()
    phone = input("Enter phone: ").strip()
    location = input("Enter location: ").strip().capitalize()
    pin = input("Set 6 digit PIN: ").strip()

    if role == "Farmer":
        user = Farmer(name, phone, location, pin)
    elif role == "BUyer":
        user = Buyer(name, phone, location, pin)
    else:
        print("Error. Must be Farmer or Buyer")
        return 
    
    save_user(user.to_dict())
    print(f"{role} created successfully")
    print(user)


if __name__ == "__main__":
    create_user()