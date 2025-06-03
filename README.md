# Face Expression Detection using YOLOv11n

This project focuses on detecting facial expressions using the YOLOv11n model, a lightweight object detection architecture fine-tuned for emotion classification. The model is trained on the `facial-emotion-trpg7-07png` dataset provided by Roboflow.

## 🚀 Features

- Real-time face expression detection using YOLOv11n
- Supports multiple expression classes like Happy, Sad, Angry, Surprised, etc.
- Lightweight and optimized for faster inference
- Easy to run on both Colab and Kaggle

## 📁 Dataset

- **Name:** `facial-emotion-trpg7-07png`
- **Source:** [Roboflow](https://roboflow.com/)
- **Classes:** Multiple facial expressions
- **Format:** YOLO format (annotated `.txt` and `.png` images)

## 🧠 Model

- **Model Used:** YOLOv11n
- **Weights File:** `yolov11n.pt`
- **Framework:** PyTorch + Ultralytics YOLO

## 🧪 Notebooks

- **Google Colab:** [Face Expression Detection - Colab Notebook](https://colab.research.google.com/your-colab-link-here)
- **Kaggle Notebook:** [Face Expression Detection - Kaggle Notebook](https://kaggle.com/your-kaggle-notebook-link-here)

## 🎥 Output Video

Watch a sample demo of the model in action:

[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

*(Replace with actual link to video output or upload `.mp4` to GitHub repo if small enough)*

## 🛠️ Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/face-expression-detection
    cd face-expression-detection
    ```

2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Run detection:
    ```bash
    python detect.py --weights yolov11n.pt --source path/to/image_or_video
    ```

## 📝 License

This project is open source under the [MIT License](LICENSE).

## 🙌 Acknowledgements

- [Roboflow](https://roboflow.com/) for the dataset
- [Ultralytics YOLO](https://github.com/ultralytics/yolov5) for the base implementation
