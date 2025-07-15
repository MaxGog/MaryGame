label afterUniversity:
    scene university with fade
    play music "Marcel_Pequel.mp3" volume 0.3
    "А сейчас вы находитесь в главном институте культуры города!"
    "..."
    "Мы шли по лестнице нашего института в последний раз."
    "Если другим было грустно, то я определённо была рада! Ведь я не особо любила этот факультет."
    "Мы уже забрали наши аттестаты."
    "Из окон светило яркое солнце, которое манило выйти на свежий воздух и прогуляться в местном парке."
    
    show mary_standby_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    #voice "voice/mary-voice1.ogg"
    mary "Какие планы у вас на сегодня?"
    "Да, это я! Маша... Ну или Мэри. Я шла с моими лучшими друзьями по этому учебному заведению."
    "Я никогда не думала, что смогу найти в этом институте таких интересных людей."

    show mary_standby_smile at right with move:
        ease 0.5 xalign 0.75
    show katy_standby_fine at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    katy "Я предлагаем где-нибудь отметить! Мы закончили учёбу!"

    "Это Катя. Стеснительная, но при этом очень умная - она всегда может поддержать разговор. Отлично разбирается в гаджетах."
    "Мы познакомились на первом курсе, когда я заинтересовалась книгой, которую она писала на ноутбуке во время пар."
    "Мы легко подружились."

    show john_standby_smile at left with moveinleft:
        zoom 1.0
        yalign 1.0
        xalign 0.1
    vana "Отличная идея! Где будем отмечать?"

    "А это Ваня. Наша местная элита. Он поступил сюда только ради возможности проводить мероприятия на корпоративах и праздниках."
    "Вот он действительно учился упорно. Мы познакомились чуть позже, чем с Катей, когда в столовой не оказалось свободных мест, и он решил присоединиться к нам."
    "Мы, конечно, не возражали."
    "Хотя мой сводный брат Крей его недолюбливал - не знаю почему..."
    "Крей в целом хороший парень, но... иногда его суждения о людях бывают странными."
    "Он хакер, возможно, поэтому такой закрытый и предвзятый."
    "Он всегда знал обо мне больше, чем я сама, но окончательное решение почему-то всегда оставлял за мной!"
    
    hide mary_standby_smile
    show mary_offer_smile at right with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    #Вставить фотки братьев.
    mary "Можно у меня! Мои братья на неделю уехали ещё вчера."
    "Да, у меня два брата!"
    "Второго зовут Честер."
    "Если Крей - активный, подтянутый, следит за собой, то Честер - его полная противоположность."
    "Несмотря на хорошие природные данные, он совсем не заботится о себе."
    "Выглядит прилично, но живот у него знатный. Да и ленив он страшно - может целыми вечерами пить пиво."
    "Дай ему ящик - неделю из дома не выйдет! Хе-хе!"

    hide katy_standby_fine
    show katy_standby_unsure at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    katy "Как-то дома не очень хочется, да и в такую солнечную погоду лучше на улице..."
    
    "Неловкая улыбка появилась на лице Кати, когда она обхватила свои локти."
    "Её стеснительность всегда меня умиляла. Она явно не хотела сидеть дома."
    "Катя обожала гулять."
    "Даже свои литературные произведения - лучшие главы - она писала в местном парке."

    hide john_standby_smile
    show john_crossed_smile at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.1
    vana "Может, тогда отправимся в кафе? Я знаю хорошее заведение неподалёку!"
    
    "Уверенно предложил Ваня, расправив плечи и гордо скрестив руки на груди."
    "Его улыбка была харизматичной и на первый взгляд холодной, но чувствовалась искренняя доброта."

    show katy_standby_unsure at center with move:
        ease 0.5 xalign 0.6
    show mary_offer_smile at center with move:
        ease 0.5 xalign 0.5
    hide mary_offer_smile
    show mary_standby_unclear at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    mary "У нас не такие богатые родители, как у тебя, Вань..."
    vana "Да я оплачу, не переживайте! Тем более... Сегодня у нас особый случай!"

    show mary_offer_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    hide mary_standby_unclear 
    "Ну уж им, миллионерам! Ха-ха!"
    "Шучу, конечно!"
    "Родители Вани не миллиардеры. Но..."
    hide mary_offer_smile
    show mary_standby_unclear at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5

    "Мне всё равно было неловко - я привыкла всё делать сама."
    "И платить тоже."
    "У нас в семье, как и у Кати, не было лишних денег, поэтому приходилось экономить, чтобы позволить себе крутые гаджеты."
    "Но... раз Ваня предлагает... Почему бы и нет?"

    hide mary_standby_unclear
    show mary_offer_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    mary "Ну ладно, давайте!"
    
    "Катя тоже недолго сомневалась."
    "Помявшись на месте пару секунд, она собралась с духом, тепло улыбнулась и согласилась."
    
    hide katy_standby_unsure
    show katy_standby_fine at right with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.6
    katy "Я согласна!"
    
    "Раз все были согласны, мы определились с местом."
    katy "Предлагаю пойти через парк!"
    "Возражений не последовало, и мы направились сначала в парк."

    return

