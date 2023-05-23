# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
image eileen = "eileen.png"

# The game starts here.
label start:
    play music "menu.mp3"
    scene black
    "Мини игра пин понг"
    jump demo_minigame_pong #Переход на игру

    return
