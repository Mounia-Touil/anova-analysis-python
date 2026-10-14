import matplotlib.pyplot as plt

# Data for A (Low), B (Medium), C (High)
data = {
    "A Low": [18, 22, 20, 24, 19, 21, 23, 17, 25, 20],
    "B Medium": [14, 15, 13, 16, 15, 14, 12, 16, 13, 14],
    "C High": [19, 18, 17, 21, 20, 22, 19, 18, 20, 21]
}

# Create box-plot
plt.figure(figsize=(8, 6))
plt.boxplot(list(data.values()), labels=list(data.keys()))
plt.title("Bug-fix Time by Comment Density")
plt.xlabel("Comment Density (A=Low, B=Medium, C=High)")
plt.ylabel("Bug-fix Time (minutes)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("boxplot_comment_density.png", dpi=300)
plt.show()
