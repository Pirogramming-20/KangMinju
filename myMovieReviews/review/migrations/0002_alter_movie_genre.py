# Generated by Django 5.0.1 on 2024-01-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('action', '액션'), ('comedy', '코미디'), ('drama', '드라마'), ('romance', '로맨스'), ('thriller', '스릴러'), ('horror', '호러'), ('sci-fi', 'SF'), ('fantasy', '판타지'), ('animation', '애니메이션'), ('documentary', '다큐멘터리'), ('musical', '뮤지컬'), ('mystery', '미스터리')], default='------', max_length=32),
        ),
    ]
