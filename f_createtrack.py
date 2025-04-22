import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib

class CreateTrackListGUI():
    def __init__(self, window):
        window.geometry("600x400")
        window.title("Create Track List")

        self.playlist = []  # Danh sách track number

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        self.add_btn = tk.Button(window, text="Add to Playlist", command=self.add_track)
        self.add_btn.grid(row=0, column=2, padx=10, pady=10)

        self.play_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist)
        self.play_btn.grid(row=1, column=0, padx=10, pady=10)

        self.reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        self.reset_btn.grid(row=1, column=1, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(window, width=50, height=12)
        self.playlist_txt.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), fg="black")
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=(10, 20))

    def add_track(self):
        key = self.input_txt.get().strip()

        self.input_txt.delete(0, tk.END)
        self.input_txt.insert(0, "")

        if not key.isdigit() or len(key) != 2:
            self.status_lbl.config(text="Invalid input. Enter a 2-digit number (e.g. 01)", fg="red")
            return

        name = lib.get_name(key)
        if name:
            if key in self.playlist:
                self.status_lbl.config(text=f"Track {key} is already in the playlist", fg="red")
                return
            self.playlist.append(key)
            self.update_playlist_display()
            self.status_lbl.config(text=f"Added track {key} - {name} to playlist", fg="green")
        else:
            self.status_lbl.config(text=f"Track {key} not found. Please try a different number.", fg="red")


    def play_playlist(self):
        if not self.playlist:
            self.status_lbl.config(text="Playlist is empty!", fg="red")
            return

        for key in self.playlist:
            lib.increment_play_count(key)
        self.status_lbl.config(text="Playlist played! Play counts updated.", fg="green")

    def reset_playlist(self):
        self.playlist.clear()
        self.playlist_txt.delete("1.0", tk.END)
        self.status_lbl.config(text="Playlist cleared.", fg="black")

    def update_playlist_display(self):
        self.playlist_txt.delete("1.0", tk.END)
        for key in self.playlist:
            name = lib.get_name(key)
            self.playlist_txt.insert(tk.END, f"{key} - {name}\n")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateTrackListGUI(window)
    window.mainloop()


