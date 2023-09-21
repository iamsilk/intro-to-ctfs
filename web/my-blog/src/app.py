from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Get the 'file' parameter from the query string
    file_param = request.args.get('file', 'files/index.html')

    try:
        # Open and read the content of the file
        with open(file_param, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        return "File not found"
    
    # Render the template with the file content
    return render_template('file_template.html', file_content=file_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)