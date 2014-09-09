# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, null=True, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'author_post', blank=True)),
                ('email', models.EmailField(unique=b'True', max_length=75, verbose_name=b'Email/Username')),
                ('password', models.CharField(max_length=30, verbose_name=b'Password')),
                ('dob', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=60, verbose_name=b'Name')),
                ('email', models.EmailField(unique=b'True', max_length=75, verbose_name=b'Email')),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'articleimage/', blank=True)),
                ('title', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, to='articles.Author', null=True)),
                ('category', models.ForeignKey(blank=True, to='articles.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='articles.Post'),
            preserve_default=True,
        ),
    ]
