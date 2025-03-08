# Object Tracking Using OpenCV

## 📌 Description
This project implements real-time object tracking using OpenCV. The program detects and tracks a pink-colored object in a video stream from the webcam, displaying directional guidance (Left, Right, Inframe, or Too Close) based on its position.

## 🚀 Features
- Tracks a pink-colored object in real time.(change color according to your need)
- Provides directional feedback on the object's position.
- Displays a warning if the object is too close to the camera.
- Uses OpenCV for image processing and contour detection.

## 🛠️ Installation
### 1. Clone the Repository
```bash
git clone 'https://github.com/breweshank/object-tracking-opencv.git'
cd object-tracking-opencv
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries:
```bash
pip install opencv-python numpy imutils
```

## 🎯 Usage
Run the Python script to start object tracking:
```bash
object traking based on color.py
```

### 📷 Controls
- Press `q` to quit the program.

## 📌 How It Works
1. Captures video from the webcam.
2. Converts the frame to HSV color space and applies color thresholding to detect pink objects.
3. Uses contour detection to find the largest pink object.
4. Determines the object's position and gives directional feedback:
   - "Left" if the object is in the left region.
   - "Right" if in the right region.
   - "Inframe" if in the center.
   - "Too Close" if the object is too near to the camera.

## 🖼️ Example Output
- The script displays the detected object and its tracking status in a window.

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to submit issues or pull requests if you'd like to improve the project.


