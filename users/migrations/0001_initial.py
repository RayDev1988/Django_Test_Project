# Generated by Django 3.0.3 on 2020-05-19 13:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('message_count', models.IntegerField(default=0)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('content', models.TextField()),
                ('rating', models.IntegerField(null=True)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('created_at', models.IntegerField()),
                ('valid_until', models.IntegerField()),
                ('phone', models.TextField(blank=True)),
                ('phone_verified', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Verification Code',
                'verbose_name_plural': 'Verification Codes',
                'db_table': 'verification_code',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('status', models.CharField(choices=[('', 'None'), ('approved', 'Approved'), ('declined', 'Declined')], default='', max_length=10)),
                ('verification_image', models.ImageField(blank=True, default='default.jpg', max_length=255, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/uploads/', location='C:\\Users\\Green\\Google Drive\\Development\\Django Projects\\django-site\\media\\uploads'), upload_to='', verbose_name='Verification Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('relationship', models.CharField(choices=[('friend', 'Friend'), ('blocked', 'Blocked'), ('ignore', 'Ignore'), ('', 'None')], default='', max_length=8)),
                ('friendship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Friendship')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('channel_name', models.CharField(default='', max_length=128, unique=True)),
                ('is_connected', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ReviewContent')),
                ('review_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_content', to='users.ReviewContent')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('image', models.ImageField(blank=True, default='default.jpg', max_length=255, storage=django.core.files.storage.FileSystemStorage(base_url='/media/uploads/', location='C:\\Users\\Green\\Google Drive\\Development\\Django Projects\\django-site\\media\\uploads'), upload_to='', verbose_name='Profile Image')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('his_age', models.CharField(blank=True, max_length=2, null=True)),
                ('her_age', models.CharField(blank=True, max_length=2, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('interests', models.TextField(blank=True, null=True)),
                ('kik', models.CharField(blank=True, max_length=30, null=True)),
                ('account_type', models.CharField(blank=True, choices=[('sm', 'Single Male'), ('sf', 'Single Female'), ('c', 'Couple')], default='', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('token', models.CharField(default='NotTokenPaypal', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('content', models.CharField(max_length=256)),
                ('has_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('content', models.TextField(null=True)),
                ('has_read', models.BooleanField(default=False)),
                ('convo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Conversation')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='friendship',
            name='users',
            field=models.ManyToManyField(through='users.Status', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversation',
            name='last_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Message'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=1589893673)),
                ('last_timestamp', models.IntegerField(default=1589893673)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip', models.CharField(blank=True, max_length=5, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'last_timestamp',
                'abstract': False,
            },
        ),
    ]
