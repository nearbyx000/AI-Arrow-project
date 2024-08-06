from g4f.client import Client

client = Client()

while True:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input()}],
    )
    print(response.choices[0].message.content)
