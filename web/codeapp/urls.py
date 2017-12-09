from django.urls import path

from . import views

app_name = 'codeapp'
urlpatterns = [
    path('app/code/', views.CodeIndexView.as_view(), name='code_list'),
    path('app/code/create/', views.CodeCreateView.as_view(), name='code_create'),
    path('app/code/<int:pk>/', views.CodeDetailView.as_view(), name='code_detail'),
    path('app/code/<int:pk>/snippet/create/', views.SnippetCreateView.as_view(), name='snippet_create'),
    # url('app/code/(?P<code_id>[0-9]+)/$', views.CodeDetailView.as_view(), name='code_detail'),
]