label inThePark:
    scene trees with fade
    play sound "park.mp3" volume 0.5
    "Погода и правда была замечательной."
    "Людей в парке было немного."

    show katy_standby_fine at right with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    show john_standby_smile at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    show mary_standby_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5

    "Мы шли по аллее, вспоминая студенческие годы. Теперь мы взрослые!"
    "Это было моё второе высшее образование, но только сейчас я ощутила вкус свободы."
    "Рядом оказался ларёк с мороженым."
    "Каждый выбрал любимый вкус: Ваня - ванильное, Катя - фруктовый сорбет, а я - клубничное."
    "Чтобы не есть на ходу, мы присели на ближайшую свободную скамейку."
    "Вокруг росло много кустов... Но один выглядел странно потрёпанным, будто через него кто-то продирался."

    hide john_standby_smile
    show john_standby_unsure at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    vana "Смотрите! Кажется, кто-то пробирался через эти кусты... И там что-то лежит..."

    "Исследовать кусты? Не самое приятное занятие..."
    "Но Ваня был прав. Кусты действительно выглядели неестественно помятыми."

    hide katy_standby_fine
    show katy_standby_unsure at right with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    katy "Может... пойдём дальше? Вдруг это бомба!"
    
    "Бомба? Я едва сдержала смех!"
    "Ну надо же..."
    "БоМбА))))00))))0)"
    "Но ей действительно было страшно."
    
    hide mary_standby_smile
    show mary_standby_unclear at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5

    menu:
        "Катя не хочет смотреть, что за кустами, а Ваня настаивает"
        "Согласиться с Ваней":
                stop sound
                hide mary_standby_unclear
                show mary_akimbo_sure at center with dissolve:
                    zoom 1.0
                    yalign 1.0
                    xalign 0.5
                mary "Давайте проверим!"
                "Предложила я с неожиданным энтузиазмом."
                vana "Катя, если хочешь, останься здесь. Только проследи, чтобы никто не мешал."
                "Он заботливо положил руку ей на плечо. Та лишь обхватила себя за локти, с опаской поглядывая на кусты."
                katy "Бр... Ладно... Но будьте осторожны!"
                hide john_standby_unsure
                show john_crossed_smile at left with dissolve:
                    zoom 1.0
                    yalign 1.0
                    xalign 0.25
                vana "Конечно! Мы - сама осторожность!"
                hide katy_standby_unsure with dissolve
                "Мы с Ваней аккуратно пробрались в кусты, пока Катя осматривалась, следя за прохожими."
                hide mary_akimbo_sure
                show mary_wow at center with dissolve:
                    zoom 1.0
                    yalign 1.0
                    xalign 0.5
                "Среди веток что-то лежало. Небольшое и чёрное."
                "Я осторожно протянула руку."
                scene findphone with pixellate
                "Это оказался телефон."
                "Последняя модель. Без царапин. Даже чехла не было."
                mary "Телефон!"
                vana "Вижу..."
                "Я нажала кнопку включения. В аппарате не было SIM-карты и пароля. Владелец не указан, но были установлены приложения."
                mary "Может, позвоним его родным? Вроде есть контакты."
                scene trees with fade
                show katy_standby_unsure at right with dissolve:
                    zoom 1.0
                    yalign 1.0
                    xalign 0.75
                show john_crossed_smile at left with dissolve:
                    zoom 1.0
                    yalign 1.0
                    xalign 0.25
                show mary_wow at center with dissolve:
                    zoom 1.0
                    yalign 1.0
                    xalign 0.5
                katy "Только со своего звоните, вдруг внутри взрывчатка..."
                "Она даже отступила на шаг."
                mary "Здесь нет SIM-карты. Придётся со своего."
                katy "Ладно, хватит. Д-давайте позже. Пошли уже, а то есть хочу!"
                "Оглядевшись, я положила телефон в сумку. Быстрым шагом мы двинулись дальше."
                $ hasphone = True
        "Согласиться с Катей":
                mary "Мне кажется, это и правда опасно... Может, просто уйдём?"
                vana "М-да... Ладно..."
                "Ваня неохотно поплёлся за нами, а Катя почти бежала впереди."
                "Я же шла спокойно."

    "Мы быстро удалились от того места."

    return

