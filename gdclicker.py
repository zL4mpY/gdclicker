
# <---------------- IMPORTING LIBS ----------------->

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
import random, time

# <---------------- WINDOW ----------------->

window = Tk()
window.geometry('900x500')
window.config(bg='white')
window.resizable(width=False, height=False)
window.title("GD Clicker")

# <---------------- IMPORTANT VARIABLES ----------------->

bg_img = PhotoImage(file = 'bg.png')
coins = 0
current_multiplier = 1
autoclicker_coins_per_second = 0
roulette_time = 0
roulette_minutes = 0
roulette_seconds = 0
dev_code = '24082'
user_input_code = ''
level = 1
clicks = 0

# <---------------- SHOP WINDOW ----------------->

shop_window = Tk()
shop_window.geometry('600x400')
shop_window.title("Магазин")
shop_window.config(bg='white')
shop_window.withdraw()

# <---------------- HIDE WINDOW ----------------->

def shop_hide():
    shop_window.withdraw()

shop_window.protocol('WM_DELETE_WINDOW', shop_hide)

# <---------------- VARIABLES AND WIDGETS ----------------->

bg = Label(window, image = bg_img)
bg.pack()

level_label = Label(text='Уровень ' + str(level), font=('Arial, 24'))

global multiplier_cost
multiplier_cost = 250
multiplier_label = Label(shop_window, text='Умножитель x2', font=('Arial, 17'))
multiplier_label.place(x=5, y=100)

multiplier_cost_label = Label(shop_window, text=str(multiplier_cost) + ' монет', font=('Arial, 15'))
multiplier_cost_label.place(x=5, y=125)

multiplier_buy_btn = Button(shop_window, text='Купить!', font=('Arial, 17'), bg='white', borderwidth=0)
multiplier_buy_btn.place(x=400, y=100)

global autoclicker_cost
autoclicker_cost = 1000
autoclicker_label = Label(shop_window, text='Авто-кликер', font=('Arial, 17'))
autoclicker_label.place(x=5, y=200)

autoclicker_cost_label = Label(shop_window, text=str(autoclicker_cost) + ' монет', font=('Arial, 15'))
autoclicker_cost_label.place(x=5, y=225)

autoclicker_buy_btn = Button(shop_window, text='Купить!', font=('Arial, 17'), bg='white', borderwidth=0)
autoclicker_buy_btn.place(x=400, y=200)

# <---------------- AUTOCLICKER AND TIME ----------------->
 
def autoclick():
    global coins
    global autoclicker_coins_per_second
    coins += autoclicker_coins_per_second
    coins_label.configure(text='Coins: ' + str(coins))
    window.after(1000, autoclick)

def change_roulette_time():
    global roulette_time
    if roulette_time > 0:
        global roulette_minutes
        global roulette_seconds
        roulette_time -= 1
        roulette_minutes = roulette_time // 60
        roulette_seconds = roulette_time % 60
        window.after(1000, change_roulette_time)

# <---------------- ON CLICK ----------------->

def on_click():
    global window
    global coins
    global clicks
    global level
    global needed_clicks
    coins += 1 * current_multiplier
    clicks += 1
    
    if clicks == 100 and level == 1:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
    elif clicks == 250 and level == 2:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
    elif clicks == 500 and level == 3:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
    elif clicks == 1000 and level == 4:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
        showinfo('Награда', 'Вы получили 2500 монет.')
        coins += 2500
    elif clicks == 1500 and level == 5:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
    elif clicks == 3000 and level == 6:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
    elif clicks == 5000 and level == 7:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
    elif clicks == 7500 and level == 8:
        level += 1
        level_lavel.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
    elif clicks == 10000 and level == 9:
        level += 1
        level_label.configure(text='Уровень ' + str(level))
        showinfo('Уровень повышен!', 'Вы достигли уровня ' + str(level) + '!')
        showinfo('Награда', 'Вы получили 15000 монет.')
        coins += 15000
    
    coins_label.configure(text='Coins: ' + str(coins))

# <---------------- ENTERING SHOP ----------------->

