import tkinter as tk
import font_manager as fonts
from f_viewtracks import TrackViewer
from f_createtrack import CreateTrackListGUI
from f_updatetrack import UpdateTracksGUI
from f_jukebox import SearchTracksGUI

class MainJukeboxGUI:
    def __init__(self, window):
        window.geometry("500x200")
        window.title("The Music Box")
        window.configure(bg="white")

        label = tk.Label(window, text="Select an option by clicking one of the buttons below", bg="white", fg="black", font=("Helvetica", 12))
        label.pack(pady=15)

        btn_frame = tk.Frame(window, bg="white")
        btn_frame.pack()

        view_btn = tk.Button(btn_frame, text="View Tracks", width=20, command=self.open_view)
        view_btn.grid(row=0, column=0, padx=10, pady=5)

        create_btn = tk.Button(btn_frame, text="Create Track List", width=20, command=self.open_create)
        create_btn.grid(row=0, column=1, padx=10, pady=5)

        update_btn = tk.Button(btn_frame, text="Update Tracks Rating", width=20, command=self.open_update)
        update_btn.grid(row=1, column=0, padx=10, pady=5)

        search_btn = tk.Button(btn_frame, text="Search and Add Tracks", width=20, command=self.open_search)
        search_btn.grid(row=1, column=1, padx=10, pady=5)

    def open_view(self):
        win = tk.Toplevel()
        TrackViewer(win)

    def open_create(self):
        win = tk.Toplevel()
        CreateTrackListGUI(win)

    def open_update(self):
        win = tk.Toplevel()
        UpdateTracksGUI(win)

    def open_search(self):
        win = tk.Toplevel()
        SearchTracksGUI(win)

if __name__ == "__main__":
    root = tk.Tk()
    fonts.configure()
    MainJukeboxGUI(root)
    root.mainloop()
