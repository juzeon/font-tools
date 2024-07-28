from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen

# Load the reference and target font files
reference_font = TTFont("sarasa.ttf")
target_font = TTFont("SuperPingFangV1.ttf")

# Get the 'cmap' table from the fonts, which maps character codes to glyph names
reference_cmap = reference_font.getBestCmap()
target_cmap = target_font.getBestCmap()

# Iterate over the range of unicode values from U+2500 to U+257F
for code in range(0x2500, 0x2580):
    if code in reference_cmap and code in target_cmap:
        reference_glyph_name = reference_cmap[code]
        target_glyph_name = target_cmap[code]

        # Get the glyph from the reference font
        reference_glyph = reference_font['glyf'][reference_glyph_name]

        # Create a pen to draw a new glyph
        pen = TTGlyphPen(target_font.getGlyphSet())

        # Create a transform pen to scale the glyph
        scale = 2  # Adjust this value to get the desired size
        transform_pen = TransformPen(pen, (scale, 0, 0, scale, 0, 0))

        # Draw the scaled glyph
        reference_glyph.draw(transform_pen, reference_font['glyf'])

        # Replace the glyph in the target font with the scaled glyph
        target_font['glyf'][target_glyph_name] = pen.glyph()

# Save the modified target font to a new file
target_font.save("modified_target.ttf")