define mary = Character('Мэри', color="#c8ffc8")
define katy = Character('Кейт', color="#6666ff")
define vana = Character('Ваня', color="#8b00ff")
#define max = Character('Макс Апшер', color="#ffffff")
#define lincoln = Character('Линкольн 1507', color="#ffffff")
define kirill = Character('Кирилл', color="#6666ff")
define unknow = Character('null', color="#ff0000")
#define cray = Character('Крей', color="#8b00ff")
define larry = Character('Ларри', color="#ff0000")

default hasphone = False
default meetlarry = False
default meetinglarry = False
default hallisinspected = False
default textpreparation = False
default decorating = False
default controller = True

label start:
    scene logo
    "Добро пожаловать!"
    "Это Дебург - маленький городок, в котором очень много всего интересного!"
    "Запомни!"
    "Любой выбор имеет свою цену..."
    "..."
    "Счастливую концовку делаешь ты."
    "Судьба в твоих руках."
    
    call afterUniversity

    scene black
    "На следующий день..."

    call nextDay

    scene backgroundnull
    menu:
        "C чего начать?"
        "Обсудить тематические цвета и украшения":
            mary "Предлагаю обсудить тематику!"
            mary "Предлагаю для этого прийти домой."
            $ decorating = True
            call SubjectMatter
        "Обсудить мероприятие":
            mary "Предлагаю обсудить программу и само мероприятие."
            $ textpreparation = True
            call TextPreparationInHome
        "Осмотреть зал":
            mary "Было бы неплохо осмотреть зал."
            $ hallisinspected = True
            call Hall

    while controller:
        if hallisinspected == True:
            if textpreparation == True:
                if decorating == True:
                    $ controller = False
        if hallisinspected == True:
            play music "Fantasy_World.mp3" volume 0.3
            scene backgroundnull
            if decorating == False:
                if textpreparation == False:
                    menu:
                        "Что дальше?"
                        "Обсудить тематические цвета и украшения":
                            mary "Предлагаю обсудить тематику!"
                            mary "Предлагаю для этого прийти домой."
                            $ decorating = True
                            call MeetToLarry
                            call SubjectMatter
                        "Обсудить шутки и диалоги":
                            mary "Предлагаю обсудить программу и само мероприятие."
                            $ textpreparation = True
                            call TextPreparationInHome
                if textpreparation == True:
                    mary "Предлагаю обсудить тематику!"
                    mary "Предлагаю для этого прийти домой."
                    $ decorating = True
                    call SubjectMatter
            if decorating == True:
                if textpreparation == False:
                        mary "Предлагаю обсудить программу и само мероприятие."
                        $ textpreparation = True
                        call TextPreparationInHome
        if decorating == True:
            play music "Fantasy_World.mp3" volume 0.3
            scene backgroundnull
            if hallisinspected == False:
                if textpreparation == False:
                    menu:
                        "Что дальше?"
                        "Осмотреть зал":
                            mary "Предлагаю обсудить тематику!"
                            mary "Предлагаю для этого прийти домой."
                            $ decorating = True
                            call MeetToLarry
                            call SubjectMatter
                        "Обсудить шутки и диалоги":
                            mary "Предлагаю обсудить программу и само мероприятие."
                            $ textpreparation = True
                            call TextPreparationInHome
                if textpreparation == True:
                    mary "Было бы неплохо осмотреть зал."
                    $ hallisinspected = True
                    call Hall
            if hallisinspected == True:
                if textpreparation == False:
                    mary "Предлагаю обсудить программу и само мероприятие."
                    $ textpreparation = True
                    call TextPreparationInHome
        if textpreparation == True:
            play music "Fantasy_World.mp3" volume 0.3
            scene backgroundnull
            if hallisinspected == False:
                if decorating == False:
                    menu:
                        "Что дальше?"
                        "Осмотреть зал":
                            mary "Было бы неплохо осмотреть зал."
                            $ hallisinspected = True
                            call Hall
                        "Обсудить тематические цвета и украшения":
                            #mary "Предлагаю обсудить тематику!"
                            #mary "Предлагаю для этого прийти домой."
                            $ decorating = True

                            call MeetToLarry

                            call SubjectMatter
                if decorating == True:
                    mary "Было бы неплохо осмотреть зал."
                    $ hallisinspected = True
                    call Hall
            if hallisinspected == True:
                if decorating == False:
                        mary "Предлагаю обсудить тематику!"
                        mary "Предлагаю для этого прийти домой."
                        $ decorating = True

                        call MeetToLarry

                        call SubjectMatter
                    

    mary "Ну, мы готовы!"
    katy "Отлично!"
    jump ComingSoon
    call conversationAtEvent

    if MeetToLarry == True:
        menu:
            "Что делать?!"
            "Попросить помомщи":
                call firstEnd
            "Разрулить самостоятельно":
                call secondEnd
    if MeetToLarry == False:
        call secondEnd

    return

label ComingSoon:
    $ renpy.movie_cutscene("videos/comingsoon.webm")
