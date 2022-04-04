from tkinter import *
import PIL
import os
from PIL import Image,ImageTk
import icone_wheather as ic
import meteo

root = Tk()
api_key = "34f23575919a8f66017360a416c31ce7"
m=meteo.Meteo(api_key,debug=False)
m.actualisation_var("Le Mans")

img =  ImageTk.PhotoImage(ic.PIL_icon_wheather(m.icon_weather))
print(m.icon_weather)
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()