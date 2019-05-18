"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def getLongestDurationCall():
    phone_dict = dict()
    for call in calls:
        makeCallPhone = call[0]
        receiveCallPhone = call[1]
        durationCall = call[3]
        if makeCallPhone in phone_dict: 
            phone_dict[makeCallPhone] += int(durationCall)
        else:
            phone_dict[makeCallPhone] = int(durationCall)
        if receiveCallPhone in phone_dict: 
            phone_dict[receiveCallPhone] += int(durationCall)
        else:
            phone_dict[receiveCallPhone] = int(durationCall)
        
    longest_duration = dict(phone="0", duration=0)
    for key, value in phone_dict.items():
        if longest_duration['duration'] < value:
            longest_duration['phone'] = key
            longest_duration['duration'] = value
    return longest_duration

longest_duration_call = getLongestDurationCall()
print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(longest_duration_call['phone'], longest_duration_call['duration']))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

