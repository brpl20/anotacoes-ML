#!/bin/bash

# Set the source directory where the CNH.pdf files are located
source_dir="/media/brpl20/CCF403F4F403E016/AaRQUIVO"

# Set the destination directory where the copied files will be placed
destination_dir="/home/brpl20/PDFs/"

# Set the starting number for the file names
number=226

# Loop through each CNH.pdf file in the source directory and copy it to the destination directory with a numbered suffix
find "$source_dir" -name "CNH.pdf" -type f | while read file; do
    # Get the filename without the extension
    filename=$(basename "$file" .pdf)

    # Copy the file to the destination directory with a numbered suffix
    cp "$file" "${destination_dir}/CNH_${number}.pdf"

    # Increment the number for the next file
    number=$((number + 1))
    echo $number
done

