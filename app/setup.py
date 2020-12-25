import tkinter as tk
from tkinter import filedialog
from .config import filename, config

def render_root():
    root = tk.Tk()
    root.resizable(False, False)
    root.iconbitmap("favicon.ico")
    root.title("Awesome tkinter")

    canvas = tk.Canvas(root, height=config.height,
                       width=config.width, bg=config.background)
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    return (root, frame)


def render_buttons(root, frame, onFileSelect):
    def openFile():
        for widget in frame.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select xls File",
            filetypes=(("Excel Files", "*.md"), ("All Files", "*.*")),
        )
        print(filename)
        label = tk.Label(frame, text=filename)
        label.pack()

    buttonFrame = tk.Frame(root)
    buttonFrame.pack(side='bottom', fill='both', padx=5, pady=5, expand=True)

    openFileButton = tk.Button(
        buttonFrame,
        text="Open File",
        padx=10,
        pady=5,
        fg="black",
        bg=config.background,
        command=openFile,
    )
    openFileButton.pack(side='left')

    runButton = tk.Button(
        buttonFrame,
        text="Run File",
        padx=10,
        pady=5,
        fg="black",
        bg=config.background,
        command=onFileSelect,
    )
    runButton.pack(side='left')

    exitButton = tk.Button(
        buttonFrame,
        text="Exit",
        padx=10,
        pady=5,
        fg="black",
        bg=config.background,
        command=root.quit,
    )
    exitButton.pack(side='right')

    return filename
