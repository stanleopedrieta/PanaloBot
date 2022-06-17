import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from tkinter import *
from tkinter import ttk
import threading
import sys
from PIL import ImageTk
from ctypes import windll
import os
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

root = Tk()
root.overrideredirect(True)
root.configure(bg='black')

mainuser = ""
only20ptable = False
mainframe = Frame(root, background="#0f0f0f")
secondframe = Frame(root)
thirdframe = Frame(root)
fourthframe = Frame(root)
fifthframe = Frame(root)
sixthframe = Frame(root)
gameframe = Frame(root)
get_initial = True


WIDTH, HEIGHT = 377, 530
root.geometry('{}x{}'.format(WIDTH, HEIGHT+41))
upimage = PhotoImage(file=".\\assets\\up.png")
downimage = PhotoImage(file=".\\assets\\down.png")
onimage = PhotoImage(file=".\\assets\\on.png")
offimage = PhotoImage(file=".\\assets\\off.png")
loginimage = PhotoImage(file=".\\assets\\login.png")
nextimage = PhotoImage(file=".\\assets\\next.png")
backimage = PhotoImage(file=".\\assets\\back.png")
back2image = PhotoImage(file=".\\assets\\back2.png")
casinoimage = PhotoImage(file=".\\assets\\888.png")
startimage = PhotoImage(file=".\\assets\\start.png")
stopimage = PhotoImage(file=".\\assets\\stop.png")
logo = PhotoImage(file=".\\assets\\roulette.png")
icon = PhotoImage(file=".\\assets\\icon.png")
num0image = PhotoImage(file=".\\assets\\0.png")
num1image = PhotoImage(file=".\\assets\\1.png")
num2image = PhotoImage(file=".\\assets\\2.png")
num3image = PhotoImage(file=".\\assets\\3.png")
num4image = PhotoImage(file=".\\assets\\4.png")
num5image = PhotoImage(file=".\\assets\\5.png")
num6image = PhotoImage(file=".\\assets\\6.png")
num7image = PhotoImage(file=".\\assets\\7.png")
num8image = PhotoImage(file=".\\assets\\8.png")
num9image = PhotoImage(file=".\\assets\\9.png")
num10image = PhotoImage(file=".\\assets\\10.png")
num11image = PhotoImage(file=".\\assets\\11.png")
num12image = PhotoImage(file=".\\assets\\12.png")
num13image = PhotoImage(file=".\\assets\\13.png")
num14image = PhotoImage(file=".\\assets\\14.png")
num15image = PhotoImage(file=".\\assets\\15.png")
num16image = PhotoImage(file=".\\assets\\16.png")
num17image = PhotoImage(file=".\\assets\\17.png")
num18image = PhotoImage(file=".\\assets\\18.png")
num19image = PhotoImage(file=".\\assets\\19.png")
num20image = PhotoImage(file=".\\assets\\20.png")
num21image = PhotoImage(file=".\\assets\\21.png")
num22image = PhotoImage(file=".\\assets\\22.png")
num23image = PhotoImage(file=".\\assets\\23.png")
num24image = PhotoImage(file=".\\assets\\24.png")
num25image = PhotoImage(file=".\\assets\\25.png")
num26image = PhotoImage(file=".\\assets\\26.png")
num27image = PhotoImage(file=".\\assets\\27.png")
num28image = PhotoImage(file=".\\assets\\28.png")
num29image = PhotoImage(file=".\\assets\\29.png")
num30image = PhotoImage(file=".\\assets\\30.png")
num31image = PhotoImage(file=".\\assets\\31.png")
num32image = PhotoImage(file=".\\assets\\32.png")
num33image = PhotoImage(file=".\\assets\\33.png")
num34image = PhotoImage(file=".\\assets\\34.png")
num35image = PhotoImage(file=".\\assets\\35.png")
num36image = PhotoImage(file=".\\assets\\36.png")


GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080


def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())

root.after(10, lambda: set_appwindow(root))
root.title("Panalo Bot")
root.wm_iconphoto(False, icon)



def move_app(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")

def quitter():
    root.quit()

dozvalue = 0
outsidevalue = 0
alternatingvalue = 0
gambitvalue = 0
coldozwait_variable = StringVar(root)
coldozwait_variable.set("8")
alternating_variable = StringVar(root)
alternating_variable.set("13")
outwait_variable = StringVar(root)
outwait_variable.set("13")
mart_var = StringVar(root)
mart_var.set("3")

# Driver variables
t = threading.Thread()
driver = webdriver

chip = "0.2"
usr = ""
passwd = ""
out_wait = 0
alt_wait = 0
col_wait = 0
out_wait_temp = 0
alt_wait_temp = 0
col_wait_temp = 0
martingale_count = 0
max_limit = 0.00
min_limit = 0.00
out_betpattern = []
col_betpattern = []
alt_betpattern = []
toexit = False
minmoney = StringVar(root)
maxmoney = StringVar(root)
minmoney.set("10.00")
maxmoney.set("5.00")
lose_count = 0
win_count = 0

# Pattern Variables
redlist = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacklist = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
small_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
big_list = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
even_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
firstdoz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seconddoz = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
thirddoz = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
firstcol = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
secondcol = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
thirdcol = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
blackcount = 0
redcount = 0
oddcount = 0
evencount = 0
smallcount = 0
bigcount = 0
firstdozcount = 0
seconddozcount = 0
thirddozcount = 0
firstcolcount = 0
secondcolcount = 0
thirdcolcount = 0

blackredcount = 0
redblackcount = 0
oddevencount = 0
evenoddcount = 0
smallbigcount = 0
bigsmallcount = 0

# Table Data Variables

table = []

table_name = ""

table_from_db = None
table_names20 = ["Who Wants To Be a Millionaire? Roulette",
                 "Mega Fire Blaze Roulette Live",
                 "Quantum Roulette Live",
                 "American Roulette",
                 "Prime Slingshot",
                 "Spread Bet Roulette",
                 "Quantum Auto Roulette",
                 "Greek Quantum Roulette",
                 "Quantum Roulette Italiana",
                 "Speed Auto Roulette",
                 "Auto Roulette",
                 ]
table_names50 = ["Roulette",
                 "Speed Roulette",
                 "UK Roulette",
                 "Deutsches Roulette",
                 "Turkish Roulette",
                 "Roleta Brasileira",
                 "Triumph Roulette",
                 "Football Roulette",
                 "Hindi Roulette",
                 "Greek Roulette"
                 ]
table_names1 = ["Prestige Roulette",
                "Roulette Italiana",
                "Slingshot",
                "888sport Roulette"
                ]
back_table_names20 = None
back_table_names50 = None
back_table_names1 = None
table_links = {}

# Other variables
chip_position = 3
name = ""
goback = False
new_roulette_link = ""
starttime = datetime.datetime.now()
temp_balance = 0

def start():
    global toexit, bet0_variable, get_initial, min_limit, max_limit
    global mainuser
    print(mainuser)

    toexit = False
    get_initial = True
    max_limit = float(maxmoney.get())
    min_limit = float(minmoney.get())
    try:
        gameframe.destroy()
    except:
        pass
    game()


def game():

    global table_from_db, table_names20, table_names50, table_names1, table_links, win_count, lose_count, close_label
    global col_wait_temp, alt_wait_temp, out_wait_temp

    global gameframe, col_wait, out_wait, alt_wait, alt_betpattern, col_betpattern, out_betpattern, t
    global startbutton, stopbutton, backbutton
    fifthframe.destroy()

    gameframe = Frame(root)
    gameframe.pack()

    canvas = Canvas(gameframe, width=WIDTH, height=HEIGHT, highlightthickness=1, highlightbackground="#0f0f0f")
    canvas.pack()

    img = ImageTk.PhotoImage(file=".\\assets\\bg6.png")
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)

    global win_count_label
    win_count_label = Label(gameframe, text="Win: " + str(win_count), font=("Sansation", 18, "bold"), fg="white",
                            bg="#00cfaa")
    win_count_label_window = canvas.create_window(109, 321, window=win_count_label)

    global lose_count_label
    lose_count_label = Label(gameframe, text="Loss: " + str(lose_count), font=("Sansation", 18, "bold"), fg="white",
                             bg="#ea5324")
    lose_count_label_window = canvas.create_window(274, 321, window=lose_count_label)

    def ending():
        global toexit
        available_label["text"] = "Please wait for program to exit"
        #available_label["text"] = "Por favor, aguarde o programa sair"
        toexit = True
        available_label["text"] = ""

    stopbutton = Button(gameframe, command=ending, image=stopimage, state="normal", bg="#ea5324",
                        activebackground="#ea5324", bd=0)
    stopbutton_window = canvas.create_window(232, 440, anchor=NW, window=stopbutton)

    backbutton = Button(gameframe, command=fifthwindow, image=back2image, state="disabled", bg="#00b6cf",
                        activebackground="#00b6cf", bd=0)
    backbutton_window = canvas.create_window(60, 440, anchor=NW, window=backbutton)



    stopbutton["state"] = "normal"
    backbutton["state"] = "disabled"
    close_label["state"] = "disabled"
    global available_label

    available_label = Label(gameframe, text="", font=("Sansation", 11), fg="white", bg="#0f0f0f")
    available_label_window = canvas.create_window(190, 370, window=available_label)

    global min_limit, max_limit, minset_money, maxset_money

    minset_money = Label(gameframe, text="$ ", font=("Sansation", 9, "bold"), fg="white", bg="#00b6cf", pady=0)
    minset_money_window = canvas.create_window(240, 218, window=minset_money, anchor=W)

    maxset_money = Label(gameframe, text="$ ", font=("Sansation", 9, "bold"), fg="white", bg="#00cfaa", pady=0)
    maxset_moneyl_window = canvas.create_window(240, 242, window=maxset_money, anchor=W)

    global status_label
    status_label = Label(gameframe, text="", fg="white", bg="#0f0f0f", font=("Sensation", 10))
    status_label_window = canvas.create_window(190, 515, window=status_label)

    if coldozwait_variable.get() == "-":
        col_wait = 100
    else:
        col_wait = int(coldozwait_variable.get())
    if outwait_variable.get() == "-":
        out_wait = 100
    else:
        out_wait = int(outwait_variable.get())
    if alternating_variable.get() == "-":
        alt_wait = 100
    else:
        alt_wait = int(alternating_variable.get())

    out_betpattern = []
    col_betpattern = []
    alt_betpattern = []

    for t in range(alt_wait):
        alt_betpattern.insert(len(alt_betpattern), 0)

    z = 1
    for i in range(martingale_count):
        alt_betpattern.insert(len(alt_betpattern), z)
        z *= 2

    for t in range(out_wait):
        out_betpattern.insert(len(out_betpattern), 0)

    z = 1
    for i in range(martingale_count):
        out_betpattern.insert(len(out_betpattern), z)
        z *= 2

    for t in range(col_wait):
        col_betpattern.insert(len(col_betpattern), 0)

    z = 1
    for i in range(martingale_count):
        col_betpattern.insert(len(col_betpattern), z)
        z *= 3

    for i in range(20):
        out_betpattern.insert(len(out_betpattern), 0)
        col_betpattern.insert(len(col_betpattern), 0)
        alt_betpattern.insert(len(alt_betpattern), 0)

    if out_wait <= 11:
        out_wait_temp = out_wait - 1
    elif out_wait <= 12:
        out_wait_temp = out_wait - 2
    else:
        out_wait_temp = out_wait - 3

    if alt_wait <= 11:
        alt_wait_temp = alt_wait - 1
    elif alt_wait <= 12:
        alt_wait_temp = alt_wait - 2
    else:
        alt_wait_temp = alt_wait - 3

    if col_wait <= 11:
        col_wait_temp = col_wait - 1
    else:
        col_wait_temp = col_wait - 2


    global usr, passwd
    with open(".\\assets\\login.txt", "w") as file:
        file.write(usr + "," + passwd)
    t = threading.Thread(target=prestart)
    t.start()
