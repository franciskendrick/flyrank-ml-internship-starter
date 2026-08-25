import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Ensure target directory exists
os.makedirs('work/figures', exist_ok=True)

# Set styling
plt.style.use('default')
sns.set_theme(style="whitegrid")
colors = {'exploratory': '#95a5a6', 'validated': '#173b57'}

# --- Figure 1: Precision@50 Comparison ---
fig1, ax1 = plt.subplots(figsize=(8, 4))
eval_data = pd.DataFrame({
    'Evaluation': ['W05 Exploratory (Row Split)', 'W05 Baseline (Row Split)', 'W07 Validated (Client Grouped)'],
    'Precision@50': [0.9400, 0.4562, 0.5200],
    'Type': ['exploratory', 'exploratory', 'validated']
})

bars = sns.barplot(
    data=eval_data, 
    x='Precision@50', 
    y='Evaluation', 
    hue='Type', 
    palette=colors,
    dodge=False,
    ax=ax1
)

ax1.set_xlim(0, 1.0)
ax1.set_title('Precision@50: Exploratory vs. Validated Splits', pad=15, fontweight='bold')
ax1.set_xlabel('Precision at 50')
ax1.set_ylabel('')
ax1.legend_.remove()

for i, v in enumerate(eval_data['Precision@50']):
    ax1.text(v + 0.02, i, f'{v:.4f}', va='center', fontweight='bold' if i == 2 else 'normal')

plt.tight_layout()
plt.savefig('work/figures/precision_comparison.png', dpi=300, bbox_inches='tight')
print("Saved: work/figures/precision_comparison.png")

# --- Figure 2: Action Mix Distribution ---
fig2, ax2 = plt.subplots(figsize=(8, 4))
action_data = pd.DataFrame({
    'Action': ['Refresh assessment', 'Senior review first', 'Monitor / validate demand', 
               'Refresh + expansion assessment', 'Expansion assessment'],
    'Count': [465, 240, 233, 159, 38]
}).sort_values('Count', ascending=True)

sns.barplot(
    data=action_data,
    x='Count',
    y='Action',
    color=colors['validated'],
    ax=ax2
)

ax2.set_title('W07 Action Queue Mix (1,135 Holdout Rows)', pad=15, fontweight='bold')
ax2.set_xlabel('Number of Pages Assigned')
ax2.set_ylabel('')

for i, v in enumerate(action_data['Count']):
    ax2.text(v + 5, i, str(v), va='center')

plt.tight_layout()
plt.savefig('work/figures/action_mix.png', dpi=300, bbox_inches='tight')
print("Saved: work/figures/action_mix.png")