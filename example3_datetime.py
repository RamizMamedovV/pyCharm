from datetime import datetime as date
import time

#                   example 10
import datetime
import pytz

#                   example 10
time_now = datetime.datetime.now(pytz.utc).strftime("%y %m %d %H:%M") # мировое время
print(time_now)  # 2023-11-09 15:00:59.248522+00:00
print(date.now()) # 2023-11-09 18:00:59.248522

#                            преобразование из мирового в местное

# Предположим, что `time_now` - это строка в формате "yy mm dd HH:MM"
time_now = "22 11 10 15:30"

# Распарсим строку и создадим объект datetime
parsed_time = date.strptime(time_now, "%y %m %d %H:%M")

# Укажем, что `parsed_time` является временем в UTC
parsed_time_utc = pytz.utc.localize(parsed_time)

# Затем преобразуем время из UTC в местное время
local_time = parsed_time_utc.astimezone(pytz.timezone('Europe/Moscow'))

print(local_time)


#                   example 9
# d1 = date.now()
# print(f"d1 = {d1}")
# time.sleep(5)
# d2 = date.now()
# print(f"d2 = {d2}")
# # print(max(d1, d2))
# list_time = [d1, d2, d1]
# print(list_time)
#
# list_time.sort()
# list_time.sort(reverse=True)
# print(list_time)


# def custom_key(people):
#     return people[1]  # second parameter denotes the age
#
#
# persons = [['Alice', 26, 'F'], ['Trudy', 25, 'M'], ['Bob', 25, 'M'], ['Alexa', 22, 'F']]
# print(f'Before sorting: {persons}')
# persons.sort(key=custom_key)
# print(f'After sorting: {persons}')

# if d2 > d1:
#     print("ok")
# else:
#     print("no")

#                   example 8
import time

# for i in range(5):
#     print(i)
#     time.sleep(1)

# seconds = time.time()
# print(seconds)              # 1_699_540_259.1261108
# print(time.ctime(seconds))  # Thu Nov  9 17:30:20 2023 today!!
# print(time.asctime())       # Thu Nov  9 17:33:52 2023 today!!
# print(time.localtime(time.time())) # time.struct_time(tm_year=2023, tm_mon=11,
#                                     # tm_mday=9, tm_hour=17,
#                                     # tm_min=36, tm_sec=45, tm_wday=3,
#                                     # tm_yday=313, tm_isdst=0)
# print(time.localtime(time.time()).tm_mday) # 9

# print(time.gmtime(time.time())) # аналогично time.struct_time(tm_year=2023,....

# print(time.strftime('%D, %M, %Y')) # 11/09/23, 46, 2023
# print(time.strftime('%d, %m, %Y')) # 09, 11, 2023

# str_time = '11 JUNE, 2020'
# print(time.strptime(str_time, "%d %B, %Y")) # time.struct_time(tm_year=2020,.....

#                   example 7
# import datetime
# sum_time = datetime.timedelta(days=5, weeks=2, hours=2, milliseconds=11, microseconds=12)
# print(sum_time) # 19 days, 2:00:00.011012
#
# minus_time = date.now() - datetime.timedelta(days= 5)
# print(minus_time) # 2023-11-04 17:12:14.910094


#                   example 6
#  преобразуем дату в строку
# log_str = date.now().strftime('%d.%m.%Y %H:%M:%S')
# print(log_str)
# #  преобразуем из строки в дату
# print_log = (date.now().strptime(log_str, '%d.%m.%Y %H:%M:%S'))
# print(print_log)


#                   example 5
# date_now = date.now()
# date_now1 = date.now()
# date_now_str = date_now.strftime("%d.%m.%y %H:%M:%S") # 09.11.23 11:58:40
# date_now_str1 = date_now.strftime("%d.%m.%y %H:%M:%S") # 09.11.23 11:59:00
# count = 2
# num = ''
# format_str = []
# for i in date_now_str:
#     if i.isdigit():
#         num += i
#         count += 1
#         if count %2 == 0:
#             format_str.append(num) # ['09', '11', '23', '15', '22', '16']
#             count = 2
#             num = ''
#
# print(format_str)
# data_new_str = (','.join(format_str))
# print(data_new_str)
# data_new = date(2023,11,23)

#                   example 4
# t1 = date(year=2018, month=7, day=12)
# t2 = date(year=2017, month=12, day=23)
# t3 = t1 - t2
# print("t3 =", t3)
# t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
# t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
# t6 = t4 - t5
# print("t6 =", t6)
# print("type of t3 =", type(t3))
# print("type of t6 =", type(t6))

#                   example 3
# print(dir(datetime))
# list_dir = dir(datetime)
# for i in list_dir:
#     print(i)


#                   example1
# date_time = datetime.now()
# date_time1 = datetime.now() - date_time
# format_time = date_time.strftime("%y.%m.%d %H:%M:%S")
# print(type(format_time))
# print(date_time.strftime("%y.%m.%d %H:%M:%S"))
# print(date_time1)


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
