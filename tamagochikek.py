import math

DecreChar = 0.03 #Уменьшение характеристик каждый ход
DecreType = 0.05 #Уменьшение характеристик в зависимости от типа питомца

#Объявление класса Tpet. В нем прописываются все характеристики питомца
def GameStart():
    class Tpet():
        def __init__(self,type,name):
            self.type = type
            self.name = name
            self.photo = ''
            self.thirst = 0.8 + DecreChar
            self.weight = 0.8 + DecreChar
            self.happiness = 0.8 + DecreChar
            self.tualet = 0.8 + DecreChar
            self.years = 1
            self.game = True


        #Функции food, water и play отвечают за алгоритмы кормления, подачи воды и игры с питомцем соответственно.
        #Переменные изменяются в зависимости от заданных параметров, если их значения соответствуют условиям.
        def food(self):
            if (pet.weight < 10.00) and (pet.weight > 0):
                if 10-pet.weight < 9.85 :
                    pet.weight = pet.weight+0.25
                    pet.thirst = pet.thirst-0.06
                    print('свежее мясо:3')
                else:
                    pet.weight = (10-pet.weight)
            else: print('кд')

        def water(self):
            if (pet.thirst < 10.00) and (pet.thirst >0):
                if (10-pet.thirst)< 9.85:
                    pet.thirst=pet.thirst+0.25
                    pet.weight=pet.weight - 0.07
                    pet.tualet=pet.tualet - 0.10
                    print('my water rise')
                else:
                    pet.thirst=(10-pet.thirst)
            else: print('my water не хочет rise')

        def play(self):
            if (pet.happiness < 10.00) and (pet.happiness > 0):
                if (10-pet.happiness) < 9.85:
                    pet.happiness = pet.happiness + 0.25
                    pet.thirst = pet.thirst - 0.07
                    pet.weight = pet.weight - 0.06
                    print('регай')
                else:
                    pet.happiness = (10-pet.happiness)
            else: print(pet.name, 'сорри пинг ребята')
        def tualet(self):
            if (pet.tualet < 10.00) and (pet.tualet > 0):
                if (10-pet.tualet) < 9.85:
                    pet.tualet = pet.tualet + 0.25
                    pet.water = pet.water - 0.03
                    pet.weight = pet.weight - 0.03


        #Функция ignore отвечает за действие "игнорировать". Все переменные остаются равны сами себе.
        def ignore(self):
            pet.weight = pet.weight
            pet.thirst = pet.thirst
            pet.happiness = pet.happiness
            pet.tualet = pet.tualet

        #Функция окончания игры. При ее выполнении игровая сессия (питомец) перестает существовать.
        def LeaveGame(self):
            print('')
            print('ггвп')
            print('')
            pet.game = False

    #Функция, отвечающая за логику меню взаимодействий с питомцем.
    def ChooseAction(action):
            if action == '1':
                pet.food()
            elif action == '2':
                pet.water()
            elif action == '3':
                pet.play()
            elif action == '4':
                pet.tualet()
            elif action == '5':
                pet.ignore()
            elif action == '6':
                pet.LeaveGame()
            else: print('ты миссанул по клавише')

    #Здесь переменная name принимает значение из введенного в консоль текста, после чего запускается цикл выбора типа питомца.
    #Цикл не будет завершен, пока не будет выбран корректный тип и переменная check не примет значение True
    print('Выберите имя своему питомцу:')
    name = input()
    print('')
    check = False

    while check == False:
            print('Выберите тип питомца: 1:ликантроп 2:кот 3:герман')
            type = input()
            pet = Tpet(type,name)
            if type == '1':
                photo = '(V._.V)'
                check = True
            elif type == '2':
                    photo = '(^._.^)'
                    check = True
            elif type == '3':
                    photo = '<:3 )~'
                    check = True
            else: print('ты че тупой?')
            print('')

    pet = Tpet(type,name)
    pet.photo = photo

    #Здесь задаются стартовые значения возраста, голода, жажды и счастья
    pet.years=1
    pet.thirst=8.00 + DecreChar
    pet.weight=8.00 + DecreChar
    pet.happiness=8.00 + DecreChar
    pet.tualet=8.00 + DecreChar


    #Жизнь питомца построена на этом цикле. Если игровая сессия запущена, ни одна характеристика не равна нулю, а возраст
    #питомца не превышает 13 лет - то цикл срабатывает, увеличивая возраст и уменьшая характеристики.
    #В зависимости от типа питомца будут так же уменьшаться определенные характеристики.
    while (pet.game == True) and ((pet.weight > 0) and (pet.thirst > 0) and(pet.happiness > 0)and (pet.years < 13) and (pet.tualet > 0)):
        age = pet.years + 0.05
        pet.years = math.trunc(age)
        pet.weight = pet.weight - DecreChar
        pet.thirst = pet.thirst - DecreChar
        pet.happiness = pet.happiness - DecreChar
        pet.tualet = pet.tualet - DecreChar

        if pet.type == '1':
            pet.happiness = pet.happiness-DecreType
        elif pet.type == '2':
            pet.thirst = pet.thirst-DecreType
        elif pet.type == '3':
            pet.tualet - pet.tualet - DecreType
        else: pet.weight = pet.weight-DecreType


        #Здесь задается внешний вид меню взаимодействия с питомцем в консоли
        print('-----------------------------------')
        print('')
        print(pet.photo)
        print('')
        print('-----------------------------------')
        print('| возраст | вес | жажда | счастье | туалет |')
        print('-----------------------------------')
        print('|  ', round(pet.years,2),'| ', round(pet.weight,2),' | ', round(pet.thirst,2),' | ', round(pet.happiness,2),' |', round(pet.tualet,2),'|',)
        print('-----------------------------------')
        print('')
        print('Выберите действие: 1: Есть 2: Пить воду 3: Играть с ',pet.name,'4: туалет 5: Игнорировать 6: Остановить игру.')
        action=input()
        ChooseAction(action)
        print('')

    #Если питомец достигнет 13 лет или одна из его характеристик станет ниже нуля - он умрет.
    if (pet.weight <= 0) or (pet.thirst<=0) or (pet.happiness<=0) or (pet.years>=13) or (pet.tualet<=0):
        print(pet.name,' мертв.......')

    print('')

