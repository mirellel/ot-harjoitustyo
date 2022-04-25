from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()

    window.title("testi")

    ui_view = UI(window)
    ui_view.start()

main()