from django.shortcuts import render
from django.http import HttpResponse
from media4.models import *
from recommend.models import *
from recommend.utils import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
#from .models import Users

# followers = Users_info.objects.order_by('date').values('followers_count')[0]
    # print(11111)
    # testrow=Comment.objects.values('totalcomment')
    # print(Users_fix.objects.filter(user_id='hamnihouse').first())
    # print(Users_info.objects.filter(ig_id=1579839464).order_by('date').values_list('followers_count').first()[0])
    # print(Comment.objects.filter(ig_id=1579839464).values_list('domain').first()[0])
    # print(Media_fix.objects.filter(owner_id=1579839464).values_list('media_id', flat=True))
    # print(Media_info.objects.filter(media_id='17982565250118885').values_list('comments_count', flat=True))
    # print(list(Media_fix.objects.filter(owner_id=1579839464).values_list('media_id', flat=True)))
    # print(cal_engagement(ig_id=1579839464))

    # firstdata = testrow[0]
    # context = {'followers' : firstdata}


# def index(request): 
#     # scores = {}
#     scores = []
#     username = ["a_arang_", "doublesoup", "calarygirl_a", "yulri_0i", "yeondukong", "lamuqe_magicup", "fallininm", "im_jella_",
#             "hamnihouse", "ssinnim", "yu__hyewon", "hyojinc_", "leojmakeup", "2__yun__2", "areumsongee", "makeup_maker_",
#             "r_yuhyeju", "vivamoon", "risabae_art", "yujin_so", "kisy0729", "ponysmakeup"]

#     for user in username:
#         id_object = Users_fix.objects.filter(user_id=user).first()
#         ig_ids = id_object.ig_id
#         score = scoring(ig_ids)
#         scores.append(score)

#     print(scores)

#     scaled_score = scale_list(scores, 1, 100)
#     context = {
#         'username' : username,
#         'scaled_score': scaled_score
#         }
    
#     return render(request,'recommend/recommend.html', context)

def index(request): 
    
 return render(request,'recommend/table.html')

@csrf_exempt
def recommend(request):
    if request.method == 'POST':
        price_value = int(request.POST.get('price'))
        market_value = int(request.POST.get('market'))
        model_value = int(request.POST.get('model'))
        product_value = int(request.POST.get('product'))

    scores = []
    username = ["a_arang_", "doublesoup", "calarygirl_a", "yulri_0i", "yeondukong", "lamuqe_magicup", "fallininm", "im_jella_",
            "hamnihouse", "ssinnim", "yu__hyewon", "hyojinc_", "leojmakeup", "2__yun__2", "areumsongee", "makeup_maker_",
            "r_yuhyeju", "vivamoon", "risabae_art", "yujin_so", "kisy0729", "ponysmakeup"]
    
    for user in username:
        id_object = Users_fix.objects.filter(user_id=user).first()
        ig_ids = id_object.ig_id
        score = scoring(ig_ids, model_value, level=price_value, market_value=market_value)
        scores.append(score)
    
    print(scores)
    scores = scale_list(scores, 1, 100)
    print(scores)

    data = {'Username': username, 'Score': scores}
    df = pd.DataFrame(data)

    sorted_df = df.sort_values(by='Score', ascending=False)
    print(sorted_df)
    top5 = sorted_df[0:5].to_dict(orient='records')
    print(top5)

    return JsonResponse({'top_influencers': top5})

@csrf_exempt
def result(request):
   if request.method == 'POST':
        username = list(request.POST.get('topInfluencers'))



   return JsonResponse({'scores': username})