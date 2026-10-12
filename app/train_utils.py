from datetime import datetime

def calculate_delay(scheduled, estimated):
    scheduled_time = datetime.strptime(scheduled, "%H:%M")
    estimated_time = datetime.strptime(estimated, "%H:%M")

    delay = estimated_time-scheduled_time
    delay_minutes = delay.total_seconds() / 60

    return delay_minutes

if __name__ == "__main__":
    result = calculate_delay("18:28", "18:36")
    print(result)