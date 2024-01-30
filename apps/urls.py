from django.conf import urls
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import path, include

from apps.views import IndexView, CustomLoginView, RegisterFormView, BlogDetailView, BlogListView, ProcessEmailView

# def custom_view(request, email):
#     response = task_send_email.delay('Temasi', 'xabari', ['xolmomin@gmail.com'])
#     response = task_send_email('Temasi', 'xabari', ['azamovshahboz06082001@gmail.com'])
#     return JsonResponse({'status': 'success'})

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('process_email/', ProcessEmailView.as_view(), name='process_email'),
    # path('send/<email>', custom_view),
    path('blog-list', BlogListView.as_view(), name='blog_list_page'),
    path('blog-detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail_page'),
    path('logout', LogoutView.as_view(next_page='index_page'), name='logout'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]


def page_404(request, *args, **kwargs):
    return render(request, 'apps/404.html', status=404)


urls.handler404 = 'apps.urls.page_404'
