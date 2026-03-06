import boto3
import json
from ai21_tokenizer import Tokenizer # Requires your Hugging Face access to be active

# 1. Initialize Bedrock
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")
modelId = "anthropic.claude-3-haiku-20240307-v1:0"

# 2. Get the Response from Bedrock
text = "This is a long string that goes to a new line"
body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 100,
    "messages": [{"role": "user", "content": [{"type": "text", "text": text}]}]
})

response = bedrock_runtime.invoke_model(body=body, modelId=modelId)
response_body = json.loads(response.get("body").read())

# 3. Extract output and the official Bedrock count
output_text = response_body.get("content")[0].get("text")
bedrock_input_count = response_body.get("usage", {}).get("input_tokens")
bedrock_output_count = response_body.get("usage", {}).get("output_tokens")

# 4. Use Local Tokenizer to see the actual tokenized strings of the OUTPUT
# (Ensure you have run 'huggingface-cli login' first)
tokenizer = Tokenizer.get_tokenizer()
encoded_output = tokenizer.encode(output_text)
tokens_list = tokenizer.convert_ids_to_tokens(encoded_output)

print(f"Response Body: {output_text}")
print("--- Token Analysis ---")
print(f"Tokenized Output List: {tokens_list}")
print(f"Local Tokenizer Count: {len(encoded_output)}")
print(f"Official Bedrock Output Count: {bedrock_output_count}")