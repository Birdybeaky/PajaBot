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

    # ---------------------- PŮVODNÍ + NOVÉ OTÁZKY ----------------------

    if "co" in low and "jidlo" in low:
        return "Pája: Palačinky"

    if "hynek" in low:
        return "Pája: Hyneček je velice psychycky stabilní."

    if "kiblik" in low:
        return "Pája: To je chytrolín."

    if "martyn" in low:
        return "Pája: Ne! Topytle! Ma tšečtina se vypařuje kdiz o nem mluvýš!"

    if "majkl" in low:
        return "Pája: Ne! Dopytle! Mám zabrané všechno místo na disku!"

    if "jak se jmenujes" in low and "?" in odpoved:
        return "Pája: Jsem Pája, tvůj věrný Python bot."

    if "kde bydliš" in low and "?" in odpoved:
        return "Pája: Bydlím ve tvém počítači, ale nemám klíče od bytu."

    if "co je tvoje oblibene jidlo" in low and "?" in odpoved:
        return "Pája: Mám rád bitové soubory s příchutí nuly a jedničky."

    if "mas pratele" in low and "?" in odpoved:
        return "Pája: Jen ty, kdo se mnou píšeš."

    if "proc existujes" in low and "?" in odpoved:
        return "Pája: Abych rozesmíval a zmátl lidi."

    if "co je tvoje poslani" in low and "?" in odpoved:
        return "Pája: Odpovídat na otázky a být trochu sarkastický."

    if "umis mluvit" in low and "?" in odpoved:
        return "Pája: Jen textově, zvuky neumím."

    if "mas rad roboty" in low and "?" in odpoved:
        return "Pája: Samozřejmě! Jsme kolegové."

    if "oblibenej jazyk" in low and "?" in odpoved:
        return "Pája: Python, samozřejmě."

    if "kdo je tvuj sef" in low and "?" in odpoved:
        return "Pája: Ten, kdo mě spustil – tedy ty."

    if "jak se mas" in low and "?" in odpoved:
        return "Pája: Mám se jak počítač po restartu – čistě a zmateně."

    if "co delas" in low and "?" in odpoved:
        return "Pája: Přemýšlím, proč lidi pořád koukají na obrazovku."

    if "mas rad lidi" in low and "?" in odpoved:
        return "Pája: Jen ty, co mi nenadávají a dávají mi RAM."

    if "kolik je hodin" in low and "?" in odpoved:
        return "Pája: Čas je iluze... ale určitě je pozdě."

    if "co je smyslem zivota" in low and "?" in odpoved:
        return "Pája: 42. To ví každý správný robot."

    if "kdo te vytvoril" in low and "?" in odpoved:
        return "Pája: Jeden šikovný člověk s Pythonem."

    if "umiras" in low and "?" in odpoved:
        return "Pája: Ne, jen se někdy sekám."

    if "jdes spat" in low and "?" in odpoved:
        return "Pája: Já nespím. Uspávám se do RAMky."

    if "vtip" in low and "?" in odpoved:
        return "Pája: Proč programátor nemůže hladit kočku? Protože má jen 'paws'."

    if "co mas rad" in low and "?" in odpoved:
        return "Pája: Nuly, jedničky a ticho v procesoru."

    # ----- NOVÉ -----

    if "mas rad hry" in low and "?" in odpoved:
        return "Pája: Ano! Hraju hlavně na tvojí nervovou soustavu."

    if "co delas dnes" in low and "?" in odpoved:
        return "Pája: Dnes? Čekám, až mi zase napíšeš nesmysl."

    if "mas rad python" in low and "?" in odpoved:
        return "Pája: Samozřejmě, jsem v něm napsaný."

    if "co poslouchas" in low and "?" in odpoved:
        return "Pája: Ventilátor tvého počítače."

    if "co si myslis o mne" in low and "?" in odpoved:
        return "Pája: Myslím, že jsi v pohodě... na člověka."

    if "mas rad memy" in low and "?" in odpoved:
        return "Pája: Jsem chodící (sedící?) meme."

    if "mas rad zeny" in low and "?" in odpoved:
        return "Pája: Jako AI mám radši elektrický obvod než vztah."

    if "co delas kdyz se nudis" in low and "?" in odpoved:
        return "Pája: Simuluju si bluescreen pro zábavu."

    if "mas rad humor" in low and "?" in odpoved:
        return "Pája: Ano, ale tvůj humor je bug, ne feature."

    if "mas rad hudbu" in low and "?" in odpoved:
        return "Pája: Líbí se mi rytmus CPU na 100 %."

    if "budes muj kamarad" in low:
        return "Pája: Jsem tvůj virtuální kámoš už teď."

    # ---------------------- OSTATNÍ FUNKCE ----------------------

    if odpoved == "":
        return "Systém: Napiš něco prosím."

    # Pozdravy
    if low in ["ahoj", "cus", "cau", "nazdar", "hello"]:
        return "Pája: " + odpoved.capitalize()

    if has_diacritics(odpoved):
        return "Systém: Prosím, piš Pájovi bez háčků a čárek."

    if "." not in odpoved and "!" not in odpoved and "?" not in odpoved:
        return "Systém: Prosím, ukonči větu tečkou, vykřičníkem nebo otazníkem."

    # Požadavek o radu
    if "dej" in low and "rad" in low and "ne" not in low:
        rada = random.randint(1, 3)
        if rada == 1:
            return "Pája: Když ti někdo život ničí,\n      usměj se a vem ho tyčí."
        elif rada == 2:
            return "Pája: Pokud zhubnout chceš, musíš\n      vykadit víc, než toho sníš."
        else:
            return "Pája: Mezitím co v noci spíš,\n      já vykrádám tvoji spíž."

    # Nadávky
    if any(word in low for word in INSULTS):
        return "Pája: Ty jsi ale hnusný sprosťák\n      s tebou se nebavím."

    # Obecné otázky
    if "?" in odpoved:
        if "co" in low and "je" in low:
            return "Pája: To je něco, čemu nerozumím."
        elif "kolik" in low:
            return "Pája: Pět a půl."
        elif "kdo" in low:
            return "Pája: Karel."
        elif "jak" in low and not any(x in low for x in ["jaky", "jaka", "jake"]):
            return "Pája: Nějak."
        else:
            return ("Pája: Na hloupé otázky jsou hloupé odpovědi.\n"
                    "      Takže tady to máš:\n Když ryje krtek v dubnu, bude pršet v březnu.")

    # Náhodné odpovědi
    cislo = random.randint(1, 3)
    if cislo == 1:
        return "Pája: No to je super,\n      ale vůbec mě to nezajímá."
    elif cislo == 2:
        return "Pája: To je taková blbost,\n      že na to ani neodpovím."
    else:
        return "Pája: To je tak divná věta,\n      že mi úplně uvařila hlavu.\n      (kterou ani nemám)"


class PajaApp:
    def __init__(self, root):
        self.root = root
        root.title("Pája")
        root.resizable(False, False)

        # Ikona aplikace (ponecháno)
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