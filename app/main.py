from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Pet gallery data: image filenames must match those in the images/ folder
gallery = [
    {"name": "Batman", "species": "Human", "image": "batman.jpg"},
    {"name": "Robin", "species": "Human", "image": "robin.jpg"}
]

@app.route('/')
def show_gallery():
    return render_template('gallery.html', gallery=gallery)

@app.route('/images/<filename>')
def image(filename):
    # This serves files from the images/ folder at the repo root
    return send_from_directory('../images', filename)

if __name__ == '__main__':
    app.run(debug=True)