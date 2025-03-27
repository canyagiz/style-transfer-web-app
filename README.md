# 🖼️ Neural Style Transfer Web App

A simple end-to-end web application that performs **neural style transfer** using pre-trained models.

### 🚀 Features
- ✨ Apply artistic styles (e.g. *candy, mosaic, udnie*) to any image
- ⚡ Fast inference powered by [Fast Neural Style](https://github.com/jcjohnson/fast-neural-style)
- 🌐 Web interface built with **Streamlit**
- 🔙 Backend powered by **FastAPI**
- 📦 Containerized with **Docker** and orchestrated using **Docker Compose**

### 🛠️ Tech Stack
- [x] Python
- [x] FastAPI (for backend API)
- [x] Streamlit (for user interface)
- [x] Docker & Docker Compose
- [x] OpenCV, NumPy, PIL

### 🧪 How It Works
1. User uploads an image via Streamlit interface.
2. The selected style is applied instantly via FastAPI.
3. Other styles are processed asynchronously in the background.
4. All generated images are saved to a shared `/storage` volume.

### 📦 Running the App (locally)

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
docker-compose up --build
```

### 🖼️ Examples
1. Candy
![image](https://github.com/user-attachments/assets/24ca0cb5-3dd9-44ef-a408-d77681f73649)

2. Composition 6
![image](https://github.com/user-attachments/assets/e5f38cbc-e839-4bf6-845b-c9772b3cc845)

3. Starry Night
![image](https://github.com/user-attachments/assets/48866b1a-ee28-4a52-a732-f0ebca41bec0)

and more!
