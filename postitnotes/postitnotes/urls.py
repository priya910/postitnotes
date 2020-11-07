"""postitnotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import list_notes, create_note, delete_note, edit, mark_done, mark_favourite, remove_favourite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', list_notes, name='notes'),
    path('create/', create_note, name='create_note'),
    path('delete/<int:id>',delete_note,name="delete"),
    path('edit/<int:id>',edit,name="edit"),
    path('done/<int:id>',mark_done,name="done"),
    path('favourite/<int:id>', mark_favourite, name="favourite"),
    path('remove/favourite/<int:id>', remove_favourite, name="remove_favourite"),

    
]
