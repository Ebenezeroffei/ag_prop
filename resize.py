import os
from PIL import Image

#imgs = [
#    r"C:\Users\HEDGE PENSIONS TRUST\Desktop\clones\Dj\ag_prop\app\static\app\images\slide1.jpg",
#    r"C:\Users\HEDGE PENSIONS TRUST\Desktop\clones\Dj\ag_prop\app\static\app\images\slide2.jpg",
#    r"C:\Users\HEDGE PENSIONS TRUST\Desktop\clones\Dj\ag_prop\app\static\app\images\slide3.jpg",
#    r"C:\Users\HEDGE PENSIONS TRUST\Desktop\clones\Dj\ag_prop\app\static\app\images\slide4.jpg",
#]

img = r"C:\Users\HEDGE PENSIONS TRUST\Desktop\clones\Dj\ag_prop\app\static\app\images\fallback.jpg"

#for img in imgs:
#    image = Image.open(img)
#    print(f"Width: {image.width}, Height: {image.height}")
#    print()
#    image = image.resize((1000,350))
#    image.save(img)

i = Image.open(img)
i = i.resize((2000,300))
i.save(img)