label inTheRestaurant:
    scene cafe with fade
    play music "Savfk.mp3"
    play sound "rest.mp3" volume 0.3

    "Выйдя из парка, мы быстро нашли ресторан. Интерьер выглядел дорого."
    "Даже как-то неловко стало."
    "Мы поднялись на крышу и заняли столик с видом на закат."
    "Уже семь."
    "Время пролетело незаметно."
    "Подошёл официант с меню."

    show john_crossed_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    vana "Не стесняйтесь! Заказывайте что хотите! Я угощаю."

    if hasphone == True:
        "Ваня был в отличном настроении, как и я, а вот Катя..."
        "Она всё ещё переживала из-за телефона."
        "Она вообще не любила авантюры."
        "Мне стало немного стыдно - она всегда терпела наши с Ваней выходки."

    hide john_crossed_smile with dissolve

    menu:
        "В меню было много вариантов. Я не могла выбрать."
        "Пицца":
            show mary_bothhand at center with dissolve:
                zoom 1.0
                yalign 1.0
                xalign 0.5
            mary "Давайте пиццу. На всех!"
            show john_crossed_smile at left with dissolve:
                zoom 1.0
                yalign 1.0
                xalign 0.25
            show katy_standby_fine at right with dissolve:
                zoom 1.0
                yalign 1.0
                xalign 0.75
            katy "Отличная идея!"
            vana "Решено!"
            "Ваня заказал большую пиццу на троих."
        "Салат":
            show mary_bothhand at center with dissolve:
                zoom 1.0
                yalign 1.0
                xalign 0.5
            mary "Как насчёт салата?"
            show john_crossed_smile at left with dissolve:
                zoom 1.0
                yalign 1.0
                xalign 0.25
            show katy_standby_fine at right with dissolve:
                zoom 1.0
                yalign 1.0
                xalign 0.75
            katy "Отлично!"
            vana "Решено!"
            "Ваня заказал нам салат."

    hide mary_bothhand

    if hasphone == True:
        show mary_standby_unclear at center with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.5
        mary "Так... что насчёт телефона?"
        hide john_crossed_smile
        show john_standby_unsure at left with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.25
        vana "Посмотри контакты, потом позвоним и скажем, что нашли."
        "Я открыла адресную книгу. Контактов было немного."
        "Но среди них был Макс - владелец корпорации Био-Tech."
        hide mary_standby_unclear
        show mary_wow at center with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.5
        "Странно и неожиданно. Значит, владелец телефона работал в этой корпорации..."
        "И явно на высокой должности."
        mary "Владелец - важная персона... Тут номер хозяина Био-Tech!"
        hide katy_standby_fine
        show katy_scary at right with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.75
        katy "Что?! Не может быть! Хотя по модели телефона..."
        vana "А нет контактов родственников? Или менее известных людей?"
        mary "Похоже, все контакты рабочие. Они в одной группе."
        hide katy_scary
        show katy_standby_unsure at right with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.75
        katy "Может, решим завтра? Я сегодня вымоталась."
        hide mary_wow
        show mary_explaining at center with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.5
        mary "Тогда телефон пока у меня..."
        vana "Значит, завтра в десять..."
        katy "На нашем месте."
    else:
        show mary_bothhand at center with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.5
        mary "Кто что завтра делает?"
        katy "Я хотела найти работу... Без опыта сложно."
        "Катя пожала плечами, не зная, с чего начать."
        "Они делали первые шаги во взрослую жизнь."
        "В отличие от меня..."
        vana "Она права."
        "Я задумалась, пока другие тоже предавались размышлениям."
        "Им нужна была помощь!"
        "В одиночку найти работу трудно. Я знаю по себе."
        mary "Может, поищем вместе? Втроём шансов больше!"
        "Реакция была положительной, судя по их лицам."
        vana "Ты права, вместе мы сможем устроиться даже на корпоративы."
        katy "Тогда завтра в десять на нашем месте?"
        mary "Отлично!"
        vana "Договорились!"
        
    "Принесли заказ, и мы принялись за еду."
    "Болтали ни о чём и обо всём."
    "Просто отдыхали после напряжённого дня и радовались окончанию учёбы."
    "Наступил вечер."
    "Ваня оплатил счёт, и мы разошлись."
    "Я направилась к метро - жила я на другом конце города."
    stop sound

    return

