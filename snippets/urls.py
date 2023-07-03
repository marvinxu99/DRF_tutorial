from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


### View Using function 
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]


### View Using class-based, or mixins or generic class-based 
urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)