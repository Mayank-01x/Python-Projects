import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_english_to_hindi():
    input_text = entry.get()
    if input_text:
        translator = Translator()
        translated = translator.translate(input_text, src='en', dest='hi')
        translated_label.config(text="Translated Hindi text:\n" + translated.text)

root = tk.Tk()
root.title("Basic English to Hindi Translator")

label = ttk.Label(root, text="Enter English text:")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(padx=20, pady=5, fill=tk.X)

translate_button = ttk.Button(root, text="Translate", command=translate_english_to_hindi)
translate_button.pack(pady=10)

translated_label = ttk.Label(root, text="", font=("Helvetica", 12), wraplength=400)
translated_label.pack()

root.geometry("500x400")
root.mainloop()
