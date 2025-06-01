import os
import time
import cv2
import numpy as np
from mtcnn import MTCNN
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, jsonify

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuration
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')
UPLOAD_FOLDER = os.path.join('static', 'uploads')
BLURRED_FOLDER = os.path.join('static', 'blurred_output')
TEST_FILE_NAME = 'Group1.jpg'  # Ensure this file exists in the same directory as app.py

# Ensure necessary directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BLURRED_FOLDER, exist_ok=True)

def allowed_file(filename: str) -> bool:
    """
    Check if the file has one of the valid extensions.
    """
    return filename.lower().endswith(VALID_EXTENSIONS)

def validate_blur_size(blur_size: int) -> int:
    """
    Ensures the blur size is at least 1 and odd.
    """
    blur_size = max(1, blur_size)
    return blur_size if blur_size % 2 == 1 else blur_size + 1

def blur_face(image: np.ndarray, detector: MTCNN, blur_size: int) -> np.ndarray:
    """
    Blurs detected faces in the image using the specified blur size.
    """
    try:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(rgb_image)
        
        if not faces:
            return image
        
        blur_size = validate_blur_size(blur_size)
        height, width = image.shape[:2]
        
        for face in faces:
            x, y, w, h = face.get('box', (0, 0, 0, 0))
            x, y = max(0, x - 10), max(0, y - 10)
            w, h = min(width - x, w + 20), min(height - y, h + 20)

            if w > 0 and h > 0:
                face_roi = image[y:y + h, x:x + w]
                blurred_roi = cv2.GaussianBlur(face_roi, (blur_size, blur_size), 0)
                image[y:y + h, x:x + w] = blurred_roi
        
        return image

    except cv2.error as cv_err:
        raise RuntimeError(f"OpenCV error while processing image: {cv_err}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error during face blurring: {e}")

def process_image(file_storage, blur_size: int) -> tuple:
    """
    Processes the uploaded image: detects and blurs faces, then saves the output.
    """
    filename = file_storage.filename
    if not allowed_file(filename):
        flash("Invalid file extension! Please upload a .jpg, .jpeg, .png, or .webp image.", 'error')
        return None, False, 0.0

    # Secure the filename
    from werkzeug.utils import secure_filename
    filename = secure_filename(filename)
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    file_storage.save(upload_path)

    output_filename = f"{os.path.splitext(filename)[0]}-blurred{os.path.splitext(filename)[1]}"
    output_path = os.path.join(BLURRED_FOLDER, output_filename)

    try:
        image = cv2.imread(upload_path)
        if image is None:
            raise ValueError("Unable to read image. It might be corrupted or in an unsupported format.")

        detector = MTCNN()

        start_time = time.time()
        processed_image = blur_face(image, detector, blur_size)
        cv2.imwrite(output_path, processed_image)
        processing_time = time.time() - start_time

        return filename, True, processing_time

    except Exception as e:
        flash(f"Error processing {filename}: {str(e)}", 'error')
        return filename, False, 0.0

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    The main route handling image upload and display.
    """
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """
    Handles the processing of the image after the user clicks "Start Processing".
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        blur_selection = int(request.form.get('blur_strength', 2))
        blur_strength_map = {1: 35, 2: 65, 3: 99}
        blur_size = blur_strength_map.get(blur_selection, 65)

        filename, success, processing_time = process_image(file, blur_size)

        if success:
            blurred_filename = f"{os.path.splitext(filename)[0]}-blurred{os.path.splitext(filename)[1]}"
            return jsonify({
                'original_image': url_for('uploaded_file', filename=filename),
                'blurred_image': url_for('blurred_file', filename=blurred_filename),
                'processing_time': processing_time
            })
        else:
            return jsonify({'error': 'Error processing image'}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """
    Serves uploaded images from the 'uploads' directory.
    """
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/blurred_output/<path:filename>')
def blurred_file(filename):
    """
    Serves blurred images from the 'blurred_output' directory.
    """
    return send_from_directory(BLURRED_FOLDER, filename)

@app.route('/download_test_file')
def download_test_file():
    """
    Serves the test file 'Group1.jpg' for download.
    """
    test_file_path = os.path.join(app.root_path, TEST_FILE_NAME)
    if os.path.exists(test_file_path):
        # Corrected the order of arguments: directory is the first positional argument
        return send_from_directory(app.root_path, TEST_FILE_NAME, as_attachment=True)
    else:
        flash("Test file 'Group1.jpg' not found.", 'error')
        return redirect(url_for('index'))

if __name__ == "__main__":
    # Ensure that the 'static/uploads' and 'static/blurred_output' directories exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(BLURRED_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=8502, debug=True)