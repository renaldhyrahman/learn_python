class Logic:
    def __init__(self, data: object):
        self.data = data

    def level_up(self):
        player = self.data.player
        size_unit = self.data.screen.size.UNIT
        if player.ycor() >= self.data.screen.MAX_Y:
            self.data.cur_level += 1
            self.data.velocity_car += size_unit / 2
            player.restart()
