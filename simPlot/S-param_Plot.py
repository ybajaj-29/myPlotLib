import matplotlib.pyplot as plt
import numpy as np
import fnmatch
import os

# This was part of my work as a Fall 2021 SURP Intern at BNL.

# Initializing lists to store 2-column x (freq) and y-data (s_param)
# from a designated COMSOL 'S-parameters.txt' file (S11 or S21).
freq = [] 
s_param = []

# Opening, then reading the file with a static function call and
# applying matplotlib processing commands to show the data
# after it has been appended to its corresponding list.
def graph_display(file_Name):
    for file_name in os.listdir('.'):
        if fnmatch.fnmatch(file_name, file_Name):
            print('\nDisplaying S-parameter plot for: ' + file_Name)
            file = open(file_Name, 'r')
            data = file.read().splitlines()
            file.close()
            for i in data:
                split_col = i.split()
                freq.append(float(split_col[0]))
                s_param.append(float(split_col[1]))
                
            plt.plot(freq, s_param, color='blue', linestyle='dashed', label=file_Name[0:3])
            plt.tight_layout()
            
            plt.legend(loc='lower right', bbox_to_anchor=(0.5, 0.025, 0.5, 0.5), fontsize=18, borderpad=0.8, edgecolor='black', handlelength=3)
            plt.tick_params(length=12, width=1.5, pad=10, direction='inout')

            plt.xlabel('Frequency (Hz)', labelpad=20, fontname='Arial', fontsize=24, fontweight='bold')
            plt.xticks(np.arange(min(freq), max(freq), 1000000000*0.75), fontsize=18)
            plt.gca().get_xticklabels()[0].set_color('red')
            plt.gca().get_xticklabels()[0].set_fontweight('bold')
            plt.gca().get_xticklabels()[23].set_color('red')
            plt.gca().get_xticklabels()[23].set_fontweight('bold')

            plt.ylabel('S-parameter (dB)', labelpad=20, fontname='Arial', fontsize=24, fontweight='bold')
            plt.yticks(np.arange(max(s_param), min(s_param)-1, -2), fontsize=18)
            
            print('\nMinimum S-parameter (dB): ' + str(min(s_param)))
            print('Maximum S-parameter (dB): ' + str(max(s_param)))
            
            plt.show()
            freq.clear()
            s_param.clear()
        
# A typical file handle I manually save after running studies on COMSOL Multiphysics 5.5 (file_Name).
# Usually designated by a date at the suffix so I don't lose track after hundreds of studies.
# After COMSOL adds a Python API, I plan to revisit this so manual saving isn't requisite.
graph_display('S11_param.txt')
