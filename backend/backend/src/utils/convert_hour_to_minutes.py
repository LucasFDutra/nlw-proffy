def convert(hour):
    hour_, minute_ = hour.split(':')
    hour = int(hour_)
    minute = int(minute_)
    minute += hour*60
    return minute
