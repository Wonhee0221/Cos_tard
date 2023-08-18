from media4.models import *
from recommend.models import *
import statistics
from datetime import datetime, timedelta

def cal_engagement(ig_id):
    media_ids = list(Media_fix.objects.filter(owner_id=ig_id).values_list('media_id', flat=True))
    # media_id에 해당하는 like_count 가져오기
    likes = list(Media_info.objects.filter(media_id__in=media_ids, like_count__isnull=False).values_list('like_count', flat=True))
    comments = list(Media_info.objects.filter(media_id__in=media_ids, like_count__isnull=False).values_list('comments_count', flat=True))
    followers = Users_info.objects.filter(ig_id=ig_id).order_by('date').values_list('followers_count').first()[0]

    if followers is None or followers == 0:
        return None # 유효성 검사

    engagement = [(like + comment) / followers for like, comment in zip(likes, comments)]
    
    avg_engagement = statistics.mean(engagement)

    return avg_engagement


def followerslevel(ig_id):
    followers = Users_info.objects.filter(ig_id=ig_id).order_by('date').values_list('followers_count').first()

    if followers is None:
        return 0  

    followers_count = followers[0]
    
    if followers_count >= 1000000:
        level = 3
    elif followers_count >= 100000:
        level = 2
    elif followers_count >= 10000:
        level = 1
    else:
        level = 0  # 기본 레벨

    return level


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

def scale_list(data_list, new_min, new_max):
    min_value = min(data_list)
    max_value = max(data_list)
    
    scaled_data = []
    for value in data_list:
        scaled_value = (value - min_value) / (max_value - min_value) * (new_max - new_min) + new_min
        scaled_data.append(scaled_value)
    
    return scaled_data

def imaging(ig_id, model_value):
    if model_value in range(1, 5):
        column_names = ['cute', 'pure', 'gorg', 'sexy']
        image = Comment.objects.filter(ig_id=ig_id).values_list(column_names[model_value - 1])[0]
    else:
        return 0
    
    imagecomment = Comment.objects.filter(ig_id=ig_id).values_list('imagecomment')[0]
    
    if imagecomment == 0:
        return 0
    
    imageagree = image / imagecomment
    return imageagree

def pricing(ig_id, level):
    follower = followerslevel(ig_id=ig_id) #팔로워 수 단위 측정
    if level == 0: #가성비 선택
        weight = 1 / follower
        return weight * 20
    elif level == 1: #가격옵션 미선택
        return 0


# 판매증대 marketing_value 0
# 바이럴 marketing_value 1

def marketvalue(market_value):
    if market_value==0:
        info_weight=5
        viral_weight=1
    if market_value==1:
        info_weight=1
        viral_weight=5

    marketweight = [info_weight, viral_weight]

    return marketweight
    

def product_type(product):
    return 0


# def 매개변수로 , image, level, info_weight, image_weight 넣어주기

def scoring(ig_id, model_value, level, image_weight, market_value):
    followerslev = followerslevel(ig_id=ig_id) #팔로워수 단위
    expert = Comment.objects.filter(ig_id=ig_id).values_list('domain').first()[0] #도메인지식 정도
    info_c = Comment.objects.filter(ig_id=ig_id).values_list('inforate').first()[0] #정보댓글 비율, 가중치는 입력받는 것으로. 매출 증대 목표
    image_c = Comment.objects.filter(ig_id=ig_id).values_list('imagerate').first()[0] # 이미지댓글 비율, 바이럴 증가? 아닌듯..바이럴마케팅은 팔로워수/인게이지에 더 가중치를
    marketweight = marketvalue(market_value)
    info_weight = marketweight[0]
    viral_weight = marketweight[1]
    engage = cal_engagement(ig_id=ig_id) #인게이지먼트
    # act = activities(ig_id=ig_id)
    # scaled_act = scaler(act, 1, 14, 15, 1)
    model_image = imaging(ig_id, model_value) # 이미지옵션
    price = pricing(ig_id, level) # 가격대옵션
    # 화장품분류
    
    
    score = (followerslev * viral_weight) + (expert * 10) + (info_c * info_weight) + (engage * viral_weight) + (model_image * 100) + price + (image_c * image_weight)

    return score


