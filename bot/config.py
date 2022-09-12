#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "7556932"
    API_HASH = "6b99e012069f373abbcac581d3cdd6db"
    BOT_TOKEN = "5504367878:AAHAGnkxPdKXCyDAx6atevENv7lzu4qSVEA"
    DEV = 1664850827
    OWNER = "1144738419 1160615379 5798143340 974552063"
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://graph.org/file/68caa8276fbeff04b1172.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
