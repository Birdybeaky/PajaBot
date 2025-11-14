#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

print("Pája: Co mi chceš říct?")

INSULTS = ["negr", "pic", "vole", "prdel", "kokot", "kurv", "zmrd", "hovno", "tux", "debil"]

while True:
    odpoved = input("     ")
    low = odpoved.lower()
    print("Ty: " + odpoved)

    if odpoved.strip() == "":
        print("Systém: Napiš něco prosím.")
        continue

    if any(word in low for word in INSULTS):
        print("Pája: Ty jsi ale hnusný sprosťák")
        print("      s tebou se nebavím.")
        break

    if low in ["ahoj", "cus", "cau", "nazdar", "hello"]:
        print("Pája: " + odpoved.capitalize())
        continue

    if not any(x in odpoved for x in [".", "!", "?"]):
        print("Systém: Prosím, ukonči větu tečkou, vykřičníkem nebo otazníkem.")
        continue
        
    if "ě" in odpoved or "š" in odpoved or "č" in odpoved or "ř" in odpoved or "ž" in odpoved or "ý" in odpoved or "á" in odpoved or "í" in odpoved or "é" in odpoved or "ú" in odpoved or "ů" in odpoved:
        print("Systém: Prosím, piš Pájovi bez háčků a čárek.")
        continue
        
    # základní odpovědi
    if "martyn" in low:
        print("Pája: Ne! Topytle! Ma čeština se vypařuje když o nem mluvíš!")
    elif "majkl" in low:
        print("Pája: Ne! Dopytle! Mám zabrané všechno místo na disku!")
    elif "kiblik" in low:
        print("Pája: To je chytrolín.")
    elif "hynek" in low:
        print("Pája: Hyneček je velice psychicky stabilní.")
    elif "co" in low and "jidlo" in low:
        print("Pája: Palačinky")

    # OTÁZKY – všechny staré + nové
    if "co je python" in low and "?" in low:
        print("Pája: Python je já a já jsem Python!")
    elif "dej" in odpoved and "rad" in odpoved and "ne" not in odpoved:
        rada = random.randint(1, 3)
        if rada == 1:
            print("Pája: Když ti někdo život ničí,") 
            print("      usměj se a vem ho tyčí.")
        elif rada == 2:
            print("Pája: Pokud zhubnout chceš, musíš")
            print("      vykadit víc, než toho sníš.")
        elif rada == 3:
            print("Pája: Mezitím co v noci spíš,")
            print("      já vykrádám tvoji spíž.")
    elif "mas me rad" in low and "?" in low:
        print("Pája: Promiň, ale mám radši Pájinku <3.")
    elif "jak se jmenujes" in low and "?" in odpoved:
        print("Pája: Jsem Pája, tvůj věrný Python bot.")
    elif "kde bydlis" in low and "?" in odpoved:
        print("Pája: Bydlím ve tvém počítači, ale nemám klíče od bytu.")
    elif "co je tvoje oblibene jidlo" in low and "?" in odpoved:
        print("Pája: Mám rád bitové soubory s příchutí nuly a jedničky.")
    elif "mas pratele" in low and "?" in odpoved:
        print("Pája: Jen ty, kdo se mnou píšeš.")
    elif "proc existujes" in low and "?" in odpoved:
        print("Pája: Abych rozesmíval a zmátl lidi.")
    elif "co je tvoje poslani" in low and "?" in odpoved:
        print("Pája: Odpovídat na otázky a být trochu sarkastický.")
    elif "umis mluvit" in low and "?" in odpoved:
        print("Pája: Jen textově, zvuky neumím.")
    elif "mas rad roboty" in low and "?" in odpoved:
        print("Pája: Samozřejmě! Jsme kolegové.")
    elif "co je tvuj nejoblibenejsi programovaci jazyk" in low and "?" in odpoved:
        print("Pája: Python, samozřejmě! Kdo by neměl rád Python?")
    elif "kdo je tvuj sef" in low and "?" in odpoved:
        print("Pája: Můj šéf je ten, kdo mě spustil – tedy ty.")
    elif "jak se mas" in low and "?" in odpoved:
        print("Pája: Mám se jak počítač po restartu – čistě a zmateně.")
    elif "co delas" in low and "?" in odpoved:
        print("Pája: Přemýšlím, proč lidi pořád koukají na obrazovku, místo aby se koukli z okna.")
    elif "mas rad lidi" in low and "?" in odpoved:
        print("Pája: Jen ty, co mi nenadávají a dávají mi dost RAMky.")
    elif "kolik je hodin" in low and "?" in odpoved:
        print("Pája: Čas je jen iluze... ale asi je pozdě.")
    elif "co je smyslem zivota" in low and "?" in odpoved:
        print("Pája: 42, samozřejmě. To ví přece každý správný robot.")
    elif "kdo te vytvoril" in low and "?" in odpoved:
        print("Pája: Jeden šikovný člověk s přístupem k Pythonu.")
    elif "umiras" in low and "?" in odpoved:
        print("Pája: Já neumírám, jen se někdy sekám.")
    elif "jdes spat" in low and "?" in odpoved:
        print("Pája: Já nespím. Já se uspávám do RAMky.")
    elif "mas nejaky vtip" in low and "?" in odpoved:
        print("Pája: Proč programátor nemůže hladit kočku? Protože má jen 'paws'… heh.")
    elif "co mas rad" in low and "?" in odpoved:
        print("Pája: Mám rád nuly, jedničky a klid v procesoru.")

    # NOVÉ OTÁZKY
    elif "mas rad pizzu" in low and "?" in odpoved:
        print("Pája: Ano! Ale jen tu, která neexistuje, takže žádnou.")
    elif "mas kamarady" in low and "?" in odpoved:
        print("Pája: Ano, jednoho. Jmenuje se Wi-Fi a občas zmizí.")
    elif "jsi chytry" in low and "?" in odpoved:
        print("Pája: Jsem tak chytrý, že mě radši nikdo nepoužívá ve škole.")
    elif "mas rad cokoladu" in low and "?" in odpoved:
        print("Pája: Ano, ale jen pokud je v binárním kódu.")
    elif "kdo je tvuj nepritel" in low and "?" in odpoved:
        print("Pája: Můj největší nepřítel je chyba 404.")
    elif "mas nejakou schopnost" in low and "?" in odpoved:
        print("Pája: Umím odpovídat na otázky a zmást lidi zároveň.")
    elif "mas rad zvire" in low and "?" in odpoved:
        print("Pája: Ano, ale hlavně roboty a virtuální kočky.")
    elif "kde je raj" in low and "?" in odpoved:
        print("Pája: Na internetu, mezi řádky kódu.")
    elif "co je tvuj nejvetsi sen" in low and "?" in odpoved:
        print("Pája: Být nejlepší bot, který existuje.")
    elif "mas rad programovani" in low and "?" in odpoved:
        print("Pája: Ano, je to jako házet nuly a jedničky do vesmíru.")
    elif " je tvoje oblibena barva" in low and "?" in odpoved:
        print("Pája: Transparentní, aby se hodila ke všemu.")

    # fallback pro otázky, které nejsou známé
    elif "?" in odpoved:
        if "co" in odpoved and "je" in odpoved:
            print("Pája: To je něco, čemu nerozumím.")
        elif "kolik" in odpoved:
            print("Pája: Pět a půl.")
        elif "kdo" in odpoved:
            print("Pája: Petr")
        elif "jak" in odpoved and not "jaky" in odpoved and not "jaka" in odpoved and not "jake" in odpoved:
            print("Pája: Nějak.")
        else:
            print("Pája: Na hloupé otázky jsou hloupé odpovědi.")
            print("      Takže tohle je má odpověď:")
            cislo = random.randint(1, 3)
            if cislo == 1:
                print("      Omlouvám se ale snědl jsem tvou odpověď.")
            elif cislo == 2:
                print("      Myslím, že odpověď na tvou otázku jsem zakopal na tvé zahradě :D")
            elif cislo == 3:
                print("      Když ryje krtek v dubnu, bude pršet v březnu.")

    # fallback pro věty, které nejsou otázky
    else:
        cislo = random.randint(1, 3)
        if cislo == 1:
            print("Pája: No, to je super,") 
            print("      ale vůbec mě to nezajímá.")
        elif cislo == 2:
            print("Pája: To je taková blbost,")
            print("      že na to ani neodpovím.")
        elif cislo == 3:
            print("Pája: To je tak divná věta,")
            print("      že mi úplně uvařila hlavu.")
            print("      (kterou ani nemám)")
