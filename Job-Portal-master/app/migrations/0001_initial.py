# Generated by Django 4.0.1 on 2022-03-07 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('image', models.ImageField(upload_to='profile_image/%y', verbose_name='Image')),
                ('first_name', models.CharField(max_length=2000, verbose_name='Full Name')),
                ('username', models.CharField(max_length=2000, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=13, unique=True, verbose_name='Phone Number')),
                ('state', models.CharField(choices=[('Maharashtra', 'Maharashtra'), ('Delhi', 'Delhi'), ('Kerla', 'Kerla'), ('Chennai', 'Chennai'), ('Karnataka', 'Karnataka'), ('Tamil Nadu', 'Tamil Nadu'), ('Hydrabad', 'Hydrabad'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Himachal', 'Himachal'), ('Punjab', 'Punjab'), ('Hariyana', 'Hariyana'), ('Rajesthan', 'Rajesthan'), ('Gujrat', 'Gujrat'), ('Sikkim', 'Sikkim'), ('Oddisha', 'Oddisha'), ('Telangana', 'Telangana'), ('Uttrakhand', 'Uttrakhand')], max_length=20, verbose_name='State')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20, verbose_name='Gender')),
                ('date_joined', models.DateTimeField(auto_now=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Last Login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=2000, verbose_name='Company Name')),
                ('industry_type', models.CharField(max_length=2000, verbose_name='Industry Type')),
                ('headquarter', models.TextField(verbose_name='Headquarter')),
                ('city', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Navi Mumbai', 'Navi Mumbai'), ('Pune', 'Pune'), ('Nashik', 'Nashik'), ('Thane', 'Thane'), ('Ratnagiri', 'Ratnagiri'), ('Aurangabad', 'Aurangabad'), ('Gurgaon', 'Gurgaon'), ('Agra', 'Agra'), ('Faridabad', 'Faridabad')], max_length=40, verbose_name='City')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('logo', models.ImageField(upload_to='company_logo/%y', verbose_name='Company Logo')),
                ('discription', models.TextField(verbose_name='Discription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmitJobsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=2000, verbose_name='Job Title')),
                ('location', models.CharField(max_length=2000, verbose_name='Location')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('salary', models.IntegerField(verbose_name='Salary')),
                ('job_type', models.CharField(choices=[('Internship', 'Internship'), ('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Temporary', 'Temporary')], max_length=15, verbose_name='Job Type')),
                ('skills', models.TextField(verbose_name='Skills')),
                ('discription', models.TextField(verbose_name='Discription')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='app.companymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeSubmitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=2000, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=13, verbose_name='Phone Number')),
                ('location', models.CharField(max_length=2000, verbose_name='Location')),
                ('linked_in', models.URLField(max_length=5000, verbose_name='Linked In')),
                ('education', models.TextField(verbose_name='Education')),
                ('higher_education', models.TextField(verbose_name='Higher Education')),
                ('skills', models.TextField(verbose_name='Skills')),
                ('project', models.TextField(verbose_name='Projects')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('nationality', models.CharField(choices=[('American', 'American'), ('Indian', 'Indian'), ('Pakistani', 'Pakistani'), ('Iranian', 'Iranian'), ('Russian', 'Russian'), ('Australian', 'Australian'), ('African', 'African'), ('British', 'British'), ('Mexican', 'Mexican')], max_length=100, verbose_name='Nationality')),
                ('hobbies', models.TextField(verbose_name='Hobbies')),
                ('address', models.TextField(verbose_name='Address')),
                ('objectives', models.TextField(verbose_name='Objectives')),
                ('declaration', models.TextField(verbose_name='Declaration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, verbose_name='Enter your full name')),
                ('email', models.EmailField(max_length=254, verbose_name='Enter your email')),
                ('message', models.TextField(verbose_name='Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.submitjobsmodel')),
                ('applyers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Applyers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]