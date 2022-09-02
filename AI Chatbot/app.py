from calendar import TextCalendar
from tkinter import *
from chatbot import response, chatbotName

BG_COLOR = "#358fde"
BG_MONOTONE = "#4d5054"
TEXT_COLOR = "#000000"

FONT_TYPE = "Helvetica 14"
FONT_BOLD = "Helvetica 12 bold"

class ChatApp:
    def __init__(self):
        self.window = Tk()
        self._setupWindow()

    def run(self):
        self.window.mainloop()

    def _setupWindow(self):
        self.window.title("Chatbot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=550, height=450, bg=BG_COLOR)

        # Head label
        headLabel = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,text="Mental Health Chatbot", 
                           font = FONT_TYPE, pady=10)
        headLabel.place(relwidth=1)

        # Divider between text head label and text bar
        line = Label(self.window,width=500, bg=BG_MONOTONE)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text bar
        self.textWidget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, 
                                font = FONT_TYPE, padx=5, pady=5)
        self.textWidget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.textWidget.configure(cursor="arrow", state=DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.textWidget)
        scrollbar.place(relheight=1, relx=0.975)
        scrollbar.configure(command=self.textWidget.yview)

        # Label at the bottom
        bottomLabel = Label(self.window, bg=BG_MONOTONE, height=80)
        bottomLabel.place(relwidth=1, rely=0.825)

        # Text entry box
        self.textEntry = Entry(bottomLabel, bg="#7bc3ed", fg=TEXT_COLOR, font=FONT_TYPE)
        self.textEntry.place(relwidth=0.74, relheight=0.06, rely=0.006, relx=0.01)
        self.textEntry.focus()
        self.textEntry.bind("<Return>", self._onEnter)

        # Send button
        sendButton = Button(bottomLabel, text="Send", font=FONT_BOLD, width=20, bg=BG_MONOTONE,
                            command=lambda: self._onEnter(None))
        sendButton.place(relx=0.77, rely=0.008, relwidth=0.22, relheight=0.06)

    # Function to enable user to enter their message with the enter key
    def _onEnter(self, event):
        txt = self.textEntry.get()
        self._insertMessage(txt, "User")

    def _insertMessage(self, txt, sender):
        if not txt:
            return
        
        # User's entry 
        self.textEntry.delete(0, END)
        txt1 = f"{sender}: {txt}\n\n"
        self.textWidget.configure(state=NORMAL)
        self.textWidget.insert(END, txt1)
        self.textWidget.configure(state=DISABLED)

        # Chatbot's reply
        txt2 = f"{chatbotName}: {response(txt)}\n\n"
        self.textWidget.configure(state=NORMAL)
        self.textWidget.insert(END, txt2)
        self.textWidget.configure(state=DISABLED)

        # Scrolls all the way down to the latest message when chatbot replies
        self.textWidget.see(END)

if __name__ == "__main__":
    app = ChatApp()
    app.run()