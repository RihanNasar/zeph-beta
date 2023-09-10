
import discord
import os
import google.generativeai as palm
from dotenv import load_dotenv
from persona import persona
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv()


def main():
    palm.configure(api_key=os.getenv('BARD_APIKEY'))
    models = [m for m in palm.list_models(
    ) if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    async def get_reply(content):
        prompt = persona(content)
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0,
            max_output_tokens=800,
        )

        if completion.result:
            print(completion)
            return completion.result
        else:
            print(completion)
            return "ask me properly or ask me later fellow struggler"

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if not message.content.strip():
            return
        # reply = get_reply(message.content)

        reply = await get_reply(message.content)
        print(reply)
        await message.channel.send(reply)

    client.run(os.getenv('TOKEN'))


if __name__ == "__main__":
    main()
