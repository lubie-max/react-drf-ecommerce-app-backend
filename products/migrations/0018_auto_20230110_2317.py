# Generated by Django 3.2.16 on 2023-01-10 17:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20230110_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0dedd339-93f8-4318-b00f-2df9691b744b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0dedd339-93f8-4318-b00f-2df9691b744b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0dedd339-93f8-4318-b00f-2df9691b744b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='colorvarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0dedd339-93f8-4318-b00f-2df9691b744b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0dedd339-93f8-4318-b00f-2df9691b744b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0dedd339-93f8-4318-b00f-2df9691b744b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sizevarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0dedd339-93f8-4318-b00f-2df9691b744b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]