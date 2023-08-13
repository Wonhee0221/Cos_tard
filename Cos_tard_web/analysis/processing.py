from media4.models import *

def follower_graph(ig_id):
    follower_trend = Users_info.objects.filter(ig_id=ig_id).order_by('-date').values('followers_count', 'date')
    follower_trend = list(follower_trend)
    xData = [data['date'] for data in follower_trend]
    yData = [data['followers_count'] for data in follower_trend]
    
    follower_trend = {
        'xData': xData,
        'yData': yData,
    }
    return (follower_trend)


