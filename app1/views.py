from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, CourseLinks
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import EmailLoginForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect
from random import choice
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import random_otp  # Import your Python_otp model here
import random
from django.utils import timezone
from datetime import timedelta
from datetime import datetime
from django.db.models import Max
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
from django.contrib.staticfiles import finders


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'signup.html', {'error_message': "Your password and confirm password are not the same!"})

        else:
            try:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                UserProfile.objects.create(user=my_user, flag=0)
                return redirect('login')
            except IntegrityError:
                return render(request, 'signup.html', {'error_message': "Username already exists. Please choose a different username."})
    return render(request, 'signup.html')

@login_required(login_url='login')
def HomePage(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    # course_links = CourseLinks.objects.filter(flag=user_profile.flag).first()  # Fetch the course link based on the flag
    course_links = CourseLinks.objects.filter(batch_number=user_profile.batch_number).first()  # Fetch the course link based on the batch number

    context = {
        'user_profile': user_profile,
        'flag': user_profile.flag,
        'Course_Links': course_links,
        'batch_number': user_profile.batch_number  # Pass batch_number to the context
    }
    return render(request, 'home2.html', context)

@login_required(login_url='login')
def req_view(request):
    return render(request, 'req.html')
def LoginPage(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                try:
                    user_profile = UserProfile.objects.get(user=user)
                    if user_profile.flag == 0:
                        return redirect('req')
                    else:
                        return redirect('home2')
                except UserProfile.DoesNotExist:
                    return render(request, 'login.html', {'form': form, 'error': 'User profile not found.'})
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid email or password.'})
    else:
        form = EmailLoginForm()

    return render(request, 'login.html', {'form': form})



def LogoutPage(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse,reverse_lazy
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.edit import FormView

class CustomPasswordResetView(FormView):
    template_name = 'password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')  # Use named URL here
    form_class = PasswordResetForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        users = User.objects.filter(email=email)
        if users.exists():
            for user in users:
                current_site = get_current_site(self.request)
                subject = 'Password Reset Requested'
                message = render_to_string('password_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'https' if self.request.is_secure() else 'http',
                })
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
        return super().form_valid(form)



from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import JoinDetails

@login_required(login_url='login')
def join_course(request):
    if request.method == 'POST':
        email = request.user.email
        JoinDetails.objects.create(email=email, join_date=timezone.now())
        course_link = request.POST.get('course_link')
        if course_link:
            return redirect(course_link)
    return HttpResponse("Invalid request", status=400)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def home(request):
	records = Record.objects.all() 
    
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})
      
# LANDING PAGE --------------------------------------    
def landingpage(request):
	records = Record_Landingpage.objects.all() 
    
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('landingpage')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('landingpage')
	else:
		return render(request, 'landingpage.html', {'records':records})
    





def register_user(request): #users register for admin
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})








from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def finalize_record(request):
    if request.method == "POST":
        payment_id = request.POST.get('payment_id')
        if payment_id and 'temp_record' in request.session:
            temp_record = request.session.pop('temp_record')
            name = temp_record['name']
            email = temp_record['email']
            phone = temp_record['phone']
            amount = Decimal(temp_record['amount'])

            # Calculate total_amount and balance_amount
            total_amount = Decimal(8000)  # Assuming the total amount is always 8000
            balance_amount = total_amount - amount

            existing_record = Record_Landingpage.objects.filter(email=email).first()
            if existing_record:
                existing_record.amount += amount
                
                existing_record.balance_amount = existing_record.balance_amount -amount
                existing_record.save()
            else:
                new_record = Record_Landingpage(
                    name=name,
                    email=email,
                    phone=phone,
                    amount=amount,
                    total_amount=total_amount,
                    balance_amount=balance_amount
                )
                new_record.save()

            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
from decimal import Decimal, InvalidOperation

from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact
from django.core.mail import send_mail

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('msg')

        # Server-side validation
        errors = {}
        if not name:
            errors['fname'] = 'Name is required.'
        if not phone or not phone.isdigit() or len(phone) != 10:
            errors['phone'] = 'Phone number must be 10 digits.'
        if not email:
            errors['email'] = 'Email is required.'
        if not message:
            errors['msg'] = 'Message is required.'

        if errors:
            return JsonResponse({'success': False, 'errors': errors})

        # Save data to the database
        Contact.objects.create(name=name, phone=phone, email=email, message=message)
        from_email=settings.EMAIL_HOST_USER 
        email_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage:\n{message}"
        send_mail(
            f'Message from Guru Tech website users doubts {email}',
            email_message,
            from_email,
            ['haritamilhp@gmail.com'],  # Replace with the website owner's email address
        )
        
        return JsonResponse({'success': True, 'message': 'Thank you for your message!'})

    return render(request, 'Contact us.html')

def terms(request):
    return render(request,'terms.html')


# ADD RECORD LANDINGPAGE
def add_record_landingpage(request):
    if request.method == "POST":
        form = AddRecordLandingpageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            try:
                amount = Decimal(form.cleaned_data['amount'])
            except InvalidOperation:
                messages.error(request, "Invalid amount. Please enter a valid number.")
                return render(request, 'add_record_landingpage.html', {'form': form})

            # Store form data in session temporarily
            request.session['temp_record'] = {
                'name': name,
                'email': email,
                'phone': phone,
                'amount': str(amount)
            }

            # Prepare context to trigger the payment function
            context = {'a': float(amount), 'payment_trigger': True}
            return render(request, 'thankyou_landingpage.html', context)
    else:
        form = AddRecordLandingpageForm()

    return render(request, 'add_record_landingpage.html', {'form': form})





def thankyou_landingpage(request):
    if request.method == 'POST':
       
        for name, value in request.POST.items():
            if name == "amount":
                a = value
                mydict = {'a': a}
        request.session['step'] = 1
        return render(request, 'thankyou_landingpage.html', {'registered': True})
    else:
      
       return render(request, 'landingpage.html', {'registered': False})





