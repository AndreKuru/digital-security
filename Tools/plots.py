import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# TECNOLOGIAS
# ==========================================

tecnologias = [
    "RAM",
    "SSD",
    "HD",
    "Pendrive",
    "microSD",
    "Blu-ray",
    "Fita LTO",
    "Google Drive",
    "Proton Drive",
]

# ==========================================
# VIDA ÚTIL (anos)
# ==========================================

vida_min = np.array([10, 5, 3, 3, 2, 10, 15, 2, 1.2])

vida_max = np.array([30, 10, 8, 10, 10, 30, 30, 2, 1.2])

# ==========================================
# CAPACIDADE (R$200)
# ==========================================

capacidade = np.array(
    [
        3.9,  # RAM
        225,  # SSD
        540,  # HD
        206,  # Pendrive
        194,  # microSD
        1031,  # Blu-ray
        2522,  # Fita LTO
        100,  # Google Drive
        200,  # Proton Drive
    ]
)

# ==========================================
# CORES (CAPACIDADE)
# ==========================================

cores_capacidade = [
    "#59a14f",
    "#59a14f",
    "#59a14f",
    "#59a14f",
    "#59a14f",
    "#59a14f",
    "#59a14f",
    "#e15759",
    "#e15759",
]

# ==========================================
# CONFIGURAÇÃO
# ==========================================

x = np.arange(len(tecnologias))
width = 0.65

plt.style.use("seaborn-v0_8-darkgrid")

plt.rcParams.update(
    {
        "font.size": 16,  # base font size
        "axes.titlesize": 22,  # title
        "axes.labelsize": 18,  # axis labels
        "xtick.labelsize": 14,  # x ticks
        "ytick.labelsize": 14,  # y ticks
        "legend.fontsize": 14,
    }
)

# ==========================================
# GRÁFICO 1 - VIDA ÚTIL
# ==========================================

fig, ax = plt.subplots(figsize=(14, 6))

# Mínimo
ax.bar(x, vida_min, width, label="Mínimo aproximado", color="#4e79a7")

# Máximo (faixa adicional)
ax.bar(
    x,
    vida_max - vida_min,
    width,
    bottom=vida_min,
    label="Máximo aproximado",
    color="#a0cbe8",
)

ax.set_title("Vida útil aproximada das tecnologias")
ax.set_ylabel("Anos")

ax.set_xticks(x)
ax.set_xticklabels(tecnologias, rotation=15)

# ==========================================
# VALORES VIDA ÚTIL (MIN E MAX)
# ==========================================

for i in range(len(tecnologias)):
    # mínimo
    ax.text(
        i,
        vida_min[i] + 0.3,
        f"{vida_min[i]:.1f}",
        ha="center",
        fontsize=14,
        color="black",
    )

    # máximo
    ax.text(
        i,
        vida_max[i] + 0.3,
        f"{vida_max[i]:.1f}",
        ha="center",
        fontsize=14,
        fontweight="bold",
        color="black",
    )

ax.legend(loc="upper right", frameon=True)

plt.tight_layout()
plt.savefig("vida_util.png", dpi=300)

# ==========================================
# GRÁFICO 2 - CAPACIDADE
# ==========================================

fig, ax = plt.subplots(figsize=(14, 6))

ax.bar(x, capacidade, width, color=cores_capacidade)

ax.set_title("Capacidade obtida com R$200")
ax.set_ylabel("GB")

ax.set_xticks(x)
ax.set_xticklabels(tecnologias, rotation=15)

# ==========================================
# VALORES NAS BARRAS (CAPACIDADE)
# ==========================================

for i, v in enumerate(capacidade):
    ax.text(i, v * 1.05, f"{v:.0f} GB", ha="center", fontsize=15)

plt.tight_layout()
plt.savefig("capacidade_por_200.png", dpi=300)
plt.show()
