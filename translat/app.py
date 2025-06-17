from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate_text():
    translation = ""

    if request.method == 'POST':
        text = request.form['text']
        target_lang = request.form['target_lang']

        try:
            # Translate using deep-translator (Google Translate API)
            translation = GoogleTranslator(source='auto', target=target_lang).translate(text)

        except Exception as e:
            translation = f"Error: {e}"

    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
