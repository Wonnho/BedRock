from ai21_tokenizer import Tokenizer
tokenizer=Tokenizer.get_tokenizer()
text="This is a long string that goes to a new line"

encoded_text=tokenizer.encode(text)

tokens=tokenizer.convert_ids_to_tokens(encoded_text)

print(tokens)
print('# of tokens:',len(encoded_text))