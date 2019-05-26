## #0 BOTS ON THE RUN

### TARGET

Gather all coins with your robot.

### DESCRIPTION

The purpose of this challenge is to teach you how to use Webots.
Your task is simply to make a script that moves the bot.
The bot should gather all coins. The coins are static and always
in the same position.

You do not have access to the coordinates of your robot
because your robot does not have any sensors yet.
In the tournament, there will be a camera streaming the arena from the ceiling.
The position of the objects can be calculated by using image recognizing.
In later challenges, image recognition will be simulated, but not yet.

You can freely modify the files under the folder ```controllers/my_robot/```.
All other files will be replaced by the original ones.

To open the challenge, open the file ```arena/challenge0.wbt``` with Webots.

### OTHER

InvaderBot is a simple helper class which has methods to control the robot.
It offers an interface over Webots' default motor controller.
You can use it, modify it or you can also use Webots' own commands.
Using the helper class is recommended because it will later help you to
transfer your code into a physical robot, which is running on Raspberry Pi.

If you have perfomance issues, lower Webot's rendering settings. You can also
try to delete a Webot's object called "DEF \_lights GROUP" to improve perfomance.