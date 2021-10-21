

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a function handle for making inferences after assignment,
    solve the CSP using backtrack search

    Returns two outputs:
       dictionary of assignments or None if there is no solution
       Number of variable assignments made in backtrack search (not counting
       assignments made by inference)
    """
    
    # See Figure 6.5 of your book for details
    def backtrack(assignment): # Returns Solution or Failure (None)
       
       if len(assignment) == len(csp.variables): # If assignment is complete, return assignment
          return assignment
       
       var = select_unassigned_variable(assignment, csp) # Var = selectUnassignedVariable(CSP, assignment)
       for value in order_domain_values(var, assignment, csp): # For each value in Order Domain Values
          if csp.nconflicts(var, value, assignment) == 0: # If value is consistent
             removals = list() # Create Empty List Called "Removals"
             csp.assign(var, value, assignment) # add {var = value} to assignment
             inferences = inference(csp, var, value, assignment, removals) #inferences <- Inference(csp, var, assignment)
             if inferences: # If Inferences != Failure
                removals += csp.suppose(var, value) # Add inferences to CSP (removals)
                recursive_result = backtrack(assignment) # Result <- Backtrack(csp, assignment) (we already have csp within the scope so just assignment)
                if recursive_result:  # If result != failure
                   return recursive_result # Return Result
                csp.restore(removals) # Otherwise remove inferences from CSP (removals)
                csp.unassign(var, assignment) # Remove {var = value} from assignment
       return None # Return Failure
   
    result = backtrack({}) # Return Backtrap(csp, {})
    return (result, csp.nassigns)
