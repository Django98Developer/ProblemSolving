def past(h, m, s):
    oneSecond = 1000
    oneMinute = 60*oneSecond
    oneHour = 60*oneMinute
    return (h*oneHour)+(m*oneMinute)+(s*oneSecond)


print(past(0, 1, 1))
