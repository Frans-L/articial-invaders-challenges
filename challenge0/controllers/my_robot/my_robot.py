from invader_bot import InvaderBot

# InvaderBot is a custom helper class that cretes interface 
# over the webots default motor controllers. 
# You can use the helper class or use the webots motor controllers
# on you own.
bot = InvaderBot() 
bot.setup()

kb = bot.robot.getKeyboard()
kb.enable(bot.timestep)

while bot.step():
    current_key = kb.getKey()
    
    if current_key == -1:
        bot.set_motors(0, 0)
    if current_key == ord('W'):
        bot.set_motors(1,1)
    if current_key == ord('S'):
        bot.set_motors(-1,-1)
    if current_key == ord('A'):
        bot.set_motors(1,-1)
    if current_key == ord('D'):
        bot.set_motors(-1,1)

print("Closing...")
