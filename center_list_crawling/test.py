json_data1 = {}
json_data2 = {}

json_list = ['store_name', 'naver_category', 'address', 'naver_map_url', 'main_img_url', 'price_list', 'open_time', 'level', 'change_time']

store_name = 'test1'
naver_category = 'test2'
address = 'test3'
naver_map_url = 'test4'
main_img_url = 'test5'
price_list = 'test6'
open_time = 'test7'
level = 'test8'
change_time = 'test9'

var_list = [store_name, naver_category, address, naver_map_url, main_img_url, price_list, open_time, level, change_time]


for i in range(len(json_list)):
    json_data1.update({json_list[i]: var_list[i]})
    json_data2.update({json_list[i]: ''})
print(json_data1)
print(json_data2)