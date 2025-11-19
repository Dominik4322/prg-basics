def time_string(hours, minutes, time_format):
    
    hours >= 0 and hours < 24
    minutes >= 0 and minutes < 60
    time_format == 12 or time_format == 24


    if time_format == 24:
        return f"{hours:02}:{minutes:02}"
    elif time_format == 12:
        period = ""
        if hours <= 12 and hours >= 0:
            period = "AM"
            return f"{hours:02}:{minutes:02} {period}"
        else:
            period = "PM"
            hours = hours - 12
            return f"{hours:02}:{minutes:02} {period}"
    




print(time_string(0,5,24))
print(time_string(14,2,12))