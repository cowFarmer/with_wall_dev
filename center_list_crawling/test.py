import json
json_file_path = './test.json'
json_data = {}
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    
for i in range(2, 9):
    print(i)

print(json_data)
json_data['climing_list'] = []

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


# for i in range(len(json_list)):
#     json_data['climing_list'].append({json_list[i]: var_list[i]})

store_name = '100'
naver_category = '100'
address = '100'
naver_map_url = '100'
main_img_url = '100'
price_list = '100'
open_time = '100'
level = '100'
change_time = '100'

climing_info = {'store_name': store_name, 'naver_category': naver_category, 'address': address, 'naver_map_url': naver_map_url, 'main_img_url': main_img_url, 'price_list': price_list, 'open_time': open_time, 'level': level, 'change_time': change_time}
climing_info2 = {'store_name': '123', 'naver_category': 'naver_category', 'address': 'address', 'naver_map_url': 'naver_map_url', 'main_img_url': 'main_img_url', 'price_list': 'price_list', 'open_time': open_time, 'level': level, 'change_time': change_time}

json_data['climing_list'].append(climing_info)
json_data['climing_list'].append(climing_info2)

with open('test.json', 'w') as f:
    json.dump(json_data, f, indent=4)