def enter_shop():
    shop_window.deiconify()

    # <---------------- MULTIPLIER BUY SYSTEM ----------------->
    
    def multiplier_buy():
        global multiplier_cost
        global coins
        global current_multiplier

        # <---------------- LEVEL 1 (X2) ----------------->
        
        if coins - multiplier_cost >= 0 and current_multiplier == 1:
            coins -= multiplier_cost
            multiplier_cost = 500
            current_multiplier = 2
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_label.configure(text='Умножитель x2.5')
            multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')

        # <---------------- LEVEL 2 (X2.5) ----------------->
        
        elif coins - multiplier_cost >= 0 and current_multiplier == 2:
            coins -= multiplier_cost
            multiplier_cost = 750
            current_multiplier = 2.5
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_label.configure(text='Умножитель x4')
            multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')

        # <---------------- LEVEL 3 (X4) ----------------->
        
        elif coins - multiplier_cost >= 0 and current_multiplier == 2.5:
            coins -= multiplier_cost
            multiplier_cost = 1000
            current_multiplier = 4
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_label.configure(text='Умножитель x8')
            multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')

        # <---------------- LEVEL 4 (X8) ----------------->
        
        elif coins - multiplier_cost >= 0 and current_multiplier == 4:
            coins -= multiplier_cost
            multiplier_cost = 1500
            current_multiplier = 8
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_label.configure(text='Умножитель x16')
            multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')

        # <---------------- LEVEL 5 (X16) ----------------->
        
        elif coins - multiplier_cost >= 0 and current_multiplier == 8:
            coins -= multiplier_cost
            multiplier_cost = 2500
            current_multiplier = 16
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_label.configure(text='Умножитель x32')
            multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')

        # <---------------- LEVEL 6 (X32) ----------------->
        
        elif coins - multiplier_cost >= 0 and current_multiplier == 16:
            coins -= multiplier_cost
            multiplier_cost = 5000
            current_multiplier = 32
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_label.configure(text='Умножитель x64')
            multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')

        # <---------------- LEVEL 7 (X64) ----------------->
        
        elif coins - multiplier_cost >= 0 and current_multiplier == 32:
            coins -= multiplier_cost
            multiplier_cost = 7500
            current_multiplier = 64
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_label.configure(text='Умножитель x128')
            multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')

        # <---------------- LEVEL 8 (MAX) (X128) ----------------->
        
        elif coins - multiplier_cost >= 0 and current_multiplier == 64:
            coins -= multiplier_cost
            multiplier_cost = 10000
            current_multiplier = 128
            coins_label.configure(text='Coins: ' + str(coins))
            multiplier_buy_btn.place_forget()
            multiplier_label.configure(text='Умножитель (MAX)')
            multiplier_cost_label.configure(text='Вы имеете максимальный уровень этого предмета')

    # <---------------- AUTOCLICKER BUY SYSTEM ----------------->
    
    def autoclicker_buy():
        global autoclicker_cost
        global coins
        global autoclicker_coins_per_second

        # <---------------- LEVEL 1 ----------------->
        
        if coins - autoclicker_cost >= 0 and autoclicker_coins_per_second == 0:
            coins -= autoclicker_cost
            autoclicker_coins_per_second = 1
            autoclicker_cost = 1500
            coins_label.configure(text='Coins: ' + str(coins))
            autoclicker_label.configure(text='Автокликер v2')
            autoclicker_cost_label.configure(text=str(autoclicker_cost) + ' монет')
            autoclick()

        # <---------------- LEVEL 2 ----------------->
        
        elif coins - autoclicker_cost >= 0 and autoclicker_coins_per_second == 1:
            coins -= autoclicker_cost
            autoclicker_coins_per_second = 5
            autoclicker_cost = 2500
            coins_label.configure(text='Coins: ' + str(coins))
            autoclicker_label.configure(text='Автокликер v3')
            autoclicker_cost_label.configure(text=str(autoclicker_cost) + ' монет')

        # <---------------- LEVEL 3 ----------------->

        elif coins - autoclicker_cost >= 0 and autoclicker_coins_per_second == 5:
            coins -= autoclicker_cost
            autoclicker_coins_per_second = 10
            autoclicker_cost = 5000
            coins_label.configure(text='Coins: ' + str(coins))
            autoclicker_label.configure(text='Автокликер v4')
            autoclicker_cost_label.configure(text=str(autoclicker_cost) + ' монет')
        
        # <---------------- LEVEL 4 ----------------->
       
        elif coins - autoclicker_cost >= 0 and autoclicker_coins_per_second == 10:
            coins -= autoclicker_cost
            autoclicker_coins_per_second = 50
            autoclicker_cost = 15000
            coins_label.configure(text='Coins: ' + str(coins))
            autoclicker_label.configure(text='Автокликер v5')
            autoclicker_cost_label.configure(text=str(autoclicker_cost) + ' монет')

        # <---------------- LEVEL 5 (MAX) ----------------->
       
        elif coins - autoclicker_cost >= 0 and autoclicker_coins_per_second == 50:
            coins -= autoclicker_cost
            autoclicker_coins_per_second = 100
            autoclicker_cost = 15000
            coins_label.configure(text='Coins: ' + str(coins))
            autoclicker_buy_btn.place_forget()
            autoclicker_label.configure(text='Автокликер (MAX)')
            autoclicker_cost_label.configure(text='Вы уже имеете максимальный уровень этого предмета')
        
    multiplier_buy_btn.configure(command=multiplier_buy)
    autoclicker_buy_btn.configure(command=autoclicker_buy)
    
# <---------------- MAIN WINDOW WIDGETS ----------------->

change_roulette_time()

gameName_label = Label(text='GD Clicker', font=('Arial, 24'), bg='white')
gameName_label.place(x=365, y=0)

btn_img = PhotoImage(file = 'btn.png')
roulette_img = PhotoImage(file = 'roulette_icon.png')
shop_img = PhotoImage(file = 'shop_icon.png')

