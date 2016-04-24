# calc-demo-aws
### AWS API Gateway and Lamba (python) demonstration.


4 function calculator web service (API Gateway) which invokes Lambda (python) to perform operation and return results.


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
*  Stub

---

## Operation (from curl)
*  Stub
