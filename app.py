from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home page
@app.route('/')
def index():
    return render_template('index.html')

# Dynamically serve pages based on the option clicked
@app.route('/load/<page>')
def load_page(page):
    # You can create a mapping here for each page's content
    pages = {
        "discover-pcs": "Discover PCs content goes here!",
        "buy-pc-parts": "Buy PC Parts content goes here!",
        "prebuilt-pcs": "Prebuilt PCs content goes here!",
        "buy-wallpapers": "Buy Wallpapers content goes here!",
        "buy-programs": "Buy Programs content goes here!"
    }

    # Return the content for the requested page
    content = pages.get(page, "Page not found")
    return content

if __name__ == '__main__':
    app.run(debug=True)
