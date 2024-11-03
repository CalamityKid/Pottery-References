from .Pottery import Pottery
class FunctionalPottery (Pottery):
    """A superclass that contains different classes of functional pottery,
    its class_category dict contains each of these classes under its individual category id, 
    str_categories is a str version of this dictionary.

    This class' category_id is the number of classes contained (index+1)"""
    category_id = 00
    str_categories = {}
    class_categories = {}

class Plate (FunctionalPottery):
    class_counter = 000
    class_path = "Functional/Plate/"

    def __init__(self, name):
        self.id = Plate.class_counter
        Plate.class_counter += 1
        Pottery.__init__(self, name)
    
    category_id = FunctionalPottery.category_id
    FunctionalPottery.category_id += 1
    FunctionalPottery.str_categories [category_id] = "Plate"

class Bowl (FunctionalPottery):
    class_counter = 000
    class_path = "Functional/Bowl/"

    def __init__(self, name):
        self.id = Bowl.class_counter
        Bowl.class_counter += 1
        Pottery.__init__(self, name)
    
    category_id = FunctionalPottery.category_id
    FunctionalPottery.category_id += 1
    FunctionalPottery.str_categories [category_id] = "Bowl"

class CupNoHandle (FunctionalPottery):
    class_counter = 000
    class_path = "Functional/CupNoHandle/"
    
    def __init__(self, name):
        self.id = CupNoHandle.class_counter
        CupNoHandle.class_counter += 1
        Pottery.__init__(self, name)
    
    category_id = FunctionalPottery.category_id
    FunctionalPottery.category_id += 1
    FunctionalPottery.str_categories [category_id] = "Cup No Handle"

class CupWithHandle (FunctionalPottery):
    class_counter = 000
    class_path = "Functional/CupWithHandle/"
    def __init__(self, name):
        self.id = CupWithHandle.class_counter
        CupWithHandle.class_counter += 1
        Pottery.__init__(self, name)
    
    category_id = FunctionalPottery.category_id
    FunctionalPottery.category_id += 1
    FunctionalPottery.str_categories [category_id] = "Cup with Handle"

class Kettle (FunctionalPottery):
    class_counter = 000
    class_path = "Functional/Kettle/"
    def __init__(self, name):
        self.id = Kettle.class_counter
        Kettle.class_counter += 1
        Pottery.__init__(self, name)
        Pottery.__init__(self, name)
    
    category_id = FunctionalPottery.category_id
    FunctionalPottery.category_id += 1
    FunctionalPottery.str_categories [category_id] = "Kettle"


FunctionalPottery.class_categories = {0: Plate, 1: Bowl, 2:CupNoHandle, 3:CupWithHandle, 4:Kettle}
