#################################################################
# File name:Final_Ivan_Morato_ITS200.py                         #
# Author: Ivan Morato                                           #
# Date:6-21-2021                                                #
# Classes:  ITS 220: Programming Languages & Concepts           #
# Instructor:Matthew Loschiavo                                  #
#                                                               #
# The program's objective is to identify the best user          #
# experience according to the main neighborhoods of San Diego.  #
# The user can also save a txt file,with the tour recommendation#
#                                                               #
#                                                               #
#################################################################
import PySimpleGUI as sg
import pandas as pd
from tkinter import messagebox
import pygame.mixer

sounds = pygame.mixer
sounds.init()
computer_s = sounds.Sound("welcome_Sd.wav")

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('What neighborhood do you want to visit?')],
            [sg.Input(size=(15,0),key='place')],
            [sg.Text('What experience are you looking for?')],
            [sg.Radio('Food','choise',key='food'),sg.Radio('Bar','choise',key='bar'),sg.Radio('History','choise',key='history'),sg.Radio('Website','choise',key='website'),sg.Radio('All Information','choise',key='allinfo')],
            [sg.Button('Discover',button_color=('white', 'green')),sg.Button('Txt File'),sg.Button('Restart',button_color=('white', 'black')),sg.Button('Quit',button_color=('white', 'red'))],
            [sg.Output(size=(70, 20), key='_output_')],
        ]
        # Window
        self.win = sg.Window("Enjoy San Diego").layout(layout)
        computer_s.play()

    def start(self):
        while True:
            # Data
            self.event, self.values = self.win.Read()
            self.place = (self.values['place']).lower()
            food = self.values['food']
            bar = self.values['bar']
            history = self.values['history']
            website = self.values['website']
            allinfo = self.values['allinfo']

            if self.place == 'ob':
                self.place = 'ocean beach'
            elif self.place == 'pb':
                self.place = 'pacific beach'

            while True: #Check if the txt file is available
                try:
                    sandiego_df = pd.read_excel(r"C:\Python\San_diego.xlsx", engine='openpyxl')
                    break
                except ValueError:
                    messagebox.showwarning('Alert','Please check your excel file?')

            if self.event == sg.WINDOW_CLOSED or self.event== 'Quit':
                [sg.SystemTray.notify('Enjoy San Diego', 'See you next time')]
                break

            elif self.event == 'Txt File':
                self.file()
                messagebox.showinfo('File', "The file was saved successfully")

            elif self.event == 'Restart':
                self.clear()
                messagebox.showwarning('Restart', "Your screen has restarted, please start again")

            elif self.place not in sandiego_df.values and self.event != 'Txt':
               messagebox.showinfo('Sorry',"This neighborhood doesn't exist in San Diego")

            elif food == True and self.event == 'Discover':
                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place,['food']])
                self.x=str("\nThe best restaurant in "+(self.place).capitalize()+" is "+(self.f.to_string(index=False, header=False)))
                print(self.x)

            elif bar == True:
                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place, ['bar']])
                self.x = str("\nThe best bar in " + (self.place).capitalize() + " is " + (self.f.to_string(index=False, header=False)))
                print(self.x)
            elif history == True:
                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place, ['history']])
                self.x = str("\n"+(self.place).upper() +" History: " + (self.f.to_string(index=False,header=False)))
                print(self.x)
            elif website == True:
                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place, ['website']])
                self.x = str("\nLearn more about the neighborhood of "+(self.place).capitalize()+" in "+(self.f.to_string(index=False, header=False)))
                print(self.x)

            elif allinfo == True:
                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place,['food']])
                self.x=str("\nThe best restaurant in "+(self.place).capitalize()+" is "+(self.f.to_string(index=False, header=False)))
                print(self.x)

                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place, ['bar']])
                self.x = str("\nThe best bar in " + (self.place).capitalize() + " is " + (self.f.to_string(index=False, header=False)))
                print(self.x)

                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place, ['history']])
                self.x = str("\n"+(self.place).upper() +" History: " + (self.f.to_string(index=False,header=False)))
                print(self.x)

                self.f = (sandiego_df.loc[sandiego_df['neighborhood'] == self.place, ['website']])
                self.x = str("\nLearn more about the neighborhood of "+(self.place).capitalize()+" in "+(self.f.to_string(index=False, header=False)))
                print(self.x)

            else:
                print("\nPlease select an option")

        self.win.close()

    def file(self): #txt file generator
        header = "Enjoy San Diego - America's Finest City"
        file = open("enjoy_sd.txt", "w")
        file.write(header + "\n"+self.x+'\n')
        file.close()

    def clear (self): #txt file generator
        self.win.FindElement('_output_').Update('')

tela = TelaPython()
tela.start()
tela.file()



