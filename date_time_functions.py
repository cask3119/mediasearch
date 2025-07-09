from datetime import datetime
   import pytz

   # Get current time in UTC
   utc_now = datetime.now(pytz.utc)

   # Convert to a specific timezone if needed
   local_tz = pytz.timezone('America/New_York')
   local_time = utc_now.astimezone(local_tz)
