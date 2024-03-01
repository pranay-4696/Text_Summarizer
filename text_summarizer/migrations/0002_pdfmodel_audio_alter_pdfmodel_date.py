# Generated by Django 4.2.4 on 2023-10-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_summarizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfmodel',
            name='audio',
            field=models.FileField(default=' ', upload_to='audios/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pdfmodel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
