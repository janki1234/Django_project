from django.urls import path
from .views import (blog_list,
	blog_view,
	blog_create,
	blog_update,
	blog_delete)

app_name='blog'

urlpatterns =[

	path('',blog_list),
	path('create/',blog_create),
	path('<id>/delete/',blog_delete),
	path('<id>/update/',blog_update),
	path('<id>/',blog_view),
]