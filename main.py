import tkinter as tk
from view.app import App

def main():
    root = tk.Tk()
    root.geometry("500x400")
    App(root).pack(expand=True, fill='both')
    root.mainloop()


if __name__ == '__main__':
    main()

