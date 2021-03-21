# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    from game import Directions
    startNode = problem.getStartState()
    openNode = []
    openNodePath = []
    closedNode = []

    directionsPath = []

    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST


    openNode.append(problem.getStartState())
    openNodePath.append(directionsPath)

    #print "succ",problem.getSuccessors((1,1))

    while len(openNode) > 0:
        currentNode = openNode.pop(-1)
        directionsPath = openNodePath.pop(-1)
        #print "Current Node: ",currentNode
        closedNode.append(currentNode)

        if problem.isGoalState(currentNode):
            #print "Found: ",directionsPath
            return directionsPath
        
        succNode = problem.getSuccessors(currentNode)


        if  succNode:
            for cnode in succNode:
                #print "cnode",cnode
                if cnode[0] not in closedNode:
                    newPath = directionsPath + [cnode[1]]
                    openNode.append(cnode[0])
                    openNodePath.append(newPath)


    
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    
    startNode = problem.getStartState()
    openNode = []
    openNodePath = []
    closedNode = []

    directionsPath = []

    openNode.append(problem.getStartState())
    openNodePath.append(directionsPath)

    while(True):

        currNode = openNode.pop(0)
        directionsPath = openNodePath.pop(0)
        closedNode.append(currNode)

        if problem.isGoalState(currNode):
            return directionsPath

        succNode = problem.getSuccessors(currNode)

        if succNode:
            for cnode in succNode:
                if cnode[0] not in closedNode and cnode[0] not in openNode:
                    newPath = directionsPath + [cnode[1]]
                    openNode.append(cnode[0])
                    openNodePath.append(newPath)



    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue

    startNode = problem.getStartState()
    openNode = PriorityQueue()
    openNodePath = []
    closedNode = []

    directionsPath = []

    openNode.push((problem.getStartState(),[]),0)

    while len(openNode.heap) > 0:
        currentNode, directionsPath = openNode.pop()
        #directionsPath = openNodePath.pop(0)
        #print "Current Node: ",currentNode
        closedNode.append(currentNode)

        if problem.isGoalState(currentNode):
            #print "Found: ",directionsPath
            return directionsPath
        
        succNode = problem.getSuccessors(currentNode)

        if  succNode:
            for cnode in succNode:
                if cnode[0] not in closedNode:
                    if cnode[0] not in (curNode[2][0] for curNode in openNode.heap):
                        newPath = directionsPath + [cnode[1]]
                        cost = problem.getCostOfActions(newPath)
                        openNode.push((cnode[0],newPath),cost)
                    
                    elif cnode[0] in (curNode[2][0] for curNode in openNode.heap):
                        for curNode in openNode.heap:
                            if curNode[2][0] == cnode[0]:
                                oldCost = problem.getCostOfActions(curNode[2][1])

                        newCost = problem.getCostOfActions(directionsPath + [cnode[1]])

                        if oldCost > newCost:
                            newPath = directionsPath + [cnode[1]]
                            openNode.update((cnode[0],newPath),newCost)






    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    def newCostFunc(cnode):
        return problem.getCostOfActions(cnode[1]) + heuristic(cnode[0],problem)

    openNode = util.PriorityQueueWithFunction(newCostFunc)

    openNodePath = []
    closedNode = []

    directionsPath = []

    openNode.push((problem.getStartState(),[]))

    while len(openNode.heap) > 0:
        currentNode, directionsPath = openNode.pop()
        #directionsPath = openNodePath.pop(0)
        #print "Current Node: ",currentNode
        if currentNode in closedNode:
            continue
        closedNode.append(currentNode)

        if problem.isGoalState(currentNode):
            #print "Found: ",directionsPath
            return directionsPath
        
        succNode = problem.getSuccessors(currentNode)

        if  succNode:
            for cnode in succNode:
                if cnode[0] not in closedNode:
                    newPath = directionsPath + [cnode[1]]
                    openNode.push((cnode[0],newPath))




    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
