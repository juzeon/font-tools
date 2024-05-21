from fontTools.ttLib import TTFont

# Open the font file
font = TTFont("ofont.ttf")
# Append each key and its corresponding value to the string
for name in font["name"].names:
    print(name)
