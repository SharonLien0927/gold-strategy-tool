from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'icons')
os.makedirs(OUT_DIR, exist_ok=True)

FONT_PATH = 'C:/Windows/Fonts/arialbd.ttf'

def make_icon(size, path):
    img = Image.new('RGB', (size, size), color='black')
    draw = ImageDraw.Draw(img)
    font_size = int(size * 0.62)
    font = ImageFont.truetype(FONT_PATH, font_size)
    text = 'X'
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - w) / 2 - bbox[0]
    y = (size - h) / 2 - bbox[1]
    draw.text((x, y), text, fill='white', font=font)
    img.save(path, 'PNG')
    print('wrote', path)

make_icon(180, os.path.join(OUT_DIR, 'apple-touch-icon.png'))
make_icon(192, os.path.join(OUT_DIR, 'icon-192.png'))
make_icon(512, os.path.join(OUT_DIR, 'icon-512.png'))
