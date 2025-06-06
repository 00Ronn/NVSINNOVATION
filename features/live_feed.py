import tkinter as tk

class LiveFeed:
    def __init__(self):
        self.frame = None

    def run(self, root, go_back_callback=None):
        self.clear_frame()
        self.frame = tk.Frame(root, bg="#8B4513")
        self.frame.pack(fill="both", expand=True)

        if go_back_callback:
            back_button = tk.Button(
                self.frame,
                text="\u2b05 Back",
                font=("Anton", 12),
                bg="#8B4513",
                fg="white",
                activebackground="#A0522D", 
                activeforeground="white",
                relief="flat",
                command=go_back_callback
            )
            back_button.pack(anchor="nw", padx=10, pady=10)

        title = tk.Label(
            self.frame,
            text="LIVE FEED",
            font=("Anton", 20, "bold"),
            fg="white",
            bg="#8B4513"
        )
        title.pack(pady=20)
        content_label = tk.Label(
            self.frame,
            text="[Live Feed Content Placeholder]",
            font=("Anton", 14),
            fg="black",
            bg="#8B4513",
            width=50,
            height=20
        )
        content_label.pack(pady=20)

    def clear_frame(self):
        if self.frame is not None:
            self.frame.destroy()