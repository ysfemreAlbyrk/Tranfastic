import keyboard
import pyperclip
import tkinter as tk
from tkinter import simpledialog
import time
import pygetwindow as gw

# Önceki aktif pencereyi sakla
active_window = None

# Kullanıcının yazı yazdığı pencereyi kaydet
def save_active_window():
    global active_window
    active_window = gw.getActiveWindow()  # Şu anki aktif pencereyi kaydet
    print(f"Aktif pencere: {active_window.title if active_window else 'None'}")

# Metin girişini kullanıcıdan alacak fonksiyon
def show_input_dialog():
    root = tk.Tk()
    # root.withdraw()  # Ana pencereyi gizle
    user_input = simpledialog.askstring("Girdi", "Yazınızı girin:")  # Yazı giriş penceresi
    root.destroy()  # Pencereyi kapat
    return user_input

# Kullanıcının yazdığı metni simüle ederek yapıştırmak
def paste_text(text):
    pyperclip.copy(text)  # Metni kopyala
    time.sleep(0.2)  # Uygulamaya yapıştırmadan önce kısa bir bekleme süresi
    if active_window:
        active_window.activate()  # Kayıtlı pencereye geri dön
        time.sleep(0.2)  # Pencereye geçiş için kısa bekleme
        keyboard.press_and_release('ctrl+v')  # Kopyalanan metni yapıştır

# Kısayol tetiklendiğinde çalışacak fonksiyon
def on_hotkey():
    save_active_window()  # Şu anki aktif pencereyi kaydet
    user_text = show_input_dialog()  # Kullanıcıdan yazı al
    if user_text:
        paste_text(user_text)  # Alınan yazıyı yapıştır

# Kısayolu dinleme
keyboard.add_hotkey('ctrl+shift+x', on_hotkey)  # Örnek kısayol: Ctrl+Shift+X

# Program çalışırken sürekli dinlemede kalsın
print("Program çalışıyor. Kısayol: Ctrl+Shift+X (Çıkmak için 'Esc' tuşuna basın)")
keyboard.wait('esc')  # Program Esc tuşuna basılana kadar çalışmaya devam eder
