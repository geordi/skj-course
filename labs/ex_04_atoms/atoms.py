import playground

class ExampleWorld(object):

    def __init__(self, size_x, size_y):
        self.width = size_x
        self.height = size_y

    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.
        
        :param size_x: world size x dimension
        :param size_y: world size y dimension
        :return: tuple of atom objects, each containing (x, y, radius) coordinates 
        """
        return ((80, 50, 10), (150, 200, 20))


if __name__ == '__main__':
    size_x, size_y = 400, 300

    world = ExampleWorld(size_x, size_y)
    playground.run((size_x, size_y), world)