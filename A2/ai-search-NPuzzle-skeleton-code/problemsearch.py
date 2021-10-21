'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, Problem, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer

from explored import Explored
    
       
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored, elapsed_s) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    elapsed_s is the elapsed wall clock time performing the search
    """

    # Code was based off Pseudo Code in Textbook

    time = Timer() # We start the timer

    explored = Explored() # Create an empty explored 

    node = Node(problem, problem.initial)

    frontier = PriorityQueue() # We create a PriorityQueue for the states to be stored
    frontier.append(node) # We append the node to the beginning of the queue an start from there
    done = False # Loop Marker

    while not done:
            node = frontier.pop() # We pop off the node from the queue and explore it
            s = node.state # We assign the node's state to variable s
            if problem.goal_test(s):
                  nodePath = node.path() # We assign the path to the nodePath variable
                  moves = node.solution() # we assign return the solution in the moves variable
                  done = True # This will end the loop since we reached the goal state
                  return nodePath, len(explored.hash_map), time.elapsed_s() # Return the Tuple
            else: # otherwise we explore the child node
                  for childNode in node.expand(problem):
                        childTuple = childNode.state.state_tuple()
                        if not explored.exists(childTuple): # If we haven't explored the node, we append it to the queue and explore the set
                              explored.add(childTuple)
                              frontier.append(childNode)

    return None # Otherwise, return None if no solution was found



