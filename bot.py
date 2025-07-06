import os
import asyncio
from aiogram import Bot, Dispatcher, types
from openai import OpenAI

# Получаем ключи из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        user_text = message.text

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты умный помощник."},
                {"role": "user", "content": user_text}
            ]
        )
        reply_text = completion.choices[0].message.content
        await message.answer(reply_text)
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
