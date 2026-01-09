# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import date, timedelta
from .models import CalendarDay
from .forms import DayEntryForm

def calendar_view(request, year=None, month=None, day=None):
    selected_date = request.GET.get("date")

    if selected_date:
        selected_date = date.fromisoformat(selected_date)
    else:
        selected_date = date.today()

    # 横スクロール用（日付 ±3日）
    days = [
        selected_date + timedelta(days=i)
        for i in range(-3, 4)
    ]

    records = CalendarDay.objects.filter(date=selected_date)

    context = {
        "selected_date": selected_date,
        "days": days,
        "records": records,
    }

    calendar_day, _ = CalendarDay.objects.get_or_create(date=selected_date)

    if request.method == 'POST':
        form = DayEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.day = calendar_day
            entry.save()
            return redirect(request.path)
    else:
        form = DayEntryForm()

    context = {
        "calendar_day": calendar_day,
        "form": form,
        "selected_date": selected_date,
    }
    return render(request, "calendar.html", context)
