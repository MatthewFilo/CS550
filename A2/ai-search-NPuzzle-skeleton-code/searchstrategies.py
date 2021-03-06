"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

This module contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is in the center, e.g.:
        123
        4 5
        678
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math

class BreadthFirst: # According to the class notes, for BreadthFirst, g = depth and h = constant k (k=0)
    "BreadthFirst - breadth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return childnode.depth
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        value = 0
        return value

# To complete:
# Write two more classes, DepthFirst and Manhattan
# that support appropriate g/h with the same signatures for the class functions
class DepthFirst: # According to class notes, for DepthFirst, g = constant k (k=0) and h = -depth

    @classmethod
    def g(cls, parentnode, action, childnode):
        value = 0
        return value
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        return searchnode.depth * -1


class Manhattan:
    
    @classmethod
    def g(cls, parentnode, action, childnode):
        return parentnode.depth + 1
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        distance = 0 # We set a variable "distance" = 0 as we have not explored anything yet

        board = searchnode.state.state_tuple() # We get the state tuple to use for an enumeration loop

        # Manhattan Heuristic of abs(xVal - xGoal) + (yVal - yGoal)
        for wantedValue, actualValue in enumerate(board): # We use enumerate because it'll automatically list what value should be there (0, 1, 2...)
            if(actualValue == None): # We make sure there is none in the board, otherwise we get an error
                continue
            goalpos = abs((actualValue-1)%3 - wantedValue%3) # We find what the value should be in the position
            actualpos = abs((actualValue-1)//3 - wantedValue//3) # we find what the value actually is in the position
            distance += goalpos + actualpos # we add them to get the distance

        
        return distance # Return the dsitance
