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


# if __name__ == "__main__":
#     result = calculate_delay("18:28", "18:36")
#     print(result)

if __name__ == "__main__":
    print(calculate_delay("18:28", "18:36"))
    print(calculate_delay("18:28", "On time"))
    print(calculate_delay("18:28", "Delayed"))
    print(calculate_delay("18:28", "Cancelled"))