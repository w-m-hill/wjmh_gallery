from flask import Blueprint, render_template
import os

main = Blueprint('main', __name__)

@main.route('/gallery/')
def gallery():
    base_dir = os.path.join(os.path.dirname(__file__), 'static', 'photos')
    gallery_structure = {}
    
    for root, dirs, files in os.walk(base_dir):
        # Filter out directories that start with '.'
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # Get the relative path of the current directory
        category = os.path.relpath(root, base_dir)
        
        # Filter and process files
        filtered_files = []
        for file in files:
            if not file.startswith('.'):  # Ignore files starting with '.'
                file_base = os.path.splitext(file)[0]  # Get file name without extension
                filtered_files.append((file, file_base))  # Append as a tuple (file, caption)
        
        if filtered_files:
            gallery_structure[category] = filtered_files
    
    return render_template('gallery.html', gallery=gallery_structure)
