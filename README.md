# Font Tools
This project is a collection of Python scripts that work with font files. It uses the fontTools Python library to manipulate TrueType font (.ttf) files. The scripts in this project allow you to merge two font files into one, read the names in a font's "name" table, rename a font file, and replace a glyph in a font file with a glyph from another font file.

## Scripts

### merge.py

This script merges two font files into one. It opens a Chinese font file and an English font file, gets the glyph names for all ASCII characters from the English font, and replaces the corresponding glyphs and their metrics in the Chinese font with the glyphs and metrics from the English font. The modified Chinese font is then saved to a new file.

### read.py
This script opens a font file and prints out all the names in the font's "name" table.

### rename.py

This script is used to rename a font file. It opens a font file, changes all names in the font's "name" table to a specified name, and then saves the modified font to a new file.

### replace.py

This script is used to replace a glyph in a target font with a glyph from a source font. It opens a source font file and a target font file, finds a specific glyph in the source font, scales the glyph, and then replaces the corresponding glyph in the target font with the scaled glyph from the source font. The modified target font is then saved to a new file.

## HTML Files
### font-test.html
This HTML file is used to test the custom font created by merge.py. It includes a CSS @font-face rule that specifies the custom font file, and sets this custom font as the default font for all elements on the page.

## Note
Please ensure that the required font files are in the same directory as the Python scripts when running them.