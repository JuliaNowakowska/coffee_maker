import tkinter as tk

root = tk.Tk()

#set up of the main window - color, title, geometry
root.geometry("%dx%d+0+0" % (0.3*root.winfo_screenwidth(), 0.3*root.winfo_screenheight()))
root.configure(background='#D7B19D')
root.title("coffee_maker")


#communication with the user
l1 = tk.Label(root, text = "Welcome to the coffe_maker!", bg = "#D7B19D", fg = "#402218", font = ("Arial", 25))
#l1.place(x = 360, y = 100, anchor = "center")
l1.pack()

l2 = tk.Label(root, text = "choose intensity of your dream coffee", bg = "#D7B19D", fg = "#402218", font = ("Arial", 18))
#l2.place(x = 355, y = 135, anchor = "center")
l2.pack()


#def zmienna(x):
#    print("zmienna: " + str(x))



v1 = tk.DoubleVar()
def show1():  
    """Function to display intensity value"""  
    sel1 = "Chosen intensity value: " + str(v1.get())
    l3 = tk.Label(root, text = sel1, bg = "#D7B19D", fg = "#402218")
    l3.place(x = 140, y = 200)
    
    sel2 = "Chosen water amount: " + str(v2.get())
    l4 = tk.Label(root, text = sel2, bg = "#D7B19D", fg = "#402218")
    l4.place(x = 135, y = 220)
    
    
    zmienna(v1.get())
    

    
#intensity scale
s1 = tk.Scale(root, variable = v1, from_ = 1, to = 10, resolution = 0.1, orient = "horizontal",  
                 bg = "#D7B19D", fg = "#865439", troughcolor = "#D7B19D")
#s1.place(x = 350, y = 150)
s1.pack()


l4 = tk.Label(root, text = "choose amount of your dream coffee", bg = "#D7B19D", fg = "#402218", font = ("Arial", 18))
#l2.place(x = 355, y = 135, anchor = "center")
l4.pack()


v2 = tk.DoubleVar()
#aroma scale
s2 = tk.Scale(root, variable = v2, from_ = 60, to = 330, orient = "horizontal",  
                 bg = "#D7B19D", fg = "#865439", troughcolor = "#D7B19D")
#s1.place(x = 350, y = 150)
s2.pack()


b1 = tk.Button(root, text = "Confirm", command = show1, bg = "#D7B19D", fg = "#865439")  
b1.pack()


root.mainloop()
