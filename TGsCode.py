# We import tkinter to make a window
from tkinter import *  # import * removes the need of typing tkinter. again and again
from tkinter import ttk  # Allows to make elements like dropdowns
from tkinter import messagebox

bg = "#AEE5D8"

root = Tk()  # Here root is a variable which holds the window

# Adding clicking values
clicked = StringVar()
clicked.set('Select a genre')

clicked2 = StringVar()
clicked2.set('Select your age group')

genreoptions = ['Adventure', 'Sci-Fi', 'Romance', 'Comedy', 'Horror']
ageoptions = ['PG-13', 'PG-16', 'PG-18', 'Kids']

root.geometry("500x400")  # to size the window
root.resizable(False, False)  # expanding the window won't work
root.configure(bg=bg)
img = PhotoImage(file="favicon.png")
root.iconphoto(False, img)


def searchmovies():
    gom = clicked.get()
    agegroup = clicked2.get()
    root.destroy()

    global movies

    if gom == "Adventure":
        if agegroup == "PG-13":
            movies = ["Avatar: The Way of the Water (2022)", "Jung E (2023)",
                      "Ant-Man and the Wasp: Quantumania (2023)", "The Wandering Earth II (2023)"]
        if agegroup == "PG-16":
            movies = ["Everything Everywhere All at Once (2022)", "Vesper (2022)",
                      "The Northman (2022)", "The Mummy (1999)", "Gladiator (2000)"]
        if agegroup == "PG-18":
            movies = ["American Psycho (2000)", "Inglourious Basterds (2009)", "Game Of Thrones (2011-2019)",
                      "The Legends of Vox Machina (2022)", "House of The Dragon (2022)"]
        if agegroup == "Kids":
            movies = ["A Bug's Life (2022)", "The Land Before (1988)", "Ratatouille (2007)",
                      "The Jungle Book 2 (2003)", "Horton Hears a Who! (2008)"]

    if gom == "Sci-Fi":
        if agegroup == "PG-13":
            movies = ["Oxygen (2021)", "Dune (2021)",
                      "The Adam Project (2022)", "Morbius (2022)", "Tenet (2022)"]
        if agegroup == "PG-16":
            movies = ["Nope (2022)", "Jiu Jitsu (2020)", "The Matrix Resurrections (2021)",
                      "Free Guy (2021)", "Jurassic World Dominion (2022)"]
        if agegroup == "PG-18":
            movies = ["Bliss (2021)", "The Platform 2019", "Annihilation (2018)",
                      "Army of the Dead (2021)", "Lucy in the Sky (2019)"]
        if agegroup == "Kids":
            movies = ["DC League of Super Pets (2022)", "We Can Be Heroes (2020)", "Sonic the Hedgehog 2 (2022)",
                      "Spider-Man into the Spider Verse (2018)", "The Incredibles 2"]

    if gom == "Romance":
        if agegroup == "PG-13":
            movies = ["The Proposal (2009)", "Ticket to Paradise (2022)",
                      "How to Lose a Guy (2003)", "Just Go With It (2011)", "Twilight (2008)"]
        if agegroup == "PG-16":
            movies = ["West Side Story (2021)", "La La Land (2016)",
                      "The Choice (2016)", "Adrift (2018)", "The Holiday (2006)"]
        if agegroup == "PG-18":
            movies = ["About Fate (2022)", "The Shape of Water (2017)", "About time (2013)",
                      "The Hating Game (2021)", "Friends With Benefits (2011)"]
        if agegroup == "Kids":
            movies = ["Abominable (2019)", "Beauty and the Beast (2017)",
                      "Aladdin (2019)", "Frozen 2 (2019)", "Anastasia (1997)"]

    if gom == "Comedy":
        if agegroup == "PG-13":
            movies = ["Dog (2022)", "Red Notice (2021)", "Despicable (2010)",
                      "Fighting with my family (2019)", "The Mask (1994)"]
        if agegroup == "PG-16":
            movies = ["Amsterdam (2022)", "The Menu (2022)", "Free Guy (2021)",
                      "Bullet Train (2022)", "Bodies Bodies Bodies (2022)"]
        if agegroup == "PG-18":
            movies = ["Jump Street (2012)", "The Hangover (2009)", "Bridesmaid (2011)",
                      "Funny People (2009)", "American Reunion (2012)"]
        if agegroup == "Kids":
            movies = ["Encanto (2021)", "Ice Age (2002)", "Shrek (2001)",
                      "Home Alone (1990)", "Boss Baby (2017)"]

    if gom == "Horror":
        if agegroup == "PG-13":
            movies = ["The invitation (2022)", "Signs (2002)", "Carriers (2009)",
                      "The Mothman Prophecies (2002)", "The Woman In Black (2012)"]
        if agegroup == "PG-16":
            movies = ["Train to Busan (2016)", "The Prodigy (2019)",
                      "Sinister (I) (2012)", "Flatliners (2017)", "Crawl (I) (2019)"]
        if agegroup == "PG-18":
            movies = ["Cam (2018)", "V/H/S (2012)", "The Autopsy of Jane Doe (2016)",
                      "Midsommar (2019)", "Videodrome (1983)"]
        if agegroup == "Kids":
            movies = ["Monster House (2006)", "Frankenweenie (2012)",
                      "Casper (1995)", "Hocus Pocus (1993)", "Beetlejuice (1988)"]


g = Label(root, text="What is the genre of the movie you want to watch?", font=(
    "Montserrat", 12), bg=bg).place(x=25, y=100)  # label makes a text

genre = ttk.Combobox(root, textvariable=clicked, value=genreoptions)
genre['state'] = 'readonly'  # so that the user cannot edit the options
genre.place(x=100, y=150)  # since we need to interact with the variable genre

Title = Label(root, text="Movie Owl", font=("Montserrat", 20),
              bg=bg).place(x=170, y=25)  # label makes a text

a = Label(root, text="What is your age group?", font=(
    "Montserrat", 12), bg=bg).place(x=25, y=200)  # label makes a text

age = ttk.Combobox(root, textvariable=clicked2, value=ageoptions)
age['state'] = 'readonly'  # so that the user cannot edit the options
age.place(x=100, y=250)  # since we need to interact with the variable genre

confirm = Button(root, text="Confirm", height=2, width=20, font=(
    "Montserrat", 10), bg="#E7E5E5", command=searchmovies)
confirm.place(x=150, y=300)

root.title('MovieOwl')
root.mainloop()  # mainloop is for the window to stay and not close imediately

root = Tk()
root.geometry("500x400")  # to size the window
root.resizable(False, False)  # expanding the window won't work
root.configure(bg=bg)
img = PhotoImage(file="favicon.png")
root.iconphoto(False, img)

try:
    listToStr = '\n\n'.join(map(str, movies))
except NameError:
    root.destroy()
    messagebox.showerror('Error', 'Please insert a movie genre and age group')

title = Label(root, text="Movie Recommendations", font=(
    "Montserrat", 25), bg=bg).place(x=35, y=25)  # label makes a text
movieslist = Label(root, text=listToStr, font=("Montserrat", 15),
                   bg=bg, justify=LEFT).place(x=60, y=100)  # label makes a text

root.title('MovieOwl')
root.mainloop()