# ## Settings for this repository
#

import pandas as pd
from obspy import UTCDateTime


# Set these values to control the notebook behaviour

# Make sure you take at least a full week (>=7 days) before the first "ban"
start = UTCDateTime("2019-12-01")

# Leaving UTCDateTime() empty means "now":
# and this means 24 hours ago: UTCDateTime() - 24*3600
end = UTCDateTime() - 24*3600


# This is the time it takes to be sure the data that we download is a complete record that
# we can reliably cache in the archive
safety_window = pd.Timedelta('2 days')


network = "S1"
station = "AUDAR"              #,sydney,brisbane jump, adelaide," # Urban stations
location = "*"
channel = "HHZ"
dataset = "AuSiS_Canberra"
time_zone = "Australia/ACT"
sitedesc = "Daramalan College, ACT"

data_provider = "http://auspass.edu.au:8080"
logo = None # 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_SED_2014.png/220px-Logo_SED_2014.png'
bans = { "2019-12-20 00:00":"Start of School Summer Holiday",
        "2020-01-28 00:00":"End of School Summer Holiday",
        "2020-03-18 00:00":'No Large Gatherings',
        "2020-03-25 12:00":'Closures',
        "2020-04-10 00:00":"Easter", 
        "2020-05-25 00:00":"Schools open (NSW)", 
        "2020-07-07 00:00":"Restrictions re-imposed (VIC)"
        }


reference = {"start": "2020-02-03 00:00",
              "end":  "2020-03-23 00:00"}

summer_hol = {"start":"2019-12-20 00:00",
              "end":  "2020-02-02 00:00"}

lockdown   = {"start":"2020-03-24 00:00",
              "end":  "2020-05-18 00:00"}

reopening    = {"start":"2020-05-25 00:00"}
