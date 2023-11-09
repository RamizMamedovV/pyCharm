from datetime import datetime

#                   example 3
# print(dir(datetime))
# list_dir = dir(datetime)
# for i in list_dir:
#     print(i)


#                   example1
date_time = datetime.now()
date_time1 = datetime.now() - date_time
format_time = date_time.strftime("%y.%m.%d %H:%M:%S")
print(type(format_time))
print(date_time.strftime("%y.%m.%d %H:%M:%S"))
print(date_time1)


#                   example2

# timestamp = 2538897322
# # timestamp = 1528797322
# date_time = datetime.fromtimestamp(timestamp)
#
# print("Date time object:", date_time)
#
# d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
# print("Output 2:", d)
#
# d = date_time.strftime("%d %b, %Y")
# print("Output 3:", d)
#
# d = date_time.strftime("%d %B, %Y")
# print("Output 4:", d)
#
# d = date_time.strftime("%I%p")
# print("Output 5:", d)
