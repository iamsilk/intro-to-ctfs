from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/show_file_content', methods=['GET'])
def show_file_content():
    # Get the 'file' parameter from the query string
    file_param = request.args.get('file')

    # Assuming you have a directory where these files are stored
    file_directory = 'files/'  # Update with your file directory path

    try:
        # Open and read the content of the file
        with open(file_directory + file_param, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        return "File not found"
    
    # Render the template with the file content
    return render_template('file_template.html', file_content=file_content)

if __name__ == '__main__':
    app.run(debug=True)