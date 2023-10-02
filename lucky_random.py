import requests
class Client():
	def __init__(self):
		self.api="https://lucky-random.ru/modules"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def random_nummer(self,unique:int=1,count:int=1):
		return requests.get(f"{self.api}/nrand/api.php?count={count}&min=1&max=1000&unique={unique}",headers=self.headers).text
	def random_nummer_2(self):
		return requests.get(f"{self.api}/nrand/api2.php?count={count}&min=1&max=1000&unique={unique}",headers=self.headers).text
	def random_steps(self,step:int=1):
		return requests.get(f"{self.api}/nrandsteps/api.php?step={step}&max=100",headers=self.headers).text
	def random_fact(self):
		return requests.get(f"{self.api}/frand/api.php",headers=self.headers).text
	def random_wisdom(self):
		return requests.get(f"{self.api}/mrand/api.php",headers=self.headers).text