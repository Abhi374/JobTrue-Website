from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/',views.SignUp,name='signup'),
    path('login/',views.LogIn,name='login'),
    
    path('',views.Index,name='index'),
    
    path('company/',views.Company,name='company'),
    path('company_data/',views.CompanyData,name='company_data'),
    path('company_data_edit/<int:pk>/',views.CompanyDataEdit,name='company_data_edit'),
    path('company_data_delete/<int:pk>/',views.CompanyDataDelete,name='company_data_delete'),
    
    path('contact/',views.Contact,name='contact'),
    
    path('jobs/',views.Jobs,name='jobs'),
    
    path('resume/',views.Resume,name='resume'),
    path('resume_data/',views.ResumeData,name='resume_data'),
    path('resume_data_edit/<int:pk>/',views.ResumeDataEdit,name='resume_data_edit'),
    path('delet_resume/<int:pk>/',views.DeleteResume,name='delet_resume'),
    
    path('searchjobs/',views.SearchJobs,name='searchjobs'),
    
    path('jobs_details/<int:pk>/',views.JobsDetails,name='jobs_details'),
    
    path('accounts/',views.Accounts,name='accounts'),
    path('accountsedits/<int:pk>/',views.AccountsEdits,name='accountsedits'),
    
    path('change_password/',views.Settings,name='settings'),
    
    path('DeleteAccount/<int:pk>/',views.DeleteAccount,name='DeleteAccount'),
    
    path('apply/<int:pk>/',views.ApplyFunc,name='apply'),
    
    path('jobs_and_company_data/',views.JobsAndCompanyFunc,name='jobs_and_company_data'),
    
    path('logout/',views.LogOut,name='logout'),
    path('forgetpassword/',views.forgetPassword, name="forgetpassword"),
    path('updatepassword/',views.updatePassword, name="updatePassword")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)