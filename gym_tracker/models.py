from django.db import models


# Create your models here.
class Member(models.Model):
    """
    מודל המייצג חבר במערכת (למשל, חדר כושר).
    כל מחלקה שיורשת מ-models.Model מתרגמת אוטומטית לטבלה במסד הנתונים דרך ה-ORM.
    """

    # CharField: שדה טקסט קצר עם הגבלת תווים מקסימלית (מתורגם ל-VARCHAR ב-SQL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # EmailField: שדה טקסט ולידציה מובנה לכתובות אימייל. unique=True מוודא שאין שני חברים עם אותו אימייל במסד
    email = models.EmailField(unique=True)

    # DateField: שדה תאריך. auto_now_add=True קובע אוטומטית את התאריך הנוכחי פעם אחת בזמן יצירת הרשומה
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        # __str__: מגדיר את הייצוג הטקסטואלי של האובייקט (מופיע בממשק הניהול Admin ובלוגים)
        return f"{self.first_name} {self.last_name}"


class WorkoutLog(models.Model):
    """
    מודל המייצג רישום אימון של חבר מסוים.
    המודל מדגים קשר גומלין (Relational Mapping).
    """

    # ForeignKey: יוצר קשר מסוג Many-to-One (הרבה אימונים יכולים להיות שייכים לחבר אחד).
    # member: שדה הקישור למודל Member.
    # on_delete=models.CASCADE: הגנה מפני מחיקת אב - אם חבר נמחק מהמערכת, כל אימוני העבר שלו יימחקו יחד איתו אוטומטית.
    # related_name='workouts': מאפשר גישה הפוכה מהחבר אל כל האימונים שלו (למשל: member.workouts.all()).
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='workouts')

    exercise_name = models.CharField(max_length=100)

    # IntegerField: שדה שמקבל ערכים מספריים שלמים בלבד (כמו מספר סטטים או חזרות)
    sets = models.IntegerField()
    reps = models.IntegerField()

    # TextField: שדה טקסט ארוך ללא מגבלת אורך קשיחה.
    # blank=True אומר שהשדה יכול להיות ריק בטפסים, null=True מאפשר לשמור ערך NULL במסד הנתונים.
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.exercise_name} {self.sets} {self.reps} {self.notes}"