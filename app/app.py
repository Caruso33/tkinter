from .setup import render_root, render_buttons
from .config import filename

def run():
    def onFileSelect():
        print(filename)

    (root, frame) = render_root()

    render_buttons(root, frame, onFileSelect)

    root.mainloop()
