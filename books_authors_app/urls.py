from django.urls import path		
from . import views

urlpatterns=[
    path ('',views.index),
    path ('books',views.new_book),
    path ('books/<book_id>',views.view_book),
    path ('books/<book_id>/new',views.view_book),
    path ('new_authors',views.new_author),
    path ('authors',views.authors),
    path ('authors/<author_id>',views.view_author),
    path ('authors/<author_id>/new',views.view_author),
    # path ('otrocon/<variable>',views.nombredeotrafuncion)
]