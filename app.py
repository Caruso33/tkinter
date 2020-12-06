import tkinter as tk
from tkinter import filedialog, Text
from types import SimpleNamespace

# globals
config = {
    "height": 700,
    "width": 700,
    "fraunhofer_green": "#179c7d",
}
config = SimpleNamespace(**config)

filename = None

# program starts here


def main():
    (root, frame) = createCanvas()

    createButtons(root, frame)

    root.mainloop()


def createCanvas():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Awesome tkinter")

    canvas = tk.Canvas(root, height=config.height,
                       width=config.width, bg=config.fraunhofer_green)
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    return (root, frame)


def createButtons(root, frame):
    def openFile():
        for widget in frame.winfo_children():
            widget.destroy()

        global filename
        filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select xls File",
            filetypes=(("Excel Files", "*.md"), ("All Files", "*.*")),
        )

        label = tk.Label(frame, text=filename)
        label.pack()

    openFileButton = tk.Button(
        root,
        text="Open File",
        padx=10,
        pady=5,
        fg="black",
        bg=config.fraunhofer_green,
        command=openFile,
    )
    openFileButton.pack()

    def runFile():
        print(filename)

    runButton = tk.Button(
        root,
        text="Run File",
        padx=10,
        pady=5,
        fg="black",
        bg=config.fraunhofer_green,
        command=runFile,
    )
    runButton.pack()

    exitButton = tk.Button(
        root,
        text="Exit",
        padx=10,
        pady=5,
        fg="black",
        bg=config.fraunhofer_green,
        command=root.quit,
    )
    exitButton.pack()

    return filename


if __name__ == "__main__":
    main()
