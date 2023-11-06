import requests
import re
from datetime import datetime, timedelta


#change with your online ics file
url = 'https://calendar.google.com/calendar/ical/[..]/[..]/basic.ics'

ical_data = requests.get(url).text

event_pattern = re.compile(r'BEGIN:VEVENT(.*?)END:VEVENT', re.DOTALL)
events = event_pattern.findall(ical_data)

today = datetime.now().date() #Date without time

now = datetime.now()
date_time = now.strftime("%d.%m.%Y / %H:%M")

for event in events:
    description_match = re.search(r'SUMMARY:(.*?)\n', event)
    start_time_match = re.search(r'DTSTART:(.*?)\n', event)
    end_time_match = re.search(r'DTEND:(.*?)\n', event)

    if description_match:
            description = description_match.group(1)
    else:
        description = 'Kein Titel'

    if start_time_match:
        start_time_str = start_time_match.group(1)
        start_time = datetime.strptime(start_time_str, "%Y%m%dT%H%M%SZ\r").date() #.strftime("%d.%m.%Y / %H:%M")
        if start_time == today:
            start_time = datetime.strptime(start_time_str, "%Y%m%dT%H%M%SZ\r").strftime("%d.%m.%Y / %H:%M")
        else:
            continue
    else:
        start_time = 'Kein Anfangszeitpunkt vorhanden'

    if end_time_match:
        end_time_str = end_time_match.group(1)
        end_time = datetime.strptime(end_time_str, "%Y%m%dT%H%M%SZ\r").date() #strftime("%d.%m.%Y / %H:%M")
        if end_time == today:
            end_time = datetime.strptime(end_time_str, "%Y%m%dT%H%M%SZ\r").strftime("%d.%m.%Y / %H:%M")
        else:
            continue #end_time = 'Kein Anfangszeitpunkt vorhanden'
    else:
        end_time = 'Kein Endzeitpunkt vorhanden'

    print("\n")
    print("Termin:", description)
    print("Start:", start_time)
    print("Ende :", end_time)
    print("\n")
