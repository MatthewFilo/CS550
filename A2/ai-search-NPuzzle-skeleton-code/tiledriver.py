'''
AffitDavit

I promise that the attached assignment is my own work. I recognize that should this not be the case, 
I will be subject to penalties as outlined in the course syllabus. -Matthew Filo
'''

'''
driver for graph search problem

'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections



def driver() :
    searches = [BreadthFirst, DepthFirst, Manhattan] # insert search methods into an array to easily scroll through them
    layout = TileBoard(8).state_tuple() # We will use 8 to make time of computation less

    #Variables for math functions
    manhattanTime = []
    manhattanNodes = []
    manhattanPath = []

    breadthTime = []
    breadthNodes = []
    breadthPath = []

    depthTime = []
    depthNodes = []
    depthPath = []

    # Loop
    for i in range(1, 32):
        print("Running Trial #" + str(i))
        for search in searches:
            puzzle = NPuzzle(n=8, force_state=layout, g= search.g, h = search.h)
            path, nodesExplored, time = graph_search(puzzle, debug=False, verbose=False)
        
            print("Search: " + search.__name__ +  " Solved in " + str(time) + " Seconds")

            # Depending on which search method we use, we take the required data and append it to it's correct list variable
            if search.__name__ == 'Manhattan':
                manhattanTime.append(time)
                manhattanNodes.append(nodesExplored)
                manhattanPath.append(len(path))
            if search.__name__ == 'BreadthFirst':
                breadthTime.append(time)
                breadthNodes.append(nodesExplored)
                breadthPath.append(len(path))
            if search.__name__ == 'DepthFirst':
                depthTime.append(time)
                depthNodes.append(nodesExplored)
                depthPath.append(len(path))

        print("Trial #" + str(i) + " Completed!")
    
    print("\nStatistics of Searches (Given in Mean / Standard Deviation)\n")
    print("Search Method Name \t\t Time \t\t Path Length \t\t Number of Nodes")
    print("Manhattan Search \t\t " + str(round(mean(manhattanTime),3)) + "/" + str(round(stdev(manhattanTime),3)) + "\t " + str(mean(manhattanPath)) + "/" + str(stdev(manhattanPath)) + "\t\t " + str(mean(manhattanNodes)) + "/" + str(stdev(manhattanNodes)))
    print("Depth First Search \t\t " + str(round(mean(depthTime),3)) + "/" + str(round(stdev(depthTime),3)) + "\t " + str(mean(depthPath)) + "/" + str(stdev(depthPath)) + "\t\t " + str(mean(depthNodes)) + "/" + str(stdev(depthNodes)))
    print("Breadth First Search \t\t " + str(round(mean(breadthTime),3)) + "/" + str(round(stdev(breadthTime),3)) + "\t " + str(mean(breadthPath)) + "/" + str(stdev(breadthPath)) + "\t\t " + str(mean(breadthNodes)) + "/" + str(stdev(breadthNodes)))

if __name__ == '__main__':
    driver()
# To do:  Run driver() if this is the entry module
