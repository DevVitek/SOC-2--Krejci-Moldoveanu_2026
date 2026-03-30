import matplotlib.pyplot as plt
import numpy as np

# --- DATA ---
data = {
    'ibm_torino': (0.69, 0.74, 2.18),
    'ibm_kingston': (2.32, 2.1, 2.23),
    'ibm_marrakesh': (2.1, 1.75, 2.12),
    'ibm_fez': (2.2, 0.8, 2.18),
    'ibm_pittsburgh': (2.2517,2.4611, 2.15 )
}

labels = list(data.keys())
v1 = [v[0] for v in data.values()]
v2 = [v[1] for v in data.values()]
v0 = [v[2] for v in data.values()]

x = np.arange(len(labels)) 
width = 0.25 

fig, ax = plt.subplots(figsize=(14,9))

# Vykreslení sloupců
rects1 = ax.bar(x - width, v1, width, label='Jedna vrstva', color='royalblue')
rects2 = ax.bar(x, v2, width, label='Dvě vrstvy', color='darkorange')
rects3 = ax.bar(x + width, v0, width, label='Bez použití protokolu', color='green')

# Červená tečkovaná čára pro klasickou limitu (S = 2)
ax.axhline(y=2, color='red', linestyle='--', linewidth=1.5, label='Klasická limita S=2')

# --- FORMÁTOVÁNÍ (ZVĚTŠENÍ POPISKŮ) ---

# NAHOŘE: Titulek
ax.set_title('Srovnání použití vrstev UUCDB na různých kvantových počítačích', fontsize=22, pad=20)

# NALEVO: Název osy a čísla
ax.set_ylabel('Hodnota S', fontsize=18, labelpad=15)
ax.tick_params(axis='y', labelsize=15)

# DOLE: Názvy počítačů
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=0, fontsize=18) 

# LEGENDA: Zůstává zvětšená
ax.legend(loc='upper left', fontsize=15, title_fontsize=17)

# Přidání popisků hodnot nad sloupce
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if not np.isnan(height):
            ax.annotate(f'{height:.2f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=17)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# Nastavení limitu osy y a mřížky
ax.set_ylim(0, 3.2)
ax.grid(axis='y', linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()