#!/bin/bash
#
# Title:post_test.sh
#
curl -v -H "Content-Type:application/json"  -d '{"operator":"mul", "operand1":"3.3", "operand2":"5.5"}' https://subkhcpd2j.execute-api.us-west-2.amazonaws.com/test/calc
#
