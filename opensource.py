import random

""" 컴퓨터와 가위바위보를 하는 프로그램 입니다. """

def main():
	""" 컴퓨터가 낼 가위바위보를 랜덤으로 선택합니다."""
	computerturn = random.randrange(3) + 1
	
	""" 자신이 낼 가위바위보를 선택합니다."""
	for i in range(10):
		myturn = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
		while not(myturn == 1 or myturn == 2 or myturn ==3):
			myturn = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
		
		""" 가위를 냈을 경우 """
		if(computerturn == 1):
			if(myturn == 1):
				print("컴퓨터가 낸 것은 가위입니다. -----> 비김~")
			elif(myturn == 2):
				print("컴퓨터가 낸 것은 가위입니다. -----> 사용자 승!")
			elif(myturn == 3):
				print("컴퓨터가 낸 것은 가위입니다. -----> 컴퓨터 승!")
		
		""" 바위를 냈을 경우"""
		elif(computerturn == 2):
			if(myturn == 1):
				print("컴퓨터가 낸 것은 바위입니다. -----> 컴퓨터 승!")
			elif(myturn == 2):
				print("컴퓨터가 낸 것은 바위입니다. -----> 비김~")
			elif(myturn == 3):
				print("컴퓨터가 낸 것은 바위입니다. -----> 사용자 승!")
		
		""" 보를 냈을 경우 """
		elif(computerturn == 3):
			if(myturn == 1):
				print("컴퓨터가 낸 것은 보입니다. -----> 사용자 승!")
			elif(myturn == 2):
				print("컴퓨터가 낸 것은 보입니다. -----> 컴퓨터 승!")
			elif(myturn == 3):
				print("컴퓨터가 낸 것은 보입니다. -----> 비김~")

main()