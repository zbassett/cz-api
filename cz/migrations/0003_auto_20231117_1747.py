# Generated by Django 3.2.15 on 2023-11-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cz', '0002_alter_player_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('tournamentid', models.AutoField(primary_key=True, serialize=False)),
                ('tournamentyear', models.CharField(max_length=15)),
                ('tournamentname', models.CharField(max_length=100)),
                ('tournamenttitle', models.CharField(max_length=25)),
                ('tournamentdescription', models.TextField()),
                ('status', models.IntegerField()),
                ('clubid', models.IntegerField()),
                ('gametype', models.IntegerField()),
                ('numends', models.IntegerField()),
                ('expanded_record', models.IntegerField()),
                ('freeguardid', models.IntegerField()),
                ('doubles', models.IntegerField()),
                ('eventid', models.IntegerField()),
                ('allowtie', models.IntegerField()),
                ('advanceddrops', models.IntegerField()),
                ('hightraffic', models.IntegerField()),
                ('bracketcolour', models.CharField(max_length=6)),
                ('statsrun', models.IntegerField()),
                ('hidedraw', models.IntegerField()),
            ],
            options={
                'db_table': 'tournament',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tournamentdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drawid', models.IntegerField()),
                ('drawname', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
                ('active', models.IntegerField()),
                ('active_games', models.IntegerField()),
                ('lastscoresupdate', models.IntegerField()),
                ('drawdatetime', models.DateTimeField()),
                ('drawtime', models.IntegerField()),
                ('drawdatetime2', models.DateTimeField()),
                ('drawtime2', models.IntegerField()),
                ('startdraw', models.IntegerField()),
                ('maxteams', models.IntegerField()),
                ('filled', models.IntegerField()),
                ('draw_pair', models.IntegerField()),
                ('official', models.IntegerField()),
            ],
            options={
                'db_table': 'tournamentdraw',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tournamenttype',
            fields=[
                ('tournamenttypeid', models.AutoField(primary_key=True, serialize=False)),
                ('format', models.IntegerField()),
                ('tournamenttype', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=50)),
                ('events', models.IntegerField()),
            ],
            options={
                'db_table': 'tournamenttype',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='clubs',
            options={'managed': False, 'verbose_name': 'Club', 'verbose_name_plural': 'Clubs'},
        ),
    ]
