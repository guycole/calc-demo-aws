# calc-demo-aws
### AWS API Gateway and Lamba (python) demonstration.


4 function calculator web service (API Gateway) which invokes Lambda (python) to perform operation and return results.

http://guycole.blogspot.com/2016/04/aws-api-gateway-and-lamba-python.html

## Installation


*  Create S3 bucket to contain Lambda calculator function
  * For simplicity, S3 bucket should reside in a region (i.e. don't pick 'US Standard') 

*  Place calc.py into a zipfile and copy to S3 bucket from step 1
```
    zip lambda.zip calc.py
    aws s3 cp lambda.zip s3://lambda.braingang.net --region us-west-2
```

*  Use Cloud Formation to create IAM permissions and Lambda function
  * cf.template will prompt for bucket information (from step 1) and warn about IAM permissions
  * Output tab will contain ARN needed for API Gateway

*  Prepare swagger.json for API Gateway
```
    edit swagger.json

    update credentials (2 references) w/GateWayRoleArn from Cloud Formation outputs tab
    "credentials": "GateWayRoleArn", //original
    "credentials": "arn:aws:iam::123456789:role/calc-GateWayRole" //tweaked

    update URI (2 references) w/AWS Region and LambdaCalcArn from Cloud Formation outputs tab
    "uri": "arn:aws:apigateway:AwsRegion:lambda:path/2015-03-31/functions/LambdaCalcArn/invocations" //original
    "credentials": "arn:aws:lambda:us-west-2:123456789:function:CalcLambdaFunction" //tweaked

    save file
```
*  Upload swagger.json as API Gateway
*  Installation Complete

---

## Operation (from AWS console)
*  HTTP Get Test (press "Test" to continue)
![alt text](https://github.com/guycole/calc-demo-aws/blob/master/images/screenshot1.png "Screen Shot 1")

*  Insert values into text boxes, press "Test" and observe update
![alt text](https://github.com/guycole/calc-demo-aws/blob/master/images/screenshot2.png "Screen Shot 2")

* HTTP Post Test (press "Test" to continue)
![alt text](https://github.com/guycole/calc-demo-aws/blob/master/images/screenshot3.png "Screen Shot 3")

*  Insert values into text boxes, press "Test" and observe update
![alt text](https://github.com/guycole/calc-demo-aws/blob/master/images/screenshot4.png "Screen Shot 4")

---

## Operation (from curl)
*  Deploy CalcDemo API
![alt text](https://github.com/guycole/calc-demo-aws/blob/master/images/screenshot5.png "Screen Shot 5")

*  Exercise CalcDemo using curl(1)
```
get example (must update URL to match dployment)
curl -v 'https://subkhcpd2j.execute-api.us-west-2.amazonaws.com/test/calc/mul?operand1=5.5&operand2=3.3'

post example (must update URL to match dployment)
curl -v -H "Content-Type:application/json"  -d '{"operator":"mul", "operand1":"3.3", "operand2":"5.5"}' https://subkhcpd2j.execute-api.us-west-2.amazonaws.com/test/calc
```
