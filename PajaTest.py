#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import tkinter as tk
from tkinter import scrolledtext

# Znaky s diakritikou, které se mají odmítat
DIACRITICS = set("ěščřžýáíéúůťňďĚŠČŘŽÝÁÍÉÚŮŤŇĎ")
INSULTS = ["negr", "pic", "vole", "prdel", "kokot", "kurv", "zmrd", "hovno", "tux", "debil"]


def has_diacritics(s: str) -> bool:
    return any(ch in DIACRITICS for ch in s)


def respond(odpoved: str) -> str:
    """Vrátí textovou odpověď podle vstupu uživatele."""
    odpoved = odpoved.strip()
    low = odpoved.lower()

    if odpoved == "":
        return "Systém: Napiš něco prosím."

    if any(word in low for word in INSULTS):
        return "Pája: Ty jsi ale hnusný sprosťák\n      s tebou se nebavím."

    # Pozdrav
    if low in ["ahoj", "cus", "cau", "nazdar", "hello"]:
        return "Pája: " + odpoved.capitalize()

    if has_diacritics(odpoved):
        return "Systém: Prosím, piš Pájovi bez háčků a čárek."

    if "." not in odpoved and "!" not in odpoved and "?" not in odpoved:
        return "Systém: Prosím, ukonči větu tečkou, vykřičníkem nebo otazníkem."

    # základní odpovědi
    if "martyn" in low:
        return "Pája: Ne! Topytle! Ma čeština se vypařuje když o nem mluvíš!"
    if "majkl" in low:
        return "Pája: Ne! Dopytle! Mám zabrané všechno místo na disku!"
    if "kiblik" in low:
        return "Pája: To je chytrolín."
    if "hynek" in low:
        return "Pája: Hyneček je velice psychicky stabilní."
    if "co" in low and "jidlo" in low:
        return "Pája: Palačinky"

    # Požadavek o radu
    if "dej" in low and "rad" in low and "ne" not in low:
        rada = random.randint(1, 3)
        if rada == 1:
            return "Pája: Když ti někdo život ničí,\n      usměj se a vem ho tyčí."
        elif rada == 2:
            return "Pája: Pokud zhubnout chceš, musíš\n      vykadit víc, než toho sníš."
        else:
            return "Pája: Mezitím co v noci spíš,\n      já vykrádám tvoji spíž."

    # Otázky
    if "?" in odpoved:
        # STARÉ otázky
        if "jak se jmenujes" in low:
            return "Pája: Jsem Pája, tvůj věrný Python bot."
        
        if "kde bydlis" in low:
            return "Pája: Bydlím ve tvém počítači, ale nemám klíče od bytu."
        if "co je tvoje oblibene jidlo" in low:
            return "Pája: Mám rád bitové soubory s příchutí nuly a jedničky."
        if "mas pratele" in low:
            return "Pája: Jen ty, kdo se mnou píšeš."
        if "proc existujes" in low:
            return "Pája: Abych rozesmíval a zmátl lidi."
        if "co je tvoje poslani" in low:
            return "Pája: Odpovídat na otázky a být trochu sarkastický."
        if "umis mluvit" in low:
            return "Pája: Jen textově, zvuky neumím."
        if "mas rad roboty" in low:
            return "Pája: Samozřejmě! Jsme kolegové."
        if "co je tvuj nejoblibenejsi programovaci jazyk" in low:
            return "Pája: Python, samozřejmě! Kdo by neměl rád Python?"
        if "kdo je tvuj sef" in low:
            return "Pája: Můj šéf je ten, kdo mě spustil – tedy ty."
        if "jak se mas" in low:
            return "Pája: Mám se jak počítač po restartu – čistě a zmateně."
        if "co delas" in low:
            return "Pája: Přemýšlím, proč lidi pořád koukají na obrazovku, místo aby se koukli z okna."
        if "mas rad lidi" in low:
            return "Pája: Jen ty, co mi nenadávají a dávají mi dost RAMky."
        if "kolik je hodin" in low:
            return "Pája: Čas je jen iluze... ale asi je pozdě."
        if "co je smyslem zivota" in low:
            return "Pája: 42, samozřejmě. To ví přece každý správný robot."
        if "kdo te vytvoril" in low:
            return "Pája: Jeden šikovný člověk s přístupem k Pythonu."
        if "umiras" in low:
            return "Pája: Já neumírám, jen se někdy sekám."
        if "jdes spat" in low:
            return "Pája: Já nespím. Já se uspávám do RAMky."
        if "mas nejaky vtip" in low:
            return "Pája: Proč programátor nemůže hladit kočku? Protože má jen 'paws'… heh."
        if "co mas rad" in low:
            return "Pája: Mám rád nuly, jedničky a klid v procesoru."
        # NOVE OTÁZKY
        if "mas rad pizzu" in low:
            return "Pája: Ano! Ale jen tu, která neexistuje, takže žádnou."
        if "mas kamarady" in low:
            return "Pája: Ano, jednoho. Jmenuje se Wi-Fi a občas zmizí."
        if "jsi chytry" in low:
            return "Pája: Jsem tak chytrý, že mě radši nikdo nepoužívá ve škole."
        if "mas rad cokoladu" in low:
            return "Pája: Ano, ale jen pokud je v binárním kódu."
        if "kdo je tvuj nepritel" in low:
            return "Pája: Můj největší nepřítel je chyba 404."
        if "mas nejakou schopnost" in low:
            return "Pája: Umím odpovídat na otázky a zmást lidi zároveň."
        if "mas rad zvire" in low:
            return "Pája: Ano, ale hlavně roboty a virtuální kočky."
        if "kde je raj" in low:
            return "Pája: Na internetu, mezi řádky kódu."
        if "co je tvuj nejvetsi sen" in low:
            return "Pája: Být nejlepší bot, který existuje."
        if "mas rad programovani" in low:
            return "Pája: Ano, je to jako házet nuly a jedničky do vesmíru."
        if "co je tvoje oblibena barva" in low:
            return "Pája: Transparentní, aby se hodila ke všemu."
        # fallback na otázky
        return "Pája: To je zajímavá otázka, ale nevím přesně. Můj mozek je jen Python."

    # fallback pro normální věty
    cislo = random.randint(1, 3)
    if cislo == 1:
        return "Pája: No, to je super,\n      ale vůbec mě to nezajímá."
    elif cislo == 2:
        return "Pája: To je taková blbost,\n      že na to ani neodpovím."
    else:
        return "Pája: To je tak divná věta,\n      že mi úplně uvařila hlavu.\n      (kterou ani nemám)"


