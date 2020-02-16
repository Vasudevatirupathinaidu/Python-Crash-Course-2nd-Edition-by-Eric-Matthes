# Creating and Using a Class
# Creating the Dog Class

class Pet: # Parent of Dog
    def breath(self):
        print('Breathing')

class Dog(Pet): # Child of Pet
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is npw sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Making an Instance from a Class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.breath()