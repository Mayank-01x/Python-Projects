### Made by Team : Tech Tribe CGC-CSE 
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TechTribeTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator")
        self.root.configure(bg="#f0f0f0")
        
        self.label = ttk.Label(root, text="Enter English text:", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.entry = ttk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(padx=20, pady=5, fill=tk.X)
        
        self.translate_button = ttk.Button(root, text="Translate", command=self.translate)
        self.translate_button.pack(pady=10)
        
        self.translated_label = ttk.Label(root, text="", font=("Helvetica", 14), wraplength=400)
        self.translated_label.pack()
        
        self.made_by_label = ttk.Label(root, text="Made by; Technology", font=("Helvetica", 10), foreground="#888888")
        self.made_by_label.pack(pady=10, side=tk.BOTTOM)

    def translate(self):
        input_text = self.entry.get()
        if input_text:
            translated_text = self.translate_english_to_hindi(input_text)
            self.translated_label.config(text="Translated Hindi text:\n" + translated_text)
    
    def translate_english_to_hindi(self, text):
        translator = Translator()
        translated = translator.translate(text, src='en', dest='hi')
        return translated.text

if __name__ == "__main__":
    root = tk.Tk()
    app = TechTribeTranslator(root)
    root.geometry("500x400")
    root.mainloop()
