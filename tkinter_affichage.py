from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image

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
    

def pushButton_Maj_action():
    global label_Pression_var
    try:
        m.actualisation_var(str(comboBox_ville_selected.get()))
        print("actualisation ...")
        label_Pression_var.set(str(m.Pbar)+" hPa")
        label_Temperature_var.set(str(m.TCelsus)+" °C")
        print(m.icon_weather)
        #label_img_weather["image"]=ImageTk.PhotoImage(ic.PIL_icon_wheather(m.icon_weather))
        img_weather=ImageTk.PhotoImage(ic.PIL_icon_wheather(m.icon_weather))
        label_img_weather.configure(image=img_weather)
        label_img_weather.image = img_weather
    except KeyError:
        print(m.dict)
    





fenetre = Tk()#creer la fenetre

fenetre.title("Météo")#titre
#fenetre.iconbitmap("logo.ico")#logo
fenetre.config(bg = "#FFFFFF")#couleur d'arriere plan de la fenetre
fenetre.geometry("600x400")# Définir les dimensions par défaut la fenêtre principale
# Limiter les dimensions d’affichage de la fenêtre principale :
fenetre.maxsize(800,600)
fenetre.minsize(300,400)
fenetre.rowconfigure(0, weight=1)
fenetre.rowconfigure(1, weight=2)
fenetre.rowconfigure(2, weight=4)
fenetre.rowconfigure(3, weight=50)
fenetre.rowconfigure(4, weight=3)
fenetre.rowconfigure(5, weight=50)

content = ttk.Frame(fenetre)
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=600, height=400)

background_image=ImageTk.PhotoImage(Image.open("icone_pth.png"))
background_label = Label(content, image=background_image)
background_label.place(x=0, y=50, relwidth=1, relheight=1)



comboBox_ville_choice_list=["Le Mans","Anger", "Paris", "Toulouse","Grenoble","Brest","Lille"]
comboBox_ville_selected=StringVar()
comboBox_ville = ttk.Combobox(content, textvariable=comboBox_ville_selected, values=comboBox_ville_choice_list)
comboBox_ville.current(0)

pushButton_Maj = ttk.Button(content, text='Actualisation', command=pushButton_Maj_action)
fenetre.bind('<Return>', lambda e: pushButton_Maj.invoke())
#pushButton_Maj.pack()

wheather_frame = ttk.Frame(content, borderwidth=2, relief="ridge", width=120, height=120)
img_weather =  ImageTk.PhotoImage(ic.PIL_icon_wheather(m.icon_weather))
print(m.icon_weather)
label_img_weather = Label(wheather_frame,image = img_weather)
wheather_frame.grid(column=0, row=1)
"""
img_pth = ImageTk.PhotoImage(Image.open("icone_pth.png"))
label_pth = Label(content, image = img_pth)
"""

label_Pression = Label(content, text = "pression")
label_Pression_var=StringVar()#str de tkinter qui permet de faire des .set()
label_Pression_var.set(str(m.Pbar)+" hPa")
label_Pression['textvariable'] = label_Pression_var
#label_Pression.pack()

label_Temperature = Label(content, text = "température")
label_Temperature_var=StringVar()#str de tkinter qui permet de faire des .set()
label_Temperature_var.set(str(m.TCelsus)+" °C")
label_Temperature['textvariable'] = label_Temperature_var
#label_Pression.pack()

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=9, rowspan=6)
comboBox_ville.grid(column=0, row=0)
pushButton_Maj.grid(column=1, row=0)
label_Pression.grid(column=0, row=5)
label_Temperature.grid(column=1, row=5)
label_img_weather.grid(column=0, row=1)
#label_pth.grid(column=1,row=2)


fenetre.mainloop()#affiche tout