"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

# urlpatterns מרכז את כל הניתובים הראשיים של הפרויקט (Project-level URLs)
urlpatterns = [
    # path('admin/') - הנתיב המובנה של Django שמפעיל את ממשק הניהול (Admin Panel) בכתובת /admin/
    path('admin/', admin.site.urls),

    # include() - פונקציה שמאפשרת "לייבא" ולשלב קובצי URLs של אפליקציות ספציפיות בפרויקט.
    # במקרה הזה, כל כתובת שמתחילה ב-'gym' תופנה לקובץ ה-urls.py שנמצא בתוך אפליקציית gym_tracker.
    path('gym', include('gym_tracker.urls')),
]