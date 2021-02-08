# Generated by Django 3.1.6 on 2021-02-07 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('categories', '0001_initial'),
        ('products', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=120)),
                ('file_path', models.CharField(max_length=250)),
                ('original_name', models.CharField(max_length=120)),
                ('file_length', models.IntegerField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_fileuploads.fileupload_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TagImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.fileupload')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tags.tag')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.fileupload')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatars', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.fileupload')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.fileupload')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='categories.category')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
    ]