def prestart():
    global usr, passwd, driver, toexit, close_label, new_roulette_link, available_label
    os.system("taskkill /f /im  msedge.exe")
    subprocess.Popen('"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --remote-debugging-port=9222',
                     shell=True)
    options = webdriver.EdgeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options.add_argument("--disable-logging")
    driver = webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    logger.setLevel(logging.WARNING)  # or any variant from ERROR, CRITICAL or NOTSET

    starting()


def starting():
    global usr, passwd, driver, toexit, close_label, new_roulette_link, available_label
    driver.implicitly_wait(3)
    driver.get("https://casino-www.888sport.com/")

    # close the cookies notification
    try:
        driver.find_element(By.XPATH, '//*[@class="close"]').click()
    except:
        pass

    # login
    try:
        driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/button').click()
        username = driver.find_element(By.ID, 'rlLoginUsername')
        password = driver.find_element(By.ID, 'rlLoginPassword')
        submitbutton = driver.find_element(By.ID, 'rlLoginSubmit')
        username.clear()
        username.send_keys(usr)
        password.clear()
        password.send_keys(passwd)
        submitbutton.click()
    except:
        pass
    if toexit:
        driver.close()
        stopbutton["state"] = "disabled"
        backbutton["state"] = "normal"
        close_label["state"] = "normal"
        sys.exit()

    time.sleep(3)
    # OPENING GAME-----------------------------------------------------------------------------------
    driver.get('https://casino-www.888sport.com/#page/game/2330035/real/1')
    time.sleep(5)
    new_roulette_link = driver.find_element(By.XPATH, '//iframe[@class="cgp-game-iframe cy-game-iframe"]').get_attribute("src")
    endlink = new_roulette_link.find("&tableAlias")
    new_roulette_link = new_roulette_link[0:endlink]
    driver.get(new_roulette_link)
    # /OPENING GAME-----------------------------------------------------------------------------------
    global starttime
    starttime = datetime.datetime.now()
    # pyautogui.hotkey('alt', "tab")
    global get_initial
    while True:
        whattodo = starting2()
        if whattodo == 'exit':
            driver.close()
            stopbutton["state"] = "disabled"
            backbutton["state"] = "normal"
            close_label["state"] = "normal"
            get_initial = True
            break
        elif whattodo == 'error':
            available_label["image"] = ""
            available_label["text"] = "Restarting Browser"
            #available_label["text"] = "Reiniciando o navegador"
            if toexit:
                available_label["text"] = "Thank you for playing!"
                # available_label["text"] = ""
                break
            starting()
        elif whattodo == "table close":
            if toexit:
                driver.close()
                stopbutton["state"] = "disabled"
                backbutton["state"] = "normal"
                close_label["state"] = "normal"
                get_initial = True
                break
            else:
                driver.get(new_roulette_link)
        elif whattodo == "relogin":
            stopbutton["state"] = "disabled"
            backbutton["state"] = "disabled"
            close_label["state"] = "normal"
            break
    sys.exit()

