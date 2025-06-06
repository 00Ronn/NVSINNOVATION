import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox
from threading import Thread
from dataclasses import dataclass
from typing import Union, List

@dataclass
class Camera:
    name: str
    source: Union[int, str]

class BindsSetup:
    def run(self):
        class CameraManagerGUI:
            def __init__(self):
                self._cameras: List[Camera] = []
                self.root = tk.Tk()
                self.root.title("Binds Setup")
                self.root.configure(bg='#2e3f4f')
                self.root.geometry("400x400")

                self.listbox = tk.Listbox(self.root, width=50)
                self.listbox.pack(pady=10)

                tk.Button(self.root, text="Add Camera", command=self.add_camera, bg='#5cb85c', fg='white').pack(pady=5)
                tk.Button(self.root, text="Remove Selected", command=self.remove_camera, bg='#d9534f', fg='white').pack(pady=5)
                tk.Button(self.root, text="Watch Selected", command=self.watch_camera, bg='#0275d8', fg='white').pack(pady=5)

                self.update_listbox()
                self.root.mainloop()

            def add_camera(self):
                name = simpledialog.askstring("Camera Name", "Enter camera name:", parent=self.root)
                if not name:
                    return
                src = simpledialog.askstring("Camera Source", "Enter index (0/1) or URL:", parent=self.root)
                if src is None:
                    return
                source = int(src) if src.isdigit() else src
                self._cameras.append(Camera(name, source))
                self.update_listbox()

            def remove_camera(self):
                idx = self.listbox.curselection()
                if not idx:
                    return
                self._cameras.pop(idx[0])
                self.update_listbox()

            def update_listbox(self):
                self.listbox.delete(0, tk.END)
                for cam in self._cameras:
                    self.listbox.insert(tk.END, f"{cam.name} → {cam.source}")

            def watch_camera(self):
                idx = self.listbox.curselection()
                if not idx:
                    return
                cam = self._cameras[idx[0]]
                Thread(target=self._show_camera_feed, args=(cam,), daemon=True).start()

            def _show_camera_feed(self, cam: Camera):
                cap = cv2.VideoCapture(cam.source)
                if not cap.isOpened():
                    messagebox.showerror("Error", "Unable to open camera feed.")
                    return
                window_name = f"Live: {cam.name}"
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    cv2.imshow(window_name, frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyWindow(window_name)

        CameraManagerGUI()