import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой музыкальный плеер")

        self.current_folder = tk.StringVar()
        self.current_folder.set("Выберите папку с музыкой")

        select_button = tk.Button(self.root, text="Выбрать папку", command=self.choose_folder)
        select_button.pack(pady=10)

        folder_label = tk.Label(self.root, textvariable=self.current_folder)
        folder_label.pack()

        play_button = tk.Button(self.root, text="Воспроизвести", command=self.play_music)
        play_button.pack(pady=10)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.current_folder.set("Выбрана папка: " + folder)
            self.music_folder = folder

    def play_music(self):
        if hasattr(self, 'music_folder'):
            music_files = [f for f in os.listdir(self.music_folder) if f.endswith(".mp3")]
            if music_files:
                file = os.path.join(self.music_folder, music_files[0])
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
            else:
                messagebox.showerror("Ошибка", "В выбранной папке нет музыкальных файлов.")
        else:
            messagebox.showerror("Ошибка", "Выберите папку с музыкой сначала.")

root = tk.Tk()
app = MusicPlayerApp(root)
root.mainloop()