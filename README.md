# Face Blur AI Agent

A simple yet powerful Flask web application that utilizes advanced AI (MTCNN and OpenCV) to detect and blur faces in uploaded images, ensuring privacy with customizable blur strength.

## Table of Contents

*   [Features](#features)
*   [User Experience (UX) Screenshots](#user-experience-ux-screenshots)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Technologies Used](#technologies-used)
*   [License](#license)

## Features

*   **Facial Detection:** Leverages the MTCNN (Multi-task Cascaded Convolutional Networks) model for accurate face detection.
*   **Adjustable Blur Strength:** Users can choose between Light, Medium, and Heavy blur settings via a slider.
*   **Intuitive Upload:** Supports drag-and-drop and click-to-upload for image files (`.jpg`, `.jpeg`, `.png`, `.webp`).
*   **Side-by-Side Comparison:** Displays the original and blurred images after processing.
*   **Processing Time Display:** Shows the time taken for the face blurring operation.
*   **Responsive UI:** Built with Bootstrap for a modern and responsive user interface.
*   **Dark Mode Support:** Adapts to the user's system preference for light or dark mode.
*   **Downloadable Test File:** Provides a `Group1.jpg` for quick testing.

## User Experience (UX) Screenshots

The screenshots are located in the `assets` folder of this repository.

### Main Interface

![Main Interface](assets/Main%20app%20ux.jpg)

### Processing Results

![Processing Results](assets/Example%20Output.jpg)

## Installation

Follow these steps to get the application up and running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/pohagan72/face_blur_images.git
    cd face_blur_images
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Place the test image:**
    Ensure `Group1.jpg` is in the root directory of the project, next to `face_blur.py`. This file is used by the "Test File" button in the UI.

## Usage

1.  **Run the Flask application:**
    Once your virtual environment is active and dependencies are installed, start the app:

    ```bash
    python face_blur.py
    ```
    The console will display messages indicating the server is running.

2.  **Access the application:**
    Open your web browser and navigate to the address shown in the console, typically:
    `http://127.0.0.1:8502`

3.  **Upload and Process:**
    *   **Drag & Drop:** Drag an image file (`.jpg`, `.jpeg`, `.png`, or `.webp`) onto the "Drag & drop your image here" zone.
    *   **Click to Upload:** Click the zone to open a file selection dialog and choose your image.
    *   **Adjust Blur Strength:** Use the "Blur Strength" slider to select your preferred blur level (Light, Medium, or Heavy).
    *   **Start Processing:** Click the "Start Processing" button.
    *   The original and blurred images will be displayed side-by-side, along with the processing time.

## Technologies Used

*   **Backend:**
    *   Python
    *   Flask
    *   MTCNN (for Face Detection)
    *   OpenCV (`cv2`) (for Image Processing)
    *   TensorFlow (backend for MTCNN)
*   **Frontend:**
    *   HTML5
    *   CSS3 (Custom styling)
    *   JavaScript (Client-side interactivity)
    *   Bootstrap 5 (UI Framework)
    *   Font Awesome (Icons)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.