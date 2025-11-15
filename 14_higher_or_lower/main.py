from control import Controller

# #######################################

def higher_or_lower():
    controller = Controller()
    controller.start()
    while controller.states.is_playing: controller.game()
    controller.exit()


# #######################################

higher_or_lower()

# Note:
# This game assuming the follower A > B, or vice versa
# Game will break if follower A == follower B
# (no logic to handle tie follower's count)