def starting2():
    try:
        global driver, out_wait, col_wait, alt_wait, max_limit, min_limit, redlist, blacklist, firstdoz, seconddoz, thirddoz, firstcol, secondcol, thirdcol, t
        global blackcount, redcount, oddcount, evencount, smallcount, bigcount, out_betpattern, col_betpattern, out_wait, col_wait, martingale_out_count, martingale_col_count, min_limit, max_limit, table_names20, table_names50, table_names1
        global small_list, big_list, odd_list, even_list, firstdozcount, seconddozcount, thirddozcount, firstcolcount, secondcolcount, thirdcolcount, table_links, table, table_name, blackredcount, redblackcount, smallbigcount, bigsmallcount, evenoddcount, oddevencount
        global starttime, opening_tables, toexit
        global balance_label, minset_money, maxset_money, get_initial
        global col_wait_temp, alt_wait_temp, out_wait_temp, temp_balance
        global back_table_names20, back_table_names50, back_table_names1, only20ptable, new_roulette_link

        if toexit:
            available_label["text"] = "Thank you for playing!"

            return "exit"
        driver.implicitly_wait(0)


        available_label['text'] = ""
        available_label['image'] = ""
        driver.implicitly_wait(0)

        time.sleep(1)
        try:
            grid = driver.find_element(By.XPATH, '//*[@class="grid-btn__toggle"]')
            ac = ActionChains(driver, duration=100)
            ac.click(grid).perform()
        except:
            pass

        init_refresh = 20

        while True:

            init_refresh -= 1
            status_label["text"] = "Refresh if no activity in " + str(init_refresh)

            try:
                if get_initial:
                    global initial_amount

                    initial_amount = float(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div[2]/div/div').text[2:])
                    temp_balance = initial_amount
                    if initial_amount-min_limit <= 0:
                        min_limit = 0.1
                        minset_money['text'] += str("{:.2f}".format(initial_amount))
                    else:
                        minset_money['text'] += str("{:.2f}".format(initial_amount))
                        min_limit = initial_amount - min_limit
                    maxset_money['text'] += str("{:.2f}".format(initial_amount))
                    max_limit = initial_amount+max_limit
                    get_initial = False
                    break
                else:
                    break
            except:
                pass
            time.sleep(1)
            if init_refresh <= 0:
                return "error"

        time.sleep(3)

        while True:
            # CHECK THE BALANCE IF WITHIN THE SET LIMITS
            try:

                balance = float(driver.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div[3]/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div[2]/div/div').text[
                                2:])

                maxset_money['text'] = "$ " + str("{:.2f}".format(balance))
                if balance > temp_balance:
                    min_limit += balance - temp_balance
                    temp_balance = balance
                elif balance <= min_limit:
                    available_label["text"] = "Stop loss reached"
                    return "exit"
            except:
                pass
            # refresh_count -= 1
            currenttime = datetime.datetime.now()
            timediff = str(currenttime - starttime)
            timesep = timediff.find(":")
            minutes_diff = int(timediff[timesep + 1:timesep + 3])
            status_label["text"] = f"Program will refresh in {30-minutes_diff} minutes"

            if toexit:
                available_label["text"] = "Thank you for playing!"
                return "exit"

            while_counter = 20
            while True:
                while_counter -= 1
                try:
                    table_count = driver.find_elements(By.XPATH, "//div[@class='lobby-table__name-container']")
                    count = 0
                    break
                except:
                    pass
                if while_counter <= 0:
                    return "error"

            for y in range(1, len(table_count) + 1):

                global name
                if toexit:
                    available_label["text"] = "Thank you for playing!"

                    return "exit"

                while_counter = 20
                while True:
                    while_counter -= 1
                    try:
                        name = ""
                        name = driver.find_element(By.XPATH, "(//div[@class='lobby-table__name-container'])[" + str(y) + "]").text
                        break
                    except:
                        pass
                    if while_counter <= 0:
                        return "error"

                if name in table_names20 or name in table_names50 or (name in table_names1 and not only20ptable):

                    table = []
                    z = (y * 10) - 10
                    for x in range(1, 11):
                        try:
                            temp = int(driver.find_element(By.XPATH,
                                                           "(//div[@class ='roulette-history-item__value-textsiwxWvFlm3ohr_UMS23f'])[" + str(
                                                               x + z) + "]").text)
                        except:
                            temp = 'B'
                        table.insert(len(table), temp)

                    available_label['text'] = "Analysing Table\n" + name

                    blackcount = 0
                    redcount = 0
                    oddcount = 0
                    evencount = 0
                    smallcount = 0
                    bigcount = 0
                    firstdozcount = 0
                    seconddozcount = 0
                    thirddozcount = 0
                    firstcolcount = 0
                    secondcolcount = 0
                    thirdcolcount = 0
                    blackredcount = 0
                    redblackcount = 0
                    oddevencount = 0
                    evenoddcount = 0
                    smallbigcount = 0
                    bigsmallcount = 0
                    go_to_page = False


                    for blackresult in table:
                        if blackresult not in blacklist:
                            break
                        else:
                            blackcount += 1

                        if blackcount == out_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Black pattern"

                    for redresult in table:
                        if redresult not in redlist:
                            break
                        else:
                            redcount += 1
                        if redcount == out_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Red pattern"

                    for oddresult in table:
                        if oddresult not in odd_list:
                            break
                        else:
                            oddcount += 1
                        if oddcount == out_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Odd pattern"

                    for evenresult in table:
                        if evenresult not in even_list:
                            break
                        else:
                            evencount += 1
                        if evencount == out_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Even pattern"

                    for smallresult in table:
                        if smallresult not in small_list:
                            break
                        else:
                            smallcount += 1
                        if smallcount == out_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Small pattern"

                    for bigresult in table:
                        if bigresult not in big_list:
                            break
                        else:
                            bigcount += 1
                        if bigcount == out_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Big pattern"

                    for firstdozresult in table:
                        if firstdozresult not in firstdoz:
                            break
                        else:
                            firstdozcount += 1
                        if firstdozcount == col_wait_temp:
                            go_to_page = True
                            available_label['text'] = "1st Dozen pattern"

                    for seconddozresult in table:
                        if seconddozresult not in seconddoz:
                            break
                        else:
                            seconddozcount += 1

                        if seconddozcount == col_wait_temp:
                            go_to_page = True
                            available_label['text'] = "2nd Dozen pattern"

                    for thirddozresult in table:
                        if thirddozresult not in thirddoz:
                            break
                        else:
                            thirddozcount += 1

                        if thirddozcount == col_wait_temp:
                            go_to_page = True
                            available_label['text'] = "3rd Dozen pattern"

                    for firstcolresult in table:
                        if firstcolresult not in firstcol:
                            break
                        else:
                            firstcolcount += 1
                        if firstcolcount == col_wait_temp:
                            go_to_page = True
                            available_label['text'] = "1st Column pattern"

                    for secondcolresult in table:
                        if secondcolresult not in secondcol:
                            break
                        else:
                            secondcolcount += 1
                        if secondcolcount == col_wait_temp:
                            go_to_page = True
                            available_label['text'] = "2nd Column pattern"

                    for thirdcolresult in table:
                        if thirdcolresult not in thirdcol:
                            break
                        else:
                            thirdcolcount += 1
                        if thirdcolcount == col_wait_temp:
                            go_to_page = True
                            available_label['text'] = "3rd Column pattern"
                    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    u = 1
                    for blackred in table:
                        if u % 2 == 1 and blackred in blacklist:
                            blackredcount += 1
                        elif u % 2 == 0 and blackred in redlist:
                            blackredcount += 1
                        else:
                            break
                        u += 1
                        if blackredcount == alt_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Black and Red Alternating"

                    u = 1
                    for redblack in table:

                        if u % 2 == 1 and redblack in redlist:
                            redblackcount += 1
                        elif u % 2 == 0 and redblack in blacklist:
                            redblackcount += 1
                        else:
                            break
                        u += 1
                        if redblackcount == alt_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Red and Black Alternating"

                    u = 1
                    for smallbig in table:

                        if u % 2 == 1 and smallbig in small_list:
                            smallbigcount += 1
                        elif u % 2 == 0 and smallbig in big_list:
                            smallbigcount += 1
                        else:
                            break
                        u += 1
                        if smallbigcount == alt_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Small and Big Alternating"

                    u = 1
                    for bigsmall in table:

                        if u % 2 == 1 and bigsmall in big_list:
                            bigsmallcount += 1
                        elif u % 2 == 0 and bigsmall in small_list:
                            bigsmallcount += 1
                        else:
                            break
                        u += 1
                        if bigsmallcount == alt_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Big and Small Alternating"
                    u = 1
                    for oddeven in table:

                        if u % 2 == 1 and oddeven in odd_list:
                            oddevencount += 1
                        elif u % 2 == 0 and oddeven in even_list:
                            oddevencount += 1
                        else:
                            break
                        u += 1

                        if oddevencount == alt_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Odd and Even Alternating"
                    u = 1
                    for evenodd in table:

                        if u % 2 == 1 and evenodd in even_list:
                            evenoddcount += 1
                        elif u % 2 == 0 and evenodd in odd_list:
                            evenoddcount += 1
                        else:
                            break
                        u += 1

                        if evenoddcount == alt_wait_temp:
                            go_to_page = True
                            available_label['text'] = "Even and Odd Alternating"
                    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


                    if go_to_page:
                        available_label['text'] += str(table) + "\n" + str(name)
                        mytable = driver.find_element(By.XPATH, "(//div[@class='lobby-table__name-container'])[" + str(y) + "]")
                        r=1
                        while True:

                            try:
                                mytable.click()
                                break
                            except:
                                try:
                                    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "(//div[@class='lobby-table__name-container'])[" + str(r) + "]"))

                                    mytable.click()
                                    break
                                except:
                                    pass
                            r += 1
                        betting()
                        driver.get(new_roulette_link)
                        time.sleep(3)

                        available_label['text'] = ""
                        available_label['image'] = ""
                    count += 1


            time.sleep(0)

            #status_label["text"] = "O navegador será reiniciado em : " + str(refresh_count)
            currenttime = datetime.datetime.now()
            timediff = str(currenttime - starttime)
            timesep = timediff.find(":")
            minutes_diff = int(timediff[timesep + 1:timesep + 3])
            status_label["text"] = f"Program will refresh in {30 - minutes_diff} minutes"
            if minutes_diff >= 30:
                return "error"
    except:
        return "error"


