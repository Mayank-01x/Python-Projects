import tkinter as tk
from googletrans import Translator

class TechTribeTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Tech Tribe Translator")
        
        self.label = tk.Label(root, text="Enter English text:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.translate_button = tk.Button(root, text="Translate", command=self.translate)
        self.translate_button.pack()
        
        self.translated_label = tk.Label(root, text="")
        self.translated_label.pack()
        
    def translate(self):
        input_text = self.entry.get()
        if input_text:
            translated_text = self.translate_english_to_hindi(input_text)
            self.translated_label.config(text="Translated Hindi text: " + translated_text)
    
    def translate_english_to_hindi(self, text):
        translator = Translator()
        translated = translator.translate(text, src='en', dest='hi')
        return translated.text

if __name__ == "__main__":
    root = tk.Tk()
    app = TechTribeTranslator(root)
    root.mainloop()
