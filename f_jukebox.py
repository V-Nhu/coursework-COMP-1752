import tkinter as tk
import track_library as lib
import font_manager as fonts
from library_item import LibraryItem

class SearchTracksGUI:
    def __init__(self, window):
        window.geometry("800x700")
        window.title("Search & Add Custom Tracks")

        self.matching_keys = []

        label = tk.Label(window, text="Enter keyword (song or artist):")
        label.pack(pady=5)

        self.search_entry = tk.Entry(window, width=40)
        self.search_entry.pack(pady=5)

        search_btn = tk.Button(window, text="Search", command=self.search)
        search_btn.pack(pady=5)

        self.result_txt = tk.Text(window, width=60, height=10)
        self.result_txt.pack(pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), fg="black")
        self.status_lbl.pack(pady=(0, 10))

        separator = tk.Label(window, text="Add New Track", font=("Helvetica", 12, "bold"))
        separator.pack(pady=(10, 2))

        form_frame = tk.Frame(window)
        form_frame.pack(pady=5)

        tk.Label(form_frame, text="Track ID (2 digits):").grid(row=0, column=0, padx=5, pady=2)
        self.new_id_entry = tk.Entry(form_frame, width=5)
        self.new_id_entry.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Track Name:").grid(row=1, column=0, padx=5, pady=2)
        self.new_name_entry = tk.Entry(form_frame, width=30)
        self.new_name_entry.grid(row=1, column=1, padx=5)

        tk.Label(form_frame, text="Artist:").grid(row=2, column=0, padx=5, pady=2)
        self.new_artist_entry = tk.Entry(form_frame, width=30)
        self.new_artist_entry.grid(row=2, column=1, padx=5)

        tk.Label(form_frame, text="Rating (0-5):").grid(row=3, column=0, padx=5, pady=2)
        self.new_rating_entry = tk.Entry(form_frame, width=5)
        self.new_rating_entry.grid(row=3, column=1, padx=5)

        add_btn = tk.Button(window, text="Add Track to Playlist", command=self.add_new_track)
        add_btn.pack(pady=10)

    def search(self):
        keyword = self.search_entry.get().lower()
        if not keyword:
            self.status_lbl.config(text="Please enter a keyword to search.", fg="red")
            return

        self.result_txt.delete("1.0", tk.END)
        self.matching_keys = []
        for key in lib.library:
            name = lib.get_name(key).lower()
            artist = lib.get_artist(key).lower()
            if keyword in name or keyword in artist:
                self.result_txt.insert(tk.END, f"{key} - {lib.get_name(key)} by {lib.get_artist(key)}\n")
                self.matching_keys.append(key)

        if not self.matching_keys:
            self.result_txt.insert(tk.END, "No matching tracks found.\n")
            self.status_lbl.config(text="No matches found. Please try a different keyword", fg="red")
        else:
            self.status_lbl.config(text=f"Found {len(self.matching_keys)} track(s).", fg="green")

    def add_new_track(self):
        key = self.new_id_entry.get().strip()
        name = self.new_name_entry.get().strip()
        artist = self.new_artist_entry.get().strip()
        rating_str = self.new_rating_entry.get().strip()
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, "")
        self.result_txt.delete("1.0", tk.END)
        self.result_txt.insert(tk.END, "")


        if not key.isdigit() or len(key) != 2:
            self.status_lbl.config(text="Invalid Track ID. Must be 2-digit.", fg="red")
            return
        
        if key in lib.library:
            self.status_lbl.config(text="Track ID already exists.", fg="red")
            return
        
        if not name:
            self.status_lbl.config(text="Track name cannot be empty.", fg="red")
            return

        if not artist:
            self.status_lbl.config(text="Artist name cannot be empty.", fg="red")
            return


        if key in lib.library:
            self.status_lbl.config(text="Track ID already exists.", fg="red")
            return

        try:
            rating = int(rating_str)
            if not (0 <= rating <= 5):
                raise ValueError
        except ValueError:
            self.status_lbl.config(text="Rating must be an integer from 0 to 5.", fg="red")
            return

        lib.library[key] = LibraryItem(name, artist, rating)
        self.status_lbl.config(text=f"Track '{name}' by {artist} added with ID {key}.", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    fonts.configure()
    SearchTracksGUI(root)
    root.mainloop()