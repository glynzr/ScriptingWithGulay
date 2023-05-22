import base64

def decoder(text):
    message_bytes = base64.b64decode(text)
    message = message_bytes.decode('ascii')
    return message

base64_message = open("b64.txt", "rb").read()
result = base64_message

for i in range(50):
    result = decoder(result)

print(result)
