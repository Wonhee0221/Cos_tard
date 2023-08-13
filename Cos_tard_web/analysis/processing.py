from media4.models import *

def follower_graph(ig_id):
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
    
    
    follower_trend = {
        'xData': xData,
        'yData': yData,
        'growth_rates' : growth_rates,
        'average_growth' : average_growth

    }
    return (follower_trend)




