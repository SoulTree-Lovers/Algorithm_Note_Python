""" 
문제를 풀다 보면 문자열을 뒤집어야 하는 경우가 발생한다. 
아래와 같이 문자열 슬라이싱을 통한 뒤집기가 가능하다.
리스트에서도 적용 가능하나, 리스트는 reverse() 함수가 존재한다.
"""

string = "hello world"
print(string[::-1])

'''
    output: dlrow olleh
'''