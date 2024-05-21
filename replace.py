from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen

# Load the source and target font files
source_font = TTFont("sarasa.ttf")
target_font = TTFont("ofont.ttf")

# Get the 'cmap' table from the fonts, which maps character codes to glyph names
source_cmap = source_font.getBestCmap()
target_cmap = target_font.getBestCmap()

# Find the glyph name for the character 'ん' in the source font
source_glyph_name = None
for code, glyph in source_cmap.items():
    if chr(code) == 'ん':
        source_glyph_name = glyph
        break

# Replace the glyph in the target font with the one from the source font
if source_glyph_name:
    target_glyph_name = target_cmap[ord('ん')]
    source_glyph = source_font['glyf'][source_glyph_name]
    
    # Create a pen to draw a new glyph
    pen = TTGlyphPen(target_font.getGlyphSet())
    
    # Create a transform pen to scale the glyph
    scale = 2  # Adjust this value to get the desired size
    transform_pen = TransformPen(pen, (scale, 0, 0, scale, 0, 0))
    
    # Draw the scaled glyph
    source_glyph.draw(transform_pen, source_font['glyf'])
    
    # Replace the glyph in the target font with the scaled glyph
    target_font['glyf'][target_glyph_name] = pen.glyph()

# Save the modified font to a new file
target_font.save("rfont.ttf")