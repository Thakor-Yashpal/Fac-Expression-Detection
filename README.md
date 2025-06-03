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

- **Google Colab:** [Face Expression Detection - Colab Notebook](https://colab.research.google.com/drive/1N_d27-8AUyteTun3tvBVp11rb7DfGexR?usp=sharing)
- **Kaggle Notebook:** [Face Expression Detection - Kaggle Notebook](https://www.kaggle.com/models/yashpalthakor/face-expression-detection)

## 🎥 Output Video



[*(Replace with actual link to video output or upload `.mp4` to GitHub repo if small enough)*](https://github.com/user-attachments/assets/f1db7209-349c-47db-9e0b-2c99a706612a)

## 🛠️ Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Thakor-Yashpal/Fac-Expression-Detection
    cd Fac-Expression-Detection
    ```

2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
## 📝 License

This project is open source under the [MIT License](LICENSE).

## 🙌 Acknowledgements

- [Roboflow](https://roboflow.com/) for the dataset
- [Ultralytics YOLO](https://github.com/ultralytics/yolov11n) for the base implementation
