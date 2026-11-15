from django.http import Http404
from django.shortcuts import redirect, render

from .services import SERVICES, SERVICES_BY_SLUG


def page(template_name):
    def view(request):
        return render(request, template_name)

    return view


def services_catalogue(request):
    categories = []
    for service in SERVICES:
        category = next((item for item in categories if item['slug'] == service['category_slug']), None)
        if category is None:
            category = {'slug': service['category_slug'], 'name': service['category'], 'services': []}
            categories.append(category)
        category['services'].append(service)
    return render(request, 'services.html', {'services': SERVICES, 'categories': categories})


def service_detail(request, service_slug):
    service = SERVICES_BY_SLUG.get(service_slug)
    if service is None:
        raise Http404('Municipal service not found')
    return render(request, 'service_detail.html', {'service': service})


def default_service_detail(request):
    return service_detail(request, 'birth-certificate-extract')


def application_create(request, service_slug=None):
    if service_slug is not None:
        if service_slug not in SERVICES_BY_SLUG:
            raise Http404('Municipal service not found')
        return redirect('document_upload_service', service_slug=service_slug)
    return render(request, 'application_create.html', {'service': None, 'services': SERVICES})


def document_upload(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'document_upload.html', context)


def verification_result(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'verification_result.html', context)


def application_review(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'application_review.html', context)


def application_complete(request, service_slug=None):
    context = {'service': None}
    if service_slug is not None:
        service = SERVICES_BY_SLUG.get(service_slug)
        if service is None:
            raise Http404('Municipal service not found')
        context['service'] = service
    return render(request, 'application_complete.html', context)