label inTheMetro:
    scene marysubwayfullscreen with fade

    "Я прошла через турникет и села в вагон."
    "Нужно было доехать до конечной."

    play sound "metro_train.mp3"

    "Надела наушники и включила любимый плейлист."
    "Зазвучала песня Моносветы. Мало кто её знает, но у неё классные треки."
    "В вагоне было немноголюдно."
    "Дебург - город небольшой, большинство предпочитало автобусы или такси."

    "Но мне нравилось метро."
    "Особенная атмосфера..."
    "Едешь под землёй, но можно работать, слушать музыку..."
    "Некоторые даже умудряются болтать при таком шуме!"
    "Мы с Катей часто так делали."
    "Зимой она переезжала к тёте."
    "Мы встречались перед парами и ехали вместе."
    "Потом подхватывали Ваню."
    "Было весело!"

    "Но вскоре... я нечаянно заснула."

    stop sound

    if hasphone == True:
        play music "Panic.mp3"
        scene black with fade
        "Просто закрыла глаза."
        "Меня разбудил низкий голос."
        "Я медленно открыла глаза..."
        " "
        hide black

        play sound "glitch.mp3"
        $ renpy.movie_cutscene("videos/metrohorror.webm")
        image animated_metro = Movie(play="videos/metrohorror.webm")
        show animated_metro behind larry
        show larry with pixellate
        unknow "Спасибо, что нашла мой телефон."

        "В вагоне никого не было. Только я и этот человек."
        "Мне стало страшно. Сон? Галлюцинация?"
        "Что происходит?!"

        mary "Кто вы?.."
        unknow "Мы встретимся с братьями. Скоро. А пока... Спасибо!"

        "В моих руках был его телефон. Он взял его - я не могла сопротивляться."

        mary "Стойте! Вы из Био-Tech?!"

        scene black with fade
        "Я моргнула..."
        scene metro with fade
        stop music

    "Открыв глаза, я увидела свою станцию."

    if hasphone == True:
        "Но телефона в сумке уже не было. Этот человек забрал его..."
        "Люди снова появились в вагоне."
        "Я выбежала и помчалась домой..."
    else:
        "Я вышла из вагона."
        "Как я могла заснуть?!"

    return

