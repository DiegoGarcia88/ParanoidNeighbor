from api.Game import *
from game.states.MenuState import *
#=================Entry point=================#
#Initialize necessary elements
g = Game()
initState = MenuState()

g.setState(initState)

g.gameLoop()
g.destroy()
