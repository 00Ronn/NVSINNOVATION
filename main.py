import tkinter as tk
from ttkbootstrap import Style, Button
from tkinter import messagebox
from features.live_feed import LiveFeed
from features.binds_setup import BindsSetup
from features.contacts_setup import ContactsSetup
from features.logs_viewer import LogsViewer
from features.graphs_viewer import GraphsViewer

class NVSInnovationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NVSINNOVATION")
        self.root.geometry("800x600")
        self.root.configure(bg="#5a8de0")
        self.features = {
            "live_feed": LiveFeed(),
            "binds": BindsSetup(),
            "contacts": ContactsSetup(),
            "logs": LogsViewer(),
            "graphs": GraphsViewer()
        }

        self.response_label = tk.Label(
            root, text="", font=("Anton", 12), bg="white", fg="black",
            wraplength=500, justify="center"
        )
        self.response_label.place(relx=0.5, y=100, anchor="center")
        self.response_label.place_forget()

        self.add_about_us()
        self.add_feature_buttons()

    def add_about_us(self):
        def show_about():
            messagebox.showinfo("About Us", "Developed by NVSINNOVATION – 2025")

        about_frame = tk.Frame(self.root, bg="#5a8de0")
        about_frame.place(relx=1.0, x=-20, y=20, anchor="ne")

        icon = tk.Label(
            about_frame, text="\u2139", font=("FontAwesome", 20), fg="black",
            bg="#5a8de0", width=4, height=2, relief="solid", borderwidth=2
        )
        icon.bind("<Button-1>", lambda e: show_about())
        icon.pack()

        label = tk.Label(
            about_frame, text="ABOUT US", font=("Anton", 8), fg="white", bg="#5a8de0"
        )
        label.pack()

    def add_feature_buttons(self):
        self.button_frame = tk.Frame(self.root, bg="#5a8de0")
        self.button_frame.place(relx=0.5, rely=1.0, y=-80, anchor="s")

        buttons = [
            ("LIVE FEED", "warning", "live_feed"),
            ("SETUP/UPDATE\nBINDS", "success", "binds"),
            ("SETUP/UPDATE\nCONTACTS", "info", "contacts"),
            ("LOGS", "light", "logs"),
            ("VIEW\nGRAPHS", "primary", "graphs"),
            ("CLOSE", "danger", "close")
        ]

        for text, style, action in buttons:
            btn = Button(
                self.button_frame,
                text=text,
                width=14,
                bootstyle=style,
                command=lambda a=action: self.trigger_feature(a),
                padding=10
            )
            btn.pack(side="left", padx=10, pady=10)

    def trigger_feature(self, key):
        if key == "close":
            self.root.destroy()
            return
        feature = self.features.get(key)
        if feature:
            if key in ("live_feed", "contacts"):
                self.button_frame.place_forget()
                self.response_label.place_forget()
                result = feature.run(self.root, self.back_to_main)
            else:
                result = feature.run()
            if isinstance(result, str):
                self.response_label.config(text=result)
                self.response_label.place(relx=0.5, y=100, anchor="center")
            elif key not in ("live_feed", "contacts"):
                self.response_label.place_forget()
        else:
            self.response_label.config(text="Invalid Feature")
            self.response_label.place(relx=0.5, y=100, anchor="center")

    def back_to_main(self):
        for feature in self.features.values():
            if hasattr(feature, 'clear_frame'):
                feature.clear_frame()
        self.button_frame.place(relx=0.5, rely=1.0, y=-80, anchor="s")
        self.response_label.place_forget()

if __name__ == "__main__":
    style = Style("flatly")
    root = style.master
    root.option_add("*TButton.Font", "Anton 10")
    app = NVSInnovationApp(root)
    root.mainloop()