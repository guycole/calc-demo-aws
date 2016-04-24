from __future__ import print_function

import json

print('Loading function')


def lambda_handler(event, context):
#    print("Received event: " + json.dumps(event, indent=2))

    operator = 'bogus'
    operand1 = "0"
    operand2 = "0"
    result = 0

    if 'body' in event:
        try:
            operator = event['body']['operator']
            operand1 = event['body']['operand1']
            operand2 = event['body']['operand2']
        except KeyError as keyError:
            print('key error noted')
    else:
        try:
            operator = event['operator']
            operand1 = event['operand1']
            operand2 = event['operand2']
        except KeyError as keyError:
            print('key error noted')

    print('-o-o-o-o-o-o-o-')
    print(operator) 
    print(operand1)
    print(operand2)
    print('-o-o-o-o-o-o-o-')

    if operator == 'add':
        result = float(operand1) + float(operand2)
    elif operator == 'sub':
        result = float(operand1) - float(operand2)
    elif operator == 'mul':
        result = float(operand1) * float(operand2)
    elif operator == 'div':
        result = float(operand1) / float(operand2)

    output = "{'operator':%s, 'operand1':%s, 'operand2':%s, 'result':%f}" % (operator, operand1, operand2, result)
    return output
