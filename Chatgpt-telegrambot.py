import telebot
from openai import OpenAI
from pprint import pprint


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
)


BOT_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
BOT = telebot.TeleBot(BOT_TOKEN)
chat_log = []

def send_to_ai(user_message):
    print("message was sent")
    chat_log.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        messages=chat_log,
        model="gpt-3.5-turbo"

    )
    return response.choices[0].message.content
    
    

@BOT.message_handler(commands=['start'])
def start_command(message):
    BOT.reply_to(message, "This is a translator and AI in one. You can write in any language, and I will return output from OpenAI in your language.")

@BOT.message_handler(func=lambda message: True)
def handle_text(message):
    user_reply = message.text
    ai_response = send_to_ai(user_reply)
    BOT.reply_to(message, f"ChatGPT: {ai_response}")

BOT.polling()
