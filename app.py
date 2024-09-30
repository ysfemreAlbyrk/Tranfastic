import tkinter as tk
from googletrans import Translator
import time

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Çeviri Uygulaması")
        self.root.geometry("400x400")
        
        # Google Translator
        self.translator = Translator()
        
        # Zamanlama ve metin
        self.text_input = ""
        self.last_input_time = time.time()
        self.translation_done = False  # Çeviri yapıldı mı kontrolü

        # Arayüz elemanları
        self.label = tk.Label(root, text="Metin girin:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.textbox = tk.Text(root, height=5, width=40)
        self.textbox.pack(pady=10)

        self.translation_label = tk.Label(root, text="Çeviri:", font=('Arial', 14))
        self.translation_label.pack(pady=10)

        # Kopyalanabilir çeviri sonucu için Text widget'ı
        self.translation_result = tk.Text(root, height=5, width=40, wrap='word')
        self.translation_result.pack(pady=10)
        self.translation_result.config(state='disabled')  # Düzenlemeyi engellemek için pasif modda
        self.translation_result.bind("<Button-1>", self.enable_copy)  # Kopyalama için tıklama dinleyicisi

        # Zamanlayıcıyı başlat
        self.root.after(100, self.check_inactivity)

    def translate_text(self):
        text = self.textbox.get("1.0", tk.END).strip()  # Metni al ve boşlukları temizle

        # Metin boşsa çeviri yapma ve daha önce çeviri yapıldıysa tekrar yapma
        if text and not self.translation_done:
            try:
                print("translate now...")
                translation = self.translator.translate(text, dest='en')
                self.translation_result.config(state='normal')  # Düzenleme için etkinleştir
                self.translation_result.delete(1.0, tk.END)  # Eski çeviriyi sil
                self.translation_result.insert(tk.END, translation.text)  # Yeni çeviriyi ekle
                self.translation_result.config(state='disabled')  # Tekrar düzenlemeyi engelle
                self.translation_done = True  # Çeviri yapıldı olarak işaretle
            except Exception as e:
                self.translation_result.config(state='normal')
                self.translation_result.delete(1.0, tk.END)
                self.translation_result.insert(tk.END, f"Çeviri hatası: {e}")
                self.translation_result.config(state='disabled')
        elif not text:  # Metin kutusu tamamen boşsa, sonucu temizle
            self.translation_result.config(state='normal')
            self.translation_result.delete(1.0, tk.END)
            self.translation_result.config(state='disabled')

    def check_inactivity(self):
        current_time = time.time()
        if current_time - self.last_input_time >= 1:  # 2 saniyelik boşta kalma süresi
            print("...function is running....")
            self.translate_text()

        self.root.after(100, self.check_inactivity)  # Her 100ms'de bir kontrol et

    def on_keypress(self, event):
        self.last_input_time = time.time()  # Her tuşa basıldığında zamanı güncelle
        self.translation_done = False  # Metin değişti, çeviri yapılabilir durumda

    def enable_copy(self, event):
        self.translation_result.config(state='normal')  # Metni seçilebilir yapar
        self.root.after(5000, lambda: self.translation_result.config(state='disabled'))  # 5 saniye sonra tekrar devre dışı bırakır

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    
    # Tuş basımı etkinliği için dinleyici
    root.bind('<KeyPress>', app.on_keypress)
    
    root.mainloop()
