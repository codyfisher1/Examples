from PlayerDefine import player
from Comparisons import *
from StatCollect import *
from Element_Compare import *

from tkinter import *
from tkinter import ttk
from GUI import NBA_GUI


if __name__ == "__main__":

    
    
    #Timberwolves Player Declarations
    MT_PG = player('Ricky','Rubio','PG','Timberwolves',36.91, 32.49, 44.71,
    43.16,19.96,22.04,63.02,27.32,25.78,29.61,70.65,69.72,83.15,29.55,89.25,82.61)
    MT_SG = player('Brandon','Rush','SG','Timberwolves', 20.17, 26.31, 27.59,
    13.29,8.40,14.40,9.29,13.89,37.97,22.25,51.74,35.03,56.57,3.47,57.63,96.98)
    MT_PF = player('Gorgui','Dieng','PF','Timberwolves', 37.40, 34.85, 47.96
    ,41.40,22.11,23.88,23.85,75.61,41.63,46.40,40.73,39.06,78.21,25.01,92.85,82.93)
    MT_SF = player('Andrew', 'Wiggins','SF', 'Timberwolves', 48.33, 17.12, 54.55,
    36.41,39.10,68.71,37.90,38.29,59.18,53.79,67.78,61.15,87.07,21.90,99.20,81.12)
    MT_C = player('Karl-Anthony','Towns','C','Timberwolves', 60.63, 21.99,65.68,
    56.54,40.65,53.01,30.21,85.95,64.84,61.34,75.00,61.60,89.31,43.01,98.94,73.22)
    
    Timberwolves = [MT_PG, MT_SG, MT_PF, MT_SF, MT_C]

    #Jazz Player Declarations
    UJ_PG = player('Shelvin','Mack','PG','Jazz', 31.49, 31.67, 35.82,
    20.83,21.67,44.18,45.32,22.01,28.25,22.82,60.70,60.34,57.73,6.96,62.50,92.81)
    UJ_SG = player('Joe','Ingles','SG','Jazz',29.63,35.73,35.42,
    24.08,14.82,17.47, 34.06, 30.62,32.79,27.14,74.57,49.27,58.88,10.81,81.87,88.27)
    UJ_PF = player('Boris','Diaw','PF','Jazz',23.18,30.06,28.04,
    13.44,12.63,19.20,26.62,21.06,34.77,16.52,47.52,29.03,42.26,7.39,67.79,90.06)
    UJ_SF = player('Gordon','Hayward','SF','Jazz',44.10,31.35,51.91,
    38.46,44.55,45.24,38.45,52.08,53.35,36.63,65.40,59.44,89.28,22.49,90.14,91.58)
    UJ_C = player('Rudy','Gobert','C','Jazz',45.19,41.86,55.77,
    59.77,8.91,24.54,25.62,88.53,48.71,47.65,33.25,34.62,84.40,50.73,94.23,53.02)
    
    Jazz = [UJ_PG, UJ_SG, UJ_PF, UJ_SF, UJ_C]

    #Creation of a players list
    PlayersList = [MT_PG, MT_SG,MT_PF,MT_SF,MT_C,UJ_PG,UJ_SG,UJ_PF,UJ_SF,UJ_C]

    #Execution of comparison functions
    #ComparePlayer(MT_C, PlayersList)

    #Excecution of the team comparison function
    OpenList = [0]
    CompareTeams(Timberwolves, PlayersList)
    #print((CompareTeams.PlayerStats))
    ElementSelection(CompareTeams.PlayerStats,84)
    Ch1 = ElementSelection.ElementList
    Not_Ch1 = ElementSelection.ExclusionList
    #print(Ch1)
    ElementSelection(CompareTeams.PlayerStats,1)
    Ch2 = ElementSelection.ElementList
    #print(Ch1)
    #print(Not_Ch1)
    

    ElementCompare(CompareTeams.PlayerStats)
    Comp_List = ElementCompare.ElementList
    print(Comp_List)
    print(len(Comp_List))
    #Correlation_Coef(Ch1,Ch2)
    #r_value = Correlation_Coef.r_array
    #print(r_value)
    
    
    #ElementCompare(CompareTeams.PlayerStats)
    #Comp_List = ElementCompare.ElementList
    #print(All_List)
    #print(len(All_List))
    #root = Tk()
    #NBA_GUI(root)
    #loop control(allows the loop to be started and stopped)
    #root.mainloop()

