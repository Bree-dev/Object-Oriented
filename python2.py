# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute

    def get_info(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def get_storage(self):
        return self.__storage

    def upgrade_storage(self, new_storage):
        if new_storage > self.__storage:
            self.__storage = new_storage
            return f"Storage upgraded to {self.__storage}GB"
        else:
            return "Upgrade failed: New storage must be greater than current."

# Subclass: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu_model):
        super().__init__(brand, model, storage)
        self.gpu_model = gpu_model

    # Overriding method (polymorphism)
    def get_info(self):
        return f"{self.brand} {self.model} (Gaming Edition) with {self.get_storage()}GB and GPU: {self.gpu_model}"

    def play_game(self, game_name):
        return f"Launching {game_name} on {self.model} with {self.gpu_model} GPU!"
