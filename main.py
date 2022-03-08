from os import listdir
from os.path import isfile, join
from datetime import datetime, timedelta
from os.path import join, basename
import sys
import logging
logging.basicConfig(filename=r'C:\Users\jmeyer\04 - Software\20 - DailyNote\example.log', encoding='utf-8', level=logging.DEBUG)
rnow = datetime.now()
logging.info(f"STARTING PROGRAM: {rnow}")

if rnow in [6,7]:
    logging.info("WEEKEND - SKIP NOTE. CLOSE OUT")
    sys.exit()

dailynote_path = r"C:\Users\jmeyer\02 - KMS\01 - KM\daily notes"
logging.info(f"LOOKING FOR NOTES IN: {dailynote_path}")

onlyfiles = [f for f in listdir(dailynote_path) if isfile(join(dailynote_path, f))]
onlyfiles.sort(reverse=True)
last_entry = onlyfiles.pop(0)
lasttimestamp = last_entry[:8]
lastdate = datetime.strptime(lasttimestamp, "%Y%m%d")

filepath = join(dailynote_path, last_entry)
with open(filepath, "r") as f:
    lines = f.readlines()
    logging.info(f"READ POST OP NOTES FROM LAST NOTE: {filepath}")
startcopy = lines.index('## PostOp\n')

for_template = ""
for x in lines[startcopy+1:]:
    for_template = for_template + x

today_date = rnow.strftime("%Y%m%d")
temptext = f"""# {today_date} DN
{rnow.strftime("%Y-%m-%d")} | {rnow.strftime("%H:%M")}
tags: #dailynote 
___

## PostOp Yesterday
{for_template}

## PreOp
NA

## PostOp

"""
new_note_title = f"{today_date} DN.md"

print(temptext)
filepath = join(dailynote_path, new_note_title)
with open(filepath, "w+") as text_file:
    logging.info(f"CREATING FILE: {filepath}")
    text_file.write(temptext)

# logging.info("READY TO EXIT")
# sys.exit(0)