coins_label = Label(text='Coins: ' + str(coins), font=('Arial, 24'), bg='white')
coins_label.place(x=5, y=5)

click_btn = Button(text='Клик!', image = btn_img, font=('Arial, 20'), bg='white', fg='white', borderwidth=0, command=on_click)
click_btn.place(x=375, y=250)

shop_btn = Button(text='Магазин', image = shop_img, font=('Arial, 20'), bg='white', fg='white', borderwidth=0, command=enter_shop)
shop_btn.place(x=0, y=125)

level_label.place(x=870, y=475, anchor='e')

# <---------------- DEV MENU ----------------->



def dev_menu_open():

    dev_menu = Tk()
    dev_menu.geometry('400x400')
    dev_menu.config(bg='white')
    dev_menu.title("Меню разработчика")

    def add_coins():
        global coins
        coins += 10000
        coins_label.configure(text='Coins: ' + str(coins))

    def change_time():
        global roulette_time
        roulette_time = 0

    def add_levels():
        global level
        level += 1
        level_label.configure(text='Уровень ' + str(level))

    add_coins_btn = Button(dev_menu, text='Добавить 10000 монет', font=('Arial, 14'), command=add_coins)
    add_coins_btn.place(x=5, y=5)
    
    change_roulette_time_btn = Button(dev_menu, text='Обнулить время на рулетку', font=('Arial, 14'), command=change_time)
    change_roulette_time_btn.place(x=5, y=45)
    
    add_levels_btn = Button(dev_menu, text='Добавить уровень', font=('Arial, 14'), command=add_levels)
    add_levels_btn.place(x=5, y=85)

def goto_dev_menu():
    global user_input_code
    global dev_code
    user_input_code = askstring('Код', 'Введите код разработчика:')
    if user_input_code == dev_code:
        dev_menu_open()
    else:
        showinfo('Код', 'Неправильный код!')

dev_menu_btn = Button(text='Режим разработчика', font=('Arial, 12'), bg='white', fg='white', borderwidth=0, command=goto_dev_menu)
dev_menu_btn.place(x=900, y=16, anchor='e')

# <---------------- ROULETTE MENU ----------------->

def roulette_menu_open():
    
    roulette_menu = Tk()
    roulette_menu.geometry('500x500')
    roulette_menu.config(bg='white')
    roulette_menu.title("Рулетка")
    
    roulette_rewards = ['1000 монет', '250 монет', 'Авто-кликер v1', 'Умножитель x2']
    reward = random.choice(roulette_rewards)
    reward_label = Label(roulette_menu, text=reward, font=('Arial, 18'), bg='white')
    reward_label.place(x=250, y=175, anchor='center')

    roulette_label = Label(roulette_menu, text='Рулетка', font=('Arial, 35'), bg='white')
    roulette_label.place(x=250, y=25, anchor='center')
    
    roulette_btn = Button(roulette_menu, text='Крутить', font=('Arial, 20'), bg='white', borderwidth=0)
    roulette_btn.place(x=250, y=250, anchor='center')

    def roll_roulette():
        global roulette_time
        if roulette_time == 0:
            roulette_menu.after(1000)
            
            for i in range(50):
                reward = random.choice(roulette_rewards)
            roulette_menu.after(1500)
            
            global coins
            global multiplier_cost
            global current_multiplier
            global autoclicker_cost
            global autoclicker_coins_per_second
            
            if reward == '1000 монет':
                coins += 1000
                coins_label.configure(text='Coins: ' + str(coins))
            elif reward == '250 монет':
                coins += 250
                coins_label.configure(text='Coins: ' + str(coins))
            elif reward == 'Авто-кликер v1':
                autoclicker_coins_per_second = 1
                autoclicker_cost = 1500
                autoclicker_label.configure(text='Автокликер v2')
                autoclicker_cost_label.configure(text=str(autoclicker_cost) + ' монет')
                autoclick()
            elif reward == 'Умножитель x2' and current_multiplier < 2:
                multiplier_cost = 500
                current_multiplier = 2
                multiplier_label.configure(text='Умножитель x2.5')
                multiplier_cost_label.configure(text=str(multiplier_cost) + ' монет')
            reward_label.configure(text='Вы выиграли ' + reward + '!')
            roulette_time = 300
            change_roulette_time()
    
    def change_txt():
        global roulette_time
        if roulette_time == 0:
            reward_label.configure(text='Крутим...')
            roulette_menu.update()
            roll_roulette()
        else:
            showinfo(title="Рулетка", message="Вы уже крутили рулетку, подождите " + str(roulette_minutes) + ' минут и ' + str(roulette_seconds) + ' секунд.')
            
    
    roulette_btn.configure(command=change_txt)
roulette_menu_btn = Button(text='Рулетка', image = roulette_img, font=('Arial, 20'), bg='white', fg='white', borderwidth=0, command=roulette_menu_open)
roulette_menu_btn.place(x=0, y=300)

window.mainloop()
