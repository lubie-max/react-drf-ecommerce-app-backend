# Generated by Django 3.2.16 on 2023-01-10 15:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20230110_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead380bb-7721-4c0f-9d13-1ae35e9efe52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead380bb-7721-4c0f-9d13-1ae35e9efe52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead380bb-7721-4c0f-9d13-1ae35e9efe52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='colorvarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead380bb-7721-4c0f-9d13-1ae35e9efe52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead380bb-7721-4c0f-9d13-1ae35e9efe52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead380bb-7721-4c0f-9d13-1ae35e9efe52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sizevarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ead380bb-7721-4c0f-9d13-1ae35e9efe52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
