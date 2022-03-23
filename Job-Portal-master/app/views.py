from django.shortcuts import render, HttpResponseRedirect, redirect
from app.models import *
from app.forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'forms':form})   


def LogIn(request):
    if request.method == 'POST':
        form = LogInForm(request=request, data=request.POST)
        if form.is_valid():
            usm = form.cleaned_data['username']
            upas = form.cleaned_data['password']
            log = authenticate(username=usm,password=upas)
            if log is not None:
                login(request, log)
                return redirect('index')
    else:
        form = LogInForm()
    return render(request, 'login.html',{'forms':form})


def Index(request):
    return render(request, 'app/index.html')


def Company(request):
    if request.method == 'POST':
        form = CompanyForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            usr = request.user
            cnam = form.cleaned_data['company_name']
            inty = form.cleaned_data['industry_type']
            hq = form.cleaned_data['headquarter']
            ct = form.cleaned_data['city']
            em = form.cleaned_data['email']
            ph = form.cleaned_data['phone']
            sd = form.cleaned_data['start_date']
            lg = form.cleaned_data['logo']
            disc = form.cleaned_data['discription']
            reg = CompanyModel(user=usr, company_name=cnam ,industry_type=inty ,headquarter=hq ,city=ct ,email=em ,
            phone=ph ,start_date=sd ,logo=lg ,discription=disc)
            messages.success(request, 'Your company information has been create successfully. ')
            reg.save()
            return redirect('company')
        else:
            messages.error(request, 'We getting find error to submit your company data.')
    else:
        form = CompanyForm()
        context = {'forms':form}
    return render(request, 'app/company.html',context)


def CompanyData(request):
    company_data = CompanyModel.objects.filter(user=request.user)
    context = {'company_data':company_data}
    return render(request, 'app/company_data.html',context)


