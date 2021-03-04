
def main():

	def avg(data):
		total = 0
		number = data["count"]

		for i in range(number):
			sum = data["employees"][i]["salary"]
			total += sum

		print(total/number)

	avg({"count":3, "employees":[{"name":"John","salary":30000 },{"name":"Bob","salary":60000 },{"name":"Jenny","salary":50000 }]})


if __name__ == '__main__':
	main()