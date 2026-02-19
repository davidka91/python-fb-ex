from flask import Flask, request, render_template_string

app = Flask(__name__)

# A simple route that renders user input without proper sanitization
@app.route('/greet', methods=['GET'])
def greet():
    user_name = request.args.get('name', 'Guest')
    # Rendering user input directly without escaping
    return render_template_string(f"<h1>Hello, {user_name}!</h1>")

if __name__ == '__main__':
    app.run(debug=True)
