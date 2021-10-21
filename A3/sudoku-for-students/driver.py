
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, mac
from backtrack import backtracking_search

def main():

    for puzzle in [easy1, harder1]:
        s = Sudoku(puzzle)  # construct a Sudoku problem

        print("Beginning of Puzzle\n:")
        s.display(s.infer_assignment())
        # solve as much as possible by AC3 then backtrack search if needed
        # using MRV and MAC.
    
        AC3(s) # First we try to solve using AC3
        print("Trying to solve using AC3\n")

        if not s.goal_test(s.curr_domains): #If AC3 did not solve, we use backtrack
            print("\nAC3 didn't work\n")
            print("\nTime for Backtrack\n")

            backtrack = backtracking_search(s, select_unassigned_variable=mrv, inference=mac)
            
            if backtrack: # If backtrack solved, return and show solution
                print("\nBacktracking worked! Solution:")
                s.display(s.infer_assignment())
                print("\n")
            else: # Otherwise state that backtrack failed
                print("\nBacktracking failed")
        elif s.goal_test(s.curr_domains): # Otherwise if AC3 did solve, return and show solution
            print("\nAC3 Worked! Solution: ") 
            s.display(s.infer_assignment())
            print("\n")

if __name__ == "__main__":
    main()