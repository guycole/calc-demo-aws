from __future__ import print_function

import json

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print('-x-x-x-x-x-x-x-')
#    print(vars(context))
#    print('-o-o-o-o-o-o-o-')

    operator = ""
    operand1 = ""
    operand2 = ""

    if 'params' in event:
        temp = event['params']
        try:
            operator = temp['path']['operator']
            operand1 = temp['querystring']['operand1']
            operand2 = temp['querystring']['operand2']
        except KeyError as keyError:
            print('key error noted')

    print('-o-o-o-o-o-o-o-')
    print(operator) 
    print(operand1)
    print(operand2)
    print('-o-o-o-o-o-o-o-')

#    operator = 'operator'
#    operand1 = 'operand1'
#    operand2 = 'operand2'
    result = 'result'

    output = "{'operator':%s, 'operand1':%s, 'operand2':%s, 'result':%s}" % (operator, operand1, operand2, result)
    return output
