# Face Blur AI Agent

This AI Agent is uses an advanced neural network to detect and blur faces in uploaded images. Users can adjust the level of blurring.

## Features

*   **Facial Detection:** Leverages the MTCNN (Multi-task Cascaded Convolutional Networks) model for accurate face detection.
*   **Adjustable Blur Strength:** Users can choose between Light, Medium, and Heavy blur settings via a slider.
*   **Intuitive Upload:** Supports drag-and-drop and click-to-upload for image files (`.jpg`, `.jpeg`, `.png`, `.webp`).
*   **Side-by-Side Comparison:** Displays the original and blurred images after processing.
*   **Processing Time Display:** Shows the time taken for the face blurring operation.
*   **Dark Mode Support:** Adapts to the user's system preference for light or dark mode.

## User Experience

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

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Place the test image:**
    Ensure `Group1.jpg` is in the root directory of the project, next to `face_blur.py`. This file is used by the "Test File" button in the UI.

