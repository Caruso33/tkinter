import tkinter as tk
from types import SimpleNamespace
from app import render_root, render_buttons

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
    (root, frame) = render_root(config)

    render_buttons(config, root, frame, filename)

    root.mainloop()


if __name__ == "__main__":
    main()
