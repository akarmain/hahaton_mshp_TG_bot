from openai import OpenAI
from bot.misc import TgKeys




def chatGPT(messages):
    """
    Функция для работы с AI
    """
    client = OpenAI(
        api_key=TgKeys.OPENAI_API_KEY,
        base_url="https://api.proxyapi.ru/openai/v1"
    )
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
        # model="gpt-4-turbo", messages=messages, max_tokens=1000
    )
    return chat_completion






if __name__ == '__main__':
    question_answers = """
1+1
    """

    print(chatGPT([{"role": "system", "content": question_answers}]).choices[0].message.content)
