from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image
from numpy import column_stack

import meteo
import icone_wheather as ic
"""
def comboBox_ville_selected_function():
    comboBox_ville_selected=1

    comboBox_ville.bind('<<ComboboxSelected>>', comboBox_ville_selected_function())
    comboBox_ville.pack()
combobox(['a','b','c','d'])

"""

m=meteo.Meteo("34f23575919a8f66017360a416c31ce7",debug=False)
m.actualisation_var("Le Mans")
    

def pushButton_Maj_action(*a):
    global label_Pression_var
    #print(a)
    try:
        m.actualisation_var(str(comboBox_ville_selected.get()))
        print("actualisation ...")
        label_Pression_var.set(str(m.Pbar)+" hPa")
        label_Temperature_var.set("{:.2f}".format(m.TCelsus)+" °C")
        label_Humiditer_var.set("{:.2f}".format(m.Hpourcent)+" %")
        if len(str(m.description_weather))<25:
            weather_padx=40
            label_img_weather.grid(column=0, row=1, padx=weather_padx, pady=10)
            label_Weather_etat.grid(column=1, row=1,columnspan=2, padx=weather_padx, pady=10)
        else:
            weather_padx=-10
            label_img_weather.grid(column=0, row=1, padx=weather_padx, pady=10)
            label_Weather_etat.grid(column=1, row=1,columnspan=2, padx=weather_padx, pady=10)
        label_Weather_etat_var.set("Description de la Météo : "+str(m.description_weather))
        print(m.icon_weather)
        print(m.description_weather)
        #label_img_weather["image"]=ImageTk.PhotoImage(ic.PIL_icon_wheather(m.icon_weather))
        img_weather=ImageTk.PhotoImage(ic.PIL_icon_wheather(m.icon_weather))
        label_img_weather.configure(image=img_weather)
        label_img_weather.image = img_weather
        label_Time_var.set(str(m.time_ascii))
    except KeyError:
        print(m.dict)
        label_Time_var.set(str("cette ville provoque une erreur"))
    





fenetre = Tk()#creer la fenetre

fenetre.title("Météo")#titre
#fenetre.iconbitmap("logo.ico")#logo
fenetre.config(bg = "#FFFFFF")#couleur d'arriere plan de la fenetre
fenetre.geometry("600x400")# Définir les dimensions par défaut la fenêtre principale
# Limiter les dimensions d’affichage de la fenêtre principale :
fenetre.maxsize(800,600)
fenetre.minsize(300,400)


content = ttk.Frame(fenetre)
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=600, height=400, padding=3)

"""
background_image=ImageTk.PhotoImage(Image.open("icone_pth.png"))
background_label = Label(content, image=background_image)
background_label.place(x=0, y=75, relwidth=1, relheight=1)
"""


comboBox_ville_choice_list=["Le Mans","Angers", "Paris", "Toulouse","Grenoble","Brest","Lille"]
comboBox_ville_selected=StringVar()
comboBox_ville = ttk.Combobox(content, textvariable=comboBox_ville_selected, values=comboBox_ville_choice_list)
comboBox_ville.bind('<<ComboboxSelected>>', pushButton_Maj_action)
comboBox_ville.current(0)


pushButton_Maj = ttk.Button(content, text='Actualisation', command=pushButton_Maj_action)
fenetre.bind('<Return>', lambda e: pushButton_Maj.invoke())
#pushButton_Maj.pack()

weather_frame = ttk.Frame(content, borderwidth=2, relief="ridge", width=120, height=120,padding=20)
weather_padx=50
img_weather =  ImageTk.PhotoImage(ic.PIL_icon_wheather(m.icon_weather))
print(m.icon_weather)
label_img_weather = Label(weather_frame,image = img_weather)


label_Pression_icone_var_img=ImageTk.PhotoImage(Image.open("pression.png"))
label_Pression_icone = Label(content, image = label_Pression_icone_var_img)

label_Temperature_icone_var_img=ImageTk.PhotoImage(Image.open("temperature.png"))
label_Temperature_icone = Label(content, image = label_Temperature_icone_var_img)

label_Humiditer_icone_var_img=ImageTk.PhotoImage(Image.open("humidite.png"))
label_Humiditer_icone = Label(content, image = label_Humiditer_icone_var_img)




label_Time = Label(content, text = "time")
label_Time_var=StringVar()#str de tkinter qui permet de faire des .set()
label_Time_var.set(str(m.time_ascii))
label_Time['textvariable'] = label_Time_var

label_Weather_etat = Label(weather_frame, text = "time")
label_Weather_etat_var=StringVar()#str de tkinter qui permet de faire des .set()
label_Weather_etat_var.set("Description de la Météo : "+str(m.description_weather))
label_Weather_etat['textvariable'] = label_Weather_etat_var

label_Pression = Label(content, text = "pression")
label_Pression_var=StringVar()#str de tkinter qui permet de faire des .set()
label_Pression_var.set(str(m.Pbar)+" hPa")
label_Pression['textvariable'] = label_Pression_var
#label_Pression.pack()

label_Temperature = Label(content, text = "température")
label_Temperature_var=StringVar()#str de tkinter qui permet de faire des .set()
label_Temperature_var.set("{:.2f}".format(m.TCelsus)+" °C")
label_Temperature['textvariable'] = label_Temperature_var
#label_Pression.pack()

label_Humiditer = Label(content, text = "température")
label_Humiditer_var=StringVar()#str de tkinter qui permet de faire des .set()
label_Humiditer_var.set("{:.2f}".format(m.Hpourcent)+" %")
label_Humiditer['textvariable'] = label_Humiditer_var
#label_Pression.pack()

fenetre.rowconfigure(0, weight=1)
fenetre.rowconfigure(1, weight=2)
fenetre.rowconfigure(2, weight=4)
fenetre.rowconfigure(3, weight=50)
fenetre.rowconfigure(4, weight=3)
fenetre.rowconfigure(5, weight=50)

fenetre.columnconfigure(0,weight=2, pad=2)
fenetre.columnconfigure(1,weight=1)
fenetre.columnconfigure(2,weight=1)
fenetre.columnconfigure(3,weight=1)



content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=6)
weather_frame.grid(column=0, row=1, columnspan=3, rowspan=1)

comboBox_ville.grid(column=0, row=0)
label_Pression_icone.grid(column=0, row=4)
label_Pression.grid(column=0, row=5)

pushButton_Maj.grid(column=1, row=0)
label_Temperature_icone.grid(column=1, row=4)
label_Temperature.grid(column=1, row=5)

label_Humiditer.grid(column=2,row=5)
label_Humiditer_icone.grid(column=2, row=4)
label_Time.grid(column=2, row=0)

label_img_weather.grid(column=0, row=1, padx=weather_padx, pady=10)
label_Weather_etat.grid(column=1, row=1,columnspan=2, padx=weather_padx, pady=10)

#label_pth.grid(column=1,row=2)


fenetre.mainloop()#affiche tout