def betting():
    global driver, out_betpattern, col_betpattern, alt_betpattern, win_count, lose_count, win_count_label, lose_count_label, toexit
    global blackcount, redcount, oddcount, evencount, smallcount, bigcount, out_betpattern, col_betpattern, out_wait, col_wait, alt_wait, min_limit, max_limit
    global firstdozcount, seconddozcount, thirddozcount, firstcolcount, secondcolcount, thirdcolcount, table, table_name, table_names, name, chip, goback, blackredcount, redblackcount, smallbigcount, bigsmallcount, evenoddcount, oddevencount
    global balance_label, martingale_count, alt_wait_temp, col_wait_temp, out_wait_temp, maxset_money, r1value
    global temp_balance

    try:
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[5]/div/div[2]/div[2]/button')))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[5]/div/div[2]/div[2]/button').click()
        return "ignore table"
    except:
        pass

    goback = False
    betoneven = False
    betonodd = False
    betonbig = False
    betonsmall = False
    betonred = False
    betonblack = False
    beton12col = False
    beton13col = False
    beton23col = False
    beton23doz = False
    beton13doz = False
    beton12doz = False
    bet0_bool = False


    driver.implicitly_wait(0)



    try:
        element = WebDriverWait(driver, 8).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div/div/div/div[1]')))
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div/div/div/div[1]').click()
        # driver.find_element(By.XPATH, '//*[@class="close-button game-tutorial__close-buttonfloRKL49s5UiSqxKLrFnwQ=="]').click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, '//*[@class ="welcome-footer__close-button"]').click()
    except:
        pass

    blackcount = 0
    redcount = 0
    oddcount = 0
    evencount = 0
    smallcount = 0
    bigcount = 0
    firstdozcount = 0
    seconddozcount = 0
    thirddozcount = 0
    firstcolcount = 0
    secondcolcount = 0
    thirdcolcount = 0
    blackredcount = 0
    redblackcount = 0
    oddevencount = 0
    evenoddcount = 0
    smallbigcount = 0
    bigsmallcount = 0
    table = []
    for x in range(1, 13):
        try:
            temp = int(driver.find_element(By.XPATH,
                                           "(//div[@class ='roulette-history-item__value-textsiwxWvFlm3ohr_UMS23f'])[" + str(
                                               x) + "]").text)
        except:
            temp = " "
        table.insert(len(table), temp)


    for blackresult in table:
        if blackresult not in blacklist:
            # blackcount = 0
            break
        blackcount += 1

    for redresult in table:
        if redresult not in redlist:
            # redcount = 0
            break
        redcount += 1

    for oddresult in table:
        if oddresult not in odd_list:
            # oddcount = 0
            break
        oddcount += 1

    for evenresult in table:
        if evenresult not in even_list:
            # evencount = 0
            break
        evencount += 1

    for smallresult in table:
        if smallresult not in small_list:
            # smallcount = 0
            break
        smallcount += 1

    for bigresult in table:
        if bigresult not in big_list:
            # bigcount = 0
            break
        bigcount += 1

    for firstdozresult in table:
        if firstdozresult not in firstdoz:
            break
        firstdozcount += 1

    for seconddozresult in table:
        if seconddozresult not in seconddoz:
            break
        seconddozcount += 1

    for thirddozresult in table:
        if thirddozresult not in thirddoz:
            break
        thirddozcount += 1

    for firstcolresult in table:
        if firstcolresult not in firstcol:
            break
        firstcolcount += 1

    for secondcolresult in table:
        if secondcolresult not in secondcol:
            break
        secondcolcount += 1

    for thirdcolresult in table:
        if thirdcolresult not in thirdcol:
            break
        thirdcolcount += 1
    u = 1
    for blackred in table:

        if u % 2 == 1 and blackred in blacklist:
            blackredcount += 1
        elif u % 2 == 0 and blackred in redlist:
            blackredcount += 1
        else:
            break
        u += 1
    u = 1
    for redblack in table:

        if u % 2 == 1 and redblack in redlist:
            redblackcount += 1
        elif u % 2 == 0 and redblack in blacklist:
            redblackcount += 1
        else:
            break
        u += 1
    u = 1
    for smallbig in table:

        if u % 2 == 1 and smallbig in small_list:
            smallbigcount += 1
        elif u % 2 == 0 and smallbig in big_list:
            smallbigcount += 1
        else:
            break
        u += 1
    u = 1
    for bigsmall in table:

        if u % 2 == 1 and bigsmall in big_list:
            bigsmallcount += 1
        elif u % 2 == 0 and bigsmall in small_list:
            bigsmallcount += 1
        else:
            break
        u += 1
    u = 1
    for oddeven in table:

        if u % 2 == 1 and oddeven in odd_list:
            oddevencount += 1
        elif u % 2 == 0 and oddeven in even_list:
            oddevencount += 1
        else:
            break
        u += 1
    u = 1
    for evenodd in table:

        if u % 2 == 1 and evenodd in even_list:
            evenoddcount += 1
        elif u % 2 == 0 and evenodd in odd_list:
            evenoddcount += 1
        else:
            break
        u += 1

    if smallcount >= out_wait:
        smallcount = out_wait - 1
    if bigcount >= out_wait:
        bigcount = out_wait - 1
    if evencount >= out_wait:
        evencount = out_wait - 1
    if oddcount >= out_wait:
        oddcount = out_wait - 1
    if blackcount >= out_wait:
        blackcount = out_wait - 1
    if redcount >= out_wait:
        redcount = out_wait - 1
    if smallbigcount >= alt_wait:
        smallbigcount = alt_wait - 1
    if bigsmallcount >= alt_wait:
        bigsmallcount = alt_wait - 1
    if oddevencount >= alt_wait:
        oddevencount = alt_wait - 1
    if evenoddcount >= alt_wait:
        evenoddcount = alt_wait - 1
    if blackredcount >= alt_wait:
        blackredcount = alt_wait - 1
    if redblackcount >= alt_wait:
        redblackcount = alt_wait - 1
    if firstdozcount >= col_wait:
        firstdozcount = col_wait - 1
    if seconddozcount >= col_wait:
        seconddozcount = col_wait - 1
    if thirddozcount >= col_wait:
        thirddozcount = col_wait - 1
    if firstcolcount >= col_wait:
        firstcolcount = col_wait - 1
    if secondcolcount >= col_wait:
        secondcolcount = col_wait - 1
    if thirdcolcount >= col_wait:
        thirdcolcount = col_wait - 1

    if (redcount < out_wait_temp and blackcount < out_wait_temp) and (
            oddcount < out_wait_temp and evencount < out_wait_temp) and (
            smallcount < out_wait_temp and bigcount < out_wait_temp) and (
            firstdozcount < col_wait_temp and seconddozcount < col_wait_temp and thirddozcount < col_wait_temp) and (
            firstcolcount < col_wait_temp and secondcolcount < col_wait_temp and thirdcolcount < col_wait_temp) and (
            smallbigcount < alt_wait_temp and bigsmallcount < alt_wait_temp) and (
            oddevencount < alt_wait_temp and evenoddcount < alt_wait_temp) and (
            blackredcount < alt_wait_temp and redblackcount < alt_wait_temp):
        goback = True

    if goback:
        try:

            balance = float(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[8]/div/div[1]/div/div[1]/div[1]/div[2]/div/div').text[2:])

            maxset_money['text'] = "$ " + str("{:.2f}".format(balance))
            global temp_balance
            if balance > temp_balance:
                min_limit += balance - temp_balance
                temp_balance = balance
            elif balance <= min_limit:
                available_label["text"] = "Stop loss reached"
                return "exit"

        except:
            pass
        time.sleep(5)
        goback = False
        return

    while True:
        whilecounter = 1000
        if toexit:
            #available_label["text"] = "Thank you for playing!"
            available_label["text"] = ""
            return
        available_label["image"] = ""
        available_label['text'] = ""
        if smallcount >= out_wait_temp:
            available_label['text'] = "Repeating Small\n"
        if bigcount >= out_wait_temp:
            available_label['text'] = "Repeating Big\n"
        if oddcount >= out_wait_temp:
            available_label['text'] = "Repeating Odd\n"
        if evencount >= out_wait_temp:
            available_label['text'] = "Repeating Even\n"
        if redcount >= out_wait_temp:
            available_label['text'] = "Repeating Red\n"
        if blackcount >= out_wait_temp:
            available_label['text'] = "Repeating Black\n"
        if firstdozcount >= col_wait_temp:
            available_label['text'] = "Repeating 1st Dozen\n"
        if seconddozcount >= col_wait_temp:
            available_label['text'] = "Repeating 2nd Dozen\n"
        if thirddozcount >= col_wait_temp:
            available_label['text'] = "Repeating 3rd Dozen\n"
        if firstcolcount >= col_wait_temp:
            available_label['text'] = "Repeating 1st Column\n"
        if secondcolcount >= col_wait_temp:
            available_label['text'] = "Repeating 2nd Column\n"
        if thirdcolcount >= col_wait_temp:
            available_label['text'] = "Repeating 3rd Column\n"
        if redblackcount >= alt_wait_temp:
            available_label['text'] = "Alternating Red and Black\n"
        if blackredcount >= alt_wait_temp:
            available_label['text'] = "Alternating Black and Red\n"
        if oddevencount >= alt_wait_temp:
            available_label['text'] = "Alternating Odd and Even\n"
        if evenoddcount >= alt_wait_temp:
            available_label['text'] = "Alternating Even and Odd\n"
        if smallbigcount >= alt_wait_temp:
            available_label['text'] = "Alternating Small and Big\n"
        if bigsmallcount >= alt_wait_temp:
            available_label['text'] = "Alternating Big and Small\n"
        available_label['text'] += "Waiting for result"
        #available_label['text'] += "Aguardando resultado"
        while True:
            while True:
                if toexit:
                    available_label["text"] = "Thank you for playing!"
                    #available_label["text"] = ""
                    return
                try:
                    result = driver.find_element(By.XPATH,
                                                 '(//*[@class="roulette-round-result-position__text"])[3]').text
                    break
                except:
                    pass
                try:
                    result = driver.find_element(By.XPATH,
                                                 '(//*[@class="roulette-round-result-position__text roulette-round-result-position__text_wwtbamrol"])[3]').text
                    break
                except:
                    pass

                whilecounter -= 1
                status_label["text"] = "Refresh if no activity in " + str(whilecounter)
                #status_label["text"] = "Atualizar se não houver atividade em " + str(whilecounter)
                time.sleep(.2)
                if whilecounter <= 0:
                    return

            if result[0:2].isdigit():
                num = int(result[0:2])
                break
            elif result[0:1].isdigit():
                num = int(result[0])
                break

        chip_elements = driver.find_elements(By.XPATH, '//*[@class="arrow-slider__scrollable-content"]/*[name()="svg"]')
        if num == 0:
            available_label['image'] = num0image

        if num == 1:
            available_label['image'] = num1image

        if num == 2:
            available_label['image'] = num2image

        if num == 3:
            available_label['image'] = num3image

        if num == 4:
            available_label['image'] = num4image

        if num == 5:
            available_label['image'] = num5image

        if num == 6:
            available_label['image'] = num6image

        if num == 7:
            available_label['image'] = num7image

        if num == 8:
            available_label['image'] = num8image

        if num == 9:
            available_label['image'] = num9image

        if num == 10:
            available_label['image'] = num10image

        if num == 11:
            available_label['image'] = num11image

        if num == 12:
            available_label['image'] = num12image

        if num == 13:
            available_label['image'] = num13image

        if num == 14:
            available_label['image'] = num14image

        if num == 15:
            available_label['image'] = num15image

        if num == 16:
            available_label['image'] = num16image

        if num == 17:
            available_label['image'] = num17image

        if num == 18:
            available_label['image'] = num18image

        if num == 19:
            available_label['image'] = num19image

        if num == 20:
            available_label['image'] = num20image

        if num == 21:
            available_label['image'] = num21image

        if num == 22:
            available_label['image'] = num22image

        if num == 23:
            available_label['image'] = num23image

        if num == 24:
            available_label['image'] = num24image

        if num == 25:
            available_label['image'] = num25image

        if num == 26:
            available_label['image'] = num26image

        if num == 27:
            available_label['image'] = num27image

        if num == 28:
            available_label['image'] = num28image

        if num == 29:
            available_label['image'] = num29image

        if num == 30:
            available_label['image'] = num30image

        if num == 31:
            available_label['image'] = num31image

        if num == 32:
            available_label['image'] = num32image

        if num == 33:
            available_label['image'] = num33image

        if num == 34:
            available_label['image'] = num34image

        if num == 35:
            available_label['image'] = num35image

        if num == 36:
            available_label['image'] = num36image


        if num == 0:
            goback = True
            if out_wait <= redcount < (out_wait + martingale_count):
                redcount += 1
                goback = False
            else:
                redcount = 0
            if out_wait <= blackcount < (out_wait + martingale_count):
                blackcount += 1
                goback = False
            else:
                blackcount = 0
            if out_wait <= smallcount < (out_wait + martingale_count):
                smallcount += 1
                goback = False
            else:
                smallcount = 0
            if out_wait <= bigcount < (out_wait + martingale_count):
                bigcount += 1
                goback = False
            else:
                bigcount = 0
            if out_wait <= oddcount < (out_wait + martingale_count):
                oddcount += 1
                goback = False
            else:
                oddcount = 0
            if out_wait <= evencount < (out_wait + martingale_count):
                evencount += 1
                goback = False
            else:
                evencount = 0
            if col_wait <= firstdozcount < (col_wait + martingale_count):
                firstdozcount += 1
                goback = False
            else:
                firstdozcount = 0
            if col_wait <= seconddozcount < (col_wait + martingale_count):
                seconddozcount += 1
                goback = False
            else:
                seconddozcount = 0
            if col_wait <= thirddozcount < (col_wait + martingale_count):
                thirddozcount += 1
                goback = False
            else:
                thirddozcount = 0
            if col_wait <= firstcolcount < (col_wait + martingale_count):
                firstcolcount += 1
                goback = False
            else:
                firstcolcount = 0
            if col_wait <= secondcolcount < (col_wait + martingale_count):
                secondcolcount += 1
                goback = False
            else:
                secondcolcount = 0
            if col_wait <= thirdcolcount < (col_wait + martingale_count):
                thirdcolcount += 1
                goback = False
            else:
                thirdcolcount = 0
            if alt_wait <= smallbigcount < (alt_wait + martingale_count):
                smallbigcount += 1
                goback = False
            else:
                smallbigcount = 0
            if alt_wait <= bigsmallcount < (alt_wait + martingale_count):
                bigsmallcount += 1
                goback = False
            else:
                bigsmallcount = 0
            if alt_wait <= oddevencount < (alt_wait + martingale_count):
                oddevencount += 1
                goback = False
            else:
                oddevencount = 0
            if alt_wait <= evenoddcount < (alt_wait + martingale_count):
                evenoddcount += 1
                goback = False
            else:
                evenoddcount = 0
            if alt_wait <= blackredcount < (alt_wait + martingale_count):
                blackredcount += 1
                goback = False
            else:
                blackredcount = 0
            if alt_wait <= redblackcount < (alt_wait + martingale_count):
                redblackcount += 1
                goback = False
            else:
                redblackcount = 0

        else:
            if num in redlist:
                redcount += 1
                blackcount = 0
                redblackcount = blackredcount + 1
                blackredcount = 0
                if betonred:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"



            elif num in blacklist:
                blackcount += 1
                redcount = 0
                blackredcount = redblackcount + 1
                redblackcount = 0
                if betonblack:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"


            if num in big_list:
                bigcount += 1
                smallcount = 0
                bigsmallcount = smallbigcount + 1
                smallbigcount = 0
                if betonbig:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"



            elif num in small_list:
                smallcount += 1
                bigcount = 0
                smallbigcount = bigsmallcount + 1
                bigsmallcount = 0
                if betonsmall:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"


            if num in even_list:
                evencount += 1
                oddcount = 0
                evenoddcount = oddevencount + 1
                oddevencount = 0
                if betoneven:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"



            elif num in odd_list:
                oddcount += 1
                evencount = 0
                oddevencount = evenoddcount + 1
                evenoddcount = 0
                if betonodd:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"


            if num in firstdoz:
                firstdozcount += 1
                seconddozcount = 0
                thirddozcount = 0
                if beton13doz or beton12doz:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"



            elif num in seconddoz:
                firstdozcount = 0
                seconddozcount += 1
                thirddozcount = 0
                if beton23doz or beton12doz:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"



            elif num in thirddoz:
                firstdozcount = 0
                seconddozcount = 0
                thirddozcount += 1
                if beton23doz or beton13doz:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"


            if num in firstcol:
                firstcolcount += 1
                secondcolcount = 0
                thirdcolcount = 0
                if beton12col or beton13col:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"



            elif num in secondcol:
                firstcolcount = 0
                secondcolcount += 1
                thirdcolcount = 0
                if beton12col or beton23col:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"


            elif num in thirdcol:
                firstcolcount = 0
                secondcolcount = 0
                thirdcolcount += 1
                if beton23col or beton13col:
                    win_count += 1
                    win_count_label["text"] = "Win: " + str(win_count)
                    available_label['image'] = ""
                    available_label['text'] = "Win!"

        if num == 0 and bet0_bool:
            win_count += 1
            win_count_label["text"] = "Win: " + str(win_count)
            available_label['image'] = ""
            available_label['text'] = "Win!"
            goback = True


        if (redcount < out_wait_temp and blackcount < out_wait_temp) and (oddcount < out_wait_temp and evencount < out_wait_temp) and (
                smallcount < out_wait_temp and bigcount < out_wait_temp) and (
                firstdozcount < col_wait_temp and seconddozcount < col_wait_temp and thirddozcount < col_wait_temp) and (
                firstcolcount < col_wait_temp and secondcolcount < col_wait_temp and thirdcolcount < col_wait_temp) and (
                smallbigcount < alt_wait_temp and bigsmallcount < alt_wait_temp) and (
                oddevencount < alt_wait_temp and evenoddcount < alt_wait_temp) and (
                blackredcount < alt_wait_temp and redblackcount < alt_wait_temp):
            goback = True

        for h in [blackcount, redcount, oddcount, evencount, smallcount, bigcount]:
            if h == out_wait + martingale_count:
                lose_count += 1
                lose_count_label["text"] = "Loss: " + str(lose_count)

        for h in [firstdozcount, seconddozcount, thirddozcount, firstcolcount, secondcolcount, thirdcolcount]:

            if h == col_wait + martingale_count:
                lose_count += 1
                lose_count_label["text"] = "Loss: " + str(lose_count)

        for h in [redblackcount, blackredcount, oddevencount, evenoddcount, smallbigcount, bigsmallcount]:
            if h == alt_wait + martingale_count:
                lose_count += 1
                lose_count_label["text"] = "Loss: " + str(lose_count)


        if goback:
            try:
                balance = float(driver.find_element(By.XPATH,
                                                    '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[8]/div/div[1]/div/div[1]/div[1]/div[2]/div/div').text[
                                2:])

                maxset_money['text'] = "$ " + str("{:.2f}".format(balance))
                if balance > temp_balance:
                    min_limit += balance - temp_balance
                    temp_balance = balance
                elif balance <= min_limit:
                    available_label["text"] = "Stop loss reached"
                    return "exit"

            except:
                pass
            time.sleep(5)
            goback = False
            return

        for z in reversed(chip_elements):
            try:
                z.click()
            except:
                pass

        if chip == "0.2" and name in table_names20:
            for q in chip_elements:
                try:
                    q.click()
                except:
                    pass
                time.sleep(.1)
                selected_chip = q.get_attribute("data-automation-locator")
                if selected_chip[15:] == "20":
                    break
        elif chip == "0.2" and name in table_names50:
            for q in chip_elements:
                try:
                    q.click()
                except:
                    pass
                time.sleep(.1)
                selected_chip = q.get_attribute("data-automation-locator")
                if selected_chip[15:] == "50":
                    break

        elif chip == "0.2" and name in table_names1:
            for q in chip_elements:
                try:
                    q.click()
                except:
                    pass
                time.sleep(.1)
                selected_chip = q.get_attribute("data-automation-locator")
                if selected_chip[15:] == "100":
                    break
        elif chip == "0.5" and (name in table_names20 or name in table_names50):
            for q in chip_elements:
                try:
                    q.click()
                except:
                    pass
                time.sleep(.1)
                selected_chip = q.get_attribute("data-automation-locator")
                if selected_chip[15:] == "50":
                    break

        elif chip == "0.5" and name in table_names1:
            for q in chip_elements:
                try:
                    q.click()
                except:
                    pass
                time.sleep(.1)
                selected_chip = q.get_attribute("data-automation-locator")
                if selected_chip[15:] == "100":
                    break
        else:
            temp_chip = str(int(float(chip) * 100))
            for q in chip_elements:
                try:
                    q.click()
                except:
                    pass
                time.sleep(.1)
                selected_chip = q.get_attribute("data-automation-locator")
                if selected_chip[15:] == temp_chip:
                    break


        rf_count = 1000
        while True:
            if toexit:
                available_label["image"] = ""
                available_label["text"] = "Thank you for playing!"
                #available_label["text"] = ""
                return
            rf_count -= 1
            status_label["text"] = "Refresh if no activity in " + str(rf_count)
            #status_label["text"] = "Atualizar se não houver atividade em " + str(rf_count)
            try:
                #if driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[2]/header/div[2]/div/span/span/div/span').text == 'FAÇA AS SUAS APOSTAS':
                if driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[2]/header/div[2]/div/span/span/div/span').text == 'PLACE YOUR BETS':
                    time.sleep(3)
                    break
            except:
                pass
            time.sleep(.5)
            if rf_count <= 0:
                return


        try:

            balance = float(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[8]/div/div[1]/div/div[1]/div[1]/div[2]/div/div').text[2:])

            maxset_money['text'] = "$ " + str("{:.2f}".format(balance))

            if balance > temp_balance:
                min_limit += balance - temp_balance
                temp_balance = balance
            elif balance <= min_limit:
                available_label["text"] = "Stop loss reached"
                return "exit"

        except:
            pass

        bet0_bool = False
        betoneven = False
        betonodd = False
        betonbig = False
        betonsmall = False
        betonred = False
        betonblack = False
        beton12col = False
        beton13col = False
        beton23col = False
        beton23doz = False
        beton13doz = False
        beton12doz = False
        ref_count = 100
        while True:
            status_label['text'] = "Refresh if no activity in " + str(ref_count)
            # status_label['text'] = "Atualizar se não houver atividade em " + str(ref_count)
            try:

                blackbet = driver.find_element(By.XPATH,
                                               '//*[@class="roulette-table-cell roulette-table-cell_side-black roulette-table-cell_group-fifty-fifty"]')
                redbet = driver.find_element(By.XPATH,
                                             '//*[@class="roulette-table-cell roulette-table-cell_side-red roulette-table-cell_group-fifty-fifty"]')
                oddbet = driver.find_element(By.XPATH,
                                             '//*[@class="roulette-table-cell roulette-table-cell_side-odd roulette-table-cell_group-fifty-fifty"]')
                evenbet = driver.find_element(By.XPATH,
                                              '//*[@class="roulette-table-cell roulette-table-cell_side-even roulette-table-cell_group-fifty-fifty"]')
                smallbet = driver.find_element(By.XPATH,
                                               '//*[@class="roulette-table-cell roulette-table-cell_side-low roulette-table-cell_group-fifty-fifty"]')
                bigbet = driver.find_element(By.XPATH,
                                             '//*[@class="roulette-table-cell roulette-table-cell_side-high roulette-table-cell_group-fifty-fifty"]')
                doz1 = driver.find_element(By.XPATH,
                                           '//*[@class="roulette-table-cell roulette-table-cell_side-first-dozen roulette-table-cell_group-dozen"]')
                doz2 = driver.find_element(By.XPATH,
                                           '//*[@class="roulette-table-cell roulette-table-cell_side-second-dozen roulette-table-cell_group-dozen"]')
                doz3 = driver.find_element(By.XPATH,
                                           '//*[@class="roulette-table-cell roulette-table-cell_side-third-dozen roulette-table-cell_group-dozen"]')
                col1 = driver.find_element(By.XPATH,
                                           '//*[@class="roulette-table-cell roulette-table-cell_side-bottom-column roulette-table-cell_group-dozen"]')
                col2 = driver.find_element(By.XPATH,
                                           '//*[@class="roulette-table-cell roulette-table-cell_side-middle-column roulette-table-cell_group-dozen"]')
                col3 = driver.find_element(By.XPATH,
                                           '//*[@class="roulette-table-cell roulette-table-cell_side-top-column roulette-table-cell_group-dozen"]')
                beton0 = driver.find_element(By.XPATH,
                                             '(//*[@class="roulette-table-cell roulette-table-cell_straight-0 roulette-table-cell_group-straight roulette-table-cell_color-green"])[2]')
                break
            except:
                ref_count -= 1

            if ref_count <= 0:
                return
        # BETTING ON BLACK-------------------------------------------------------
        if redcount >= out_wait:
            status_label["text"] = "Clicking Black"
            for i in range(out_betpattern[redcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(blackbet).perform()
                betonblack = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        # BETTING ON RED-------------------------------------------------------

        if blackcount >= out_wait:

            status_label["text"] = "Clicking Red"
            for i in range(out_betpattern[blackcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(redbet).perform()

                betonred = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        # BETTING ON ODD-------------------------------------------------------
        if evencount >= out_wait:
            status_label["text"] = "Clicking Odd"
            for i in range(out_betpattern[evencount]):

                ac = ActionChains(driver, duration=100)
                ac.click(oddbet).perform()
                betonodd = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        # BETTING ON EVEN-------------------------------------------------------
        if oddcount >= out_wait:

            status_label["text"] = "Clicking Even"
            for i in range(out_betpattern[oddcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(evenbet).perform()
                betoneven = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        # BETTING ON SMALL-------------------------------------------------------
        if bigcount >= out_wait:

            status_label["text"] = "Clicking Small"
            for i in range(out_betpattern[bigcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(smallbet).perform()
                betonsmall = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        # BETTING ON BIG-------------------------------------------------------
        if smallcount >= out_wait:

            status_label["text"] = "Clicking Big"
            for i in range(out_betpattern[smallcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(bigbet).perform()
                betonbig = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        # BETTING ON 2ND AND 3RD DOZ-------------------------------------------------------
        if firstdozcount >= col_wait:

            for i in range(col_betpattern[firstdozcount]):

                ac = ActionChains(driver, duration=100)
                ac.move_to_element(doz2).move_by_offset(30, 5).click().perform()
                ac.move_to_element(doz3).move_by_offset(30, 5).click().perform()
                beton23doz = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if seconddozcount >= col_wait:

            for i in range(col_betpattern[seconddozcount]):

                ac = ActionChains(driver, duration=100)
                ac.move_to_element(doz3).move_by_offset(30, 5).click().perform()
                ac.move_to_element(doz1).move_by_offset(30, 5).click().perform()

                beton13doz = True
                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if thirddozcount >= col_wait:
            for i in range(col_betpattern[thirddozcount]):

                ac = ActionChains(driver, duration=100)
                ac.move_to_element(doz2).move_by_offset(30, 5).click().perform()
                ac.move_to_element(doz1).move_by_offset(30, 5).click().perform()
                beton12doz = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if firstcolcount >= col_wait:

            for i in range(col_betpattern[firstcolcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(col2).perform()
                ac.click(col3).perform()
                beton23col = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if secondcolcount >= col_wait:

            for i in range(col_betpattern[secondcolcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(col3).perform()
                ac.click(col1).perform()
                beton13col = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if thirdcolcount >= col_wait:

            for i in range(col_betpattern[thirdcolcount]):

                ac = ActionChains(driver, duration=100)
                ac.click(col2).perform()
                ac.click(col1).perform()
                beton12col = True

                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if blackredcount >= alt_wait:

            status_label["text"] = "Clicking Black"
            ac = ActionChains(driver, duration=100)
            for i in range(alt_betpattern[blackredcount]):

                ac.click(blackbet).perform()
                betonblack = True
                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if redblackcount >= alt_wait:

            status_label["text"] = "Clicking Red"
            ac = ActionChains(driver, duration=100)
            for i in range(alt_betpattern[redblackcount]):

                ac.click(redbet).perform()
                betonred = True
                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if smallbigcount >= alt_wait:

            status_label["text"] = "Clicking SMALL"
            ac = ActionChains(driver, duration=100)
            for i in range(alt_betpattern[smallbigcount]):

                ac.click(smallbet).perform()
                betonsmall = True
                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if bigsmallcount >= alt_wait:

            status_label["text"] = "Clicking BIG"
            ac = ActionChains(driver, duration=100)
            for i in range(alt_betpattern[bigsmallcount]):

                ac.click(bigbet).perform()
                betonbig = True
                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if oddevencount >= alt_wait:

            status_label["text"] = "Clicking ODD"
            ac = ActionChains(driver, duration=100)
            for i in range(alt_betpattern[oddevencount]):

                ac.click(oddbet).perform()
                betonodd = True
                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"
        if evenoddcount >= alt_wait:

            status_label["text"] = "Clicking EVEN"
            ac = ActionChains(driver, duration=100)
            for i in range(alt_betpattern[evenoddcount]):

                ac.click(evenbet).perform()
                betoneven = True
                if r1value == 1:
                    bet0_bool = True
                available_label["text"] = f"Bet confirm"

        if bet0_bool:
            for z in reversed(chip_elements):
                try:
                    z.click()
                except:
                    pass

            if bet0_variable.get() == "0.2" and name in table_names20:
                for q in chip_elements:
                    try:
                        q.click()
                    except:
                        pass
                    time.sleep(.1)
                    selected_chip = q.get_attribute("data-automation-locator")
                    if selected_chip[15:] == "20":
                        break
            elif bet0_variable.get() == "0.2" and name in table_names50:
                for q in chip_elements:
                    try:
                        q.click()
                    except:
                        pass
                    time.sleep(.1)
                    selected_chip = q.get_attribute("data-automation-locator")
                    if selected_chip[15:] == "50":
                        break

            elif bet0_variable.get() == "0.2" and name in table_names1:
                for q in chip_elements:
                    try:
                        q.click()
                    except:
                        pass
                    time.sleep(.1)
                    selected_chip = q.get_attribute("data-automation-locator")
                    if selected_chip[15:] == "100":
                        break
            elif bet0_variable.get() == "0.5" and (name in table_names20 or name in table_names50):
                for q in chip_elements:
                    try:
                        q.click()
                    except:
                        pass
                    time.sleep(.1)
                    selected_chip = q.get_attribute("data-automation-locator")
                    if selected_chip[15:] == "50":
                        break

            elif bet0_variable.get() == "0.5" and name in table_names1:
                for q in chip_elements:
                    try:
                        q.click()
                    except:
                        pass
                    time.sleep(.1)
                    selected_chip = q.get_attribute("data-automation-locator")
                    if selected_chip[15:] == "100":
                        break
            else:
                temp_chip = str(int(float(bet0_variable.get()) * 100))
                for q in chip_elements:
                    try:
                        q.click()
                    except:
                        pass
                    time.sleep(.1)
                    selected_chip = q.get_attribute("data-automation-locator")
                    if selected_chip[15:] == temp_chip:
                        break

            ac = ActionChains(driver, duration=100)
            ac.click(beton0).perform()



def db_check():
    #Database check for username and password
    secondwindow()

dozvalue = IntVar()
dozvalue = 0


def dozcolonoff():
    global dozvalue, offimage, onimage, dozcol_check, gambitvalue
    if dozvalue == 0:
        dozvalue = 1
        dozcol_check["image"] = onimage
        gambitvalue = 0
        gambit_check["image"] = offimage
    else:
        dozvalue = 0
        dozcol_check["image"] = offimage
        gambitvalue = 0
        gambit_check["image"] = offimage


outsidevalue = IntVar()
outsidevalue = 0


def outsideonoff():
    global outsidevalue, offimage, onimage, outside_check, gambitvalue
    if outsidevalue == 0:
        outsidevalue = 1
        outside_check["image"] = onimage
        gambitvalue = 0
        gambit_check["image"] = offimage
    else:
        outsidevalue = 0
        outside_check["image"] = offimage
        gambitvalue = 0
        gambit_check["image"] = offimage


alternatingvalue = IntVar()
alternatingvalue = 0


def alternatingonoff():
    global alternatingvalue, offimage, onimage, alternating_check, gambitvalue
    if alternatingvalue == 0:
        alternatingvalue = 1
        alternating_check["image"] = onimage
        gambitvalue = 0
        gambit_check["image"] = offimage
    else:
        alternatingvalue = 0
        alternating_check["image"] = offimage
        gambitvalue = 0
        gambit_check["image"] = offimage


gambitvalue = IntVar()
gambitvalue = 0


def gambitonoff():
    global gambitvalue, offimage, onimage, gambit_check, outside_check, dozvalue, outsidevalue, alternatingvalue
    if gambitvalue == 0:
        gambitvalue = 1
        gambit_check["image"] = onimage
        dozvalue = 1
        dozcol_check["image"] = onimage
        outsidevalue = 1
        outside_check["image"] = onimage
        alternatingvalue = 1
        alternating_check["image"] = onimage

    else:
        gambitvalue = 0
        gambit_check["image"] = offimage


def fifthwindow():
    global fifthframe, fourthframe, username_entry, password_entry, sixthframe, bet0_variable
    fourthframe.destroy()
    gameframe.destroy()


    fifthframe = Frame(root)
    fifthframe.pack()
    canvas = Canvas(fifthframe, width=WIDTH, height=HEIGHT, highlightthickness=1, highlightbackground="#0f0f0f")
    canvas.pack()

    img = ImageTk.PhotoImage(file=".\\assets\\bg5.png")
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)

    logo_label = Label(fifthframe, image=casinoimage, bg="#0f0f0f", bd=0)
    logo_label_window = canvas.create_window(150, 150, window=logo_label)

    title_label = Label(fifthframe, text="Login", font=("Sansation", 23, "bold"), bg="#0f0f0f", bd=0,
                        fg="white")
    title_label_window = canvas.create_window(230, 150, window=title_label)

    with open(".\\assets\\login.txt", "r") as file:
        from_file = file.readline()

    charfind = from_file.find(",")
    user = from_file[0:charfind]
    from_file = from_file[charfind + 1:]
    secretword = from_file[0:]

    global username_entry, password_entry

    username_entry = Entry(fifthframe, width=14, bd=1, background="#0f0f0f", font=("Sansation", 12), fg="white",
                           insertbackground="white")
    username_entry_window = canvas.create_window(215, 229, window=username_entry)

    username_entry.insert(END, user)

    password_entry = Entry(fifthframe, show='*', width=14, bd=1, background="#0f0f0f", font=("Sansation", 12),
                           fg="white", insertbackground="white")
    password_entry_window = canvas.create_window(215, 285, window=password_entry)

    password_entry.insert(END, secretword)

    def checking():
        if username_entry.get() == "" or password_entry.get() == "":
            stat3["text"] = "O nome de usuário ou a senha não podem ficar em branco"
        else:
            global usr, passwd
            usr = username_entry.get()
            passwd = password_entry.get()
            start()


    toback = Button(fifthframe, text="Login", command=fourthwindow, borderwidth=0, image=backimage, bg="#0f0f0f",
                    activebackground="#0f0f0f")
    toback_window = canvas.create_window(100, 370, window=toback)
    toadvance = Button(fifthframe, command=checking, image=startimage, borderwidth=0, bg="#0f0f0f",
                       activebackground="#0f0f0f")
    toadvance_window = canvas.create_window(280, 370, window=toadvance)

    global stat3
    stat3 = Label(fifthframe, text="", font=("Sansation", 10),
                  fg="red", bg="#0f0f0f")
    stat3_window = canvas.create_window(190, 430, window=stat3)


bet0 = IntVar()
bet0.set(0)
bet0_variable = StringVar()
r1value = IntVar()
r1value = 0


def fourthwindow():

    global thirdframe, fourthframe, chip, bet0
    global coldozwait_variable, outwait_variable, alternating_variable
    thirdframe.destroy()
    fifthframe.destroy()
    fourthframe = Frame(root)
    fourthframe.pack()

    canvas = Canvas(fourthframe, width=WIDTH, height=HEIGHT, highlightthickness=1, highlightbackground="#0f0f0f")
    canvas.pack()

    img = ImageTk.PhotoImage(file=".\\assets\\bg4.png")
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)

    if gambitvalue == 1:
        coldozwait_variable.set("6")
        outwait_variable.set("13")
        alternating_variable.set("13")

    big20p = PhotoImage(file=".\\assets\\20pbig.png")
    small20p = PhotoImage(file=".\\assets\\20psmall.png")
    big50p = PhotoImage(file=".\\assets\\50pbig.png")
    small50p = PhotoImage(file=".\\assets\\50psmall.png")
    big1 = PhotoImage(file=".\\assets\\1big.png")
    small1 = PhotoImage(file=".\\assets\\1small.png")
    big5 = PhotoImage(file=".\\assets\\5big.png")
    small5 = PhotoImage(file=".\\assets\\5small.png")
    big10 = PhotoImage(file=".\\assets\\10big.png")
    small10 = PhotoImage(file=".\\assets\\10small.png")
    big25 = PhotoImage(file=".\\assets\\25big.png")
    small25 = PhotoImage(file=".\\assets\\25small.png")
    big100 = PhotoImage(file=".\\assets\\100big.png")
    small100 = PhotoImage(file=".\\assets\\100small.png")

    def chip20p():
        global chip
        chip = "0.2"
        chip20p_button["image"] = big20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    def chip50p():
        global chip
        chip = "0.5"
        chip50p_button["image"] = big50p

        chip20p_button["image"] = small20p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    def chip1():
        global chip
        chip = "1"
        chip1_button["image"] = big1

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    def chip5():
        global chip
        chip = "5"
        chip5_button["image"] = big5

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    def chip10():
        global chip
        chip = "10"
        chip10_button["image"] = big10

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    def chip25():
        global chip
        chip = "25"
        chip25_button["image"] = big25

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip100_button["image"] = small100

    def chip100():
        global chip
        chip = "100"
        chip100_button["image"] = big100

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25

    chip20p_button = Button(fourthframe, command=chip20p, image=big20p, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    chip20p_button_window = canvas.create_window(40, 145, window=chip20p_button)
    chip50p_button = Button(fourthframe, command=chip50p, image=small50p, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    chip50p_button_window = canvas.create_window(90, 145, window=chip50p_button)
    chip1_button = Button(fourthframe, command=chip1, image=small1, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    chip1_button_window = canvas.create_window(140, 145, window=chip1_button)
    chip5_button = Button(fourthframe, command=chip5, image=small5, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    chip5_button_window = canvas.create_window(190, 145, window=chip5_button)
    chip10_button = Button(fourthframe, command=chip10, image=small10, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    chip10_button_button_window = canvas.create_window(240, 145, window=chip10_button)
    chip25_button = Button(fourthframe, command=chip25, image=small25, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    chip25_button_window = canvas.create_window(290, 145, window=chip25_button)
    chip100_button = Button(fourthframe, command=chip100, image=small100, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    chip100_button_window = canvas.create_window(340, 145, window=chip100_button)

    global chip
    if chip == "0.2":
        chip20p_button["image"] = big20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    elif chip == "0.5":
        chip50p_button["image"] = big50p

        chip20p_button["image"] = small20p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    elif chip == "1":
        chip1_button["image"] = big1

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    elif chip == "5":

        chip5_button["image"] = big5

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip10_button["image"] = small10
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    elif chip == "10":

        chip10_button["image"] = big10

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip25_button["image"] = small25
        chip100_button["image"] = small100

    elif chip == "25":

        chip25_button["image"] = big25

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip100_button["image"] = small100

    elif chip == "100":

        chip100_button["image"] = big100

        chip20p_button["image"] = small20p
        chip50p_button["image"] = small50p
        chip1_button["image"] = small1
        chip5_button["image"] = small5
        chip10_button["image"] = small10
        chip25_button["image"] = small25

    global bet0_variable
    global bet0, bet0chip
    global r1value

    def r1bet():
        global r1value
        if r1value == 0:
            r1value = 1

            r1["image"] = onimage
            bet0chip["state"] = "normal"
            bet0_variable.set("0.2")


        else:
            r1value = 0
            r1["image"] = offimage
            bet0chip["state"] = "disabled"
            bet0_variable.set("0")

    r1 = Button(fourthframe, image=offimage, borderwidth=0, command=r1bet, bg="#0f0f0f", activebackground="#0f0f0f")
    r1_window = canvas.create_window(300, 327, window=r1)
    if r1 == 1:
        r1["image"] = onimage

    s = ttk.Style()
    s.configure("TMenubutton", background="#0f0f0f", foreground="white", font=("Sansation", 12))
    bet0chip = ttk.OptionMenu(fourthframe, bet0_variable, bet0_variable.get(), "0.2", '0.5', '1', '5', '10', '25', "100")
    bet0chip["menu"].config(background="#0f0f0f", foreground="white", font=("Sansation", 12))
    bet0chip_window = canvas.create_window(240, 327, window=bet0chip)

    if r1value == 0:
        r1['image'] = offimage
        bet0chip["state"] = "disabled"
        bet0_variable.set("0")
    else:
        r1['image'] = onimage
        bet0chip["state"] = "normal"

    min_entry = Entry(fourthframe, width=5, textvariable=minmoney, bd=0, background="#0f0f0f", font=("Sansation", 9), fg="white", insertbackground="white")
    min_entry_window = canvas.create_window(275, 267, anchor=NW, window=min_entry)


    max_entry = Entry(fourthframe, width=5, textvariable=maxmoney, bd=0, background="#0f0f0f", font=("Sansation", 9), fg="white", insertbackground="white")

    max_entry_window = canvas.create_window(275, 215, anchor=NW, window=max_entry)



    def mart_up():
        temp = int(martingale_entry.get()) + 1
        martingale_entry.delete(0, END)
        martingale_entry.insert(END, str(temp))

    def mart_down():
        temp = int(martingale_entry.get())
        if temp <= 1:
            martingale_entry.delete(0, END)
            martingale_entry.insert(END, "1")
        else:
            temp -= 1
            martingale_entry.delete(0, END)
            martingale_entry.insert(END, str(temp))

    global martingale_entry, mart_var

    martingale_entry = Entry(fourthframe, width=3, bd=0, textvariable=mart_var, bg="#0f0f0f", font=("Sansation", 10), fg="white", insertbackground="white")
    martingale_entry_window = canvas.create_window(275, 370, anchor=NW, window=martingale_entry)

    valueup = Button(fourthframe, command=mart_up, image=upimage, borderwidth=0, bg="#0f0f0f",
                    activebackground="#0f0f0f")
    valueup_window = canvas.create_window(304, 373, anchor=NW, window=valueup)
    valuedown = Button(fourthframe, command=mart_down, image=downimage, borderwidth=0, bg="#0f0f0f",
                    activebackground="#0f0f0f")
    valuedown_window = canvas.create_window(292, 373, anchor=NW, window=valuedown)

    def convert():
        if martingale_entry.get().isdigit():
            try:
                global martingale_count, max_limit, min_limit
                martingale_count = int(martingale_entry.get())
                max_limit = float(maxmoney.get())
                min_limit = float(minmoney.get())
                fifthwindow()
            except:
                stat4["text"] = "Invalid inputs, Please check your values"

        else:
            stat4["text"] = "Invalid inputs, Please check your values"



    toback = Button(fourthframe, command=thirdwindow, image=backimage, borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f")
    toback_window = canvas.create_window(45, 410, anchor=NW, window=toback)

    toadvance = Button(fourthframe, command=convert, image=nextimage, borderwidth=0, bg="#0f0f0f",
                       activebackground="#0f0f0f")
    toadvance_window = canvas.create_window(220, 410, anchor=NW, window=toadvance)
    global stat4

    stat4 = Label(fourthframe, text="", font=("Sansation", 12, "bold"), fg="red", bg="#0f0f0f")
    stat4_window = canvas.create_window(190, 470, window=stat4)




def thirdwindow():
    global gambitvalue, dozvalue, outsidevalue, alternatingvalue, thirdframe

    secondframe.destroy()
    fourthframe.destroy()
    thirdframe = Frame(root)
    thirdframe.pack()

    canvas = Canvas(thirdframe, width=WIDTH, height=HEIGHT, highlightthickness=1, highlightbackground="#0f0f0f")
    canvas.pack()

    img = ImageTk.PhotoImage(file=".\\assets\\bg3.png")
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)
    s = ttk.Style()
    s.configure("TMenubutton", background="#0f0f0f", foreground="white", font=("Sansation", 12, "bold"))

    global coldozwait_variable

    coldozwait_entry = ttk.OptionMenu(thirdframe, coldozwait_variable, coldozwait_variable.get(), '4', '5', '6', '7', '8', '9', '10', '11', '12')
    coldozwait_entry["menu"].config(background="#0f0f0f", foreground="white", font=("Sansation", 12, "bold"))
    coldozwait_entry_window = canvas.create_window(280, 178, anchor=NW, window=coldozwait_entry)

    outside_label = Label(thirdframe, text="Repetitions:", font=("Sansation", 15, "bold"))
    global outwait_variable
    outwait_entry = ttk.OptionMenu(thirdframe, outwait_variable, outwait_variable.get(), '4', '5', '6', '7', '8', '9', '10', '11',
                                   '12', '13')
    outwait_entry["menu"].config(background="#0f0f0f", foreground="white", font=("Sansation", 12, "bold"))
    outwait_entry_window = canvas.create_window(280, 232, anchor=NW, window=outwait_entry)

    global alternating_variable

    alternating_entry = ttk.OptionMenu(thirdframe, alternating_variable, alternating_variable.get(), '4', '5', '6', '7', '8', '9',
                                       '10', '11', '12', '13')
    alternating_entry["menu"].config(background="#0f0f0f", foreground="white", font=("Sansation", 12, "bold"))
    alternating_entry_window = canvas.create_window(280, 284, anchor=NW, window=alternating_entry)

    if gambitvalue == 1:

        outwait_entry["state"] = "disabled"
        coldozwait_entry["state"] = "disabled"
        alternating_entry["state"] = "disabled"
        outwait_variable.set("-")
        coldozwait_variable.set("-")
        alternating_variable.set("-")
    else:
        if outsidevalue == 1:
            outwait_entry["state"] = "normal"
            if outwait_variable.get() == "-":
                outwait_variable.set("4")
            else:
                outwait_variable.set(outwait_variable.get())
        else:
            outwait_entry["state"] = "disabled"
            outwait_variable.set("-")

        if dozvalue == 1:
            coldozwait_entry["state"] = "normal"
            if coldozwait_variable.get() == "-":
                coldozwait_variable.set("4")
            else:
                coldozwait_variable.set(coldozwait_variable.get())
        else:
            coldozwait_entry["state"] = "disabled"
            coldozwait_variable.set("-")

        if alternatingvalue == 1:
            alternating_entry["state"] = "normal"
            if alternating_variable.get() == "-":
                alternating_variable.set("4")
            else:
                alternating_variable.set(alternating_variable.get())
        else:
            alternating_entry["state"] = "disabled"
            alternating_variable.set("-")



    def change20ptables():
        global only20ptable
        if only20ptable:
            only20ptablebutton["image"] = offimage
            only20ptable = False
            only20ptablelabel["fg"] = "grey"
        elif not only20ptable:
            only20ptablebutton["image"] = onimage
            only20ptable = True
            only20ptablelabel["fg"] = "white"



    only20ptablelabel = Label(thirdframe, text="Only 50p tables?", borderwidth=0, bg="#0f0f0f", activebackground="#0f0f0f", fg="white", font=("Sansation", 14, "bold"))
    #only20ptablelabel_window = canvas.create_window(58, 450, anchor=NW, window=only20ptablelabel)

    only20ptablebutton = Button(thirdframe, image=onimage, borderwidth=0, command=change20ptables, bg="#0f0f0f",
                               activebackground="#0f0f0f")
    #only20ptablebutton_window = canvas.create_window(260, 445, anchor=NW, window=only20ptablebutton)

    if only20ptable:
        only20ptablebutton["image"] = onimage
        only20ptablelabel["fg"] = "white"
    elif not only20ptable:
        only20ptablebutton["image"] = offimage
        only20ptablelabel["fg"] = "grey"

    toback = Button(thirdframe, command=secondwindow, image=backimage, borderwidth=0, bg="#0f0f0f",
                    activebackground="#0f0f0f")
    toback_window = canvas.create_window(45, 370, anchor=NW, window=toback)
    toadvance = Button(thirdframe, command=fourthwindow, image=nextimage, borderwidth=0, bg="#0f0f0f",
                       activebackground="#0f0f0f")
    toadvance_window = canvas.create_window(220, 370, anchor=NW, window=toadvance)


def secondwindow():
    global onimage, offimage, dozcol_check, secondframe, dozvalue, outsidevalue, alternatingvalue, gambitvalue

    mainframe.destroy()
    thirdframe.destroy()
    secondframe = Frame(root)
    secondframe.pack()
    canvas = Canvas(secondframe, width=WIDTH, height=HEIGHT, highlightthickness=1, highlightbackground="#0f0f0f")
    canvas.pack()

    img = ImageTk.PhotoImage(file=".\\assets\\bg2.png")
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)

    global dozcol_check
    dozcol_check = Button(secondframe, image=offimage, borderwidth=0, command=dozcolonoff, bg="#0f0f0f",
                          activebackground="#0f0f0f")
    dozcol_check_window = canvas.create_window(260, 173, anchor=NW, window=dozcol_check)
    if dozvalue == 1:
        dozcol_check["image"] = onimage

    global outside_check
    outside_check = Button(secondframe, image=offimage, borderwidth=0, command=outsideonoff, bg="#0f0f0f",
                           activebackground="#0f0f0f")
    outside_check_window = canvas.create_window(260, 225, anchor=NW, window=outside_check)
    if outsidevalue == 1:
        outside_check["image"] = onimage

    global alternating_check
    alternating_check = Button(secondframe, image=offimage, borderwidth=0, command=alternatingonoff, bg="#0f0f0f",
                               activebackground="#0f0f0f")
    alternating_check_window = canvas.create_window(260, 276, anchor=NW, window=alternating_check)
    if alternatingvalue == 1:
        alternating_check["image"] = onimage

    global gambit_check
    gambit_check = Button(secondframe, image=offimage, borderwidth=0, command=gambitonoff, bg="#0f0f0f",
                          activebackground="#0f0f0f")
    #gambit_check_window = canvas.create_window(260, 328, anchor=NW, window=gambit_check)
    if gambitvalue == 1:
        gambit_check["image"] = onimage

    def check2ndwindows():
        if dozvalue == 0 and outsidevalue == 0 and alternatingvalue == 0 and gambitvalue == 0:
            stat2["text"] = "Please select one"

        else:
            thirdwindow()

    toadvance = Button(secondframe, command=check2ndwindows, image=nextimage, borderwidth=0, bg="#0f0f0f",
                       activebackground="#0f0f0f")
    toadvance_window = canvas.create_window(220, 370, anchor=NW, window=toadvance)

    global stat2
    stat2 = Label(secondframe, text="", font=("Sansation", 12, "bold"), fg="red", bg="#0f0f0f")
    stat2_window = canvas.create_window(190, 430, window=stat2)


def mainwindows():
    global failpassword_label, username_entry, password_entry, close_label

    try:
        gameframe.destroy()
    except:
        pass
    mainframe.pack()
    canvas = Canvas(mainframe, width=WIDTH, height=HEIGHT, highlightthickness=1, highlightbackground="black")
    canvas.pack()

    img = ImageTk.PhotoImage(file=".\\assets\\bg1.png")
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=NW, image=img)

    # Put a tkinter widget on the canvas.

    username_entry = Entry(mainframe, width=14, bd=2, background="black", font=("Sansation", 12), fg="white", insertbackground="white")
    username_entry_window = canvas.create_window(149, 250, anchor=NW, window=username_entry)


    password_entry = Entry(mainframe, show='*', width=14, bd=2, background="black", font=("Sansation", 12), fg="white", insertbackground="white")
    password_entry_window = canvas.create_window(149, 305, anchor=NW, window=password_entry)


    login = Button(mainframe, text="", command=db_check, borderwidth=0, image=loginimage, bg="black", activebackground="black")
    login_window = canvas.create_window(220, 370, anchor=NW, window=login)
    global failpassword_label
    failpassword_label = Label(mainframe, text="", font=("Sansation", 12, "bold"), fg="red", bg="black")
    failpassword_label_window = canvas.create_window(190, 430, window=failpassword_label)


title_bar = Frame(root, relief="raised", borderwidth=0, highlightbackground="#0f0f0f", highlightthickness=2, background="#0f0f0f")
title_bar.pack(fill=X)
title_bar.bind("<B1-Motion>", move_app)

global available_label
def close_hover(e):
    if close_label['state'] == "disabled":
        title_label["image"] = ""
        title_label["fg"] = "white"
        title_label["text"] = "               Please stop the program first"

def close_leave(e):
    title_label["image"] = logo
    title_label["text"] = ""


global close_label
close_label = Button(title_bar, text="X", fg="white", bg="#0f0f0f", font=("Sansation", 12, "bold"), bd=0, command=quitter)
close_label.pack(side=RIGHT, padx=5, pady=0)
close_label.bind("<Enter>", close_hover)
close_label.bind("<Leave>", close_leave)


title_label = Label(title_bar, image=logo, bg="#0f0f0f", font=("Sansation", 12, "bold"))
title_label.pack(side=LEFT)

if __name__ == "__main__":
    mainwindows()


root.mainloop()
