from datetime import datetime
import pytz

def get_time(place):
    try:
        timezone = pytz.timezone(place)
        current_time = datetime.now(timezone)
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
    except pytz.UnknownTimeZoneError:
        return "Unknown timezone. Please provide a valid place."

