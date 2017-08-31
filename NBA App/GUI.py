from tkinter import *
from tkinter import ttk
from Comparisons import *
from pass_button import pass_button


class NBA_GUI:
    
    def __init__(self, master):
        master.geometry('1075x700')
        master.title('NBA_GUI')
    

        #Base Frame
        GUIFrame = ttk.Frame(master)
        GUIFrame.grid(row =0, column = 0, sticky = W)

        #Graphic Canvas
        img = PhotoImage(file ="C:/Users/Cody Fisher/Documents/Third Evolution/Code/Third_Evo/NBA App/court1.GIF")
        master.img = img

        Label1  = Label(GUIFrame, image = img)
        #Label1.create_image(image = img, anchor = 'center')
        Label1.grid(row =4, column =3, pady = 30)

        #Dropdown lists (row = 0 - 2, column 2 - 4)
        combobox1 = ttk.Combobox(GUIFrame)
        combobox1['values'] = ('Ricky Rubio (PG)','Brandon Rush (SG)','Gorgui Dieng (PF)',
        'Andrew Wiggins (SF)','Karl-Anthony Towns (C)','Shelvin Mack (PG)','Joe Ingles (SG)','Boris Diaw (PF)',
        'Gordon Hayward (SF)','Rudy Gobert (C)')
        combobox1.grid(row = 1, column = 3, sticky = W)

        combobox3 = ttk.Combobox(GUIFrame)
        combobox3['values'] = ('Timberwolves', 'Jazz' )
        combobox3.grid(row = 1, column = 3, sticky = N)

        combobox2 = ttk.Combobox(GUIFrame)
        combobox2['values'] = ('Ricky Rubio (PG)','Brandon Rush (SG)','Gorgui Dieng (PF)',
        'Andrew Wiggins (SF)','Karl-Anthony Towns (C)','Shelvin Mack (PG)','Joe Ingles (SG)','Boris Diaw (PF)',
        'Gordon Hayward (SF)','Rudy Gobert (C)')
        combobox2.grid(row = 1, column = 3, sticky = E)

        #Dropdown lists Label
        Label1 = ttk.Label(GUIFrame, text='Player', font = '16')
        Label1.grid(row = 0, column = 3, sticky =W)

        Label2 = ttk.Label(GUIFrame, text='Opposing Team', font = '16')
        Label2.grid(row = 0, column = 3, sticky =N)

        Label3 = ttk.Label(GUIFrame, text='Opposing Player', font = '16')
        Label3.grid(row = 0, column = 3, sticky =E)

        Button2 = ttk.Button(GUIFrame, text = 'Compare', command = pass_button)
        Button2.grid(row =  2, column = 3, sticky = N)

        Button2 = ttk.Button(GUIFrame, text = 'Compare', command = pass_button)
        Button2.grid(row =  2, column = 3, sticky = E)

        #PLayer Box
        pointgaurdbox = ttk.Frame(GUIFrame)
        pointgaurdbox.grid(row = 5, column = 3, sticky = N)

        pointgaurdlabel = ttk.Label(pointgaurdbox, text = 'Opposing PG', font = '16')
        pointgaurdlabel.pack()

        centerbox = ttk.Frame(GUIFrame)
        centerbox.grid(row = 3, column = 4, sticky = E)

        centerlabel = ttk.Label(centerbox, text = 'Opposing C', font = '16')
        centerlabel.pack()

        shootingforwardbox = ttk.Frame(GUIFrame)
        shootingforwardbox.grid(row = 4, column = 2, sticky = S)

        shootingforwardlabel = ttk.Label(shootingforwardbox, text = 'Opposing SF', font = '16')
        shootingforwardlabel.pack()

        powerforwardbox = ttk.Frame(GUIFrame)
        powerforwardbox.grid(row = 3, column = 2, sticky = W)

        powerforwardlabel = ttk.Label(powerforwardbox, text = 'Opposing PF', font = '16')
        powerforwardlabel.pack()

        shootinggaurdbox = ttk.Frame(GUIFrame)
        shootinggaurdbox.grid(row = 4, column = 4, sticky = S)

        shootinggaurdlabel = ttk.Label(shootinggaurdbox, text = 'Opposing SG', font = '16')
        shootinggaurdlabel.pack()

        Pointguardtext1 = Label(pointgaurdbox,text = 'Total Player Advantage: + str(round(Total_Player_Adv,2)', fg = 'green')
        Pointguardtext1.pack()

        Pointguardtext2 = Label(pointgaurdbox,text = 'Player Offense Advantage: + str(round(off_Adv,2)', fg = 'green')
        Pointguardtext2.pack()

        Pointguardtext3 = Label(pointgaurdbox,text = 'Player Offense Advantage: + str(round(def_Adv,2)', fg = 'red')
        Pointguardtext3.pack()

        shootinggaurdtext1 = Label(shootinggaurdbox,text = 'Total Player Advantage: + str(round(Total_Player_Adv,2)', fg = 'red')
        shootinggaurdtext1.pack()

        shootingguardtext2 = Label(shootinggaurdbox,text = 'Player Offense Advantage: + str(round(off_Adv,2)', fg = 'red')
        shootingguardtext2.pack()

        shootingguardtext3 = Label(shootinggaurdbox,text = 'Player Offense Advantage: + str(round(def_Adv,2)', fg = 'red')
        shootingguardtext3.pack()

        shootingforwardtext1 = Label(shootingforwardbox,text = 'Total Player Advantage: + str(round(Total_Player_Adv,2)', fg = 'green')
        shootingforwardtext1.pack()

        shootingforwardtext2 = Label(shootingforwardbox,text = 'Player Offense Advantage: + str(round(off_Adv,2)', fg = 'green')
        shootingforwardtext2.pack()

        shootingforwardtext3 = Label(shootingforwardbox,text = 'Player Offense Advantage: + str(round(def_Adv,2)', fg = 'red')
        shootingforwardtext3.pack()

        powerforwardtext1 = Label(powerforwardbox,text = 'Total Player Advantage: + str(round(Total_Player_Adv,2)', fg = 'green')
        powerforwardtext1.pack()

        powerforwardtext2 = Label(powerforwardbox,text = 'Player Offense Advantage: + str(round(off_Adv,2)', fg = 'red')
        powerforwardtext2.pack()

        powerforwardtext3 = Label(powerforwardbox,text = 'Player Offense Advantage: + str(round(def_Adv,2)', fg = 'red')
        powerforwardtext3.pack()

        centertext1 = Label(centerbox,text = 'Total Player Advantage: + str(round(Total_Player_Adv,2)', fg = 'green')
        centertext1.pack()

        centertext2 = Label(centerbox,text = 'Player Offense Advantage: + str(round(off_Adv,2)', fg = 'green')
        centertext2.pack()

        centertext3 = Label(centerbox,text = 'Player Offense Advantage: + str(round(def_Adv,2)', fg = 'green')
        centertext3.pack()
        