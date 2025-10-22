from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Pet gallery data: image filenames must match those in the images/ folder
gallery = [
    {"name": "Batman", "species": "Human", "image": "batman.jpg"},
<<<<<<< HEAD
    {"name": "Robin", "species": "Human", "image": "robin.jpg"}
=======
    {"name": "Robin", "species": "Human", "image": "robin.jpg"},
    {"name": "Spiderman", "species": "Human", "image": "spiderman.jpg"}
    {"name": "Sperman", "species": "Kryptonian", "image": "superman.jpg"}
>>>>>>> fd17f9508fff7ae89222e81b40e5d783a233835f
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
