from media4.models import *
from recommend.models import *
import statistics
from datetime import datetime, timedelta
import math
import pandas as pd

def cal_engagement(ig_id):
    media_ids = list(Media_fix.objects.filter(owner_id=ig_id).values_list('media_id', flat=True))
    # media_id에 해당하는 like_count 가져오기
    likes = list(Media_info.objects.filter(media_id__in=media_ids, like_count__isnull=False).values_list('like_count', flat=True))
    comments = list(Media_info.objects.filter(media_id__in=media_ids, like_count__isnull=False).values_list('comments_count', flat=True))
    followers = Users_info.objects.filter(ig_id=ig_id).order_by('date').values_list('followers_count').first()[0]

    if followers is None or followers == 0:
        return None # 유효성 검사

    engagement = [(like + comment) / followers * 100 for like, comment in zip(likes, comments)]
    
    avg_engagement = statistics.mean(engagement)

    return avg_engagement


def followerslevel(ig_id):
    followers = Users_info.objects.filter(ig_id=ig_id).order_by('date').values_list('followers_count', flat=True).first()

    if followers is None:
        return 0  
    
    rounded = round(math.log(followers),2)

    return rounded


def activities(ig_id):
    mediatime = Media_fix.objects.filter(owner_id=ig_id).order_by('-timestamp')[:14].values('timestamp')

    date_format = "%Y-%m-%d %H:%M:%S"
    parsed_dates = [datetime.strptime(item['timestamp'], date_format) for item in mediatime]

    date_intervals = []
    for i in range(1, len(parsed_dates)):
        interval = abs((parsed_dates[i].date() - parsed_dates[i - 1].date()).days)
        date_intervals.append(interval)

    average_interval = sum(date_intervals) / len(date_intervals)

    return average_interval



def scaler(value, min_value, max_value, new_min, new_max):
    # 입력된 value를 min_value와 max_value 사이의 비율로 변환
    scaled_value = (value - min_value) / (max_value - min_value)
    
    # 스케일된 비율을 new_min과 new_max 사이의 값으로 매핑
    scaled_value = scaled_value * (new_max - new_min) + new_min
    
    # 결과 반환
    return scaled_value

def rescale(value, old_min, old_max, new_min, new_max):
    # 이전 범위에서의 비율 계산
    old_range = old_max - old_min
    new_range = new_max - new_min
    scaled_value = ((value - old_min) / old_range) * new_range + new_min
    return scaled_value

def rescale_list(data_list, old_max, new_max):
    rate = new_max/old_max
    scaled_data_list = [(value * rate) for value in data_list]
    
    return scaled_data_list


def scale_list(data_list, new_min, new_max):
    min_value = min(data_list)
    max_value = max(data_list)
    
    scaled_data = []
    for value in data_list:
        scaled_value = (value - min_value) / (max_value - min_value) * (new_max - new_min) + new_min
        scaled_data.append(scaled_value)
    
    return scaled_data

def reverse(value):
    min_value = 16
    max_value = 11

    scaled_value = max_value + min_value - value

    return scaled_value

def scale_line(data_list, mymax, target):
    scaled_data=[]
    for value in data_list:
        scaled_value = (value / mymax) * target
        scaled_data.append(scaled_value)
    
    return scaled_data

# model 일치 계산
def imaging(ig_id, model_value):
    if model_value in range(1, 5):
        column_names = ['cute', 'pure', 'gorg', 'sexy']
        image = Comment.objects.filter(ig_id=ig_id).values_list(column_names[model_value - 1], flat=True)[0]
    else:
        return 0
    
    imagecomment = Comment.objects.filter(ig_id=ig_id).values_list('imagecomment', flat=True)[0]
    
    if imagecomment == 0:
        return 0
    
    imageagree = image / imagecomment
    return imageagree

# 특정 이미지 키워드 댓글 개수
def getimage(ig_id, model_value):
    if model_value in range(1, 5):
        column_names = ['cute', 'pure', 'gorg', 'sexy']
        image = Comment.objects.filter(ig_id=ig_id).values_list(column_names[model_value - 1], flat=True)[0]
    else:
        return 0
    
    return image


