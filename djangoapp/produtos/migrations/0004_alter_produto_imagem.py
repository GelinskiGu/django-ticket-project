# Generated by Django 4.1.5 on 2023-06-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_remove_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='bar-system/produto_imagens/%Y/%m/'),
        ),
    ]
