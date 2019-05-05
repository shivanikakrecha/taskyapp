#enerated by Django 2.2.1 on 2019-05-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField()),
                ('duration', models.DateTimeField()),
                ('avtar', models.ImageField(blank=True, null=True, upload_to='cars')),
            ],
        ),
    ]