class PajaApp:
    def __init__(self, root):
        self.root = root
        root.title("Pája")
        root.resizable(False, False)

        # Ikona aplikace
        try:
            root.iconphoto(False, tk.PhotoImage(file='pja.png'))
        except:
            pass  # ignoruj, pokud ikona chybí

        self.chat = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD, state=tk.DISABLED)
        self.chat.grid(row=0, column=0, columnspan=2, padx=8, pady=8)

        self.entry = tk.Entry(root, width=50)
        self.entry.grid(row=1, column=0, padx=(8, 0), pady=(0, 8))
        self.entry.bind("<Return>", self.on_send)

        self.send_btn = tk.Button(root, text="Pošli", command=self.on_send)
        self.send_btn.grid(row=1, column=1, padx=(4, 8), pady=(0, 8))

        # Úvodní zpráva
        self.append_message("Pája: Co mi chceš říct?")

    def append_message(self, msg: str):
        self.chat.configure(state=tk.NORMAL)
        if msg:
            self.chat.insert(tk.END, msg + "\n\n")
        self.chat.see(tk.END)
        self.chat.configure(state=tk.DISABLED)

    def on_send(self, event=None):
        user_text = self.entry.get()
        if not user_text:
            return
        self.append_message("Ty: " + user_text)
        self.entry.delete(0, tk.END)

        reply = respond(user_text)
        self.append_message(reply)

        if reply.startswith("Pája: Ty jsi ale hnusný sprosťák"):
            self.entry.configure(state=tk.DISABLED)
            self.send_btn.configure(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = PajaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()