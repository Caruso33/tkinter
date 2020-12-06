from app import render_root, render_buttons, config


# globals
filename = None


# program starts here
def main():
    (root, frame) = render_root(config)

    render_buttons(config, root, frame, filename)

    root.mainloop()


if __name__ == "__main__":
    main()
