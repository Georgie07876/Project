# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define ch = Character('Щербаков', color="#c8ffc8", image = 'cherbakov')
define va = Character('Вадим', color="#023a8c", image = 'vadim')
define v= Character('Вероника', color="#b52b46", image = 'veronika')
define nn = Character('Неизвестный голос', color = "#e2c900")
define nn2 = Character('Низкий голос', color = "#e2c900")
define ne = Character('Некто', color = "#e2c900")
define ao = Character('Алексей Олегович', color="#2bca55")
define en = Character('Екатерина Николаевна', color="#2bca55")

# Музыка и звуки
define audio.musnormal = "music/stan.ogg"
define audio.muss = "audio/step.ogg"
define audio.musss = "audio/onestep.ogg"
define audio.musk = "audio/klav.ogg"
define audio.musm = "audio/murch.ogg"
define audio.musfear = "music/fear.ogg"
define audio.mudver = "audio/dver.ogg"
define audio.mubus = "audio/abobus.ogg"
define audio.muffice = "music/office.ogg"


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    $ right2 = Position(xalign = 0.7, yalign = -0.7)
    $ right3 = Position(xalign = 1.0, yalign = -0.7)
    $ left2 = Position(xalign = 0.1, yalign = -0.7)
    $ left2 = Position(xalign = 0.3, yalign = -0.7)
    $ ml = Position(xaling = 0.9, yaling = 0.1)
    $ ml2 = Position(xalign = 0.5, yalign = -0.7)
# Игра начинается здесь:
label start:

    scene bg black
    stop music
    "....."

    nn "-эй, проснись, ну же, он идёт сюда...."

    play music musfear
    play sound muss

    v "“Кто идёт, куда идёт ? Стоп, кто это вообще ?“"


    scene bg clas
    with fade

    show veronika emo at left2
    with dissolve

    v "!!!!!"

    show cherbakov2 at right2
    with easeinright

    ch " -Вероника, с вами всё в порядке ? {w} Неважно себя чувствуете ? "

    v standart  " Да……нет….всё в порядке…"
    "“КТО ЭТО И КУДА Я ПОПАЛА ?!?!?!“"

    stop music fadeout 5
    stop sound fadeout 2
    ch "-Тогда спешу пожелать доброго утра. {w} Давайте решим задачку вместе, читайте
     условие."
    v "...Хорошо."

    hide veronika
    with dissolve
    hide cherbakov
    with dissolve
    #сдесь будет задача


    scene bg clas
    with fade

    show cherbakov3 at right2
    with dissolve

    show veronika standart at left2
    with dissolve

    play sound musk
    ch "-Могу вас поздравить, вы совершаете первые успехи ! {w}Так, давайте перейдём к
     следующем заданию..."
    v "....."
    play sound musm
    "“Что это  ? Похоже на звонок“ "
    ch "Ладно, разберём в другой раз, группа, можете быть свободны."
    hide cherbakov3
    with dissolve
    "*Нужно поскорее покинуть этот кабинет*"

    play sound muss 

    hide veronika with moveoutright

    scene bg corridor
    with wipeleft
    stop sound fadeout 1
    "Выйдя из кабинета я словно попала в лабиринт. {w}Продолговатый коридор с кучей дверей, в
    конце находиться выход, туда мне наверное и следует пойти чтобы выбраться.   "
    "Я уж было собралась идти на встречу свободе, как вдруг..."

    show vadim small at ml
    with dissolve

    nn2 " я тебя повсюду ищу, вот ты где !"

    hide vadim small
    with dissolve

    "Я поняла, что это обращение было адресовано мне, {w} Ведь из кабинета я вылетела первой,
    а в коридоре не было никого."
    play sound muss 
    stop sound fadeout 2

    show vadim1 at ml2
    with dissolve

    "Обернувшись, я заметила, что в мою сторону идет высокий, черноволосый парень одетый
