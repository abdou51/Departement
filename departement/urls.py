from django.contrib import admin
from django.urls import path
from core.views import index,index_eng,login,logout,licence,coursedetails,planningexams,submit_document,profpanel,delete_document,edit_document,about,clubs
from django.conf import settings
from django.views.static import serve
import os
from django.conf.urls.static import static

urlpatterns = [

    path('', index , name='index'),
    path('admin/', admin.site.urls),
    path('about/', about , name='about'),
    path('clubs/', clubs , name='clubs'),
    path('login/', login , name='login'),
    path('logout', logout , name='logout'),
    path('courses/licence', licence , name='licence'),
    path('courses/licence/<str:pk>', coursedetails , name='coursedetails'),
    path('courses/licencedocuments/<str:path>', serve, {'document_root': os.path.join(settings.BASE_DIR, 'documents')}),
    path('scolarite/planningexams/documents/<str:path>', serve, {'document_root': os.path.join(settings.BASE_DIR, 'documents')}),
    path('scolarite/planningexams', planningexams , name='planningexams'),
    path('submit', submit_document , name='submit_document'),
    path('profpanel/', profpanel , name='profpanel'),
    path('delete_document/<int:pk>', delete_document, name='delete_document'),
    path('edit_document/', edit_document, name='edit_document'),
    path('edit/<int:pk>', edit_document, name='edit_document'),
    # path('de', display_degrees , name='display_degrees'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.error_404'

