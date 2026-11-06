# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        create a person, given a name and date of birth
        """
        if not isinstance(name,str):
            raise TypeError("name must be str")
        if name == "":
            raise ValueError("name can't be empty")
        if not isinstance:
            raise TypeError

        self.name = name
        self.birth = birth

    def initial(self):
        """
        return the uppercased each part of this person's name
        join together into a single string.

        """


        result = ""
        for part in self.name.split():
            result = result + part[0].upper()
        return result

    def is_birthday(self):
        """
        if today is this person's birthday return true, otherwise return false
        
        """



        today = date.today()
        return today.mouth == self.birth.month and today.day ==self.birth.day

















    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
