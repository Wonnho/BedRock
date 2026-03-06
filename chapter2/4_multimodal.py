import base64
import boto3
import json

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

with open("marriage.jpg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

# define prompt
prompt_config = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": "what kind of this image? explain it"
                }
            ],
        }
    ],
}

body = json.dumps(prompt_config)
modelId = "anthropic.claude-3-haiku-20240307-v1:0"
accept = "application/json"
contentType = "application/json"

response = bedrock_runtime.invoke_model(
    body=body, modelId=modelId,
    accept=accept,
    contentType=contentType
)

response_body = json.loads(response.get("body").read())
results = response_body.get("content")[0].get("text")
print(results)
