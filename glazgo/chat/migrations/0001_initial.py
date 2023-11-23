# Generated by Django 4.2.7 on 2023-11-23 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200)),
                ('attachment', models.FileField(blank=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('conversation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.conversation')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]