# Определение персонажей
define mary = Character('Мэри', color="#c8ffc8", what_italic=True)
define katy = Character('Катя', color="#6666ff", what_outlines=[(1, "#1a1a1a")])
define vana = Character('Ваня', color="#8b00ff", what_slow=10)
define kirill = Character('Кирилл', color="#6666ff", what_bold=True)
define larry = Character('Ларри', color="#ff0000", what_size=32)
define unknow = Character('Неизвестный', color="#ff0000", what_size=32)

# Переменные состояния
default secrets_unlocked = {
    "hasphone": False,
    "meetlarry": False,
    "hall_inspected": False,
    "texts_decrypted": False
}

default hasphone = False
default meetlarry = False
default meetinglarry = False
default hallisinspected = False
default textpreparation = False
default decorating = False
default controller = True

# Определение кастомных трансформаций
transform slow_fadein:
    alpha 0.0
    linear 3.0 alpha 1.0

transform choice_transformation(xpos, ypos):
    xpos xpos ypos ypos
    zoom 0.9
    easein 0.5 zoom 1.0

label start:
    scene black with Dissolve(2.0)
    play sound "heartbeat.wav" fadein 1.5

    show title as title at truecenter:
        alpha 0.0
        linear 2.0 alpha 1.0
        pause 1.0
        linear 1.0 alpha 0.0

    "{cps=15}Город, где тени длиннее зданий...{/cps}"
    "{cps=20}Где любой выбор оставляет шрам...{/cps}"
    play music "ambient_drone.ogg" volume 0.4

    show text "Счастливый конец — это иллюзия\nТы лишь выбираешь,\nкакой кошмар предпочтительнее" at center:
        xalign 0.5
        yalign 0.7
        slow_fadein

    pause 3.0
    scene black with irisout

    # Основной сюжет
    call afterUniversity from _call_afterUniversity
    call inThePark from _call_inThePark
    call inTheRestaurant from _call_inTheRestaurant
    call inTheMetro from _call_inTheMetro

    scene black
    show text "24 часа спустя..." at truecenter with dissolve
    pause 1.5
    scene black with dissolve
    
label preparation_loop:
    play music "tension_loop.ogg" volume 0.3 fadein 2.0
    scene backgroundnull with dissolve:
        blur 5

    if secrets_unlocked["hall_inspected"] and secrets_unlocked["texts_decrypted"]:
        jump conversationAtEvent
    else:
        call screen preparation_choices

label inspect_hall:
    scene office with blinds:
        matrixcolor BrightnessMatrix(-0.1)
    
    "Старый конференц-зал пахнет затхлостью и озоном..."
    show mary_standby_unclear at left with dissolve
    mary "Обратите внимание на систему вентиляции..."
    show katy_standby_unsure at right with moveinright
    katy "По документам здесь последний раз ремонтировали в 2005..."
    play sound "metal_creak.wav"
    with hpunch
    $ secrets_unlocked["hall_inspected"] = True
    call Hall from __call_Hall
    $ hallisinspected = True
    jump preparation_loop

label research_tech:
    scene servers
    show text "{font=DejaVuSans-Bold.ttf}Протокол L-7{/font}" at truecenter:
        alpha 0.0
        linear 2.0 alpha 0.7
    
    play sound "glitch.wav"
    $ secrets_unlocked["texts_decrypted"] = True
    call TextPreparationInHome from _call_TextPreparationInHome
    call MeetToLarry from _call_MeetToLarry
    call SubjectMatter from _call_SubjectMatter
    $ textpreparation = True
    jump preparation_loop

label ComingSoon:
    $ renpy.movie_cutscene("videos/comingsoon.webm")
    return