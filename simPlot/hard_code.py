import matplotlib.pyplot as plt
import numpy as np

freq = []
rf_exp = []
s_comsol = []

rf_file = open('RF_Exp_1x.txt', 'r')
rf_data = rf_file.read().splitlines()
for i in rf_data:
    split_col = i.split() # The COMSOL-generated .txt organizes data in a two-column format.
    freq.append(float(split_col[0]))
    rf_exp.append(float(split_col[1]))

plt.plot(freq, rf_exp, color='lightgreen', linestyle='solid', label='RF_Exp_1x')
plt.ticklabel_format(axis='x', style='sci', scilimits=(9, 9))
plt.xticks(np.arange(5000000000, 18000000000, 5000000000), fontsize=14)
plt.yticks(fontsize=14)
freq.clear()

comsol_file = open('Selected S21_1x.txt', 'r')
comsol_data = comsol_file.read().splitlines()
for i in comsol_data:
    split_col = i.split()
    freq.append(float(split_col[0]))
    s_comsol.append(float(split_col[1]))

plt.plot(freq, s_comsol, color='red', linestyle='dashed', label='COMSOL', marker='*', markevery=18)
plt.ticklabel_format(axis='x', style='sci', scilimits=(9, 9))
plt.xticks(np.arange(5000000000, 18000000000, 5000000000), fontsize=14)
plt.yticks(fontsize=14)
freq.clear()

plt.grid(visible=True)
plt.tight_layout()
plt.xlabel('Frequency (GHz)', labelpad=14, fontname='Arial', fontsize=18)  # fontweight='bold'
plt.ylabel('S-parameter (dB)', labelpad=14, fontname='Arial', fontsize=18) # fontweight='bold'
plt.legend(loc='upper right', fontsize=9, borderpad=0.8, edgecolor='black', handlelength=3)
plt.tick_params(length=12, width=1.5, pad=10, direction='inout')

plt.show()