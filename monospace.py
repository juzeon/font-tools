from fontTools.ttLib import TTFont

def make_font_monospace(font_path, output_path):
    # Open the font file
    font = TTFont(font_path)

    # Set the monospace flag in the 'post' table
    font['post'].isFixedPitch = 1

    # Save the modified font to a new file
    font.save(output_path)

# Usage
make_font_monospace('input.ttf', 'output.ttf')