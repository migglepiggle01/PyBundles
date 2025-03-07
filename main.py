#######################
#       IMPORTS       #
#######################

from lib.customstructs import PreciseStruct, UnpreciseUnion
from lib.datatypes import List
from lib.privateclasses import SecureStorage
from lib.privacyutils import GetPass
from lib.geometry import *

def main(): 

    '''

    list_a = List([])
    list_a.append("val", "other val", 1, 2, 3)
    print(list_a)
    list_a.remove("val", 1, 3)
    print(list_a)
    list_a.setlist([1,2,3,4,5])
    list_a.pop(2,3,4)
    print(list_a)
    
    union_b = PreciseStruct()
    union_b.int_val = 100
    print(union_b.int_val)
    union_b.float_val = 3.14
    print(union_b.float_val)
    union_b.string_val = "Hello world"
    print(union_b.string_val)
    print(union_b)
    
    master_password = GetPass.get_hidden_pass(prompt="Set your master password: ")
    secure_storage = SecureStorage(master_password)
    
    password = GetPass.get_hidden_pass(prompt="Set your main password: ")
    api_key = GetPass.get_hidden_pass(prompt="Set your API key: ")

    secure_storage.save({"password": password, "api_key": api_key})
    print("Encrypted Data:", secure_storage.load(encrypted=True))  # Show only encrypted values

    # User must enter the correct password to see decrypted data
    decrypted_data = secure_storage.load()
    if decrypted_data:
        print("Decrypted Data:", decrypted_data)

    '''

    # Create a triangle with specific points
    t = Geometry2D.Triangle((0, 0), (0, 0), (0, 0))  # Points for an equilateral triangle
    print(t)

    # Create a plane and add the triangle to it
    plane = Plane2D(name="My Plane")
    plane.add_shape(t)
    print(plane.output())


if __name__ == "__main__":
    main()