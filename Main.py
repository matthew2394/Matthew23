import time
import tkinter as tk

class TypingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing App")
        self.text_to_type = "..."
        self.current_input = ""
        self.start_time = 0

        self.label_text = tk.StringVar()
        self.label = tk.Label(self.root, textvariable=self.label_text)
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.focus_set()

        self.entry.bind("<Key>", self.key_pressed)

    def key_pressed(self, event):
        if self.start_time == 0:
            self.start_time = time.time()

        self.current_input += event.char
        self.label_text.set(self.current_input)

        if self.current_input == self.text_to_type:
            elapsed_time = time.time() - self.start_time
            typing_speed = len(self.text_to_type) / elapsed_time
            self.label_text.set("Succeed! typing speed: {:.2f} characters per second".format(typing_speed))

    def run(self):
        self.root.mainloop()

app = TypingApp()
app.run()
