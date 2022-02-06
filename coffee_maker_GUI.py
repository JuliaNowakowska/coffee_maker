#!/usr/bin/env python
# coding: utf-8

# In[81]:


import tkinter as tk

root = tk.Tk()

#set up of the main window - color, title, geometry
root.geometry("%dx%d+0+0" % (0.5*root.winfo_screenwidth(), 0.5*root.winfo_screenheight()))
root.configure(background='#D7B19D')
root.title("coffee_maker")


#communication with the user
l1 = tk.Label(root, text = "Welcome to the coffe_maker!", bg = "#D7B19D", fg = "#402218", font = ("Arial", 25))
l1.place(x = 360, y = 100, anchor = "center")

l2 = tk.Label(root, text = "choose intensity of your dream coffee", bg = "#D7B19D", fg = "#402218", font = ("Arial", 18))
l2.place(x = 355, y = 135, anchor = "center")


v1 = tk.DoubleVar()
def show1():  
    """Function to display intensity value"""  
    sel = "Chosen intensity value: " + str(v1.get())
    l3 = tk.Label(root, text = sel, bg = "#D7B19D", fg = "#402218")
    l3.place(x = 360, y = 225)

    
#intensity scale
s1 = tk.Scale(root, variable = v1, from_ = 1, to = 10, orient = "horizontal",  
                 bg = "#D7B19D", fg = "#865439", troughcolor = "#D7B19D")
s1.place(x = 350, y = 150)
b1 = tk.Button(root, text = "Confirm", command = show1, bg = "#D7B19D", fg = "#865439")  



l1.pack()
l2.pack()
s1.pack()
b1.pack()

root.mainloop()