def pricing(ig_id, level):
    follower = followerslevel(ig_id=ig_id) #팔로워 수 단위 측정
    if level == 0: #가성비광고 선택
        follower_price = reverse(follower) + 10
        return follower_price
    elif level == 1: #고가광고 선택
        return follower


# 판매증대 marketing_value 0
# 바이럴 marketing_value 1

def marketvalue(market_value):
    if market_value==0:
        effect_weight=0.5
        impact_weight=1.5
    if market_value==1:
        effect_weight=1.5
        impact_weight=0.5
    else:
        effect_weight = 1
        impact_weight = 1

    marketweight = [effect_weight, impact_weight]

    return marketweight
    

def product_type(ig_id, product):
    rows = Brand.objects.filter(ig_id=ig_id).values_list('type',flat=True)

    for row in rows:
        if product == row:
            return 1
    return 0




# def 매개변수로 , image, level, info_weight, image_weight 넣어주기

# def scoring(ig_id, model_value, level, market_value):
#     followerslev = followerslevel(ig_id=ig_id) #팔로워수 단위
#     expert = Comment.objects.filter(ig_id=ig_id).values_list('domain').first()[0] #도메인지식 정도
#     info_c = Comment.objects.filter(ig_id=ig_id).values_list('inforate').first()[0] #정보댓글 비율, 가중치는 입력받는 것으로. 매출 증대 목표
#     image_c = Comment.objects.filter(ig_id=ig_id).values_list('imagerate').first()[0] # 이미지댓글 비율, 충성도에 영향
#     marketweight = marketvalue(market_value)
#     info_weight = marketweight[0]
#     viral_weight = marketweight[1]
#     engage = cal_engagement(ig_id=ig_id) #인게이지먼트
#     # act = activities(ig_id=ig_id)
#     # scaled_act = scaler(act, 1, 14, 15, 1)
#     model_image = imaging(ig_id, model_value) # 이미지옵션
#     price = pricing(ig_id, level) # 가격대옵션
#     # 화장품분류
    
    
#     score = (followerslev * viral_weight) + (expert * 10) + (info_c * info_weight) + (engage * viral_weight) + (model_image * 100) + price + (image_c)

#     return score



def scoring(ig_id, model_value, level, market_value, product_value):
    followerslev = pricing(ig_id=ig_id, level=level)
    engage = round(cal_engagement(ig_id=ig_id),2)
    action = Activity.objects.filter(ig_id=ig_id).values('imgcmt','infocmt','channelsize','contentpower','adratio','lifefeed', 'brandnum','reactfeed','followerfeed').first()
    image = imaging(ig_id, model_value=model_value)
    market_w = marketvalue(market_value=market_value)
    producthist = product_type(ig_id=ig_id, product=product_value)

    expertised = action['channelsize'] * action['contentpower'] + producthist
    loyalty = followerslev + engage + (action['imgcmt']/action['lifefeed']) + action['reactfeed']
    impact = followerslev + action['contentpower'] + action['adratio']
    effect = engage + (action['infocmt']/action['lifefeed']) + action['contentpower'] + action['followerfeed'] + image
    f = Users_info.objects.filter(ig_id=ig_id).order_by('date').values_list('followers_count', flat=True).first()

    score = round((expertised+loyalty+ market_w[1] * impact+ market_w[0] * effect),2)


    result = { 'id':ig_id, 'followersnum':f, 'engage':engage, 'Score': score, 'expertised':expertised, 'loyalty':loyalty, 'impact':impact, 'effect':effect, 'image':image}

    return result

#협업 브랜드
def branding(ig_id):
    try:
        distinct_brands = Brand.objects.filter(ig_id=ig_id).values('brand').distinct()
        brand_list = [item['brand'] for item in distinct_brands]
        if not brand_list:
            brand_list = []
        else:
            brand_list = brand_list[:5]  # Limit the list to maximum 5 items
    except Brand.DoesNotExist:
        brand_list = []

    return brand_list



