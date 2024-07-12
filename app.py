import io
import os
import base64
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import sqlite3
import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.static_folder = 'static'  # Set the static folder to 'static'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/videos'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}
app.config['DATABASE'] = 'instance/blog3.db'

DATABASE = app.config['DATABASE']

def logit(argvs):
    argv = argvs   
    log_file = "app_log.txt"  # Path to your log file
    timestamp = datetime.datetime.now().strftime("%A_%b-%d-%Y_%H-%M-%S")
    with open(log_file, "a") as log:
        log.write(f"{timestamp}: {argv}\n")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_video/<int:post_id>', methods=['POST'])
def upload_video(post_id):
    if 'videoFile' not in request.files:
        logit('No file part')
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['videoFile']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        logit(f"Filename: {filename}")
        # Update the database with the filename
        update_video_filename(post_id, filename)
        flash('Video uploaded successfully')
        return redirect(url_for('post', post_id=post_id))
    else:
        flash('Allowed file types are .mp4')
        return redirect(request.url)

def update_video_filename(post_id, filename):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE post SET video_filename = ? WHERE id = ?', (filename, post_id))
        conn.commit()

# Initialize SQLite database if not exists
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE,
                content TEXT NOT NULL,
                video_filename TEXT NULL,
                image BLOB
            )
        ''')
        conn.commit()

# Function to fetch a single post by ID
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    if request.method == 'POST':
        return upload_video(post_id)

    post = get_post(post_id)
    if not post:
        flash('Post not found')
        return redirect(url_for('home'))

    image_data = get_image_data(post_id)
    video_filename = post[4] if post[4] else None  # Adjust index based on your database schema

    return render_template('post.html', post=post, image_data=image_data, video_filename=video_filename)


def get_post(post_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, content, image, video_filename FROM post WHERE id = ? ORDER BY id DESC', (post_id,))
        post = cursor.fetchone()
    return post
# Function to fetch all posts
def get_posts(limit=None):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        if limit:
            cursor.execute('SELECT id, title, content, image, video_filename FROM post ORDER BY id DESC LIMIT ?', (limit,))
        else:
            cursor.execute('SELECT id, title, content, image, video_filename FROM post ORDER BY id DESC')
        posts = cursor.fetchall()
    return posts

# Function to fetch image data
def get_image(post_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT image FROM post WHERE id = ?', (post_id,))
        post = cursor.fetchone()
        if post and post[0]:
            return post[0]  # Return base64 encoded image data
        return None

@app.route('/')
def home():
    posts = get_posts(limit=6) 
    for post in posts:
        logit(post[3])# Limit to last 4 posts
    return render_template('home.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files['image'].read() if 'image' in request.files and request.files['image'].filename != '' else None
        if image:
            image = base64.b64encode(image).decode('utf-8')
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO post (title, content, image) VALUES (?, ?, ?)', (title, content, image))
            conn.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('new_post.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image_data = get_image(post_id)  # Get the current image data
        if 'image' in request.files and request.files['image'].filename != '':
            image = request.files['image'].read()
            image_data = base64.b64encode(image).decode('utf-8')  # Update with new image data
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE post SET title = ?, content = ?, image = ? WHERE id = ?', (title, content, image_data, post_id))
            conn.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('post', post_id=post_id))
    return render_template('edit_post.html', post=post)

@app.route('/contents')
def contents():
    posts = get_posts()
    contents_data = []
    for post in posts:
        excerpt = post[2][:300] + '...' if len(post[2]) > 300 else post[2]  # Assuming content is in the third column (index 2)
        contents_data.append({
            'id': post[0],
            'title': post[1],
            'excerpt': excerpt
        })
    return render_template('contents.html', contents_data=contents_data)

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM post WHERE id = ?', (post_id,))
        conn.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('home'))

def load_txt_files(directory):
    init_db()  # Initialize the SQLite database if not already created
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    title = os.path.splitext(filename)[0]
                    content = file.read()
                    cursor.execute('SELECT id FROM post WHERE title = ? ORDER BY id DESC', (title,))
                    existing_post = cursor.fetchone()
                    if not existing_post:
                        cursor.execute('INSERT INTO post (title, content) VALUES (?, ?)', (title, content))
                        conn.commit()
                        print(f'Added post: {title}')
                    else:
                        print(f'Skipped existing post: {title}')
    except sqlite3.Error as e:
        print(f'SQLite error: {e}')
    finally:
        conn.close()

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_terms = request.form['search_terms']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Define the search terms
        search_terms = search_terms.split(",")  # Split by comma to get individual search terms
        results = []
        
        # Construct the WHERE clause for the SQL query to filter rows based on all search terms
        where_conditions = []
        for term in search_terms:
            where_conditions.append(f"content LIKE ?")
        
        where_clause = " AND ".join(where_conditions)
        
        # Create a tuple of search terms with wildcard characters for the SQL query
        search_terms_tuple = tuple(f"%{term.strip()}%" for term in search_terms)
        
        # Execute the SELECT query with the constructed WHERE clause
        query = f"SELECT ROWID, title, content, image, video_filename FROM post WHERE {where_clause}"
        rows = cursor.execute(query, search_terms_tuple)
        
        for row in rows:
            results.append((row[0], row[1], row[2], row[3], row[4]))
        
        conn.close()
        return render_template('search.html', results=results)
    
    return render_template('search.html', results=[])


def get_image_data(post_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT image FROM post WHERE id = ?', (post_id,))
        post = cursor.fetchone()
        if post and post[0]:
            return base64.b64decode(post[0])  # Decode base64 to binary
        else:
            return None

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    if request.method == 'POST':
        if 'videoFile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['videoFile']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE post SET video_filename = ? WHERE id = ?', (filename, post_id))
                conn.commit()
                flash('Video uploaded successfully')

            return redirect(url_for('show_post', post_id=post_id))

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, content, image, video_filename FROM post WHERE id = ? ORDER BY id DESC', (post_id,))
        post = cursor.fetchone()
        if not post:
            flash('Post not found')
            return redirect(url_for('home'))
        
        image_data = base64.b64decode(post[3]) if post[3] else None
        video_filename = post[4] if post[4] else None
    logit(f"video_filename: {video_filename}")
    return render_template('post.html', post=post, image_data=image_data, video_filename=video_filename)

@app.route('/image/<int:post_id>')
def view_image(post_id):
    image_data = get_image_data(post_id)
    if image_data:
        return send_file(io.BytesIO(image_data), mimetype='image/jpeg')
    else:
        return "No image found", 404
    
TEXT_FILES_DIR = "static/TEXT"
# Check if the text files directory exists, if not, create it
if not os.path.exists(TEXT_FILES_DIR):
    os.makedirs(TEXT_FILES_DIR)    
    
    
# Index route to display existing text files and create new ones
@app.route("/edit_text", methods=["GET", "POST"])
def edit_text():
    if request.method == "POST":
        filename = request.form["filename"]
        text = request.form["text"]
        save_text_to_file(filename, text)
        return redirect(url_for("edit_text"))
    else:
        # Path to the file containing list of file paths
        files = os.listdir(TEXT_FILES_DIR)
        # Call the function to list files by creation time
        files = list_files_by_creation_time(files)
        files = sorted(files)
        return render_template("edit_text.html", files=files)
 # Route to edit a text file
@app.route("/edit/<filename>", methods=["GET", "POST"])
def edit(filename):
    if request.method == "POST":
        text = request.form["text"]
        save_text_to_file(filename, text)
        return redirect(url_for("index"))
    else:
        text = read_text_from_file(filename)
        return render_template("edit.html", filename=filename, text=text)
# Route to delete a text file
@app.route("/delete/<filename>")
def delete(filename):
    filepath = os.path.join(TEXT_FILES_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        logit(f"File deleted: {filename}")
    return redirect(url_for("index"))
def list_files_by_creation_time(file_paths):
    """
    List files by their creation time, oldest first.
    
    Args:
    file_paths (list): List of file paths.
    
    Returns:
    list: List of file paths sorted by creation time.
    """
    # Log the start of the function
    def list_files_by_creation_time(file_paths):
    """
    List files by their creation time, oldest first.
    
    Args:
    file_paths (list): List of file paths.
    
    Returns:
    list: List of file paths sorted by creation time.
    """
    # Log the start of the function
    logit('Listing files by creation time...')
    
    # Create a dictionary to store file paths and their creation times
    file_creation_times = {}
    
    # Iterate through each file path
    for file_path in file_paths:
        # Get the creation time of the file
        try:
            creation_time = os.path.getctime(file_path)
            # Store the file path and its creation time in the dictionary
            file_creation_times[file_path] = creation_time
        except FileNotFoundError:
            # Log a warning if the file is not found
            logit(f'File not found: {file_path}')
    
    # Sort the dictionary by creation time
    sorted_files = sorted(file_creation_times.items(), key=lambda x: x[1])
    
    # Extract the file paths from the sorted list
    sorted_file_paths = [file_path for file_path, _ in sorted_files]
    
    # Log the end of the function
    def list_files_by_creation_time(file_paths):
    """
    List files by their creation time, oldest first.
    
    Args:
    file_paths (list): List of file paths.
    
    Returns:
    list: List of file paths sorted by creation time.
    """
    # Log the start of the function
    def list_files_by_creation_time(file_paths):
    """
    List files by their creation time, oldest first.
    
    Args:
    file_paths (list): List of file paths.
    
    Returns:
    list: List of file paths sorted by creation time.
    """
    # Log the start of the function
    logit('Listing files by creation time...')
    
    # Create a dictionary to store file paths and their creation times
    file_creation_times = {}
    
    # Iterate through each file path
    for file_path in file_paths:
        # Get the creation time of the file
        try:
            creation_time = os.path.getctime(file_path)
            # Store the file path and its creation time in the dictionary
            file_creation_times[file_path] = creation_time
        except FileNotFoundError:
            # Log a warning if the file is not found
            logging.warning(f'File not found: {file_path}')
    
    # Sort the dictionary by creation time
    sorted_files = sorted(file_creation_times.items(), key=lambda x: x[1])
    
    # Extract the file paths from the sorted list
    sorted_file_paths = [file_path for file_path, _ in sorted_files]
    
    # Log the end of the function
    logit('File listing complete.')
    
    # Return the sorted file paths
    return sorted_file_paths
('Listing files by creation time...')
    
    # Create a dictionary to store file paths and their creation times
    file_creation_times = {}
    
    # Iterate through each file path
    for file_path in file_paths:
        # Get the creation time of the file
        try:
            creation_time = os.path.getctime(file_path)
            # Store the file path and its creation time in the dictionary
            file_creation_times[file_path] = creation_time
        except FileNotFoundError:
            # Log a warning if the file is not found
            logging.warning(f'File not found: {file_path}')
    
    # Sort the dictionary by creation time
    sorted_files = sorted(file_creation_times.items(), key=lambda x: x[1])
    
    # Extract the file paths from the sorted list
    sorted_file_paths = [file_path for file_path, _ in sorted_files]
    
    # Log the end of the function
    logit('File listing complete.')
    
    # Return the sorted file paths
    return sorted_file_paths
('File listing complete.')
    
    # Return the sorted file paths
    return sorted_file_paths
('Listing files by creation time...')
    
    # Create a dictionary to store file paths and their creation times
    file_creation_times = {}
    
    # Iterate through each file path
    for file_path in file_paths:
        # Get the creation time of the file
        try:
            creation_time = os.path.getctime(file_path)
            # Store the file path and its creation time in the dictionary
            file_creation_times[file_path] = creation_time
        except FileNotFoundError:
            # Log a warning if the file is not found
            logit(f'File not found: {file_path}')
    
    # Sort the dictionary by creation time
    sorted_files = sorted(file_creation_times.items(), key=lambda x: x[1])
    
    # Extract the file paths from the sorted list
    sorted_file_paths = [file_path for file_path, _ in sorted_files]
    
    # Log the end of the function
    logit('File listing complete.')
    
    # Return the sorted file paths
    return sorted_file_paths


if __name__ == '__main__':
    directory = 'static/TEXT'
    load_txt_files(directory)
    app.run(debug=True,port=5100)
