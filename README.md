# 🖼️ Social Media Filter WebApp

A web-based image processing app built with **Flask** and **OpenCV** that allows users to upload an image and apply a variety of **social media-style filters**.

## 📌 Project Description

This project, developed as part of the *Image Processing & Pattern Recognition* course, provides users with a simple and interactive web interface to upload images and apply filters like:

- Gaussian Blur  
- Edge Detection (Canny, Sobel, Laplacian)  
- Morphological Filters (Dilation, Erosion)  
- Color Transformations (YCbCr, HSV)  
- Stylization Effects (Cartoon, Pencil Sketch, Stylization)  
- Thresholding and Pseudo Coloring  
- Contour Detection  

This app showcases the use of **Flask for backend routing**, **OpenCV for real-time image processing**, and **HTML/CSS for a clean UI**.

## ⚙️ Tech Stack

- **Python 3**
- **Flask**
- **OpenCV**
- **NumPy**
- **HTML5**, **CSS3**

## 🚀 Features

- Upload and preview images in the browser  
- Select from 15+ popular filter types  
- View filtered image instantly  
- Download filtered image with a single click

## 📁 Project Structure

<pre>
social-media-filter-app/
│
├── app.py                         # Main Flask backend
├── requirements.txt               # Dependencies
├── static/ 
│   └── uploads/                   # Uploaded input images
├── templates/
│   └── index.html                 # Web UI
└── README.md
</pre>

## ▶️ How to Run

```bash
# Step 1: Clone the repository
git clone https://github.com/VRV37/social-media-filter-app.git
cd social-media-filter-app

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
python app.py


