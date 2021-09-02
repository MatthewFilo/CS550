
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan that avoids ghost by gathering their direction and turning away from them
    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """
        #If the ghost is not scared and is in the same row, less then 3 units away, we follow this if statement and return the direction of the ghost
        if(ghost.isScared() == False and (pacman.getPosition()[0] == ghost.getPosition()[0]) and (abs(pacman.getPosition()[1] - ghost.getPosition()[1]) <= dist) ):
            # We use some mathematics to calculate which direction the ghost is coming from in the column pacman is in, if it's a negative value
            # The ghost is coming from the north, if it is a positive value, the ghost is coming from the south
            # The mathematics used is using pacman's y position on the map subtracted by the ghost's y position on the map
            if( (pacman.getPosition()[1] - ghost.getPosition()[1]) < 0 ):
                return Directions.NORTH
            if( (pacman.getPosition()[1] - ghost.getPosition()[1]) > 0 ):
                return Directions.SOUTH
        
        #If the ghost is not scared, less then 3 units away, and in the same column, We follow this if statement
        if(ghost.isScared() == False and (pacman.getPosition()[1] == ghost.getPosition()[1]) and (abs(pacman.getPosition()[0] - ghost.getPosition()[0]) <= dist) ):
            # The same approach is used as the previous if statement, using mathematics and positive/negative values, we calculate the direction of the ghost
            if( (pacman.getPosition()[0] - ghost.getPosition()[0]) < 0 ):
                return Directions.EAST
            if( (pacman.getPosition()[0] - ghost.getPosition()[0]) > 0 ):
                return Directions.WEST

        # Otherwise, if the criteria for pacman being in danger is not met, we return Directions.STOP
        else:
            return Directions.STOP
       
    
    def getAction(self, state):
        """
        state - GameState

        We make a decision based on pacman's current game state and whether or not he is "In Danger"

        This function calls the inDanger() function stored in our class, TimidAgent, that returns the direction of a ghost attacking pacman
        given that it meets a certain criteria that would consider pacman to be "In Danger"

        We gather each of the ghosts individual state and feed it into the inDanger() function, allowing for pacman
        to see if he is in danger from any of the ghost, rather then just an individual ghost

        Once inDanger() is called, while pacman is in danger, we return valid action directions such as:
        - Reversing the current direction of pacman
        - Turning PacMan to the left
        - Turning to the right
        - And in worse case scenario, we continue in the direction of danger

        However, while Pacman is not in danger, then we emulate the LeftTurnAgent in the pacmanAgents.py file
        This allows for proper movement across the board while pacman is not in danger, so that way he is not
        constantly moving in a way that is meant to avoid the ghosts
        """
        # # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        # # Get the agent's state from the game state
        agentState = state.getPacmanState()
        ghostState = state.getGhostStates()

        # Find agent heading
        heading = agentState.getDirection()

        if heading == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH

        # We cycle through ghoststate in order to input the ghosts one at a time for inDanger()
        for ghostState in state.getGhostStates():
            dangerDirection = self.inDanger(agentState, ghostState)
            
        # This means that we are not in danger, so therefore we emulate LeftTurnAgent
        if(dangerDirection == Directions.STOP):
            left = Directions.LEFT[heading] # We use [heading] after direction to turn the direction we want regardless of current direction
            if left in legal:
                action = left
            else: # If we cannot turn left, we pursue other options
                if heading in legal: # If north is possible, we continue north
                    action = heading
                elif Directions.RIGHT[heading] in legal: # If the previous option is not available, we turn right (if legal)
                    action = Directions.RIGHT[heading]
                elif Directions.Reverse[heading] in legal: # If the previous option is not available, we reverse our direction (if legal)
                    action = Directions.REVERSE[heading]
                else:
                    action = Directions.STOP # Otherwise, we cannot move, so we stop
        # This if statement signals that pacman is inDanger(), so we continue with the instructions given
        # Note: This if statement does emulate LeftTurnAgent, but with the expected responses
        elif(dangerDirection != Directions.STOP):
            reverse = Directions.REVERSE[heading] # We assign reverse to a variable
            if reverse in legal: # We make sure reverse is legal and if so, then we assign our action to reverse
                action = reverse
            else: # Reverse is not a legal move, so continue onto other options
                if Directions.LEFT[heading] in legal: # We turn left based on the heading
                    action = Directions.LEFT[heading]
                elif Directions.RIGHT[heading] in legal: # We turn right based on the heading
                    action = Directions.RIGHT[heading]
                else:
                    action = dangerDirection # no legal moves, so we continue in the direction of danger

        return action