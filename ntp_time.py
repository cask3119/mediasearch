import ntplib
   from time import ctime

   def get_ntp_time():
       client = ntplib.NTPClient()
       response = client.request('pool.ntp.org')
       return ctime(response.tx_time)

   print("NTP Time:", get_ntp_time())
