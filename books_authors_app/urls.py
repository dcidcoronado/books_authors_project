from django.urls import path		
from . import views

urlpatterns=[
    path ('',views.index),
    path ('books',views.new_book),
    path ('books/<book_id>',views.view_book),
    path ('books/<book_id>/new',views.view_book),
    path ('authors',views.authors),
    path ('new_authors',views.new_author),
    # path ('otrocon/<variable>',views.nombredeotrafuncion)
]