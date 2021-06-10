# Import Module
from tkinter import *
from get_rating import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Movie Rating finder")
# Set geometry (widthxheight)
root.geometry('700x400')

lbl = Label(root, text = "Enter Movie Name")
lbl.grid()
# adding Entry Field
txt = Entry(root, width=15)
txt.grid(column =1, row =0)



    
def clicked():
    name = txt.get()
    score=''
    rating=''
    consensus=''
    score=get_movie_score(name)
    rating=get_imdb_rating(name)
    consensus=get_critical_consensus(name)
    plot=get_imdb_plot(name)
    movie_lbl = Label(root, text = "Rotten tomato score "+score+"%" +" IMDB Rating: "+ rating)
    movie_lbl.grid(column =0, row =1)
 #   consensus_lbl=Label(root, text="Critical Consenseus:\n"+consensus)
 #   consensus_lbl.grid(column =0, row=3)
    plot_lbl=Label(root, text = "Plot:")
    plot_lbl.grid(column =0, row =3)
    Tp = Text(root, height = 5, width = 60)
    Tp.insert(END,plot)
    Tp.grid(column=0, row = 4)
    consensus_lbl=Label(root, text = "Critical Consenseus:")
    consensus_lbl.grid(column =0, row =5)
    Tc = Text(root, height = 5, width = 60)
    Tc.insert(END,consensus)
    Tc.grid(column=0, row = 6)
# button widget with red color text
# inside
btn = Button(root, text = "Go" ,
             fg = "black", command=clicked)
# set Button grid
btn.grid(column=2, row=0)
 
# all widgets will be here
# Execute Tkinter
root.mainloop()