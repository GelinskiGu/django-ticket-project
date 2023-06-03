# Generated by Django 4.1.3 on 2022-11-20 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('estoque', models.PositiveIntegerField(blank=True, null=True)),
                ('mostrar', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produtos.categoria')),
            ],
        ),
    ]