from django.shortcuts import render, redirect
# from .models import GrowthRecord

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