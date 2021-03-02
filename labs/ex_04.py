class Battlestar:
    """
    Represents a battlestar
    (its name and commander).
    """
    
    def __init__(self, name, commander): # initializer
        self.name = name                 # instance variable
        self.commander = commander

    def identify(self):                  # method
        return 'This is Battlestar {}, commanded by {}.'.format(self.name, self.commander)

galactica = Battlestar('Galactica', 'Bill Adama')
pegasus = Battlestar('Pegasus', 'Helena Cain')

print(galactica.identify())

print(pegasus.identify())



"""
Task:

Create Dog and Cat classes. Both classes will have the same 
constructor that will take one argument and name the animal.

Next, implement the "make_sound" method, which prints a string:
    "Name: MNAU!"
    or
    "Name: HAF!"
    depending on whether you are implementing a cat or a dog.

Finally, create a list in which you put several instances of classes
Dog and Cat. Using the for loop call the make_sound method.
In this way we find out that in dynamically typed languages ​​it is not necessary to 
implement a common ancestor or a common interface to obtain a polymorphism.
"""

class Cat:
    pass


#animals = [ Pes("Lassie"), Kocka("Mikes"), Pes("Zeryk") ]

#for animal in animals:
#     animal.make_sound()