label nextDay:
    scene street with fade
    play music "Spring_In_My_Step.mp3"
    show mary_standby_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5

    "Я встала рано."

    hide mary_standby_smile
    show mary_standby_unclear at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    "..."
    "Что за музыка?!"
    "Я что... в игре? Это же визуальная новелла!"
    hide mary_standby_unclear
    show mary_standby_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5

    "Быстро собравшись, я направилась к месту встречи."
    "На небольшой площади, где мы обычно собирались перед институтом, друзья уже ждали."
    "Я радостно помахала им и подбежала."
    "Они ответили на приветствие улыбками."

    mary "Привет, ребята!"
    show katy_hello_smile at right with moveinright:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    katy "Мэри! Доброе утро!"

    "Катя держала стаканчик с кофе."

    show john_hello_smile at left with moveinleft:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    vana "Привет!"

    if hasphone == True:
        mary "Я вам кое-что расскажу!"

        hide katy_hello_smile
        show katy_standby_fine at right with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.75
        katy "У тебя что-то случилось?"

        mary "Телефон забрал его владелец!"
        hide katy_standby_fine
        show katy_standby_unsure at right with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.75
        katy "Это... очень странно..."

        "Моя подруга явно забеспокоилась."

        hide mary_standby_smile
        show mary_unsure at center with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.5
        mary "И вот что странно - откуда он узнал, что это мы нашли телефон? И что я буду в метро..."

        hide john_hello_smile
        show john_standby_unsure at left with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.25
        vana "По GPS?"

        "Предположил Ваня."

        katy "Возможно..."

        vana "Нужно что-то предпринять... Вдруг будут проблемы?"
        mary "Он мне не понравился..."
        mary "Был в маске..."
        mary "Синие волосы..."
        mary "Странно говорил..."

        hide john_standby_unsure
        show john_standby_smile at left with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.25
        vana "Вы с братом хакеры! Да и мы разбираемся. Почему бы его не взломать? Зацепка есть."

        katy "Мне кажется, это неправильно..."
        mary "Лучше это, чем ничего."
        katy "Ну... ладно..."

        hide john_standby_smile
        show john_hello_smile at left with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.25
        vana "Давайте обсудим это где-нибудь, но не здесь."

        hide mary_unsure
        show mary_standby_smile at center with dissolve:
            zoom 1.0
            yalign 1.0
            xalign 0.5
        hide katy_standby_unsure
    else:
        katy "Какие новости? Может, насчёт работы?"
        "С надеждой спросила Катя."
        mary "К сожалению, нет... Но есть идеи!"
        vana "Может, обсудим за чашкой кофе?"
        "Ваня был прав - здесь не лучшее место."
        hide katy_hello_smile

    show katy_standby_fine at right with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    mary "Куда пойдём?"
    vana "Мне нужно забрать новую карту, зайдём по пути?"
    katy "Конечно! Какая карта?"
    vana "От Беты Банка. Кредитка. Месяц без процентов!"
    mary "В Серебе проценты 4-5."
    vana "Но там сразу начисляют?"
    katy "Лучшая карта в Троиц Банке! Год без процентов!"
    mary "Но без кэшбека!"
    katy "Ну... да..."
    vana "В Бете есть кэшбек 10 процентов."
    mary "Пф! В Серебе 15 процентов!"
    katy "В Троиц обслуживание бесплатное!"
    vana "Да это мелочи!"
    mary "Мелочи? 100 рублей в месяц за карту в твоём Бете."

    katy "Ребята! Хватит рекламировать вымышленные банки! Пошли уже?"
    "Катя встала между нами, прерывая спор."

    menu:
        "Прекратить спор?"
        "Да":
            "Мы переглянулись и направились по делам Вани."

    hide mary_standby_smile
    hide katy_standby_fine
    hide john_hello_smile

    "Место было недалеко."
    "Но народу - тьма."

    scene bank with fade
    "Войдя внутрь, мы встали в очередь."
    "Над дверью висел колокольчик, оповещающий о клиентах."
    stop music
    play music "null.mp3"
    "Прозвенел дважды, когда на полу появилась огромная тень антропоморфной акулы."
    "Обернувшись, мы увидели владельца Био-Tech!"
    "Он здесь клиент? У него счёт в этом банке?"

    image animated_bank = Movie(play="videos/heartbeat.webm")
    show animated_bank behind katy_scary
    show katy_scary at right with moveinright:
        zoom 1.0
        yalign 1.0
        xalign 0.75

    katy "У него тут счёт?.."
    show john_standby_unsure at left with moveinleft:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    vana "В этом банке?.."

    "Я была в шоке."
    "Думала, у антропоморфных и людей разные банки..."
    "Либо исключение, либо..."
    "Не знаю, что и думать."

    stop music
    play sound "button_press.mp3"
    "Почему мы испугались?"
    "Во-первых - он создал проект по переносу сознания в сеть!"
    "Во-вторых - ходят слухи, что его окружение часто пропадает."
    "Что хищник может сделать с жертвой?"

    play music "null.mp3"
    show mary_standby_unclear at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    mary "Вань, быстрее забирай карту и уходим!"
    vana "Я уже через телефон оформляю!"
    "Ваня не терял времени - у него был смартфон последней модели."
    katy "Я слышала, он кого-то съел..."
    mary "Тебя?"
    vana "Меня?!"
    katy "Не смешно. Ты знаешь, о ком я. Давай уже!"
    "Катя была готова бежать."
    stop music
    play sound "iphone.mp3"
    "Вдруг у неё зазвонил телефон."
    stop sound
    hide katy_scary with moveoutright
    
    "И она выбежала. Повод нашёлся."
    "Я осталась с Ваней - не брошу друга."
    vana "Готово! Пошли."
    "Мы незаметно покинули банк."

    play sound "park.mp3" volume 0.3
    scene street with PushMove(1.0, "pushleft")
    "Краем глаза я взглянула на морду здоровяка."
    "Он не выглядел таким грозным, как о нём говорят."
    "Мы подошли к Кате - она уже улыбалась."
    show katy_standby_fine at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    katy "Фух! Молодцы, что быстро! И..." 
    katy "Нас пригласили на презентацию в Сейф-Сеть!"
    show mary_offer_smile at right with moveinright:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    mary "Как быстро ты переключаешься... Ладно..."
    "Я удивилась смене настроения. Будто ничего не было."
    "А должно ли было?"
    mary "Но это круто!"
    show john_standby_smile at left with moveinleft:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    vana "Вау! Это же отлично! Но... как нас нашли?"
    katy "Я оставляла заявку! Эта компания сотрудничает с нашим вузом."
    katy "Кажется, забыла вам сказать..."
    "Ваня обрадовался."
    "Мне было всё равно, но они молодцы."
    mary "Сейчас напомню себе..."
    katy "Надо готовиться."
    mary "Дали детали?"
    katy "Только адрес."
    vana "Тогда чего ждём?"
    "Мы пошли по адресу, чтобы оценить место."

    "Доехали на автобусе."
    "Здание было невысоким, но современным."
    "Стекло, гранитные ступени."

    scene office with fade
    play sound "office.mp3" volume 0.3
    "Компания оказалась серьёзнее, чем казалось."
    "В приёмной мы представились выпускниками, приглашёнными для проведения корпоратива."
    "Нас пропустили, лишь обыскав."
    show mary_unsure at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    mary "Пронесло..."
    show katy_standby_unsure at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    katy "Спасибо, что не контора-однодневка."
    "Катя толкнула меня плечом, идя вперёд."
    "Хоть и неуверенно..."

    show john_standby_smile at right with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    vana "Это же круто!"
    mary "Для тебя - да, а я бы что-нибудь взломала."
    "Фыркнула я, скрестив руки."
    "Когда Крей приезжает?"
    hide katy_standby_unsure
    show katy_standby_fine at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    katy "Как раз тебе сюда!"
    "Катя хихикнула, глядя на моё смятение."
    hide mary_unsure
    hide katy_standby_fine
    hide john_standby_smile
    "Мы вошли в кабинет."
    "Там нас ждал куратор..."

    show kirill_smile at center with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.5
    play music "Marcel_Pequel.mp3" volume 0.3
    kirill "Здравствуйте!"
    "Харизматично поприветствовал нас представитель."
    show john_hello_smile at left with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.25
    vana "Здравствуйте!"
    show katy_hello_smile at right with dissolve:
        zoom 1.0
        yalign 1.0
        xalign 0.75
    katy "Добрый день!"
    mary "Приветствую!"
    "Ответили мы почти хором."
    kirill "Я Кирилл, старший менеджер отдела разработки."
    kirill "Екатерина, я звонил вам, так как сотрудничал с вашим вузом и хочу, чтобы вы провели презентацию нашего нового продукта."
    kirill "Эта разработка изменит интернет!"
    katy "Для нас честь, учитывая, что мы вчера ещё были студентами!"
    "С энтузиазмом ответила Катя."
    kirill "Понимаю. Программа выступления почти готова - вам нужно лишь адаптировать её."
    mary "Без проблем!"
    "Я осматривала помещение."
    "Ничего особенного..."
    "Стоп!"
    "На ноутбуке был логотип Био-Tech!"
    play sound "smile.mp3"
    unknow "Конечно!"
    unknow "Думаете, я вас не взломаю? Зря."
    play sound "smile.mp3"
    kirill "Ах да... Бюджет за наш счёт, но постарайтесь минимизировать затраты."
    vana "Без проблем!"
    
    "Кирилл вручил нам документы."
    "Там было описание продукта и его комментарии."
    "Должно быть просто..."
    stop sound

    return