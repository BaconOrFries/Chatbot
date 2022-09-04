from tkinter import *
from chatbot import response, chatbotName

FONT_BOLD = "Helvetica 12 bold"
window_size="560x500"

class ChatApp(Frame):
    def __init__(self):
        self.window = Tk()
        self._setupWindow()

    def run(self):
        self.window.mainloop()

    def _setupWindow(self, master=None):
        Frame.__init__(self,master)
        
        self.window.title("Chatbot")
        self.window.geometry(window_size)
        self.font = "Helvetica 12"
        self.bgColour = "#358fde"
        self.bgMono = "#ccdced"
        self.textColour = "#000000"
        self.textBoxColour = "#7bc3ed"

        self.textFrame = Frame(self.master, bd=6)
        self.textFrame.pack(expand=True,fill=BOTH)

        # Scrollbar
        scrollbar = Scrollbar(self.textFrame, bd=0)
        scrollbar.pack(fill=Y, side=RIGHT)

        # Text bar
        self.textWidget = Text(self.textFrame, yscrollcommand=scrollbar.set, width=20, height=2, bg=self.bgColour, fg=self.textColour, 
                                font = "Helvetica 12", padx=5, pady=5, wrap=WORD)
        self.textWidget.pack(expand=True, fill=BOTH)
        self.textWidget.configure(cursor="arrow")
        self.textWidget.configure(state=DISABLED)
        scrollbar.configure(command=self.textWidget.yview)
        
        # Frame for text entry box
        self.textEntryFrame = Frame(self.window, bg=self.bgMono, bd=1)
        self.textEntryFrame.pack(side=LEFT, fill=BOTH, expand=True)

        # Text entry box
        self.textEntry = Entry(self.textEntryFrame, bg=self.textBoxColour, fg=self.textColour, font="Helvetica 12", bd=1, justify=LEFT)
        self.textEntry.pack(fill=X, padx=6, pady=6, ipady=8)
        self.textEntry.focus()
        self.textEntry.bind("<Return>", self.onEnter)

        # Frame for send message button
        sendButtonFrame = Frame(self.window, bd=0)
        sendButtonFrame.pack(fill=BOTH)

        # Send button
        self.sendButton = Button(sendButtonFrame, text="SEND", font=FONT_BOLD, width=20, bg=self.bgMono, fg=self.textColour,
                            command=lambda: self.onEnter(None))
        self.sendButton.pack(side=LEFT, padx=6, pady=6, ipady=6)

        # Menu bar
        myMenu = Menu(self.window)
        self.window.config(menu=myMenu)

        # File menu
        fileMenu = Menu(myMenu, tearoff=0)
        myMenu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Clear Chat", command=self.clear)
        fileMenu.add_command(label="Exit", command=self.window.quit)

        # Options menu
        options = Menu(myMenu, tearoff=0)
        myMenu.add_cascade(label="Options", menu=options) 

        # Varying font sizes under options
        fontSize = Menu(options,tearoff=0)
        options.add_cascade(label="Font Size", menu=fontSize)     
        fontSize.add_command(label="12", command=self.fontSize12)
        fontSize.add_command(label="14", command=self.fontSize14)
        fontSize.add_command(label="16", command=self.fontSize16)
        fontSize.add_command(label="18", command=self.fontSize18)
        fontSize.add_command(label="20", command=self.fontSize20)   

        # Varying colour under options   
        chatColour = Menu(options, tearoff=0)
        options.add_cascade(label="Colour Theme", menu=chatColour)
        chatColour.add_command(label="Default", command=self.theme1)
        chatColour.add_command(label="Accessible", command=self.theme2)
        chatColour.add_command(label="Light Mode", command=self.theme3)
        chatColour.add_command(label="Dark Mode", command=self.theme4)

    # Function to clear all messages in the text box
    def clear(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.delete(1.0, END)
        self.textWidget.configure(state=DISABLED)

    # Function to enable user to enter their message with the enter key
    def onEnter(self, event):
        txt = self.textEntry.get()
        self.insertMessage(txt, "You")

    # Function to input user and chatbot's message into text box
    def insertMessage(self, txt, sender):
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

    # Varying font sizes so users can enlarge their message if necessary 
    def fontSize12(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(font="Helvetica 12")
        self.textEntry.config(font="Helvetica 12")
        self.font = "Helvetica 12"
        self.textWidget.configure(state=DISABLED)    
    def fontSize14(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(font="Helvetica 14")
        self.textEntry.config(font="Helvetica 14")
        self.font= "Helvetica 14"
        self.textWidget.configure(state=DISABLED)
    def fontSize16(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(font="Helvetica 16")
        self.textEntry.config(font="Helvetica 16")
        self.font = "Helvetica 16"
        self.textWidget.configure(state=DISABLED)
    def fontSize18(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(font="Helvetica 18")
        self.textEntry.config(font="Helvetica 18")
        self.font = "Helvetica 18"
        self.textWidget.configure(state=DISABLED)
    def fontSize20(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(font="Helvetica 20")
        self.textEntry.config(font="Helvetica 20")
        self.font = "Helvetica 20"
        self.textWidget.configure(state=DISABLED)
       
    # Varying colour palette for user depending on their mood, black and white for colourblind user.   
    def theme1(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(bg="#358fde", fg="#000000")
        self.textEntry.config(bg="#7bc3ed", fg="#000000")
        self.textEntryFrame.config(bg="#ccdced")
        self.sendButton.config(bg="#ccdced", fg="#000000")
        self.textWidget.configure(state=DISABLED)
    def theme2(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(bg="#FFC20A", fg="#0C7BDC")
        self.textEntry.config(bg="#FFC20A", fg="#0C7BDC")
        self.textEntryFrame.config(bg="#d55e00")
        self.sendButton.config(bg="#FFC20A", fg="#0C7BDC")
        self.textWidget.configure(state=DISABLED)
    def theme3(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(bg="#e4e5e1", fg="#000000")
        self.textEntry.config(bg="#e4e5e1", fg="#000000")
        self.textEntryFrame.config(bg="#d2d3db")
        self.sendButton.config(bg="#d2d3db", fg="#000000")
        self.textWidget.configure(state=DISABLED)
    def theme4(self):
        self.textWidget.configure(state=NORMAL)
        self.textWidget.config(bg="#3A3B3C", fg="#E4E6EB")
        self.textEntry.config(bg="#3A3B3C", fg="#E4E6EB")
        self.textEntryFrame.config(bg="#242526")
        self.sendButton.config(bg="#3A3B3C", fg="#E4E6E8")
        self.textWidget.configure(state=DISABLED)

if __name__ == "__main__":
    app = ChatApp()
    app.run()