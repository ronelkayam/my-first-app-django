from django.shortcuts import render
from .models import Member, WorkoutLog


# Create your views here.

def member_list(view_request):
    """
    View שמטפל בבקשת ה-HTTP להצגת רשימת כל החברים במערכת.
    מקבל אובייקט request ומחזיר אובייקט response (קובץ HTML מרונדר).
    """

    # Member.objects.all() - שליפה של כל הרשומות מהטבלה באמצעות ה-ORM של Django (ללא כתיבת שאילתת SQL ידנית).
    # הערה לימודית: השאילתא מבוצעת בפועל ב-Lazy Evaluation רק כשניגשים לנתונים בתבנית ה-HTML.
    members = Member.objects.all()

    # context - מילון (Dictionary) שדרכו מעבירים את הנתונים מה-Backend אל קובץ ה-Template (ה-HTML).
    # המפתח במילון ('members') יהיה שם המשתנה שבו נשתמש בתוך ה-HTML בתוך תגיות הלולאה.
    context = {'members': members}

    # render - פונקציה שמקבלת את הבקשה, את נתיב קובץ ה-HTML, ואת מילון הנתונים (Context),
    # מייצרת את עמוד ה-HTML הסופי ומחזירה אותו כ-HttpResponse לדפדפן של המשתמש.
    return render(view_request, 'gym_tracker/member_list.html', context)