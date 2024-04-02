import sys
import re
from datetime import timedelta

if len(sys.argv) == 1:
    sys.stdout.write("Usage: \t\tpython3 subfps.py file_location [subtitle_file_fps] [target_video_fps]\nExample: \tpython3 subfps.py \"D:\\Username\\Documents\\Subtitles\\My Subtitle.srt\" 25 23.976")
    quit()
elif len(sys.argv) == 2:
    sys.stdout.write("No fps arguments given. Assuming origin is 25 and target is 23.976\n")
    fileLocation = sys.argv[1]
    originFramerate = 25
    targetFramerate = 23.976
elif len(sys.argv) >= 4:
    fileLocation = sys.argv[1]
    originFramerate = sys.argv[2]
    targetFramerate = sys.argv[3]

targetLocation = fileLocation.removesuffix(".srt") + "_{}fps".format(targetFramerate) + ".srt"

sys.stdout.write("Reading file\n")
originalFile = open(fileLocation, "r")
targetFile = open(targetLocation, "w")
originalLines = originalFile.readlines()

sys.stdout.write("Converting from {}fps to {}fps\n".format(originFramerate, targetFramerate))

def modify(timestring):
    timeStrings = timestring.split(":")
    inSeconds = float(timeStrings[0]) * 3600 + float(timeStrings[1]) * 60 + float(timeStrings[2].replace(",", "."))
    newSeconds = inSeconds * float(originFramerate) / float(targetFramerate)
    
    output = str(timedelta(seconds=newSeconds)).replace(".", ",")
    return output[0:-3]

lineCount = len(originalLines)
for lineIndex in range(lineCount):
    if re.search("([0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9])", originalLines[lineIndex]):
        times = originalLines[lineIndex].split(" --> ")
        times[0] = modify(times[0])
        times[1] = modify(times[1].removesuffix("\n"))
        originalLines[lineIndex] = times[0] + " --> " + times [1] + "\n"
        
    sys.stdout.write("\rWriting Line: " + str(lineIndex + 1) + " / " + str(lineCount))
    sys.stdout.flush()
    targetFile.write(originalLines[lineIndex])
    
sys.stdout.write("\nDone!\nSynced File Location: \t\"{}\"".format(targetLocation))