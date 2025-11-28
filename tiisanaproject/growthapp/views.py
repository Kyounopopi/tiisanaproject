from django.views import View
from django.shortcuts import render, redirect
# from .models import GrowthRecord

<<<<<<< HEAD
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
=======
# def growth_view(request):

#     # POST（データ登録）
#     if request.method == "POST":
#         date = request.POST.get("date")
#         height = request.POST.get("height")
#         weight = request.POST.get("weight")
#         development = request.POST.get("development")
#         comment = request.POST.get("comment")

#         # DBに保存
#         GrowthRecord.objects.create(
#             date=date,
#             height=height,
#             weight=weight,
#             development=development,
#             comment=comment
#         )

#         # 登録後はリロード（F5押しても二重登録を防ぐ）
#         return redirect("growth")

#     # GET（画面表示）
#     growthapp = GrowthRecord.objects.all().order_by("-date")

#     return render(request, "growthapp.html", {
#         "growthapp": growthapp
#     })
>>>>>>> 53c451e021eb6e121a0ae6408b69e6a8ed3a4967