по всем стандартам официального стиля (брюки, заправленная белая рубашка, галстук. {w}
И судя по его прожигающему взгляду он идёт ко мне.."
    stop sound fadeout 1

    ne " Вероника, у тебя что-то случилось? {w}Почему ты н ходишь на пары? {w}
    Начинать обучение с такого большого количества пропусков- не самая хорошая затея."

    menu:
        "что же делать ?"
        "Промолчать":
            jump say1

        "Спросить, кто он ?":
            jump say2
label say1:
    v "....."

    va "Можно было бы и поздароваться ввиду столько долго отсутствия..."
label say2:
    v "-Что? Мы знакомы ?"
    ne " - Я конено понимаю, что ты у нас не частый гость, но своего старосту могла бы и
запомнить.."

    hide vadim1

    show vadim2 at ml2
    ne "Ладно, проехали, меня зовут Вадим.{w} Если не возражаешь, мы продолжим этот разговор в
арке, хочется подышать свежим воздухом. "

    va " -Следуй за мной."
    play sound muss
    hide vadim2
    with dissolve

    scene bg street
    with dissolve
    play music musnormal

    show vadim1 at right2
    with dissolve

    play music musnormal

    va "-Ну так планируешь ходить на пары?   "

    show veronika sad at left2
    with dissolve

    menu:
        "Спросить о парах ? "
        "да":
            jump quest1
        "нет":
            jump quest2
label quest1:
    v "-Ээээ… Пары?"

    va "- Ахах, ну да, в институте пары. {w}Это как уроки в школе только длятся 1 час 30 минут "

    v " - Ого. Как вы столько времени на них сидите? "

    va "-  Ну вообще-то не вы, а мы. {w} Тебе так то тоже следовало бы их посещать… "

    v "-“Ничего не понятно, но нужно узнать где я и как мне попасть домой. Все будто сошли с
ума. Может это какой-то большой розыгрыш?”  "
label quest2:
    v "- А где мы сейчас вообще? "

    va "- Ну, мы учимся в РИНХе на факультете КТиИБ.{w} Ты меня пугаешь.{w}Ты будто с луны
свалилась. "

    v "- Что такое КТиИБ? Это какой-то шифр? "

    va "- Сокращённое название факультета компьютерных технологий и информационной
безопасности."
    va "На нашем факультете есть несколько направлений: Прикладная
информатика, прикладная математика и информатика, программная инженерия,
информационные системы и технологии, бизнес информатика, фундаментальная
информатика и информационная безопасность."

    v "  - А что у нас сейчас была за пара ?"

    va " - Информационная безопасность  "

    show serov at right3
    play sound muss
    "....."
    hide serov with moveoutleft

    "'Хм, какие-то они тут все странные. {w}Кажется, нужно скорее уходить отсюда.'"

    va "-Пойдем на следующую пару? "

    v "В:-Нет, я пожалуй домой. Подскажешь как мне туда доехать? "

    va "-Мы можем поехать вместе, но для начала нужно сходить на пару. "

    "'Ну, вариантов у меня не много. Придется идти на пару'"
    stop music fadeout 4

    v "Ладно, пошли. "

    hide vadim1 with moveoutright
    hide veronika with moveoutright
#здесь работа филиппа с моими корректировками
#
#
label parttwo:
    scene bg clas2

    show veronika standart at left2
    with moveinleft
    show vadim3 at right2
    with moveinleft


    va "Давай сядем на первую парту? Мне очень нравится это предмет, тут правда очень интересно."
    v "Хорошо."

    hide veronika
    with dissolve

    hide vadim3
    with dissolve
    "Не могу поверить. {w} Я сижу за первой партой. {w}Сегодня действительно самый странный день в моей жизни. Слишком много новых ощущений."
    play sound muss
    show serov at right2
    with moveinleft
    ao "Всем привет, есть какие-то вопросы по прошлой лабораторной?"
    v  "Кто это? Преподаватель?"
    va "Да, это Алексей Олегович."
    ao "Вадим, а кто твоя подружка? У вас новенькая в группе?"

    play music muffice
    show veronika standart at left2
    with dissolve
    show vadim2 at right3
    with dissolve

    va "Не совсем, это Вероника."
    ao "А, ничего себе, быстро вы Вероника сдались.{w} Я уже делал ставки, что вы не придёте до сессии.{w} Эх... теперь я должен кофе Сергею Михайловичу. Подводите!"
    ao "Ну раз пришла, тогда может решишь задачку?"
    v "Я? Не...нет... я же ничего не знаю."
    ao "Я помогу если будет нужно, но я уверен, что ты справишься и без моей помощи."
    hide vadim2
    with dissolve
    hide veronika
    with dissolve
    hide serov
    with dissolve
#ЗАДАЧКА


    show serov at right2
    with dissolve
    ao "Ну вот. Видишь, ты сама все сделала. Больше боялась.{w} Ходи на пары почаще, и из тебя выйдет не плохой программист"
    ao "Кстати, сегодня в 15:00 будет встреча КВА. Вы пойдёте?"

    show veronika standart at left2
    with dissolve
    v  "КВ..... {w}что?"
    ao "КВА"
    v  "Вадим, почему это преподаватель квакает и претворяется лягушкой? Вам не кажется это странным?"
    '"Вадим засмеялся"'
    ao "Вероника, судя по вашему лицу и реакции Вадима, вы не в курсе, что такое КВА. {w} Это клуб нашего факультета.{w} Мы проводим различные мероприятия. {w}Например, недавно к нам приходил тимлид одной из лучший web-студий города и рассказывал о том, как начать свою карьеру уже сейчас."
    show vadim1 at right3
    with dissolve
    va "Да, я уже даже начал следовать советам и думаю летом попробовать устроиться к ним в команду."
    ao "Кстати, Вадим, если будут вопросы по программированию, ты всегда можешь написать мне в ВК, я обычно быстро отвечаю."
#Звонок
    play sound musm

    scene bg hall2
    with wipeleft
    show vadim2 at left2
    with dissolve
    va "Идёшь на последнюю пару?"
    v  "Будто у меня есть выбор…"
    v  "Хоть скажи что за пара."
    va "Прикладная информатикa."
    v  "А что мы там будем делать?"
    va "Учить различные языки."
    v  "Вау, даже Французский?"
    va "Ахахах…ты не дала мне договорить! {w} Языки программирования, например Python, C++, Java и многие другие."

    hide vadim3
    with dissolve
    stop music
#######################
    scene bg clas3
    with wiperight
    show veronika standart at left2
    with moveinleft
    show vadim3 at right2
    with moveinleft
    va "Тут лучше сесть на последнюю парту."
    v  "Ого, я уже думала, что ты тот самый отличник. {w} Кстати, ты случайно не носишь очки?"
    va "Не нужно из меня делать зануду. {w} Та пара действительно была интересной. {w} Эта тоже, но сейчас поймёшь почему мы сели на последнюю парту."

    hide veronika standart
    with dissolve
    hide vadim3
    with dissolve


    show lozina3 at right2
    with moveinleft
    play sound mudver
    en "Здравствуйте ребята."
    hide lozina3

    play sound musss
    show lozina1 at right2
    en "Вы все прошли опрос, который я попросила Вадима сбросить вам в беседу?"
    en "Рита, ты прошла опрос?"
    "Рита опускает глаза вниз"
    en "Неужели так сложно выполнить мою маленькую просьбу?"
    va "Теперь поняла почему мы сели подальше?"
    v  "Ахаха, да."
    hide lozina1
    show lozina2 at right2
    en "Кстати, на следующей неделе у нас будет особое мероприятие, посвященное первокурсникам. {w} Я вас всех на него приглашаю. {w} Советую сходить, там будет очень интересно."
    va "Я пойду туда. {w} Не хочешь со мной?"
    v "Не знаю точно, очень хочется домой а не на мероприятие."
    va "Ты так дома всю свою жизнь просидишь. Пошли на мероприятие, там будет круто!"
    v  "Ладно…"
    en "Ребят, я подготовила для вас очень интересное задние."
    hide lozina2
#Задание
    show lozina3 at right2
    en "Вы все молодцы, хорошо постарались. {w} Пара окончена, вы можете быть свободны."
    scene bg hall
    with wipeleft
    show veronika standart at left2
    with moveinleft
    show vadim1 at right2
    with moveinleft
    va "Ну что, поехали в общагу ?"
    v  "Зачем? Мы же собирались домой."
    hide vadim1
    show vadim2 at right2
    va "Можешь конечно поехать домой, но мне кажется, ты тогда не успеешь завтра на пары. {w} Кататься с твоего города в Ростов каждое утро не самая хорошая идея."
    scene bg under
    with fade
    v  "Мы в Ростове?"
    va "Да, ты вправду какая-то странная. {w} Ладно, Лунтик, пошли уже на остановку."
    v  "О боже мой. {w} Ты тоже живёшь в общежитии?"
    va "Да. Ты же уже познакомилась со своими соседями?"
    v  "Ты про тараканов?"
    va "Ну, они конечно очень дружелюбные существа, но нет, я про соседей."
    v  "Я ни разу ещё не была в общежитии"
    va "Ого, тогда я проведу тебе экскурсию. {w} Кстати заходи ко мне вечером на чай"
    v  "Хорошо, спасибо Вадим."
    scene bg black
    with fade
    play sound mubus
    '.....'
    '.....'
    '...'
    '....'
#ПРЕДЛАГАЮ ТУТ ЗАКОНЧИТЬ ПОКА ЧТО.

    return
