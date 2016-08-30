import re
import csv

with open('/users/sausageparty/dsp/python/faculty.csv') as f:
    data = f.read()

search_email = re.findall('[\w|\.]+@[\w|\.]+', data)
print(search_email)

with open('/users/sausageparty/dsp/python/emails.csv', 'wb') as fp:
    wr = csv.writer(fp)
    for se in search_email:
        wr.writerow([se,])
