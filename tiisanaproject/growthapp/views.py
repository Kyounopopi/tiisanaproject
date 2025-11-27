from django.views import View
from django.shortcuts import render, redirect
from .models import GrowthRecord

class GrowthView(View):

    def get(self, request):
        """成長データ一覧を表示"""
        growth = GrowthRecord.objects.all().order_by("-date")
        return render(request, "growth.html", {
            "growth": growth
        })

    def post(self, request):
        """成長データを登録"""
        date = request.POST.get("date")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        development = request.POST.get("development")
        comment = request.POST.get("comment")

        # DB保存
        GrowthRecord.objects.create(
            date=date,
            height=height,
            weight=weight,
            development=development,
            comment=comment
        )

        # 登録後リダイレクト（更新ボタンで重複登録を防ぐ）
        return redirect("growth")