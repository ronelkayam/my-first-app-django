from django.contrib import admin
from .models import Member, WorkoutLog

# Register your models here.

# admin.site.register() - רישום המודלים בממשק הניהול המובנה של Django.
# פעולה זו מוסיפה אוטומטית את הטבלאות למסך הניהול (Django Admin) ומאפשרת
# לבצע פעולות CRUD (יצירה, קריאה, עדכון ומחיקה) ישירות דרך הדפדפן.
admin.site.register(WorkoutLog)
admin.site.register(Member)

# --- דוגמאות לפעולות ORM בקוד (שנשמרו בהערה לצורך לימוד ותרגול) ---
# יצירת מופע (Object) חדש ושמירתו במסד הנתונים:
# new_member = Member(first_name='John', last_name='Doe', email='jhon@mail.com')
# new_member.save()

# שליפת כל הרשומות מהטבלה באמצעות ה-ORM:
# all_members = Member.objects.all()