def CompanyDataEdit(request, pk):
    if request.method == 'POST':
        data = CompanyModel.objects.get(pk=pk)
        form = CompanyForm(data=request.POST, files=request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('company_data')
    else:
        data = CompanyModel.objects.get(pk=pk)
        form = CompanyForm(instance=data)
    context = {'forms':form}
    return render(request, 'app/company.html',context)


def CompanyDataDelete(request, pk):
    if request.method == 'POST':
        company_data = CompanyModel.objects.filter(pk=pk)
        company_data.delete()
        return redirect('company_data')


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            usr = request.user
            fnm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            reg = ContactModel(user=usr, name=fnm,email=em,message=msg)
            messages.success(request, 'Your message has been send successfully.')
            reg.save()
            return redirect('contact')
        else:
            messages.error(request, 'Please write correct your name, email or message.')
    else:
        form = ContactForm()
        context = {'forms':form}
    return render(request, 'app/contact.html',context)


def Jobs(request):
    if request.method == 'POST':
        form = SubmitJobsForms(request.POST)
        if form.is_valid():
            usr = request.user
            job_title = form.cleaned_data['job_title']
            location = form.cleaned_data['location']
            email = form.cleaned_data['email']
            company_name = form.cleaned_data['company_name']
            salary = form.cleaned_data['salary']
            job_type = form.cleaned_data['job_type']
            skills = form.cleaned_data['skills']
            discription = form.cleaned_data['discription']
            reg = SubmitJobsModel(user=usr,job_title=job_title,location=location,email=email,company_name=company_name,
            salary=salary,job_type=job_type,skills=skills,discription=discription)
            messages.success(request, 'Your job information has been submited successfully.')
            reg.save()
            return redirect('jobs')
        else:
            messages.error(request, 'We getting find error to submit your job.')
    else:
        form = SubmitJobsForms()
        context = {'forms':form}
    return render(request, 'app/jobs.html',context)


def Resume(request):
    if request.method == 'POST':
        form = ResumeSubmitForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            usr = request.user
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            location = form.cleaned_data['location']
            linked_in = form.cleaned_data['linked_in']
            education = form.cleaned_data['education']
            higher_education = form.cleaned_data['higher_education']
            skills = form.cleaned_data['skills']
            project = form.cleaned_data['project']
            birth_date = form.cleaned_data['birth_date']
            nationality = form.cleaned_data['nationality']
            hobbies = form.cleaned_data['hobbies']
            address = form.cleaned_data['address']
            objectives = form.cleaned_data['objectives']
            declaration = form.cleaned_data['declaration']
            reg = ResumeSubmitModel(user=usr,full_name=full_name,email=email,phone=phone,location=location,linked_in=linked_in,
            education=education,higher_education=higher_education,skills=skills,project=project,birth_date=birth_date,
            nationality=nationality,hobbies=hobbies,address=address,objectives=objectives,declaration=declaration)
            messages.success(request, 'Your resume has been submit successfully.')
            reg.save()
            return redirect('resume')
        else:
            messages.error(request, 'We getting find error to submit resume.')
    else:
        form = ResumeSubmitForm()
        context = {'forms':form}
    return render(request, 'app/resume.html',context)


def ResumeData(request):
    resume_data = ResumeSubmitModel.objects.filter(user=request.user)
    context = {'resume_data':resume_data} 
    return render(request, 'app/resume_data.html',context)


def ResumeDataEdit(request, pk):
    if request.method == 'POST':
        resume_data = ResumeSubmitModel.objects.get(pk=pk)
        form = ResumeSubmitForm(request.POST, instance=resume_data)
        if form.is_valid():
            form.save()
            return redirect('resume_data')
    else:
        resume_data = ResumeSubmitModel.objects.get(pk=pk)
        form = ResumeSubmitForm(instance=resume_data)
        context = {'forms':form}
    return render(request, 'app/resume.html',context)


def DeleteResume(request, pk):
    if request.method == 'POST':
        data = ResumeSubmitModel.objects.filter(pk=pk)
        data.delete()
        return redirect('resume_data')


def SearchJobs(request):
    search_data = SubmitJobsModel.objects.filter()
    context = {'search_data':search_data}
    return render(request, 'app/searchjobs.html',context)


def Accounts(request):
    return render(request, 'app/account.html')


def DeleteAccount(request, pk):
    if request.method == 'POST':
        data = UserAccount.objects.filter(pk=pk)
        data.delete()
        return redirect('index')


def AccountsEdits(request, pk):
    if request.method == 'POST':
        form = UserEditForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Your JOBTrue account has been update successfully.')
            form.save()
            return redirect('accountsedits', request.user.id)
        else:
            messages.error(request, 'We getting find error to update your account.')
    else:
        form = UserEditForm(instance=request.user)
        user_data = UserAccount.objects.filter(pk=pk)
        context = {'forms':form,'user_data':user_data}
    return render(request, 'app/account_edit.html',context)


def Settings(request):
    if request.method == 'POST':
        form = PasswordUpdateForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your JOBTrue password has been changed successfully.')
            return redirect('settings')
        else:
            messages.error(request, 'Please write correct password.')
    else:
        form = PasswordUpdateForm(request.user)
    return render(request, 'app/settings.html',{'forms':form})


def JobsDetails(request, pk):
    if request.user.is_authenticated:
        jobs_data = SubmitJobsModel.objects.filter(pk=pk)
        jobs_data12 = SubmitJobsModel.objects.get(pk=pk)
        apply_data = ApplyModel.objects.filter(user=request.user, apply=jobs_data12)
        context = {'jobs_data':jobs_data, 'apply_data':apply_data}
        return render(request, 'app/job_details.html',context)
    else:
        return redirect('login')


def ApplyFunc(request, pk):
    if request.method == 'POST':
        user = request.user
        user_id = request.POST.get('user_id')
        applyers = UserAccount.objects.get(id=user_id)
        job_id = SubmitJobsModel.objects.get(pk=pk)        
        apply, create = ApplyModel.objects.get_or_create(user=user, apply=job_id, applyers=applyers)        
        if create:
            apply.save()
        else:
            apply.delete()            
    return redirect('jobs_details', job_id.id)


def JobsAndCompanyFunc(request):
    job_data = ApplyModel.objects.filter(applyers=request.user)
    context = {'job_data':job_data}
    return render(request, 'app/jobs_and_company_data.html',context)


def LogOut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('index')

def forgetPassword(request):
    return render(request, 'app/forgetEmail.html')

def updatePassword(request):
    return render(request, 'app/newPassword.html')