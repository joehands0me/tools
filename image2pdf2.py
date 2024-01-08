import os
import sys

from fpdf import FPDF

pdf = FPDF(orientation="L")
image_directory = input("Please provide the directory you want to convert to a pdf")

# Get a list of all image files in the directory
image_files = [image for image in os.listdir(image_directory) if image.endswith(".png")]

# Sort the list of image files in ascending order
image_files.sort()

# Iterate over the sorted list of image files
for image in image_files:
    pdf.add_page()
    pdf.image(os.path.join(image_directory, image), x=10, y=8, w=277)

pdf.output("output.pdf", "F")

print(sys.path)
