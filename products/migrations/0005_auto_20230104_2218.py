# Generated by Django 3.2.16 on 2023-01-04 16:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20221231_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='products.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('eaa41ed5-3e33-417c-aa7c-2fcdf7f681b2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='colorvarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('eaa41ed5-3e33-417c-aa7c-2fcdf7f681b2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('eaa41ed5-3e33-417c-aa7c-2fcdf7f681b2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='id',
            field=models.UUIDField(default=uuid.UUID('eaa41ed5-3e33-417c-aa7c-2fcdf7f681b2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sizevarient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('eaa41ed5-3e33-417c-aa7c-2fcdf7f681b2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
    ]