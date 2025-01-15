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
    
    call afterUniversity from _call_afterUniversity
    call inThePark from _call_inThePark
    call inTheRestaurant from _call_inTheRestaurant
    call inTheMetro from _call_inTheMetro

    scene black
    "На следующий день..."

    call nextDay from _call_nextDay

    scene backgroundnull
    menu:
        "Нам нужно представить новую разработку Сейф-сеть с помощью внутренней презентации их компаний. Что нужно начать?"
        "Обсудить план мероприятия":
            mary "Предлагаю обсудить сначала программу и само мероприятие."
            mary "Предлагаю для этого прийти домой."
            $ decorating = True
            call SubjectMatter from _call_SubjectMatter
        "Обсудить саму компанию и их разработку":
            mary "Предлагаю обсудить сначала саму технологию."
            $ textpreparation = True
            call TextPreparationInHome from _call_TextPreparationInHome
        "Осмотреть зал":
            mary "Было бы неплохо сначала осмотреть зал."
            $ hallisinspected = True
            call Hall from _call_Hall

    while controller:
        if hallisinspected == True and textpreparation == True and decorating == True:
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
                            call MeetToLarry from _call_MeetToLarry
                            call SubjectMatter from _call_SubjectMatter_1
                        "Обсудить шутки и диалоги":
                            mary "Предлагаю обсудить программу и само мероприятие."
                            $ textpreparation = True
                            call TextPreparationInHome from _call_TextPreparationInHome_1
                else:
                    mary "Предлагаю обсудить тематику!"
                    mary "Предлагаю для этого прийти домой."
                    $ decorating = True
                    call SubjectMatter from _call_SubjectMatter_2
            else:
                if textpreparation == False:
                        mary "Предлагаю обсудить программу и само мероприятие."
                        $ textpreparation = True
                        call TextPreparationInHome from _call_TextPreparationInHome_2
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
                            call MeetToLarry from _call_MeetToLarry_1
                            call SubjectMatter from _call_SubjectMatter_3
                        "Обсудить шутки и диалоги":
                            mary "Предлагаю обсудить программу и само мероприятие."
                            $ textpreparation = True
                            call TextPreparationInHome from _call_TextPreparationInHome_3
                else:
                    mary "Было бы неплохо осмотреть зал."
                    $ hallisinspected = True
                    call Hall from _call_Hall_1
            else:
                if textpreparation == False:
                    mary "Предлагаю обсудить программу и само мероприятие."
                    $ textpreparation = True
                    call TextPreparationInHome from _call_TextPreparationInHome_4
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
                            call Hall from _call_Hall_2
                        "Обсудить тематические цвета и украшения":
                            #mary "Предлагаю обсудить тематику!"
                            #mary "Предлагаю для этого прийти домой."
                            $ decorating = True

                            call MeetToLarry from _call_MeetToLarry_2

                            call SubjectMatter from _call_SubjectMatter_4
                else:
                    mary "Было бы неплохо осмотреть зал."
                    $ hallisinspected = True
                    call Hall from _call_Hall_3
            else:
                if decorating == False:
                        mary "Предлагаю обсудить тематику!"
                        mary "Предлагаю для этого прийти домой."
                        $ decorating = True

                        call MeetToLarry from _call_MeetToLarry_3

                        call SubjectMatter from _call_SubjectMatter_5
                    

    mary "Ну, мы готовы!"
    katy "Отлично!"
    #jump ComingSoon
    call conversationAtEvent from _call_conversationAtEvent

    return

label ComingSoon:
    $ renpy.movie_cutscene("videos/comingsoon.webm")
