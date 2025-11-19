---

# 📚 **iVeman · Book Recommender System**

### *ML-powered book recommendations with a neon-themed modern UI*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" /> 
  <img src="https://img.shields.io/badge/Framework-Flask-orange?logo=flask" />
  <img src="https://img.shields.io/badge/Deployed%20On-Render-46E3B7?logo=render&logoColor=white" />
  <img src="https://img.shields.io/github/stars/iveman99/Book-Recommender-System?style=social" />
  <img src="https://img.shields.io/github/forks/iveman99/Book-Recommender-System?style=social" />
</p>

---

## 🚀 **Live Demo**

🔗 **Try the Deployed App:**
👉 [https://iveman-booksenseai-berf.onrender.com/](https://iveman-booksenseai-berf.onrender.com/)

---

# 🎨 **Preview**

### ⭐ Home – Top 50 Books

<img width="1895" height="945" alt="image" src="https://github.com/user-attachments/assets/dc736b3f-f469-478e-8541-2a6afc1b6f82" />

### 🔍 Recommend Page

<img width="1913" height="948" alt="image" src="https://github.com/user-attachments/assets/d4e24e95-8b0e-4c97-b882-463dee4b6593" />


### ℹ️ About Page

<img width="1890" height="936" alt="image" src="https://github.com/user-attachments/assets/c4d4fca4-52c5-4692-a427-eabe2b0dd30b" />


---

# 🧠 **About The Project**

*iVeman Recommender System* is a neon-themed, ML-powered book recommendation engine that understands what readers love using similarity-based AI.

This system uses:

* 📘 Collaborative Filtering
* 🧮 Cosine Similarity
* 📊 User–Item Rating Matrix
* 🖥️ Flask Backend
* ✨ Modern Custom UI
* ☁️ Render Deployment with Google Drive PKL Download

The goal is simple: **recommend the best books instantly based on real-world rating patterns**.

---

# 🏗️ **How It Works**

## 1️⃣ Data Collection

Dataset contains:

* Books
* Users
* Ratings

Processed inside **Jupyter Notebook** — cleaned, merged, filtered low-rating books.

## 2️⃣ Feature Engineering

You created:

* `pt.pkl` → Pivot table (User × Book ratings)
* `popular.pkl` → Top-50 trending books
* `books.pkl` → Complete book metadata
* `similarity_scores.pkl` → Cosine similarity matrix of 7000+ books

## 3️⃣ ML Model

The model computes similarity between books using:

```
Cosine Similarity
```

Then recommends **top 4 similar books**.

## 4️⃣ Backend with Flask

Flask routes:

* `/` → Homepage
* `/recommend` → Search page
* `/recommend_books` → ML Recommendation
* `/about` → Project description

Loads `.pkl` models → Computes → Renders results.

## 5️⃣ UI/Frontend

A stylish, neon-orange custom theme:

* Responsive
* Clean & simple
* Modern card layout for books

## 6️⃣ Render Deployment

Because `.pkl` files > 25MB, you used:

📦 **Google Drive** → Auto-download in Render using:

```python
gdown.download_folder("https://drive.google.com/drive/folders/156kwjjNUCXxYPDSGkE-DwNOq7CRczhBB")
```

📄 **Procfile**

```
web: gunicorn app:app
```

Render builds → Installs → Downloads PKL → App runs flawlessly.

---

# 📁 Project Structure

```
│── app.py
│── requirements.txt
│── Procfile
│── books.pkl
│── popular.pkl
│── pt.pkl
│── similarity_scores.pkl
│── templates/
│   ├── index.html
│   ├── recommend.html
│   ├── about.html
│── assets/
│   ├── home.png
│   ├── recommend.png
│   ├── about.png
```

---

# 🔥 Features

✔ ML-based book recommendations
✔ Top 50 trending books
✔ Clean neon UI
✔ Auto-download PKL for Render
✔ Error-handling for missing books
✔ Fast recommendation engine
✔ Local + Cloud support

---

# ⚙️ Installation (Local Setup)

### **1️⃣ Clone Repository**

```bash
git clone https://github.com/iveman99/Book-Recommender-System.git
```

### **2️⃣ Create Virtual Environment**

```bash
python -m venv venv
```

### **3️⃣ Install Packages**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run the App**

```bash
python app.py
```

---

# ☁️ Deployment on Render

### Your Render setup includes:

* `Procfile`
* `requirements.txt`
* PKL download using `gdown`
* Python 3.10 environment
* Gunicorn production server

Deploy steps:

1. Connect GitHub Repo
2. Add environment variable:

   ```
   GOOGLE_DRIVE_MODELS = true
   ```
3. Deploy!

---

# 🤝 Contributing

Contributions, PRs, and suggestions are welcome.
Feel free to fork and enhance the UI/ML logic.

---

# 👨‍💻 Author

**Veman Shrinivas Chippa**
*Data Science • Machine Learning • Python*

📧 **[info.veman99@gmail.com](mailto:info.veman99@gmail.com)**
🔗 [https://www.linkedin.com/in/veman-chippa/](https://www.linkedin.com/in/veman-chippa/)
🔗 [https://iveman.vercel.app/]

---

# 📜 License

This project is under the **MIT License**.

---
