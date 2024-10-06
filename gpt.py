from openai import OpenAI
import config
import sql_init

class Gpt:
    def __init__(self):
        self.client = OpenAI(api_key=config.gpt_key)
        self.database = sql_init.create_tables

    def ask_question(self, question: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                    {"role": "system",
                     "content": f"You are a helpful assistant. Give answers based on this SQL database: {self.database}"},
                    {"role": "user", "content": question}
                ],
                stream=True,
        )
        responseList = []
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                responseList.append(chunk.choices[0].delta.content)
        result = "".join(responseList)
        return result