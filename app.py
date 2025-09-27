from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list of items to display
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# --- Routes ---

@app.route('/')
def home():
    """
    Homepage of the application.
    Displays a welcome message and a link to the items page.
    """
    return render_template('home.html')

@app.route('/about')
def about():
    """
    About page.
    Provides some information about the application.
    """
    return render_template('about.html')

@app.route('/items')
def list_items():
    """
    Displays a list of items.
    """
    return render_template('items.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    """
    Allows users to add a new item to the list.
    Handles both GET (display form) and POST (submit form) requests.
    """
    if request.method == 'POST':
        new_item = request.form['item_name']
        if new_item and new_item not in items: # Prevent adding empty or duplicate items
            items.append(new_item)
        return redirect(url_for('list_items'))
    return render_template('add_item.html')

@app.route('/item/<name>')
def view_item(name):
    """
    Displays details for a specific item.
    """
    item_found = None
    for item in items:
        if item.lower() == name.lower():
            item_found = item
            break
    if item_found:
        return render_template('view_item.html', item=item_found)
    return "Item not found!", 404

# --- Run the application ---
if __name__ == '__main__':
    app.run(debug=True)
