def getColor(player_pos, centerpoint):
    if player_pos.x > centerpoint:
        color = (0, 200, 0)
    else:
        color = (0, 255, 0)
    return color

