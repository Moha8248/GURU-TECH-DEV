# Generated by Django 5.0.2 on 2024-06-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_delete_java_batch_delete_products_of_the_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advance_Java_Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advance_java_test_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Advance_Python_Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advance_python_test_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Basic_java_test_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Basic_python_test_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('certificate_id', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intern_Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Java_Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Python_Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='random_otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
                ('cert', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record_advance_java_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record_advance_java_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
                ('cert', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record_advance_python_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record_advance_python_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
                ('cert', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record_basic_java_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record_basic_python_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record_community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record_intern_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record_intern_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
                ('cert', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2')], default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Record_java',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_out_year', models.CharField(blank=True, max_length=4, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('working', 'Currently Working'), ('unemployed', 'Currently Unemployed'), ('still_studying', 'Currently Still Studying')], max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, default='nil', max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('disclaimer', models.BooleanField(default=False)),
                ('cert', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppLink_community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppLink_java',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WhatsAppLink_python',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
    ]