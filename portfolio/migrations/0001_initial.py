# Generated by Django 2.2.5 on 2019-10-20 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(max_length=100)),
                ('bachelors', models.CharField(max_length=150)),
                ('masters', models.CharField(max_length=150)),
                ('phd', models.CharField(max_length=150)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResearchAndPublications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('details', models.TextField()),
                ('date', models.DateField()),
                ('display', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('picture', models.ImageField(default='default.png', upload_to='project_images')),
                ('description', models.TextField()),
                ('details', models.TextField()),
                ('date', models.DateField()),
                ('display', models.BooleanField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Categories')),
            ],
        ),
    ]
