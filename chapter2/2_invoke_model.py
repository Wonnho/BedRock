import json
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages":
        [
            {
                "role": "user",
                "content": "what is DNR?"
            }
        ]
    }
)


# define model
# modelId = "us.anthropic.claude-3-5-sonnet-20240620-v1:0"
modelId = "anthropic.claude-3-haiku-20240307-v1:0"


# define HTTP
accept = "application/json"
contentType = "application/json"

# response
response = bedrock.invoke_model(
    body=body, modelId=modelId, accept=accept, contentType=contentType)
response_body = json.loads(response.get("body").read())

answer = response_body["content"][0]["text"]
print(answer)
