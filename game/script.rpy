define mary = Character('Мэри', color="#c8ffc8") #Мэри
define katy = Character('Катя', color="#6666ff") #Кейт
define vana = Character('Ваня', color="#8b00ff") #Ваня
#define max = Character('Макс Апшер', color="#ffffff")
#define lincoln = Character('Линкольн 1507', color="#ffffff")
define kirill = Character('Кирилл', color="#6666ff") #Кирилл
define unknow = Character('null', color="#ff0000") #Ларри
#define cray = Character('Крей', color="#8b00ff")
define larry = Character('Ларри', color="#ff0000") #Ларри

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

    while controller:
        play music "Fantasy_World.mp3" volume 0.3
        scene backgroundnull
        if hallisinspected and textpreparation and decorating:
            $ controller = False
        elif hallisinspected and not decorating and not textpreparation:
            menu:
                "Что дальше?"
                "Обсудить тематические цвета и украшения":
                    mary "Предлагаю обсудить тематику!"
                    mary "Для этого предлагаю прийти ко мне домой завтра!"
                    katy "Отличная идея!"
                    $ decorating = True
                    call MeetToLarry from _call_MeetToLarry
                    call SubjectMatter from _call_SubjectMatter
                "Обсудить шутки и диалоги":
                    mary "Предлагаю обсудить программу и само мероприятие."
                    $ textpreparation = True
                    call TextPreparationInHome from _call_TextPreparationInHome
        elif not hallisinspected and decorating and not textpreparation:
            menu:
                "Что дальше?"
                "Осмотреть зал":
                    mary "Предлагаю осмотреть зал завтра!"
                    $ hallisinspected = True
                    call MeetToLarry from _call_MeetToLarry_2
                    call Hall from __call_Hall
                "Обсудить шутки и диалоги":
                    mary "Предлагаю обсудить программу и само мероприятие."
                    $ textpreparation = True
                    call TextPreparationInHome from _call_TextPreparationInHome_2
        elif not hallisinspected and not decorating and textpreparation:
            menu:
                "Что дальше?"
                "Осмотреть зал":
                    mary "Было бы неплохо осмотреть зал."
                    $ hallisinspected = True
                    call Hall from _call_Hall
                "Обсудить тематические цвета и украшения":
                    $ decorating = True
                    call MeetToLarry from _call_MeetToLarry_3
                    call SubjectMatter from _call_SubjectMatter_2
        elif hallisinspected and not textpreparation and decorating:
            mary "Предлагаю обсудить программу и само мероприятие."
            $ textpreparation = True
            call TextPreparationInHome from _call_TextPreparationInHome_3
        elif hallisinspected and textpreparation and not decorating:
            mary "Предлагаю обсудить тематику!"
            mary "Для этого предлагаю прийти ко мне домой завтра!"
            $ decorating = True
            call SubjectMatter from _call_SubjectMatter_3
        elif not hallisinspected and decorating and textpreparation:
            mary "Дальше было бы неплохо осмотреть зал..."
            $ hallisinspected = True
            call Hall from _call_Hall_2
        else:
            menu:
                "Нам нужно представить новую разработку Сейф-сеть с помощью внутренней презентации их компаний. Что нужно начать?"
                "Обсудить план мероприятия":
                    mary "Предлагаю обсудить сначала программу и само мероприятие."
                    mary "Предлагаю для этого прийти домой."
                    $ decorating = True
                    call SubjectMatter from _call_SubjectMatter_4
                "Обсудить саму компанию и их разработку":
                    mary "Предлагаю обсудить сначала саму технологию."
                    $ textpreparation = True
                    call TextPreparationInHome from _call_TextPreparationInHome_4
                "Осмотреть зал":
                    mary "Было бы неплохо сначала осмотреть зал."
                    $ hallisinspected = True
                    call Hall from _call_Hall_3      

    mary "Ну, мы готовы!"
    katy "Отлично!"

    call conversationAtEvent from _call_conversationAtEvent

    return

label ComingSoon:
    $ renpy.movie_cutscene("videos/comingsoon.webm")
