import math
from datetime import datetime

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def detect_spoof(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    last_lat, last_lon, last_time = None, None, None
    for line in lines:
        if "$GPRMC" in line:
            parts = line.split(',')
            if parts[3] and parts[5]:
                lat = float(parts[3][:2]) + float(parts[3][2:]) / 60
                lon = float(parts[5][:3]) + float(parts[5][3:]) / 60
                time_str = parts[1]
                time_obj = datetime.strptime(time_str[:6], "%H%M%S")

                if last_lat:
                    dist = haversine(lat, lon, last_lat, last_lon)
                    time_diff = (time_obj - last_time).seconds or 1
                    speed = (dist / time_diff) * 3600
                    if speed > 300:
                        print(f"🚨 Possible spoofing at {time_obj.time()}: Speed = {speed:.2f} km/h")

                last_lat, last_lon, last_time = lat, lon, time_obj

if __name__ == "__main__":
    detect_spoof("sample_log.nmea")
