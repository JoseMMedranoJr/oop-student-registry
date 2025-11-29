class Student:
    
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self.grade = grade
    
    # Getter for name attribute
    @property
    def get_name(self):
        return self._name
    
    # Setter for name attribute
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and new_name.isalpha():
            self._name = new_name
        else:
            print("Name must be a string.")




    pass