#В этой функции задается вывод инструкции к игре через консоль
def Instructions():
    print('--------------------------------------------------------------------------------------')
    print('')
    print('Инструкция: ')
    print('')
    print(' + Сначала вы должны создать животное, вы должны выбрать имя и какого именно питомца вы хотите')
    print(' Вы можете выбрать между собакой, кошкой или крысой.')
    print('')
    print(' + После вы несете ответственность за жизнь своего питомца, для этого вы должны его кормить,')
    print(' поить и играть с ним.')
    print('')
    print(' + Обратите внимание, что каждое ваше действие изменяет статистику')
    print(' ваш питомец, когда вы его кормите, будет набирать вес, но будет больше пить, когда')
    print(' будете поить - будет более голодным, если вы с ним поиграете, то будет более голодным и жаждущим.')
    print('')
    print(' + Помните, что если вы игнорируете своего питомца, все его характеристики будут снижаться каждый ход.')
    print('')
    print(' + Если вы опустите любую из характеристик до 0, ваш питомец умрет.')
    print('')
    print(' + У каждого вида питомцев есть особые потребности, собаке требуется больше времени для игр,')
    print('Кошке нужно чаще пить воду, а крысе нужно больше есть.')
    print('')
    print('--------------------------------------------------------------------------------------')
    print('+ в туалет ходи')

#В этой функции прописаны логика и вывод в консоль главного меню игры
def MenuStart():
    print('')
    print('Добро пожаловать!')
    menu = False
    while not menu:
        print('Выберите вариант 1:Играть 2:Инструкция 3:Выйти.')
        option = input()
        if option == '1':
            GameStart()
        elif option == '2':
            Instructions()
        elif option =='3':
            menu = True
        else: print('Введите доступный вариант.')

#Запуск функции, отвечающей за главное меню, после чего игра начинается.
MenuStart()