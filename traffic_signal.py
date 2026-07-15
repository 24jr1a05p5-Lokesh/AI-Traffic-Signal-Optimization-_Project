def calculate_signal_time(total_vehicles):

    if total_vehicles <= 10:
        return 15

    elif total_vehicles <= 20:
        return 30

    elif total_vehicles <= 40:
        return 45

    else:
        return 60