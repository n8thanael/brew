# Generated by Django 4.0.4 on 2022-07-24 01:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='AaronsTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': "Aaron's Tag",
                'verbose_name_plural': 'Aaron Tags',
            },
        ),
        migrations.CreateModel(
            name='AaronPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('files', wagtail.fields.StreamField([('audio_file', wagtail.documents.blocks.DocumentChooserBlock())], use_json_field=True)),
                ('buttonimage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aarons_tags', to='aaron.aaronstag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': "Aaron's Page",
                'verbose_name_plural': "Aaron's Pages",
            },
            bases=('wagtailcore.page',),
        ),
    ]