from tkinter import Tk, Menu, Text, filedialog, INSERT
import os


def QuitFrame():
    quit()


def Open():
    """
    Open a file for reading
    :return: Str
    """
    fileName = filedialog.askopenfile(initialdir="/", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                      title="Choose a file."
                                      )

    file = open(fileName, 'r')
    f = file.readlines()
    t.inser(INSERT, f.read())


class Clients(object):
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def getWidth(self):
        """
        returns the width of the frame
        :return: Int
        """
        return self.width

    def getHeight(self):
        """
        returns the height of the frame
        :return: Int
        """
        return self.height

    def getTitle(self):
        """
        return the title of the frame
        :return: Str
        """
        return self.title

    def draw(self):
        win = Tk()
        win.geometry(f"{self.getWidth()}x{self.getHeight()}")
        win.title(f"{self.getTitle()}")

        menubar = Menu(win)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=Open)
        filemenu.add_command(label="New", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Save", command="")
        filemenu.add_command(label="Save As", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=QuitFrame)
        menubar.add_cascade(label="File", menu=filemenu)

        T = Text(win, width=self.width, height=self.height)
        T.pack()
        win.config(menu=menubar)
        win.mainloop()


myClient = Clients(1280, 720, "Editor")
myClient.draw()
