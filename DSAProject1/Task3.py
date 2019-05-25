"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def findAreaCodes():
    code_set = set()   
    bangaloreCode = "(080)"
    callToBangalore = 0
    bangaloreCalls = 0
    for call in calls:
        makingCall = call[0]
        if bangaloreCode in makingCall:
            bangaloreCalls += 1
            receivingCall = call[1]
            if bangaloreCode in receivingCall:
                callToBangalore += 1
            code = re.search('\(*([0-9]{1,4})[0-9]?\)* *([0-9]+)', receivingCall).group(1)
            code_set.add(code)
    
    percentage = (callToBangalore * 100) / bangaloreCalls
    sort_codes = sorted(code_set)
    return sort_codes, percentage

codes, percentage = findAreaCodes()
print("The numbers called by people in Bangalore have codes:\n{}".format('\n'.join(codes)))
print("{:0.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(percentage))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
