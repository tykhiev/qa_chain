from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get('OPENAI_API_KEY')
modelGPT = "gpt-3.5-turbo"


@app.route('/gpt', methods=['POST'])
def gpt():
    prompt = request.json['prompt']
    response = openai.ChatCompletion.create(
        model=modelGPT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,)

    res = "ChatGPT: " + response.choices[0]["message"]['content']
    print(res)
    return jsonify(res)


@app.route('/dalle', methods=['POST'])
def dalle():
    prompt = request.json['prompt']
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024")

    image_url = response['data'][0]['url']
    print(image_url)
    return jsonify(image_url)


if __name__ == '__main__':
    app.run()
