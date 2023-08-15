from media4.models import *
from recommend.models import *
import statistics
from datetime import datetime, timedelta

def cal_engagement(ig_id):
    media_ids = Media_fix.objects.filter(ig_id=ig_id).values_list('media_id', flat=True)
    # media_id에 해당하는 like_count 가져오기
    likes = Media_info.objects.filter(media_id__in=media_ids).values('like_count', flat=True)
    comments = Media_info.objects.filter(media_id__in=media_ids).values('comments_count', flat=True)
    followers = Users_info.objects.filter(ig_id=ig_id).order_by('date').values('followers_count').first()

    if followers is None or followers['followers_count'] == 0:
        return None # 유효성 검사

    engagement = [(like + comment) / followers['followers_count'] for like, comment in zip(likes, comments)]
    
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
    mediatime = Media_fix.objects.filter(ig_id=ig_id).order_by('-timestamp')[:14].values('timestamp')

    date_format = "%Y-%m-%dT%H:%M:%S%z"
    parsed_dates = [datetime.strptime(item['timestamp'], date_format) for item in mediatime]

    # 기록 간격 계산
    intervals = [parsed_dates[i] - parsed_dates[i-1] for i in range(1, len(parsed_dates))]

    # 평균 기록 간격 계산
    average_interval = sum(intervals, timedelta(0)) / len(intervals)

    return average_interval


def scaler(value, min_value, max_value, new_min, new_max):
    # 입력된 value를 min_value와 max_value 사이의 비율로 변환
    scaled_value = (value - min_value) / (max_value - min_value)
    
    # 스케일된 비율을 new_min과 new_max 사이의 값으로 매핑
    scaled_value = scaled_value * (new_max - new_min) + new_min
    
    # 결과 반환
    return scaled_value


def scoring(ig_id):
    followerslev = followerslevel(ig_id=ig_id)
    expert = Comment.objects.filter(ig_id=ig_id).values('domain')
    info = Comment.objects.filter(ig_id=ig_id).values('inforate')
    engage = cal_engagement(ig_id=ig_id)
    act = activities(ig_id=ig_id)
    scaled_act = scaler(act, 1, 14, 15, 1)

    score = (followerslev * 5) + (sum([item['domain'] for item in expert]) * 10) + (sum([item['inforate'] for item in info]) * 0.2) + (engage * 0.2) + scaled_act

    return score

