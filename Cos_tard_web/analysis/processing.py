from media4.models import *

def follower_graph(ig_id):

    ##검색한 인플루언서##
    follower_trend = Users_info.objects.filter(ig_id=ig_id).order_by('date').values('followers_count', 'date')
    follower_trend = list(follower_trend)
    xData = [data['date'] for data in follower_trend]
    yData = [data['followers_count'] for data in follower_trend]
    growth_rates = [0]

    for i in range(1, len(yData)):
        prev_value = yData[i - 1]
        current_value = yData[i]
        
        growth_rate = ((current_value - prev_value) / prev_value) * 100
        growth_rates.append(growth_rate)
    
    total_growth = sum (growth_rates)
    average_growth = total_growth / len(yData)

    max_growth = max (growth_rates)
    index = growth_rates.index(max_growth)
    max_growth_date = xData[index]

    ##검색한 인플루언서 이외, 비교군##

    ##이상치
    exclude = "1579839464"

    all_users= Users_fix.objects.exclude(ig_id=ig_id).values('ig_id')
    all_users = [data['ig_id'] for data in all_users if data['ig_id'] != exclude]

    contrast = []
    
    for i in all_users:
        follower_other = Users_info.objects.filter(ig_id=i).order_by('date').values('followers_count','date')
        follower_other = list(follower_other)
        y = [data['followers_count'] for data in follower_other]
        growth_other = [0]

        for i in range(1, len(y)):
            prev_value = y[i - 1]
            current_value = y[i]
        
            growth_rate = ((current_value - prev_value) / prev_value) * 100
            growth_other.append(growth_rate)

        contrast.append(growth_other)

    contrast = list(zip(*contrast))
    growth_rate_average = [sum(data) / len(data) for data in contrast]

    total_growth_average = sum (growth_rate_average)
    average_average_growth = total_growth_average / len(y)
    

    follower_trend = {

        'xData': xData,
        'yData': yData,
        'growth_rates' : growth_rates, #인플루언서 증가율
        'growth_rate_average': growth_rate_average, #비교군 증가율
        'average_growth' : average_growth, #인플루언서 증가율 평균
        'average_average_growth' : average_average_growth, #비교군 증가율 평균
        'max_growth_date' : max_growth_date
    }
    return (follower_trend)

def get_image(ig_id): 
    media_id = Media_fix.objects.filter(owner_id=ig_id).order_by('-timestamp').values('media_id')[:5]
    media_id=list(media_id)
    return (media_id)




