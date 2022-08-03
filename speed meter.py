def get_speed_status(speed):
    # Complete this function
    if speed<60:
        result="Normal"
    elif 60<=speed<80:
        result="Warning"
    else:
        result="Over Speed"
    return(result)
speed = int(input())
# Call the get_speed_status function
result=get_speed_status(speed)
print(result)