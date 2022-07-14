from ij import IJ
# Importing the requisite (Fiji Is Just) ImageJ modules.
from ij.io import OpenDialog
from ij.measure import ResultsTable
import os
# import csv

IJ.run("Fresh Start");

# cellCount
# a static Jython iteration of auto_cellCount that processes individual images without saving them.
# Intended to support more robust functions that require 'IJ.selectWindow()' calls and
# more advanced thresholding.
# Click 'Run' and choose a file to process.

open_dialog = OpenDialog("Choose a file", None)
# Prompts the user with a "Choose a file" dialog box.                               					
directory = open_dialog.getDirectory()
# Gets the file directory.
path = open_dialog.getPath()
# Gets the file path.                                                  					
file_name = open_dialog.getFileName()
# Gets the file name.                                         					

print directory																				 	
# print path                                                                					
print file_name									                                				

open_image = IJ.openImage(path)
open_image.show()

IJ.run("Subtract Background...", "rolling=10");                               					
IJ.run("Set Scale...", "distance=1.075 known=1 unit=µm global");              					
IJ.run("Color Threshold...",);
IJ.selectWindow("Threshold Color");
IJ.run("Close");
IJ.run("Split Channels");
IJ.selectWindow(file_name + " (red)");
IJ.run("Auto Threshold", "method=Default white");                             					
IJ.run("Analyze Particles...", "size 1-5 show=Nothing summarize");            					

IJ.renameResults("Summary", "Results");                                       					
results_table = ResultsTable.getResultsTable()
count = results_table.getValue("Count", 0)

output = open("C:/Coding Projects/Python/cellCount/output.txt", "a")
output.write(str(file_name) + ": " + (str(results_table.getValue("Count", 0))) + "\n")
output.close()

# with open("C:/Coding Projects/Python/cellCount/output.csv", "a") as output:
#	cell_labels = ["File Name", "Count"]
#	csv_writer = csv.DictWriter(output, cell_labels)
#	csv_writer.writeheader()
#	csv_writer.writerow({"File Name": file_name, "Count": count})

IJ.run("Close");
IJ.run("Fresh Start");