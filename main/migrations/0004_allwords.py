# Generated by Django 5.0.1 on 2024-02-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_allwords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allwords',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=60)),
                ('code', models.IntegerField()),
                ('code_parent', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('type_sub', models.CharField(max_length=10)),
                ('type_ssub', models.CharField(max_length=10)),
                ('plural', models.SmallIntegerField()),
                ('gender', models.CharField(max_length=3)),
                ('wcase', models.CharField(max_length=4)),
                ('comp', models.CharField(max_length=5)),
                ('soul', models.SmallIntegerField()),
                ('transit', models.CharField(max_length=6)),
                ('perfect', models.SmallIntegerField()),
                ('face', models.CharField(max_length=4)),
                ('kind', models.CharField(max_length=3)),
                ('time', models.CharField(max_length=4)),
                ('inf', models.SmallIntegerField()),
                ('vozv', models.SmallIntegerField()),
                ('nakl', models.CharField(max_length=5)),
                ('short', models.SmallIntegerField()),
            ],
        ),
    ]
