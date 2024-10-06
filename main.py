from db import *
from gpt import Gpt
import json


sqlOnlyRequest = "Give me a MySQL statement that answers the question. Only respond with MySQL syntax, and don't explain any errors."

strategies = {
    "zero_shot": sqlOnlyRequest,
    "single_domain_double_shot": "Which customer deposited the most money at one time?" +
    "\nSELECT u.Name\nFROM Transaction t\nJOIN Account a ON t.AccountID = a.AccountID\nJOIN User u ON a.UserID = u.UserID"+
    "\nWHERE t.Type = 'Deposit'\nORDER BY t.Amount DESC\nLIMIT 1;\n" + sqlOnlyRequest
}

questions = [
    "Which two customers had the largest transaction?",
    "Who has the lowest account balance?",
    "Which user has the most transactions of every type?",
    "Which user withdrew the most money overall?",
    "Which bank location and name has the most users?",
    "Which bank has the most transactions?",
    "Who deposited the most money into their account overall?",
    "Are there any customers who chose not to add an email to their account?"
]


def cleanSql(sql):
        startmarker = "```sql"
        endmarker = "```"
        if startmarker in sql:
            sql = sql.split(startmarker)[1]
        if endmarker in sql:
            sql = sql.split(endmarker)[0]
        return sql


def main():
    db = Db()
    db.init_tables()
    print("Database initialized.")
    print("Running requested gpt queries...")
    gpt = Gpt()
    for strategy in strategies:
        responses = {"strategy": strategy, "prompt_prefix": strategies[strategy]}
        results = []
        for question in questions:
            error = "None"
            try:
                print("input to gpt: "+strategies[strategy]+ " "+ question)
                sql_res = gpt.ask_question(strategies[strategy]+ " "+ question)
                sql_res = cleanSql(sql_res)
                print(sql_res)
                raw_res = str(db.execute_statement(sql_res))
                print(raw_res)
                friendly_prompt = "I asked the question \"" + question + "\" and the result was \"" + raw_res +"\" Give me a translation of that result into spoken English in a friendly way, without giving additional suggestions."
                friendly_res = gpt.ask_question(friendly_prompt)
                print(friendly_res)
            except Exception as e:
                error = str(e)
                print(e)
            results.append({
                "question": question,
                "sql": sql_res,
                "raw_res": raw_res,
                "friendly_res": friendly_res,
                "error": error
            })
        responses["results"] = results

        with open(f"{strategy}_response.json", "w") as outfile:
            json.dump(responses, outfile, indent=2)


if __name__ == "__main__":
    main()