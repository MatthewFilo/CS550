
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
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

        if(ghost.isScared() == False and (pacman.getPosition()[0] == ghost.getPosition()[0]) and (abs(pacman.getPosition()[1] - ghost.getPosition()[1]) <= dist) ):
            if( (pacman.getPosition()[1] - ghost.getPosition()[1]) < 0 ):
                return Directions.NORTH
            if( (pacman.getPosition()[1] - ghost.getPosition()[1]) > 0 ):
                return Directions.SOUTH
        
        if(ghost.isScared() == False and (pacman.getPosition()[1] == ghost.getPosition()[1]) and (abs(pacman.getPosition()[0] - ghost.getPosition()[0]) <= dist) ):
            if( (pacman.getPosition()[0] - ghost.getPosition()[0]) < 0 ):
                return Directions.EAST
            if( (pacman.getPosition()[0] - ghost.getPosition()[0]) > 0 ):
                return Directions.WEST

        else:
            return Directions.STOP
       
        # raise NotImplemented
    
    def getAction(self, state):
        """
        state - GameState

        When the pacman is not in danger, it should function similarly to the LeftTurnAgent. That is, it
        turns left whenever possible. If not possible it runs until it can’t go any further in the current
        direction, then tries a right turn or U-turn. If no action is possible, sets the action to
        Directions.Stop.

        Based on the direction from which the pacman is in danger, we
        select a new direction. We check for legal directions in the following order: reversing the
        current direction, turning to the left, then turning to the right. If none of these are legal, we
        continue in the direction of the danger, or stop if no move is legal (only possible in contrived
        boards)
        
        Fill in appropriate documentation
        """
        # # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        # # Get the agent's state from the game state and find agent heading
        agentState = state.getPacmanState()
        ghostState = state.getGhostStates()

        heading = agentState.getDirection()

        if heading == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH

        # We cycle through ghoststate in order to input the ghosts one at a time for inDanger()
        for ghostState in state.getGhostStates():
            dangerDirection = self.inDanger(agentState, ghostState)
            
        # This means that we are not in danger, so therefore we emulate LeftTurnAgent
        if(dangerDirection == Directions.STOP):
            left = Directions.LEFT[heading]
            if left in legal:
                action = left
            else:
                if heading in legal:
                    action = heading
                elif Directions.RIGHT[heading] in legal:
                    action = Directions.RIGHT[heading]
                elif Directions.Reverse[heading] in legal:
                    action = Directions.REVERSE[heading]
                else:
                    action = Directions.STOP

        elif(dangerDirection != Directions.STOP):
            reverse = Directions.REVERSE[heading]
            if reverse in legal:
                action = reverse
            else:
                if Directions.LEFT[heading] in legal:
                    action = Directions.LEFT[heading]
                elif Directions.RIGHT[heading] in legal:
                    action = Directions.RIGHT[heading]
                else:
                    action = Directions.STOP

        return action