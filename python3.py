# Polymorphism demonstration
def display_device_info(device):
    print(device.get_info())

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
phone2 = GamingSmartphone("ASUS", "ROG Phone 7", 256, "Adreno 730")

# Displaying info using polymorphic function
display_device_info(phone1)  # Uses Smartphone's get_info
display_device_info(phone2)  # Uses GamingSmartphone's overridden get_info

# Calling other methods
print(phone1.call("123-456-7890"))
print(phone2.play_game("Asphalt 9"))
print(phone1.upgrade_storage(256))
