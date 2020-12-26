import requests
import json

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "> " + json_data[0]['q'] + "\n> - " + json_data[0]['a']
    return quote

def calculate(n1: str, operator: str, n2: str):
    if n1 == 'x' or n2 == 'x' or operator == 'x':
        print("Missing arguments")
    try:
        ### Variables

        result = 0
        num1 = int(n1)
        num2 = int(n2)
        
        ### Operations

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        else:
            return "Invalid operation"
        return result
    except:
        return "Invalid operation"