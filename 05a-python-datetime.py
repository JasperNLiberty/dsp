from datetime import datetime

# 1
date_start = '01-02-2013'
date_stop = '07-28-2015'

#'Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'
date_object1 = datetime.strptime(date_start, '%m-%d-%Y')
date_object2 = datetime.strptime(date_stop, '%m-%d-%Y')

date_passed = date_object2 - date_object1
print(date_passed)


# 2
date_start = '12312013'
date_stop = '05282015'

date_object1 = datetime.strptime(date_start, '%m%d%Y')
date_object2 = datetime.strptime(date_stop, '%m%d%Y')

date_passed = date_object2 - date_object1
print(date_passed)

# 3
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

date_object1 = datetime.strptime(date_start, '%d-%b-%Y')
date_object2 = datetime.strptime(date_stop, '%d-%b-%Y')

date_passed = date_object2 - date_object1
print(date_passed)
