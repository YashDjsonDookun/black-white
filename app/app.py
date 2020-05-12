# Convert images to Black and White

import PIL.Image
import numpy as np
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo
import tkinter.ttk as ttk
import os

# Create Window
window = Tk()
window.title('Black-White')
window.geometry('500x100')
window.og = ""

def convert_image_to_bw():
    flag = False
    result = r.get()
    og_image = str(window.og)
    while (flag==False):
        if len(result) != 0:   
            #print(og_image)
            im = PIL.Image.open(og_image)
            a = np.asarray(im)
            im = PIL.Image.fromarray(a)
            bw_img = im.convert('L')
            file_extension = og_image.split(".")[1]
            index = og_image.rfind("/")
            saved_directory = og_image[:index]
            saved_at = saved_directory + "/"+ result + "_bw." + file_extension
            bw_img.save(saved_at)
            showinfo(title="Black-White", message= f"Image Successfully converted!\nSaved at: {saved_at}" )
            exit()
            break
        else:
            showerror(title="Beeepop!",message="Please give an output name!")
            flag = True

def browsefunc():
    window.og = filedialog.askopenfilename(filetypes=(("jpeg files","*.jpg"),("png file", ".png"),("All files","*.*")))
    #print(window.og)
    return window.og

b1=ttk.Button(window,text="Choose Image",command=browsefunc)
b1.grid(row=0,column=1)

original_Label = ttk.Label(window, text="Orginal Image Full Path:", foreground="blue", font=("",12))
original_Label.grid(row=0,column=0)

result_Label = ttk.Label(window, text="Name of Converted Image:", foreground="blue", font=("",12))
result_Label.grid(row=1,column=0)
r = ttk.Entry(window, width=25)
r.grid(row=1,column=1)

button = ttk.Button(window, text="Convert", command=convert_image_to_bw)
button.grid(row=2, column=0, columnspan=2)

window.mainloop()
