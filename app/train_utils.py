from datetime import datetime

def calculate_delay(scheduled, estimated):
    try:
        scheduled_time = datetime.strptime(scheduled, "%H:%M")
        estimated_time = datetime.strptime(estimated, "%H:%M")

        delay = estimated_time-scheduled_time
        delay_minutes = delay.total_seconds() / 60

        return delay_minutes

    except ValueError:
        return None

def get_train_status(scheduled, estimated) :
    if estimated == "Cancelled" :
        return "cancelled"
    elif estimated == "On time" :
        return "on_time"
    elif estimated == "Delayed" :
        return "delayed"
    else:
        delay_minutes = calculate_delay(scheduled, estimated)
        if delay_minutes is None :
            return "unknown"
        elif delay_minutes > 0 :
            return "delayed"
        else:
            return "on_time"


# if __name__ == "__main__":
#     result = calculate_delay("18:28", "18:36")
#     print(result)

if __name__ == "__main__":
    print(get_train_status("18:28", "18:36"))
    print(get_train_status("18:28", "18:28"))
    print(get_train_status("18:28", "On time"))
    print(get_train_status("18:28", "Cancelled"))
    print(get_train_status("18:28", "Delayed"))
    print(get_train_status("18:28", "Unknown"))