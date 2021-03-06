# Generated by Django 3.0.7 on 2020-07-07 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evento', '0009_auto_20200708_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStat',
            fields=[
                ('ES_id', models.AutoField(primary_key=True, serialize=False)),
                ('ES_heading', models.CharField(max_length=100)),
                ('ES_count', models.IntegerField()),
                ('ES_img', models.ImageField(upload_to='Evento/images')),
            ],
        ),
    ]
