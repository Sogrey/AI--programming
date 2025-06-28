"""
Background Remover Web Application

A Flask-based web service for removing image backgrounds using Rembg.
Provides REST API endpoint for image processing and web interface for user interaction.
"""

from flask import Flask, render_template, request
from rembg import remove
from io import BytesIO
from PIL import Image
import base64
import logging

# Initialize Flask application
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    """Render the main page with image upload interface.
    
    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    """Handle image upload and background removal.
    
    Returns:
        dict: JSON response with processed image or error message
        int: HTTP status code
    """
    if 'file' not in request.files:
        logger.warning("No file uploaded in request")
        return {'error': 'No file uploaded'}, 400
    
    file = request.files['file']
    
    # Validate file type
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        logger.warning(f"Invalid file type: {file.filename}")
        return {'error': 'Invalid file type'}, 400
    
    try:
        # Read and validate image
        input_image = Image.open(file.stream)
        file_size = len(file.read())
        file.seek(0)  # Reset file pointer after reading
        logger.info(f"Processing image: {file.filename}, size: {file_size} bytes")
        
        # Process image - remove background
        output_image = remove(input_image)
        if not output_image:
            raise ValueError("Background removal failed")
        
        # Prepare response
        img_io = BytesIO()
        output_image.save(img_io, 'PNG', quality=95)
        img_io.seek(0)
        response_size = img_io.getbuffer().nbytes
        logger.info(f"Returning processed image, size: {response_size} bytes")
        
        # Convert to base64 for web display
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        return {
            'status': 'success',
            'image': f"data:image/png;base64,{img_base64}",
            'size': response_size
        }
        
    except Image.UnidentifiedImageError:
        logger.error("Invalid image file provided")
        return {'error': 'Invalid image file'}, 400
    except ValueError as e:
        logger.error(f"Background removal error: {str(e)}")
        return {'error': str(e)}, 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {'error': 'Internal server error'}, 500

if __name__ == '__main__':
    app.run(debug=True)
    