#!/bin/bash

# Change to the directory containing the PDF files

# Loop over all PDF files in the directory
for file in *.pdf; do
  basename $file
  pdftoppm -png $file $file.png
done
