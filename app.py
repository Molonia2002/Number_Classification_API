from flask import Flask, request, jsonify
from flask_cors import CORS
import requests 

app = Flask(__name__) 
CORS(app) #Enable CORS

def is_prime(n): 
	if n < 2: 
		return False 
	for i in range(2, int(n ** 0.5) + 1): 
		if n % i == 0: 
			return False 
	return True 

def is_perfect(n): 
	return sum(i for i in range(1, n) if n % i == 0) == n 

def is_armstrong(n): 
	digits = [int(d) for d in str(n)]
	power = len(digits) 
	return sum(d ** power for d in digits) == n 

def classify_number(n): 
	properties = []
	if is_armstrong(n):
		properties.append("armstrong")
	properties.append("odd" if n % 2 else "even") 

	return {
		"number": n, 
		"is_prime": is_prime(n), 
		"is_perfect": is_perfect(n),
		"properties": properties,
		"digit_sum": sum(int(d) for d in str(n)), 
	}

@app.route('/api/classify-number', methods=['GET'])
def classify():
	num = request.args.get('number')

	if not num or not num.isdigit():
		return jsonify({"number": num, "error": True}), 400

	num = int(num)
	data = classify_number(num) 

	try: 
		response = requests.get(f"http://numberapi.com/{num}/math")
		data["fun_fact"] = response.text
	except requests.exceptions.RequestException: 
		data["fun_fact"] = "No fun fact available"

	return jsonify(data)

if __name__== '__main__': 
	app.run(debug=True)
