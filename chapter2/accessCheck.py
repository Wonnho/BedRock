import boto3

# Ensure the region matches where you did the setup
client = boto3.client("bedrock", region_name="us-east-1")

response = client.list_foundation_models(byProvider='anthropic')

print("Your Authorized Anthropic Models:")
for model in response['modelSummaries']:
    print(f"- {model['modelId']}")
