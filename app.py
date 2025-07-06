from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    uploaded = False
    current_image_path = os.path.join(UPLOAD_FOLDER, "current_upload.jpg")

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != "":
                file.save(current_image_path)
                uploaded = True

        filter_type = request.form.get("filter")

        if os.path.exists(current_image_path) and filter_type:
            image = cv2.imread(current_image_path)

            if filter_type == "gaussian_blur":
                processed_image = cv2.GaussianBlur(image, (15, 15), 0)
            elif filter_type == "average_blur":
                processed_image = cv2.blur(image, (15, 15))
            elif filter_type == "median_blur":
                processed_image = cv2.medianBlur(image, 15)
            elif filter_type == "bilateral_filter":
                processed_image = cv2.bilateralFilter(image, 15, 75, 75)
            elif filter_type == "canny_edge":
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                processed_image = cv2.Canny(gray, 100, 200)
            elif filter_type == "sobel_edge":
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                processed_image = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)
                processed_image = cv2.convertScaleAbs(processed_image)
            elif filter_type == "laplacian_edge":
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                processed_image = cv2.Laplacian(gray, cv2.CV_64F)
                processed_image = cv2.convertScaleAbs(processed_image)
            elif filter_type == "sharpen":
                kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
                processed_image = cv2.filter2D(image, -1, kernel)
            elif filter_type == "otsu_threshold":
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                _, processed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            elif filter_type == "dilation":
                kernel = np.ones((5,5), np.uint8)
                processed_image = cv2.dilate(image, kernel, iterations=1)
            elif filter_type == "erosion":
                kernel = np.ones((5,5), np.uint8)
                processed_image = cv2.erode(image, kernel, iterations=1)
            elif filter_type == "convert_ycbcr":
                processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
            elif filter_type == "convert_hsv":
                processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            elif filter_type == "pseudo_color":
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                processed_image = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
            elif filter_type == "stylization":
                processed_image = cv2.stylization(image, sigma_s=60, sigma_r=0.6)
            elif filter_type == "pencil_sketch":
                gray, _ = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
                processed_image = gray
            elif filter_type == "cartoon":
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray = cv2.medianBlur(gray, 5)
                edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                              cv2.THRESH_BINARY, 9, 9)
                color = cv2.bilateralFilter(image, 9, 300, 300)
                processed_image = cv2.bitwise_and(color, color, mask=edges)
            elif filter_type == "contours":
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(gray, 127, 255, 0)
                contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                processed_image = cv2.drawContours(image.copy(), contours, -1, (0,255,0), 2)
            else:
                processed_image = image

            processed_img_path = os.path.join(UPLOAD_FOLDER, "processed.jpg")
            cv2.imwrite(processed_img_path, processed_image)

            return render_template("index.html", uploaded_image="static/uploads/current_upload.jpg", processed_image="static/uploads/processed.jpg")

    return render_template("index.html", uploaded_image=None, processed_image=None)

if __name__ == "__main__":
    app.run(debug=True)
