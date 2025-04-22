import tkinter as tk
import font_manager as fonts
import track_library as lib

class UpdateTracksGUI():
    def __init__(self, window):
        window.geometry("700x420")
        window.title("Update Track Rating")

        track_lbl = tk.Label(window, text="Enter Track Number")
        track_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.track_input = tk.Entry(window, width=5)
        self.track_input.grid(row=0, column=1, padx=10, pady=10)

        rating_lbl = tk.Label(window, text="Enter New Rating (0-5)")
        rating_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.rating_input = tk.Entry(window, width=5)
        self.rating_input.grid(row=1, column=1, padx=10, pady=10)

        self.update_btn = tk.Button(window, text="Update Rating", command=self.update_rating)
        self.update_btn.grid(row=2, column=0, columnspan=2, pady=10)

        self.output_txt = tk.Text(window, width=75, height=10)
        self.output_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=2, sticky="W", padx=10, pady=10)

    def update_rating(self):
        key = self.track_input.get()
        if not key.isdigit() or len(key) != 2:
            self.status_lbl.config(text="Invalid input. Enter a 2-digit number (e.g. 01)", fg="red")
            self.output_txt.delete("1.0", tk.END)
            self.output_txt.insert(tk.END, "")
            return
        
        try:
            rating = int(self.rating_input.get())
            if rating < 0 or rating > 5:
                raise ValueError("Rating out of range")
        except ValueError:
            self.output_txt.delete("1.0", tk.END)
            self.output_txt.insert(tk.END, "")
            self.status_lbl.config(text="Rating must be an integer from 0 to 5.", fg="red")
            return

        if lib.get_name(key):
            lib.set_rating(key, rating)
            name = lib.get_name(key)
            play_count = lib.get_play_count(key)
            self.output_txt.delete("1.0", tk.END)
            self.output_txt.insert(tk.END, f"{name}\nNew Rating: {rating}\nPlay Count: {play_count}")
            self.status_lbl.config(text="Track rating updated successfully", fg="green")
        else:
            self.output_txt.delete("1.0", tk.END)
            self.output_txt.insert(tk.END, f"Track {key} not found")
            self.status_lbl.config(text="Track not found. Please try a different number." , fg="red")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTracksGUI(window)
    window.mainloop()
