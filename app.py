import time
from googletrans import Translator

def translate_and_print(text):
    translator = Translator()
    # Hedef dilinizi burada belirtin (örneğin, 'en' İngilizce için)
    translation = translator.translate(text, dest='en')
    print(translation.text)

def main():
    start_time = time.time()
    text = ""

    while True:
        new_char = input()
        text += new_char

        if time.time() - start_time >= 2:
            translate_and_print(text)
            text = ""
            start_time = time.time()

if __name__ == "__main__":
    main()