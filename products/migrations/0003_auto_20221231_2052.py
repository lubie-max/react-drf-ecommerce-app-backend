# Generated by Django 3.2.16 on 2022-12-31 15:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221231_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5763d1b9-4718-4c14-a711-699bf1fdbae2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='colorvarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5763d1b9-4718-4c14-a711-699bf1fdbae2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='product_color', to='products.ColorVarient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5763d1b9-4718-4c14-a711-699bf1fdbae2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='product_size', to='products.SizeVarient'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5763d1b9-4718-4c14-a711-699bf1fdbae2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sizevarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5763d1b9-4718-4c14-a711-699bf1fdbae2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
