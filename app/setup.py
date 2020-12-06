import tkinter as tk
from tkinter import Grid, filedialog


def render_root(config):
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


def render_buttons(config, root, frame, filename):
    def openFile():
        for widget in frame.winfo_children():
            widget.destroy()

        global filename
        filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select xls File",
            filetypes=(("Excel Files", "*.xls"), ("All Files", "*.*")),
        )

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

    def runFile():
        global filename
        print(filename)

    runButton = tk.Button(
        buttonFrame,
        text="Run File",
        padx=10,
        pady=5,
        fg="black",
        bg=config.background,
        command=runFile,
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
