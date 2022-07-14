#@ File    (label = "Input directory", style = "directory") srcFile
#@ File    (label = "Output directory", style = "directory") dstFile
#@ String  (label = "File extension", value=".tif") ext
#@ String  (label = "File name contains", value = "") containString
#@ boolean (label = "Keep directory structure when saving", value = true) keepDirectories

# auto_cellCount
# a Jython iteration of ImageJ that automates particle analysis for every .tif file in a directory.
# Click 'Run' in the ImageJ scripting window, making sure to
# designate an "Input directory", "Output directory", and "File extension" (i.e., .tif).
 
from ij import IJ
# Importing the requisite (Fiji Is Just) ImageJ modules.
from ij.measure import ResultsTable
import os
# import csv
# Used for the alternative output function below.

def batch_process():
  srcDir = srcFile.getAbsolutePath()
  dstDir = dstFile.getAbsolutePath()
  for root, directories, filenames in os.walk(srcDir):
    filenames.sort()
    for filename in filenames:
      # Check for file extension
      if not filename.endswith(ext):
        continue
      # Check for file name pattern
      if containString not in filename:
        continue
      process(srcDir, dstDir, root, filename, keepDirectories)
 
def process(srcDir, dstDir, currentDir, fileName, keepDirectories):
# Opening and showing all images in a desginated "Input directory" (srcFile).
  print "\nProcessing File Name:", fileName
  imp = IJ.openImage(os.path.join(currentDir, fileName))
  imp.show()
   
# Applying (Fiji Is Just) ImageJ processing commands to these images as they are opened and showed.
  IJ.run("Subtract Background...", "rolling=10");
  # Minimizes artifacts from microscopy lighting.
  IJ.run("Set Scale...", "distance=1.075 known=1 unit=µm global");
  # Sets a global scale, to be adapted as necessary.
  IJ.run("Color Threshold...",);
  IJ.selectWindow("Threshold Color");
  IJ.run("Close");
  IJ.run("Analyze Particles...", "size 1-5 show=Nothing summarize");
  
  IJ.renameResults("Summary", "Results");
  # Allows for integration with the 'ResultsTable' package.
  results_table = ResultsTable.getResultsTable()
  count = results_table.getValue("Count", 0)
  # Output function that writes filename and cell count per image into a '.txt' file.
  def export_to(path):
    output = open(path, "a")
    output.write(str(fileName) + ": " + (str(results_table.getValue("Count", 0))) + "\n\n")
    output.close()
  export_to("C:/Coding Projects/Python/cellCount/output.txt")
  # Path of user's choice.

# Alternative output function that writes filename and cell count per image into adjacent '.csv' cells.
#  with open("C:/Coding Projects/Python/cellCount/output.csv", "a") as output:
#   cell_labels = ["File Name", "Count"]
#   csv_writer = csv.DictWriter(output, cell_labels)
#   csv_writer.writeheader()
#   csv_writer.writerow({"File Name": fileName, "Count": count})
  
# Saving the processed images to a designated "Output directory" (dstFile).
  saveDir = currentDir.replace(srcDir, dstDir) if keepDirectories else dstDir
  if not os.path.exists(saveDir):
    os.makedirs(saveDir)
  print "Saving to", saveDir
  IJ.saveAs(imp, "Tiff", os.path.join(saveDir, fileName));
  IJ.run("Close");
  imp.close()
  # Closing the images after they have been opened, showed, processed, and saved.

batch_process()