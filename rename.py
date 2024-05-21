from fontTools.ttLib import TTFont

# Load the font file
font = TTFont("merged_font.ttf")

# Change all names
for name in font['name'].names:
    if name.platformID == 3 and name.platEncID == 1 and name.langID == 0x409:
        name.string = "SuperSFMonoV1".encode("utf-16-be")

# Save the modified font to a new file
font.save("SuperSFMonoV1.ttf")