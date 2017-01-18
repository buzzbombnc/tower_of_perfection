import sys
import os
import os.path

from PIL import Image

TOP_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, TOP_DIR)
from tower_of_perfection import settings

MEDIA_PATH = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, 'blog', '1')
try:
    os.makedirs(MEDIA_PATH)
except:
    pass

small=Image.new('RGB', (200, 200), '#ff0000')
try:
    small.save(os.path.join(MEDIA_PATH, '200x200.png'))
except:
    pass

big=Image.new('RGB', (1500, 1500), '#0000ff')
try:
    big.save(os.path.join(MEDIA_PATH, '1500x1500.png'))
except:
    pass

