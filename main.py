app = Flask(name)

@app.route('/alice', methods = ['POST'])
def resp():
    text = request.json.get('request', {}).get('command')
    response_text = f'Вы сказали {text}'
    response = {
        'response': {
            'text': response_text,
            'end_session': False,
            'suggests': ['йоу']
        },
        'version': '1.0'
    }
    return response
app.run('0.0.0.0', port = 5000, debug = True)
