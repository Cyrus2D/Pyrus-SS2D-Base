from lib.action.go_to_point import *


def get_decision(agent):
    GoToPoint(agent.world().ball().pos(), 2, 100).execute(agent)
    return True