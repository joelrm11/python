class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = self.__validate_age(age)
        self.__address = address
    
    def __validate_age(self, age):
        if isinstance(age, int) and age > 0:
            return age
        raise ValueError("Age must be a positive integer")
    
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = self.__validate_age(age)
        
    def set_address(self, address):
        self.__address = address
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_address(self):
        return self.__address

# Create an instance of the Person class
person = Person("Alice", 23, "123 Main St")

# Get and print attributes
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())

# Update attributes using setter methods
person.set_name("Bob")
person.set_age(25)
person.set_address("456 Elm St")

# Get and print updated attributes
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())