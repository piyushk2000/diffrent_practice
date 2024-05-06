from openai import OpenAI



client = OpenAI(
  api_key= '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'
)

def generate_short_story(prompt):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a short story writer."},
      {"role": "user", "content": prompt}
    ]
  )

  answer = completion

  print(answer.choices[0].message.content)

# Get user input for the story prompt
user_prompt = input("Enter a story prompt: ")

generate_short_story(user_prompt)
