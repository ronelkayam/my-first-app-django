from django.urls import path
from . import views

# urlpatterns הוא רשימה שבה Django מחפש התאמה בין כתובת ה-URL שהמשתמש ביקש לבין פונקציית ה-View המתאימה.
urlpatterns = [
    # path() מקבל שלושה פרמטרים עיקריים:
    # 1. route ('') - מחרוזת המייצגת את הנתיב היחסי (כאן זהו הנתיב הראשי של האפליקציה, למשל /gym/).
    # 2. view (views.member_list) - פונקציית ה-View שתופעל ברגע שהמשתמש יכנס לכתובת זו.
    # 3. name ('member_list') - שם ייחודי שמאפשר לקרוא לנתיב הזה בקלות מתוך קוד ה-Python או תבניות ה-HTML (בעזרת {% url %}).
    path('', views.member_list, name='member_list'),
]