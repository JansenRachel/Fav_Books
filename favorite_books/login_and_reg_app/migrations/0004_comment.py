# Generated by Django 2.2 on 2021-09-12 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_reg_app', '0003_messagepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_and_reg_app.MessagePost')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_and_reg_app.User')),
            ],
        ),
    ]