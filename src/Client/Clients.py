from tkinter import Tk
window = Tk()


class Client(object):
    def __init__(self, width, height, title, win):
        self.width = width
        self.height = height
        self.title = title
        self.win = win

    def getWidth(self):
        """
        return width of frame
        :return: Int
        """
        return self.width

    def getHeight(self):
        """
        return height of frame
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
        self.win.geometry(f"{self.width}x{self.height}")
        self.win.title(f"{self.title}")
        self.win.mainloop()


myClient = Client(1280, 720, "Title", window)
myClient.draw()
