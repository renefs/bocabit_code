from django.urls import path

from . import views

app_name = 'codeapp'
urlpatterns = [
    #
    # CODE
    #
    path('app/code/', views.CodeIndexView.as_view(), name='code_list'),
    path('app/code/create/', views.CodeCreateView.as_view(), name='code_create'),
    path('app/code/<int:pk>/', views.CodeDetailView.as_view(), name='code_detail'),
    path('app/code/<int:pk>/update/', views.CodeUpdateView.as_view(), name='code_update'),
    #
    # SNIPPET
    #
    path('app/code/<int:code_id>/snippet/create/', views.SnippetCreateView.as_view(), name='snippet_create'),
    path('app/code/<int:code_id>/snippet/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet_detail'),
    path('app/code/<int:code_id>/snippet/<int:pk>/update/', views.SnippetUpdateView.as_view(), name='snippet_update'),
    #
    # TAG
    #
    path('app/tag/', views.TagIndexView.as_view(), name='tag_list'),
    path('app/tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('app/tag/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('app/tag/<int:pk>/update/', views.TagUpdateView.as_view(), name='tag_update'),
    # url('app/code/(?P<code_id>[0-9]+)/$', views.CodeDetailView.as_view(), name='code_detail'),
]