import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def generate_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        if email:
            try:
                # Fetch the last sent OTP ID from session or initialize it
                last_sent_otp_id = request.session.get('last_sent_otp_id', 0)
                
                # Fetch the next OTP in the cycle
                otp_instance = Python_otp.objects.filter(id__gt=last_sent_otp_id).first()
                if not otp_instance:
                    # If no OTP found, start from the beginning
                    otp_instance = Python_otp.objects.first()
                
                # Update the last sent OTP ID in session
                request.session['last_sent_otp_id'] = otp_instance.id
                request.session['last_sent_otp_code'] = otp_instance.otp 
                # Email sending logic
                sender_email = settings.EMAIL_HOST_USER
                sender_password = settings.EMAIL_HOST_PASSWORD

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = 'Your OTP Code'

                body = f'Your OTP code is {otp_instance.otp}'
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, email, text)
                server.quit()
                print("OTP Email sent successfully!")
                return JsonResponse({'status': 'success', 'message': 'OTP generated and sent successfully'})
            except Exception as e:
                print(f"Error sending OTP Email: {e}")
                return JsonResponse('')
        return JsonResponse({'status': 'error', 'message': 'Email is required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



def verify_otp(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        # Retrieve the last sent OTP code from session
        last_sent_otp_code = request.session.get('last_sent_otp_code')
        if last_sent_otp_code and verification_code == last_sent_otp_code:
            return JsonResponse({'message': 'OTP verified', 'status': 'success'})
        else:
            return JsonResponse({'message': 'Invalid OTP', 'status': 'error'})
    return JsonResponse({'message': 'Method Not Allowed', 'status': 'error'}, status=405)



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Save the form data without committing to the database yet
            add_record = form.save(commit=False)
            # Fetch all WhatsApp links from the database
            whatsapp_links = WhatsAppLink_python.objects.all()
            if whatsapp_links.exists():
                # Choose a random link from the queryset
                random_link_instance = random.choice(whatsapp_links)
                random_link = random_link_instance.link
                # Save the selected link to the record
                add_record.whatsapp_link = random_link
                add_record.save()
                messages.success(request, "Python Record Added ")
                # Redirect to the randomly chosen link
                return redirect(random_link)
            
    return render(request, 'add_record_python.html', {'form': form})

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



def python(request):
    records = Record.objects.all() 
    return render(request, 'python.html', {'records':records})


# !------------Java  records functions------------!

def customer_record_java(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_java.objects.get(id=pk)
		return render(request, 'record_java.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record_java(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_java.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')




def add_record_java(request):
    form = AddRecordForm_java(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Save the form data without committing to the database yet
            add_record_java = form.save(commit=False)
            # Fetch all WhatsApp links from the database
            whatsapp_links = WhatsAppLink_java.objects.all()
            if whatsapp_links.exists():
                # Choose a random link from the queryset
                random_link_instance = random.choice(whatsapp_links)
                random_link = random_link_instance.link
                # Save the selected link to the record
                add_record_java.whatsapp_link = random_link
                add_record_java.save()
                messages.success(request, "Java Record Added ")
                # Redirect to the randomly chosen link
                return redirect(random_link)
            # else:
            #     messages.error(request, "No WhatsApp links available.")
    return render(request, 'add_record_java.html', {'form': form})



def update_record_java(request, pk):
	if request.user.is_authenticated:
		current_record = Record_java.objects.get(id=pk)
		form = AddRecordForm_java(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_java.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



def java(request):
    records = Record_java.objects.all() 
    return render(request, 'java.html', {'records':records})




#!--------community--------!
# from django.contrib.auth.decorators import login_required

# @login_required

def customer_record_community(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_community.objects.get(id=pk)
		return render(request, 'record_community.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record_community(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_community.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')




def add_record_community(request):
    form = AddRecordForm_community(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Save the form data without committing to the database yet
            add_record_community = form.save(commit=False)
            # Fetch all WhatsApp links from the database
            whatsapp_links = WhatsAppLink_community.objects.all()
            if whatsapp_links.exists():
                # Choose a random link from the queryset
                random_link_instance = random.choice(whatsapp_links)
                random_link = random_link_instance.link
                # Save the selected link to the record
                add_record_community.whatsapp_link = random_link
                add_record_community.save()
                messages.success(request, "community Record Added ")
                # Redirect to the randomly chosen link
                return redirect(random_link)
            # else:
            #     messages.error(request, "No WhatsApp links available.")
    return render(request, 'add_record_community.html', {'form': form})

def update_record_community(request, pk):
	if request.user.is_authenticated:
		current_record = Record_community.objects.get(id=pk)
		form = AddRecordForm_community(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_community.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



def community(request):
    records = Record_community.objects.all() 
    return render(request, 'community.html', {'records':records})




# Helper function to generate a random OTP
def generate_random_otp_1():
    return random.randint(100000, 999999)

def delete_expired_otps():
    expired_threshold = timezone.now() - timedelta(minutes=5)
    expired_otps = random_otp.objects.filter(created_at__lt=expired_threshold)
    expired_otps.delete()
    
    
# View to generate and send OTP
@csrf_exempt
def generate_otp_community(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        if email:
            try:
                # Generate a random OTP
                otp = generate_random_otp_1()
                
                # Save the email and OTP to the database
                random_otp.objects.create(email=email, otp=otp)
                # Call the function to delete expired OTPs
                delete_expired_otps()
               
                # Email sending logic
                sender_email = settings.EMAIL_HOST_USER
                sender_password = settings.EMAIL_HOST_PASSWORD

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = 'Your OTP Code'

                body = f'Your OTP code is {otp}'
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, email, text)
                server.quit()
                print("OTP Email sent successfully!")
                return JsonResponse({'status': 'success', 'message': 'OTP generated and sent successfully to your email'})
            except Exception as e:
                print(f"Error sending OTP Email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Failed to send OTP'})
        return JsonResponse({'status': 'error', 'message': 'Email is required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# View to verify the OTP
@csrf_exempt
def verify_otp_community(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        verification_code = request.POST.get('verification_code')
        
        
        try:
            otp_instance = random_otp.objects.filter(email=email).latest('created_at')
            if otp_instance.otp == verification_code:
                otp_instance.delete()  # Delete the OTP entry from the database
                return JsonResponse({'message': 'OTP verified succesfully', 'status': 'success'})
            else:
                return JsonResponse({'message': 'OTP Entered is incorrect', 'status': 'error'})
        except random_otp.DoesNotExist:
            return JsonResponse({'message': 'Invalid OTP', 'status': 'error'})
    return JsonResponse({'message': 'Method Not Allowed', 'status': 'error'}, status=405)


#!---------basic_python_certificate------------!
def customer_record_basic_python_certificates(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_basic_python_certificates.objects.get(id=pk)
		return render(request, 'record_basic_python_certificates.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def delete_record_basic_python_certificates(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_basic_python_certificates.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')




def update_record_basic_python_certificates(request, pk):
	if request.user.is_authenticated:
		current_record = Record_basic_python_certificates.objects.get(id=pk)
		form = AddRecordForm_basic_python_certificates(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_basic_python_certificates.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def basic_python_certificates(request):
    records = Record_basic_python_certificates.objects.all() 
    return render(request, 'basic_python_certificates.html', {'records':records})

def add_record_basic_python_certificates(request):
    form = AddRecordForm_basic_python_certificates(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record_community = form.save()
            messages.success(request, "Basic python CERTIFICATE Record Added...")
            name = form.cleaned_data['name']

            # Generate certificate ID
            current_year = datetime.now().year
            latest_certificate = Certificate.objects.aggregate(Max('certificate_id'))
            latest_certificate_id = latest_certificate['certificate_id__max']
            if latest_certificate_id:
                latest_certificate_id_number = int(latest_certificate_id.split('/')[1])
            else:
                latest_certificate_id_number = 100000
            next_certificate_id_number = latest_certificate_id_number + 1
            certificate_id = f"{current_year}/{next_certificate_id_number:06d}"

            # Save certificate ID to the database
            Certificate.objects.create(name=name, certificate_id=certificate_id)

            pdf_file = generate_certificate_basic_python(name, certificate_id)

            # Serve the PDF for download
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="certificate_{name}.pdf"'
            return response

    return render(request, 'add_record_basic_python_certificates.html', {'form': form})

@csrf_exempt
def generate_otp_basic_python_certificates(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        if email:
            try:
                # Check if the email exists in the Record table and cert value is 1
                if Record.objects.filter(email=email, cert=1).exists():
                    # Check if the email has already been issued a certificate
                    if Record_basic_python_certificates.objects.filter(email=email).exists():
                            return JsonResponse({'status': 'error', 'message': 'Certificate already issued for this email'})
                    # Generate a random OTP
                    otp = generate_random_otp_1()
                    
                    # Save the email and OTP to the database
                    random_otp.objects.create(email=email, otp=otp)
                    # Call the function to delete expired OTPs
                    delete_expired_otps()
                   
                    # Email sending logic
                    sender_email = settings.EMAIL_HOST_USER
                    sender_password = settings.EMAIL_HOST_PASSWORD

                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = email
                    msg['Subject'] = 'Your OTP Code'

                    body = f'Your OTP code is {otp}'
                    msg.attach(MIMEText(body, 'plain'))

                    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    text = msg.as_string()
                    server.sendmail(sender_email, email, text)
                    server.quit()
                    print("OTP Email sent successfully!")
                    return JsonResponse({'status': 'success', 'message': 'OTP generated and sent successfully to your email'})
                elif Record.objects.filter(email=email, cert=0).exists():
                    # Update the cert value to 2
                    Record.objects.filter(email=email, cert=0).update(cert=2)
                    return JsonResponse({'status': 'error', 'message': 'contact admin for basic python certificates '})
                elif Record.objects.filter(email=email, cert=2).exists():
                    
                    return JsonResponse({'status': 'error', 'message': 'You can\'t further get certificates for basic python.you are blocked '})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Email is not registered for this course'})
            except Exception as e:
                print(f"Error sending OTP Email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Failed to send OTP'})
        return JsonResponse({'status': 'error', 'message': 'Email is required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



def generate_certificate_basic_python(name, certificate_id):
    buffer = BytesIO()
    document_title = "CERTIFICATE"
    title_2="OF INTERN COMPLETION"
    course_name = "Full Stack Python Developer"
    description = "For Successfully Completing Of The Full Stack Intern Python Developer"
    offered_by = "Offered By The Training Division Of Guru Tech"
    signature = "Selva Kumar\nHead of Proprietor"
    date = "Date: 2024-06-18"  # Example, can be dynamically generated
    LEDGER = (11*inch, 8.5*inch)
    c = canvas.Canvas(buffer, pagesize=LEDGER)
    width, height = LEDGER

    # Default image
    logo_path =finders.find('images/basic_python_cer.png')
    logo_width = width
    logo_height = height
    c.drawImage(logo_path, 0, 0, width=logo_width, height=logo_height)

    c.setFont("Helvetica-Bold", 18)
    text_width = c.stringWidth(name, "Helvetica-Bold", 18)
    text_x = (width - text_width) / 2.0
    text_y = height - 3.5 * inch
    c.drawString(text_x, text_y, name)

    # c.setFont("Helvetica", 12)
    # certificate_id_text = f"/{certificate_id}"
    # text_width = c.stringWidth(certificate_id_text, "Helvetica", 12)
    # text_x = (width - text_width) / 2.0
    # text_y -= 0.5 * inch
    # c.drawString(text_x, text_y, certificate_id_text)
    c.setFont("Helvetica", 12)
    certificate_id_text = f"/{certificate_id}"
    text_width = c.stringWidth(certificate_id_text, "Helvetica", 12)
    # text_x = (width - text_width) / 2.0
    # text_y -= 0.5 * inch
    offset = 40
    text_x = (width - text_width) / 2.0+ offset
    text_y = 0.5 * inch  # Position it 0.5 inch from the bottom of the page
    c.drawString(text_x, text_y, certificate_id_text)
    
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


#!---------basic_java_certificate------------!
def customer_record_basic_java_certificates(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_basic_java_certificates.objects.get(id=pk)
		return render(request, 'record_basic_java_certificates.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def delete_record_basic_java_certificates(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_basic_java_certificates.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')





def update_record_basic_java_certificates(request, pk):
	if request.user.is_authenticated:
		current_record = Record_basic_java_certificates.objects.get(id=pk)
		form = AddRecordForm_basic_java_certificates(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_basic_java_certificates.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def basic_java_certificates(request):
    records = Record_basic_java_certificates.objects.all() 
    return render(request, 'basic_java_certificates.html', {'records':records})

def add_record_basic_java_certificates(request):
    form = AddRecordForm_basic_java_certificates(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record_community = form.save()
            messages.success(request, "Basic java CERTIFICATE Record Added...")
            name = form.cleaned_data['name']

            # Generate certificate ID
            current_year = datetime.now().year
            latest_certificate = Certificate.objects.aggregate(Max('certificate_id'))
            latest_certificate_id = latest_certificate['certificate_id__max']
            if latest_certificate_id:
                latest_certificate_id_number = int(latest_certificate_id.split('/')[1])
            else:
                latest_certificate_id_number = 100000
            next_certificate_id_number = latest_certificate_id_number + 1
            certificate_id = f"{current_year}/{next_certificate_id_number:06d}"

            # Save certificate ID to the database
            Certificate.objects.create(name=name, certificate_id=certificate_id)

            pdf_file = generate_certificate_basic_java(name, certificate_id)

            # Serve the PDF for download
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="certificate_{name}.pdf"'
            return response

    return render(request, 'add_record_basic_java_certificates.html', {'form': form})
@csrf_exempt
def generate_otp_basic_java_certificates(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        if email:
            try:
                # Check if the email exists in the Record table and cert value is 1
                if Record_java.objects.filter(email=email, cert=1).exists():
                    # Check if the email has already been issued a certificate
                    if Record_basic_java_certificates.objects.filter(email=email).exists():
                            return JsonResponse({'status': 'error', 'message': 'Certificate already issued for this email'})
                    # Generate a random OTP
                    otp = generate_random_otp_1()
                    
                    # Save the email and OTP to the database
                    random_otp.objects.create(email=email, otp=otp)
                    # Call the function to delete expired OTPs
                    delete_expired_otps()
                   
                    # Email sending logic
                    sender_email = settings.EMAIL_HOST_USER
                    sender_password = settings.EMAIL_HOST_PASSWORD

                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = email
                    msg['Subject'] = 'Your OTP Code'

                    body = f'Your OTP code is {otp}'
                    msg.attach(MIMEText(body, 'plain'))

                    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    text = msg.as_string()
                    server.sendmail(sender_email, email, text)
                    server.quit()
                    print("OTP Email sent successfully!")
                    return JsonResponse({'status': 'success', 'message': 'OTP generated and sent successfully to your email'})
                elif Record_java.objects.filter(email=email, cert=0).exists():
                    # Update the cert value to 2
                    Record_java.objects.filter(email=email, cert=0).update(cert=2)
                    return JsonResponse({'status': 'error', 'message': 'contact admin for basic java certificates '})
                elif Record_java.objects.filter(email=email, cert=2).exists():
                    
                    return JsonResponse({'status': 'error', 'message': 'You can\'t further get certificates for basic java.you are blocked '})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Email is not registered for the course'})
            except Exception as e:
                print(f"Error sending OTP Email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Failed to send OTP'})
        return JsonResponse({'status': 'error', 'message': 'Email is required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



def generate_certificate_basic_java(name, certificate_id):
    buffer = BytesIO()
    document_title = "CERTIFICATE"
    title_2="OF INTERN COMPLETION"
    course_name = "Full Stack Python Developer"
    description = "For Successfully Completing Of The Full Stack Intern Python Developer"
    offered_by = "Offered By The Training Division Of Guru Tech"
    signature = "Selva Kumar\nHead of Proprietor"
    date = "Date: 2024-06-18"  # Example, can be dynamically generated
    LEDGER = (11*inch, 8.5*inch)
    c = canvas.Canvas(buffer, pagesize=LEDGER)
    width, height = LEDGER

    # Default image
    logo_path =finders.find('images/basic_java_cer.png')
    logo_width = width
    logo_height = height
    c.drawImage(logo_path, 0, 0, width=logo_width, height=logo_height)

    c.setFont("Helvetica-Bold", 18)
    text_width = c.stringWidth(name, "Helvetica-Bold", 18)
    text_x = (width - text_width) / 2.0
    text_y = height - 3.5 * inch
    c.drawString(text_x, text_y, name)

    # c.setFont("Helvetica", 12)
    # certificate_id_text = f"/{certificate_id}"
    # text_width = c.stringWidth(certificate_id_text, "Helvetica", 12)
    # text_x = (width - text_width) / 2.0
    # text_y -= 0.5 * inch
    # c.drawString(text_x, text_y, certificate_id_text)
    c.setFont("Helvetica", 12)
    certificate_id_text = f"/{certificate_id}"
    text_width = c.stringWidth(certificate_id_text, "Helvetica", 12)
    # text_x = (width - text_width) / 2.0
    # text_y -= 0.5 * inch
    offset = 40
    text_x = (width - text_width) / 2.0+ offset
    text_y = 0.5 * inch  # Position it 0.5 inch from the bottom of the page
    c.drawString(text_x, text_y, certificate_id_text)
    
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer



def generate_certificate(name):
    buffer = BytesIO()
    document_title = "CERTIFICATE"
    title_2="OF INTERN COMPLETION"
    course_name = "Full Stack Python Developer"
    description = "For Successfully Completing Of The Full Stack Intern Python Developer"
    offered_by = "Offered By The Training Division Of Guru Tech"
    signature = "Selva Kumar\nHead of Proprietor"
    certificate_id = "Certificate ID: 12345"  # Example, can be dynamically generated
    date = "Date: 2024-06-18"  # Example, can be dynamically generated
    LEDGER = (11*inch, 8.5*inch)
    c = canvas.Canvas(buffer, pagesize=LEDGER)
    width, height = LEDGER

    # Default image
    logo_path =finders.find('images/cer.jpeg')
    logo_width = width
    logo_height = height
    c.drawImage(logo_path, 0, 0, width=logo_width, height=logo_height)

    c.setFont("Helvetica-Bold", 18)
    text_width = c.stringWidth(name, "Helvetica-Bold", 18)
    text_x = (width - text_width) / 2.0
    text_y = height - 3.5 * inch
    c.drawString(text_x, text_y, name)
    
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer





def search_certificate(request):
    certificate_id = request.GET.get('certificate_id', None)
    certificate = None
    not_found = False
    if certificate_id:
        try:
            certificate = Certificate.objects.get(certificate_id=certificate_id)
        except Certificate.DoesNotExist:
            not_found = True
    return render(request, 'search_certificate.html', {'certificate': certificate, 'not_found': not_found})

#!---------_advance_python_reg------------!
def customer_record_advance_python_reg(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_advance_python_reg.objects.get(id=pk)
		return render(request, 'record_advance_python_reg.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_record_advance_python_reg(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_advance_python_reg.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
def add_record_advance_python_reg(request):
    form = AddRecordForm_advance_python_reg(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Save the form data without committing to the database yet
                form.save()
                messages.success(request, "Python Record Added ")
                # Redirect to the randomly chosen link
                return redirect('thank_you_for_reg')
            # else:
            #     messages.error(request, "No WhatsApp links available.")
    return render(request, 'add_record_advance_python_reg.html', {'form': form})

def update_record_advance_python_reg(request, pk):
	if request.user.is_authenticated:
		current_record = Record_advance_python_reg.objects.get(id=pk)
		form = AddRecordForm_advance_python_reg(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_advance_python_reg.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
def advance_python_reg(request):
    records = Record_advance_python_reg.objects.all() 
    return render(request, 'advance_python_reg.html', {'records':records})
def thank_you_for_reg(request):
    return render(request, 'thank_you_for_reg.html')

#!---------advance_python_certificate------------!
def customer_record_advance_python_certificates(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_advance_python_certificates.objects.get(id=pk)
		return render(request, 'record_advance_python_certificates.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def delete_record_advance_python_certificates(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_advance_python_certificates.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def update_record_advance_python_certificates(request, pk):
	if request.user.is_authenticated:
		current_record = Record_advance_python_certificates.objects.get(id=pk)
		form = AddRecordForm_advance_python_certificates(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_advance_python_certificates.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def advance_python_certificates(request):
    records = Record_advance_python_certificates.objects.all() 
    return render(request, 'advance_python_certificates.html', {'records':records})

def add_record_advance_python_certificates(request):
    form = AddRecordForm_advance_python_certificates(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record_community = form.save()
            messages.success(request, "Advance python CERTIFICATE Record Added...")
            name = form.cleaned_data['name']

            # Generate certificate ID
            current_year = datetime.now().year
            latest_certificate = Certificate.objects.aggregate(Max('certificate_id'))
            latest_certificate_id = latest_certificate['certificate_id__max']
            if latest_certificate_id:
                latest_certificate_id_number = int(latest_certificate_id.split('/')[1])
            else:
                latest_certificate_id_number = 100000
            next_certificate_id_number = latest_certificate_id_number + 1
            certificate_id = f"{current_year}/{next_certificate_id_number:06d}"

            # Save certificate ID to the database
            Certificate.objects.create(name=name, certificate_id=certificate_id)

            pdf_file = generate_certificate_advance_python(name, certificate_id)

            # Serve the PDF for download
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="certificate_{name}.pdf"'
            return response
    
    return render(request, 'add_record_advance_python_certificates.html', {'form': form})
@csrf_exempt
def generate_otp_advance_python_certificates(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        if email:
            try:
                # Check if the email exists in the Record table and cert value is 1
                if Record_advance_python_reg.objects.filter(email=email, cert=1).exists():
                    # Check if the email has already been issued a certificate
                    if Record_advance_python_certificates.objects.filter(email=email).exists():
                            return JsonResponse({'status': 'error', 'message': 'Certificate already issued for this email'})
                    # Generate a random OTP
                    otp = generate_random_otp_1()
                    
                    # Save the email and OTP to the database
                    random_otp.objects.create(email=email, otp=otp)
                    # Call the function to delete expired OTPs
                    delete_expired_otps()
                   
                    # Email sending logic
                    sender_email = settings.EMAIL_HOST_USER
                    sender_password = settings.EMAIL_HOST_PASSWORD

                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = email
                    msg['Subject'] = 'Your OTP Code'

                    body = f'Your OTP code is {otp}'
                    msg.attach(MIMEText(body, 'plain'))

                    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    text = msg.as_string()
                    server.sendmail(sender_email, email, text)
                    server.quit()
                    print("OTP Email sent successfully!")
                    return JsonResponse({'status': 'success', 'message': 'OTP generated and sent successfully to your email'})
                elif Record_advance_python_reg.objects.filter(email=email, cert=0).exists():
                    # Update the cert value to 2
                    Record_advance_python_reg.objects.filter(email=email, cert=0).update(cert=2)
                    return JsonResponse({'status': 'error', 'message': 'contact admin for advance python certificates '})
                elif Record_advance_python_reg.objects.filter(email=email, cert=2).exists():
                    
                    return JsonResponse({'status': 'error', 'message': 'You can\'t further get certificates for advance python.you are blocked '})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Email is not registered for the course'})
            except Exception as e:
                print(f"Error sending OTP Email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Failed to send OTP'})
        return JsonResponse({'status': 'error', 'message': 'Email is required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
def generate_certificate_advance_python(name, certificate_id):
    buffer = BytesIO()
    
    LEDGER = (11*inch, 8.5*inch)
    c = canvas.Canvas(buffer, pagesize=LEDGER)
    width, height = LEDGER

    # Default image
    logo_path =finders.find('images/advance_python_cer.png')
    logo_width = width
    logo_height = height
    c.drawImage(logo_path, 0, 0, width=logo_width, height=logo_height)

    c.setFont("Helvetica-Bold", 18)
    text_width = c.stringWidth(name, "Helvetica-Bold", 18)
    text_x = (width - text_width) / 2.0
    text_y = height - 3.5 * inch
    c.drawString(text_x, text_y, name)

    c.setFont("Helvetica", 12)
    certificate_id_text = f"/{certificate_id}"
    text_width = c.stringWidth(certificate_id_text, "Helvetica", 12)
    # text_x = (width - text_width) / 2.0
    # text_y -= 0.5 * inch
    offset = 40
    text_x = (width - text_width) / 2.0+ offset
    text_y = 0.5 * inch  # Position it 0.5 inch from the bottom of the page
    c.drawString(text_x, text_y, certificate_id_text)
     
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


#!---------_advance_java_reg------------!
def customer_record_advance_java_reg(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_advance_java_reg.objects.get(id=pk)
		return render(request, 'record_advance_java_reg.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_record_advance_java_reg(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_advance_java_reg.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
def add_record_advance_java_reg(request):
    form = AddRecordForm_advance_java_reg(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Save the form data without committing to the database yet
                form.save()
                messages.success(request, "java Record Added ")
                # Redirect to the randomly chosen link
                return redirect('thank_you_for_reg')
            # else:
            #     messages.error(request, "No WhatsApp links available.")
    return render(request, 'add_record_advance_java_reg.html', {'form': form})

def update_record_advance_java_reg(request, pk):
	if request.user.is_authenticated:
		current_record = Record_advance_java_reg.objects.get(id=pk)
		form = AddRecordForm_advance_java_reg(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_advance_java_reg.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
def advance_java_reg(request):
    records = Record_advance_java_reg.objects.all() 
    return render(request, 'advance_java_reg.html', {'records':records})


#!----------advance_java_certificate------------!
def customer_record_advance_java_certificates(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_advance_java_certificates.objects.get(id=pk)
		return render(request, 'record_advance_java_certificates.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def delete_record_advance_java_certificates(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_advance_java_certificates.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def update_record_advance_java_certificates(request, pk):
	if request.user.is_authenticated:
		current_record = Record_advance_java_certificates.objects.get(id=pk)
		form = AddRecordForm_advance_java_certificates(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_advance_java_certificates.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



def advance_java_certificates(request):
    records = Record_advance_java_certificates.objects.all() 
    return render(request, 'advance_java_certificates.html', {'records':records})





def add_record_advance_java_certificates(request):
    form = AddRecordForm_advance_java_certificates(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record_community = form.save()
            messages.success(request, "Advance java CERTIFICATE Record Added...")
            name = form.cleaned_data['name']

            # Generate certificate ID
            current_year = datetime.now().year
            latest_certificate = Certificate.objects.aggregate(Max('certificate_id'))
            latest_certificate_id = latest_certificate['certificate_id__max']
            if latest_certificate_id:
                latest_certificate_id_number = int(latest_certificate_id.split('/')[1])
            else:
                latest_certificate_id_number = 100000
            next_certificate_id_number = latest_certificate_id_number + 1
            certificate_id = f"{current_year}/{next_certificate_id_number:06d}"

            # Save certificate ID to the database
            Certificate.objects.create(name=name, certificate_id=certificate_id)

            pdf_file = generate_certificate_advance_java(name, certificate_id)

            # Serve the PDF for download
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="certificate_{name}.pdf"'
            return response
    
    return render(request, 'add_record_advance_java_certificates.html', {'form': form})


@csrf_exempt
def generate_otp_advance_java_certificates(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        if email:
            try:
                # Check if the email exists in the Record table and cert value is 1
                if Record_advance_java_reg.objects.filter(email=email, cert=1).exists():
                    # Check if the email has already been issued a certificate
                    if Record_advance_java_certificates.objects.filter(email=email).exists():
                            return JsonResponse({'status': 'error', 'message': 'Certificate already issued for this email'})
                    # Generate a random OTP
                    otp = generate_random_otp_1()
                    
                    # Save the email and OTP to the database
                    random_otp.objects.create(email=email, otp=otp)
                    # Call the function to delete expired OTPs
                    delete_expired_otps()
                   
                    # Email sending logic
                    sender_email = settings.EMAIL_HOST_USER
                    sender_password = settings.EMAIL_HOST_PASSWORD

                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = email
                    msg['Subject'] = 'Your OTP Code'

                    body = f'Your OTP code is {otp}'
                    msg.attach(MIMEText(body, 'plain'))

                    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    text = msg.as_string()
                    server.sendmail(sender_email, email, text)
                    server.quit()
                    print("OTP Email sent successfully!")
                    return JsonResponse({'status': 'success', 'message': 'OTP generated and sent successfully to your email'})
                elif Record_advance_java_reg.objects.filter(email=email, cert=0).exists():
                    # Update the cert value to 2
                    Record_advance_java_reg.objects.filter(email=email, cert=0).update(cert=2)
                    return JsonResponse({'status': 'error', 'message': 'contact admin for advance java certificates '})
                elif Record_advance_java_reg.objects.filter(email=email, cert=2).exists():
                    
                    return JsonResponse({'status': 'error', 'message': 'You can\'t further get certificates for advance java.you are blocked '})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Email is not registered for the course'})
            except Exception as e:
                print(f"Error sending OTP Email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Failed to send OTP'})
        return JsonResponse({'status': 'error', 'message': 'Email is required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def generate_certificate_advance_java(name, certificate_id):
    buffer = BytesIO()
    
    LEDGER = (11*inch, 8.5*inch)
    c = canvas.Canvas(buffer, pagesize=LEDGER)
    width, height = LEDGER

    # Default image
    logo_path =finders.find('images/advance_java_cer.png')
    logo_width = width
    logo_height = height
    c.drawImage(logo_path, 0, 0, width=logo_width, height=logo_height)

    c.setFont("Helvetica-Bold", 18)
    text_width = c.stringWidth(name, "Helvetica-Bold", 18)
    text_x = (width - text_width) / 2.0
    text_y = height - 3.5 * inch
    c.drawString(text_x, text_y, name)

    c.setFont("Helvetica", 12)
    certificate_id_text = f"/{certificate_id}"
    text_width = c.stringWidth(certificate_id_text, "Helvetica", 12)
    # text_x = (width - text_width) / 2.0
    # text_y -= 0.5 * inch
    offset = 40
    text_x = (width - text_width) / 2.0+ offset
    text_y = 0.5 * inch  # Position it 0.5 inch from the bottom of the page
    c.drawString(text_x, text_y, certificate_id_text)
     
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


#!---------intern_reg------------!
def customer_record_intern_reg(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_intern_reg.objects.get(id=pk)
		return render(request, 'record_intern_reg.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def delete_record_intern_reg(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_intern_reg.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
def add_record_intern_reg(request):
    form = AddRecordForm_intern_reg(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Save the form data without committing to the database yet
                form.save()
                messages.success(request, "intern Record Added ")
                # Redirect to the randomly chosen link
                return redirect('thank_you_for_reg')
            # else:
            #     messages.error(request, "No WhatsApp links available.")
    return render(request, 'add_record_intern_reg.html', {'form': form})

def update_record_intern_reg(request, pk):
	if request.user.is_authenticated:
		current_record = Record_intern_reg.objects.get(id=pk)
		form = AddRecordForm_intern_reg(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_intern_reg.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
def intern_reg(request):
    records = Record_intern_reg.objects.all() 
    return render(request, 'intern_reg.html', {'records':records})

#!----------intern_certificate------------!
def customer_record_intern_certificates(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record_intern_certificates.objects.get(id=pk)
		return render(request, 'record_intern_certificates.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


def delete_record_intern_certificates(request, pk):
	if request.user.is_authenticated:
		delete_it = Record_intern_certificates.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def update_record_intern_certificates(request, pk):
	if request.user.is_authenticated:
		current_record = Record_intern_certificates.objects.get(id=pk)
		form = AddRecordForm_intern_certificates(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record_intern_certificates.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



def intern_certificates(request):
    records = Record_intern_certificates.objects.all() 
    return render(request, 'intern_certificates.html', {'records':records})





def add_record_intern_certificates(request):
    form = AddRecordForm_intern_certificates(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record_community = form.save()
            messages.success(request, "Advance java CERTIFICATE Record Added...")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Check if the email exists in Record_intern_reg
            existing_record = Record_intern_reg.objects.filter(email=email).first()
            if existing_record:
                start_date = existing_record.start_date
                end_date = existing_record.end_date
            else:
                start_date = None
                end_date = None

            # Generate certificate ID
            current_year = datetime.now().year
            latest_certificate = Certificate.objects.aggregate(Max('certificate_id'))
            latest_certificate_id = latest_certificate['certificate_id__max']
            if latest_certificate_id:
                latest_certificate_id_number = int(latest_certificate_id.split('/')[1])
            else:
                latest_certificate_id_number = 100000
            next_certificate_id_number = latest_certificate_id_number + 1
            certificate_id = f"{current_year}/{next_certificate_id_number:06d}"

            # Save certificate ID to the database
            Certificate.objects.create(name=name, certificate_id=certificate_id)

            #pdf_file = generate_certificate_intern(name, certificate_id)
            pdf_file = generate_certificate_intern(name, certificate_id, start_date, end_date)

            # Serve the PDF for download
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="certificate_{name}.pdf"'
            return response
    
    return render(request, 'add_record_intern_certificates.html', {'form': form})


@csrf_exempt
def generate_otp_intern_certificates(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        if email:
            try:
                # Check if the email exists in the Record table and cert value is 1
                if Record_intern_reg.objects.filter(email=email, cert=1).exists():
                    # Check if the email has already been issued a certificate
                    if Record_intern_certificates.objects.filter(email=email).exists():
                            return JsonResponse({'status': 'error', 'message': 'Certificate already issued for this email'})
                    # Generate a random OTP
                    otp = generate_random_otp_1()
                    
                    # Save the email and OTP to the database
                    random_otp.objects.create(email=email, otp=otp)
                    # Call the function to delete expired OTPs
                    delete_expired_otps()
                   
                    # Email sending logic
                    sender_email = settings.EMAIL_HOST_USER
                    sender_password = settings.EMAIL_HOST_PASSWORD

                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = email
                    msg['Subject'] = 'Your OTP Code'

                    body = f'Your OTP code is {otp}'
                    msg.attach(MIMEText(body, 'plain'))

                    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    text = msg.as_string()
                    server.sendmail(sender_email, email, text)
                    server.quit()
                    print("OTP Email sent successfully!")
                    return JsonResponse({'status': 'success', 'message': 'OTP generated and sent successfully to your email'})
                elif Record_intern_reg.objects.filter(email=email, cert=0).exists():
                    # Update the cert value to 2
                    Record_intern_reg.objects.filter(email=email, cert=0).update(cert=2)
                    return JsonResponse({'status': 'error', 'message': 'contact admin for advance java certificates '})
                elif Record_intern_reg.objects.filter(email=email, cert=2).exists():
                    
                    return JsonResponse({'status': 'error', 'message': 'You can\'t further get certificates for advance java.you are blocked '})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Email is not registered for the course'})
            except Exception as e:
                print(f"Error sending OTP Email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Failed to send OTP'})
        return JsonResponse({'status': 'error', 'message': 'Email is required'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def generate_certificate_intern(name, certificate_id, start_date=None, end_date=None):
    buffer = BytesIO()
    
    LEDGER = (11*inch, 17*inch)
    c = canvas.Canvas(buffer, pagesize=LEDGER)
    width, height = LEDGER
    
    # Convert the name to title case
    name = name.title()
    

    # Page 1: current date, name, certificate ID
    logo_path = finders.find('images/1.png')
    c.drawImage(logo_path, 0, 0, width=width, height=height)

    current_date = datetime.now().strftime('%Y-%m-%d')
    c.setFont("Helvetica-Bold", 18)
    offset = 270  # Adjust this value as needed for the left side offset
    current_date_text = f"{current_date}"
    current_date_text_width = c.stringWidth(current_date_text, "Helvetica-Bold", 18)
    current_date_text_x = (width-current_date_text_width) /2.0 - offset
    current_date_text_y = height - 4 * inch
    c.drawString(current_date_text_x, current_date_text_y, current_date_text)
    
    c.setFont("Helvetica-Bold", 18)
    offset2 = 220
    name_text_width = c.stringWidth(name, "Helvetica-Bold", 18)
    # name_text_x = (width - name_text_width) / 2.0 - offset2
    # name_text_y = height - 4.3* inch
    name_text_x = 1.1 * inch
    name_text_y = 12.7 * inch
    c.drawString(name_text_x, name_text_y, name)
    
    c.setFont("Helvetica", 17)
    offset7 = 210
    name2 = f"Dear {name},"
    name_text_width = c.stringWidth(name2, "Helvetica", 17)
    name_text_x = 1.1 * inch
    name_text_y = height - 6.3 * inch
    c.drawString(name_text_x, name_text_y, name2)
    
    c.setFont("Helvetica", 15)
    certificate_id_text = f"/{certificate_id}"
    text_width = c.stringWidth(certificate_id_text, "Helvetica", 15)
    offset3=133
    text_x = (width - text_width) / 2.0 - offset3
    text_y = 1.02 * inch
    c.drawString(text_x, text_y, certificate_id_text)
    
    

    c.showPage()

    # Page 2: start date, end date, certificate ID
    logo_path2 = finders.find('images/2.png')
    c.drawImage(logo_path2, 0, 0, width=width, height=height)
    
    if start_date:
        formatted_start_date = start_date.strftime('%d-%m-%Y')
        c.setFont("Helvetica-Bold", 14)
        start_date_text = f"Start Date: {formatted_start_date}"
        start_date_text_width = c.stringWidth(start_date_text, "Helvetica-Bold", 14)
        offset5=241
        start_date_text_x = (width - start_date_text_width) / 2.0 - offset5
        start_date_text_y = height - 4.8 * inch
        c.drawString(start_date_text_x, start_date_text_y, start_date_text)

    if end_date:
        formatted_end_date = end_date.strftime('%d-%m-%Y')
        c.setFont("Helvetica-Bold", 14)
        end_date_text = f"End Date: {formatted_end_date}"
        end_date_text_width = c.stringWidth(end_date_text, "Helvetica-Bold", 14)
        offset6=242
        end_date_text_x = (width - end_date_text_width) / 2.0 - offset6
        end_date_text_y = start_date_text_y - 0.3 * inch
        c.drawString(end_date_text_x, end_date_text_y, end_date_text)

    # c.setFont("Helvetica", 12)
    # c.drawString(text_x, text_y, certificate_id_text)
    
    # validation_text_y = text_y + 0.25 * inch
    # c.drawString(validation_text_x, validation_text_y, validation_text)
    c.setFont("Helvetica", 15)
    certificate_id_text = f"/{certificate_id}"
    text_width = c.stringWidth(certificate_id_text, "Helvetica", 15)
    offset3=133
    text_x = (width - text_width) / 2.0 - offset3
    text_y = 1.02 * inch
    c.drawString(text_x, text_y, certificate_id_text)
    
    
    
    

    c.showPage()

    # Page 3: name, certificate ID
    logo_path3 = finders.find('images/3.png')
    c.drawImage(logo_path3, 0, 0, width=width, height=height)

    # c.setFont("Helvetica-Bold", 18)
    # c.drawString(name_text_x, name_text_y, name)
    c.setFont("Helvetica-Bold", 17)
    offset2 = 205
    name1 = f"{name},"
    name_text_width = c.stringWidth(name1, "Helvetica-Bold", 17)
    name_text_x = 1.3 * inch
    name_text_y = height - 5 * inch
    c.drawString(name_text_x, name_text_y, name1)
    
    # c.setFont("Helvetica", 12)
    # c.drawString(text_x, text_y, certificate_id_text)
    
    # c.drawString(validation_text_x, validation_text_y, validation_text)
    c.setFont("Helvetica", 15)
    certificate_id_text = f"/{certificate_id}"
    text_width = c.stringWidth(certificate_id_text, "Helvetica", 15)
    offset3=133
    text_x = (width - text_width) / 2.0 - offset3
    text_y = 1.02 * inch
    c.drawString(text_x, text_y, certificate_id_text)
    
    

    c.showPage()
    
    c.save()
    
    buffer.seek(0)
    return buffer






