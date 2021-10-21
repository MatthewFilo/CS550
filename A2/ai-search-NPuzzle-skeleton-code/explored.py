"""
Class for maintaining explored sets
"""

class Explored(object):
    """
    Maintain an explored set.  Assumes that states are hashable
    (e.g. state is represented by a tuple)
    """

    def __init__(self):
        "__init__() - Create an empty explored set"
        
        self.hash_map = dict()

    def exists(self, state):
        """
        exists(state) - Has this state already been explored?

        :param state:  Hashable problem state
        :return: True if already seen, False otherwise4
        """

        # We return the state and if an error occurs, we return False
        try:
            return state in self.hash_map[hash(state)]
        except:
            return False


    def add(self, state):
        """
        add(state) - Add a given state to the explored set

        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """

        if hash(state) not in self.hash_map.keys(): # If the state is not in the set of keys, create a set
            self.hash_map[hash(state)] = set()
        self.hash_map[hash(state)].add(state) # Add the state to the map
        return None



