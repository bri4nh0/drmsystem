from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.db import models
from django.utils import timezone
from matplotlib import pyplot as plt


#

class ImageFile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

    def delete(self):
        self.image.delete()
        super().delete()

    def save(self):
        super().save()
        im = Image.open(self.image.path)
        width, height = im.size
        draw = ImageDraw.Draw(im)
        text = "DRM SYStem Watermark"
        font = ImageFont.truetype('arial.ttf', 80)
        textwidth, textheight = draw.textsize(text, font)
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, font=font)
        im.show()

        im.save(self.image.path)


class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    created = models.DateTimeField(auto_now_add=True)

    def delete(self):
        self.file.delete()
        super().delete()
