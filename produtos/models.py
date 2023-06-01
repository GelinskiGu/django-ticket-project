import os

from django.conf import settings
from django.db import models
from PIL import Image

from utils import utils


class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(
        upload_to='bar-system/produto_imagens/%Y/%m/', blank=True, null=True)
    preco = models.FloatField(verbose_name='Preço')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    estoque = models.PositiveIntegerField(blank=True, null=True)
    mostrar = models.BooleanField(default=True)

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco)
    get_preco_formatado.short_description = 'Preço'
    
    """
    @staticmethod
    def resize_image(img, new_width=96):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        max_image_size = 96

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)
    """

    def __str__(self):
        return self.nome
