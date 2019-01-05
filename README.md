# sample-lambda-layers
Sample common functions working as AWS Lambda Layers

## Requirements
* Bash
* AWS CLI  
See [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).
* Permission for AWS Lambda with AWS CLI  
See [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

## Register common functions with AWS Lambda Layers
1. Select a language of AWS Lambda runtime
* [python](python)

2. Go to any function directory you like such as [python/slack](python/slack)
```bash
cd python/slack
```

3. Run "register_lambda_layer" script with layer name
```bash
../bin/register_lambda_layer slack
```
