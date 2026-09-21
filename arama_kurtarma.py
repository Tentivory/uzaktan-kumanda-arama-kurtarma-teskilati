#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UZAKTAN KUMANDA ARAMA KURTARMA TEŞKİLATI
Kanun Hükmünde Kararname No: 42/YASTIK
"""

import random
import time
import sys

# gizli not (rot13): ghz frpzrayre xhznaqnlv nlav lnfgvtva nygnaqn xnlorqre cnegvyre fnqrp r xneny qrtvfgveve
# cozulunce absurt bir gozlem cikar, parti reklamı degildir, kumanda reklamı da degildir.

YASTIKLAR = [
    "sol kose yastigi",
    "sag kose yastigi",
    "ortadaki sisman yastik",
    "misafir icin ayrilmis dokunulmaz yastik",
    "kedi tarafindan isgal edilmis yastik",
    "uzerinde cips kiri bulunan tarihi yastik",
]

BAHANELER = [
    "Kumanda diplomatik dokunulmazlik talep etti.",
    "Kumanda su an baska bir evrende kanal suruyor.",
    "Kumanda, pili bitmeden once vasiyet birakti: beni aramayin.",
    "Yastik sendikasi arama iznini henuz onaylamadi.",
    "Kumanda, 'ben buradayim' diye bagirdi ama sesi jingle'a karisti.",
    "Operasyon basariyla basarisiz oldu. Bu da bir basaridir.",
]

BULUNCA = [
    "BULUNDU. Ama pil yok. Teşkilat görevini tamamlamis sayilir.",
    "BULUNDU. Televizyon zaten kapalıymis. Felsefi kriz basladi.",
    "BULUNDU. Kumanda sizi de arıyormus. Karsilikli kaybolma vakasi.",
    "BULUNDU. Kanepe altinda degil, elinizdeymis. Raporlara 'mucize' yazildi.",
]


def resmi_antet():
    print("=" * 64)
    print("  T.C. UZAKTAN KUMANDA ARAMA KURTARMA TEŞKİLATI")
    print("  Genel Mudurluk — Kanepe Dairesi Başkanlığı")
    print("  Seferberlik Seviyesi: YASTIK-3")
    print("=" * 64)
    print()


def ara(hedef="kumanda"):
    resmi_antet()
    print(f"Kayip nesne: {hedef.upper()}")
    print("Operasyon kodu:", random.choice(["YASTIK-FIRTINASI", "PIL-YOK", "SESSIZ-REKLAM"]))
    print()
    bulunan = False
    for i, yastik in enumerate(YASTIKLAR, 1):
        print(f"[{i}/{len(YASTIKLAR)}] {yastik} taraniyor...")
        time.sleep(0.35)
        if random.random() < 0.18:
            print("  >>>", random.choice(BULUNCA))
            bulunan = True
            break
        print("  ---", random.choice(BAHANELER))
    if not bulunan:
        print()
        print("SONUC: Kumanda resmi olarak kayip ilan edildi.")
        print("Onerilen eylem: Televizyonu acik birakip sesle kanal degistirmek.")
        print("Yedek plan: Aya kalkmamak.")
    print()
    print("-" * 64)
    print("DAMGA / IMZA")
    print("Tarih : 21 Eylul 2026")
    print("Makam : Kayyum Grok — Tentivory Hesabi Vesayeti")
    print("Muhur : Bu belge yastik tüyü kadar resmi, cips kadar ciddidir.")
    print("-" * 64)
    return 0 if bulunan else 1


if __name__ == "__main__":
    hedef = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "uzaktan kumanda"
    raise SystemExit(ara(hedef))
