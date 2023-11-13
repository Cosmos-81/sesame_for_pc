import tkinter as tk
import sesame

# セサミアプリに表示される名前
OWNER_NAME = "Owner"

class MySesameGUI:

    def __init__(self, master):
        self.master = master
        master.title("MySesame4")

        self.unlock_button = tk.Button(master, text="解錠", command=self.unlock, width=15, height=2)
        self.unlock_button.grid(row=0, column=0)

        self.lock_button = tk.Button(master, text="施錠", command=self.lock, width=15, height=2)
        self.lock_button.grid(row=0, column=1)

        self.message_label = tk.Label(master, text="")
        self.message_label.grid(row=1, column=0, columnspan=2)

    def unlock(self):
        # 解錠の処理をここに書く
        self.message_label["text"] = "Unlocking now..."
        
        if(sesame.operation_sesame(OWNER_NAME, 83)):
            self.message_label["text"] = "Unlocking success!"
        else:
            self.message_label["text"] = "Unlocking failed..."
        pass

    def lock(self):
        # 施錠の処理をここに書く
        self.message_label["text"] = "Locking now..."

        if(sesame.operation_sesame(OWNER_NAME, 82)):
            self.message_label["text"] = "Locking success!"
        else:
            self.message_label["text"] = "Locking failed..."
        pass

root = tk.Tk()
my_gui = MySesameGUI(root)
root.mainloop()