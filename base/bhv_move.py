from lib.action.go_to_point import *
from base.strategy_formation import *
from lib.debug.logger import *
from lib.player.templates import *


class BhvMove:
    def __init__(self):
        pass

    def execute(self, agent: PlayerAgent):
        st = StrategyFormation().i()
        wm: WorldModel = agent.world()
        dlog.add_line(Level.BLOCK, start=wm.self().pos(), end=wm.ball().pos(), color=Color(string="black"))
        dlog.add_text(Level.BLOCK, f"Test {wm.self().pos()}")  # Aref come on :))) # HA HA HA HA :D
        dlog.add_circle(cicle=Circle2D(wm.self().pos(), 3), color=Color(string="blue"))
        target = st.get_pos(agent.world().self().unum())
        min_dist_ball = 1000
        nearest_tm = 0
        for u in range(1, 12):
            tm = wm.our_player(u)
            if tm.unum() is not 0:
                dist = tm.pos().dist(wm.ball().pos())
                if dist < min_dist_ball:
                    min_dist_ball = dist
                    nearest_tm = u
        if nearest_tm == wm.self().unum():
            target = wm.ball().pos()

        GoToPoint(target, 1, 100).execute(agent)
        return True
