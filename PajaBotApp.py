#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import tkinter as tk
from tkinter import scrolledtext

# Characters with diacritics to reject
DIACRITICS = set("ěščřžýáíéúůťňďĚŠČŘŽÝÁÍÉÚŮŤŇĎ")
INSULTS = ["negr", "pic", "vole", "prdel", "kokot", "kurv", "zmrd", "hovno","tux","debil"]

# Preload images
IMAGES = {}

try:
    IMAGES["dog"] = tk.PhotoImage(file="dog.png")
except Exception as e:
    print("Error loading images:", e)
    IMAGES = {}  # fallback if images not found


def has_diacritics(s: str) -> bool:
    return any(ch in DIACRITICS for ch in s)


def respond(odpoved: str):
    """
    Return a tuple (text_reply, optional_image) based on the user input.
    """
    odpoved = odpoved.strip()
    low = odpoved.lower()

    if "martyn" in low:
        return ("Pája: Ne! Topytle! Ma tšečtina se vypařuje kdiz o nem mluvýš!", None)
    
    if "majkl" in low:
        return ("Pája: Ne! Dopytle! Mám zabrané všechno místo na disku!", None)
    
    if odpoved == "":
        return ("Systém: Napiš něco prosím.", None)

    # exact match greetings
    if low in ["ahoj", "cus", "cau", "nazdar", "hello"]:
        img = IMAGES.get("dog")
        return ("Pája: " + odpoved.capitalize(), img)

    if has_diacritics(odpoved):
        return ("Systém: Prosím, piš Pájovi bez háčků a čárek.", None)

    if "." not in odpoved and "!" not in odpoved and "?" not in odpoved:
        return ("Systém: Prosím, ukonči větu tečkou, vykřičníkem nebo otazníkem.", None)

    # Advice request
    if "dej" in low and "rad" in low and "ne" not in low:
        rada = random.randint(1, 3)
        if rada == 1:
            return ("Pája: Když ti někdo život ničí,\n      usměj se a vem ho tyčí.", None)
        elif rada == 2:
            return ("Pája: Pokud zhubnout chceš, musíš\n      vykadit víc, než toho sníš.", None)
        else:
            return ("Pája: Mezitím co v noci spíš,\n      já vykrádám tvoji spíž.", None)

    # insults -> disable input
    if any(word in low for word in INSULTS):
        return ("Pája: Ty jsi ale hnusný sprosťák\n      s tebou se nebavím.", None)

    # questions
    if "?" in odpoved:
        if "co" in low and "je" in low:
            return ("Pája: To je něco, čemu nerozumím.", None)
        elif "kolik" in low:
            return ("Pája: Pět a půl.", None)
        elif "kdo" in low:
            return ("Pája: Karel.", None)
        elif "jak" in low and not any(x in low for x in ["jaky", "jaka", "jake"]):
            return ("Pája: Nějak.", None)
        else:
            return ("Pája: Na hloupé otázky jsou hloupé odpovědi.\n      Takže tohle je má odpověď:\n Když ryje krtek v dubnu, bude pršet v březnu.", None)

    # fallback random replies
    cislo = random.randint(1, 3)
    if cislo == 1:
        return ("Pája: No, to je super,\n      ale vůbec mě to nezajímá.", None)
    elif cislo == 2:
        return ("Pája: To je taková blbost,\n      že na to ani neodpovím.", None)
    else:
        return ("Pája: To je tak divná věta,\n      že mi úplně uvařila hlavu.\n      (kterou ani nemám)", None)


class PajaApp:
    def __init__(self, root):
        self.root = root
        root.title("Pája")
        root.resizable(False, False)

        try:
            root.iconphoto(False, tk.PhotoImage(file='pja.png'))
        except:
            pass  # ignore if icon missing

        self.chat = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD, state=tk.DISABLED)
        self.chat.grid(row=0, column=0, columnspan=2, padx=8, pady=8)

        self.entry = tk.Entry(root, width=50)
        self.entry.grid(row=1, column=0, padx=(8, 0), pady=(0, 8))
        self.entry.bind("<Return>", self.on_send)

        self.send_btn = tk.Button(root, text="Pošli", command=self.on_send)
        self.send_btn.grid(row=1, column=1, padx=(4, 8), pady=(0, 8))

        # initial greeting
        self.append_message("Pája: Co mi chceš říct?")

    def append_message(self, msg: str, img: tk.PhotoImage = None):
        self.chat.configure(state=tk.NORMAL)
        if msg:
            self.chat.insert(tk.END, msg + "\n\n")
        if img:
            self.chat.image_create(tk.END, image=img)
            self.chat.insert(tk.END, "\n\n")
            # Keep reference to prevent garbage collection
            if not hasattr(self.chat, 'images'):
                self.chat.images = []
            self.chat.images.append(img)
        self.chat.see(tk.END)
        self.chat.configure(state=tk.DISABLED)

    def on_send(self, event=None):
        user_text = self.entry.get()
        if not user_text:
            return
        self.append_message("Ty: " + user_text)
        self.entry.delete(0, tk.END)

        reply, img = respond(user_text)
        self.append_message(reply, img)

        if reply.startswith("Pája: Ty jsi ale hnusný sprosťák"):
            self.entry.configure(state=tk.DISABLED)
            self.send_btn.configure(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = PajaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
