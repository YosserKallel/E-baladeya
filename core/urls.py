from django.urls import path

from .views import application_complete, application_create, application_review, default_service_detail, document_upload, page, service_detail, services_catalogue, verification_result

urlpatterns = [
    path('', page('home.html'), name='home'),
    path('services/', services_catalogue, name='services'),
    path('services/detail/', default_service_detail, name='service_detail'),
    path('services/<slug:service_slug>/', service_detail, name='service_detail_slug'),
    path('dashboard/', page('dashboard.html'), name='dashboard'),
    path('requests/new/', application_create, name='application_create_generic'),
    path('applications/new/<slug:service_slug>/', application_create, name='application_create'),
    path('requests/documents/', document_upload, name='document_upload'),
    path('applications/<slug:service_slug>/documents/', document_upload, name='document_upload_service'),
    path('requests/verification/', verification_result, name='verification_result'),
    path('applications/<slug:service_slug>/verification/', verification_result, name='verification_result_service'),
    path('requests/review/', application_review, name='application_review'),
    path('applications/<slug:service_slug>/review/', application_review, name='application_review_service'),
    path('requests/complete/', application_complete, name='application_complete'),
    path('applications/<slug:service_slug>/complete/', application_complete, name='application_complete_service'),
    path('requests/detail/', page('application_detail.html'), name='application_detail'),
    path('administration/', page('employee_dashboard.html'), name='employee_dashboard'),
    path('administration/requests/detail/', page('employee_application_detail.html'), name='employee_application_detail'),
    path('administration/analytics/', page('analytics.html'), name='analytics'),
    path('login/', page('login.html'), name='login'),
    path('register/', page('register.html'), name='register'),
]
