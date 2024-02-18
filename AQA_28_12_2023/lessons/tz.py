from datetime import datetime, timedelta, timezone


kyiv_offset = timezone(timedelta(hours=1))
kyiv_time = datetime.now(kyiv_offset)

print(kyiv_time)