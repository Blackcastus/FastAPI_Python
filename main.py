from urllib import request, parse
from time import sleep
from random import randint
import json

def prepare_data(data1, data2):
	data = {
		"data1": data1,
		"data2": data2
	}
	params = json.dumps(data).encode()
	return params

# ess Output respone_data Chuoi du lieu nhan ve tu Server Thing speak lot 
def my_post(params):
# o Tạo Header trong giao thuc HTTP POST
	req = request.Request('http://35.221.87.87/update_post', method="POST") 
	req.add_header("accept", "application/json")
	req.add_header("Content-Type", "application/json")
	r = request.urlopen(req, data = params)
	respone_data = r.read()
	return respone_data

while True:
	data_random1 = randint(0,50) # Tạo các gia tri du lieu ngau nhien
	data_random2 = randint(0,50) # Tạo các gia tri du lieu ngau nhien

	params = prepare_data(data_random1, data_random2)
	print(params)

	print(my_post(params))
	
	sleep(30)