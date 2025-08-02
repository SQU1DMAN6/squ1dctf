def getColor(player_pos, centerpoint):
    if player_pos.x > centerpoint:
        color = (0, 200, 0)
    else:
        color = (0, 255, 0)
    return color

def checkflagcap(x, y, x2, y2):
        if x > x2 and x < x2 + 120 and y > y2 and y < y2 + 120:
            return True
        else:
            return False