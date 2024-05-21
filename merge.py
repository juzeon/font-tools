from fontTools.ttLib import TTFont

# Open the Chinese and English font files
chinese_font = TTFont('SuperPingFangV1.ttf')
english_font = TTFont('SFMono-Regular.ttf')

# Get the glyph names for all ASCII characters from the English font
ascii_glyphs = english_font.getGlyphNames()

# Replace the corresponding glyphs and their metrics in the Chinese font with the glyphs and metrics from the English font
for glyph in ascii_glyphs:
    if glyph in chinese_font['glyf'].glyphs:
        chinese_font['glyf'].glyphs[glyph] = english_font['glyf'].glyphs[glyph]
        if glyph in english_font['hmtx'].metrics:
            chinese_font['hmtx'].metrics[glyph] = english_font['hmtx'].metrics[glyph]

# Save the modified Chinese font to a new file
chinese_font.save('merged_font.ttf')