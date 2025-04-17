# 🌐 Flask + Nextcloud File Uploader

This is a simple web application built using **Flask** that allows users to upload files directly to a **Nextcloud** server. It includes a minimal frontend built with Tailwind CSS and a Dockerized setup for easy deployment alongside a Nextcloud and MariaDB stack.

---

## 🚀 Features

- Upload files via a simple web form
- Store uploaded files directly to a Nextcloud instance via WebDAV
- Dockerized setup with Flask, Nextcloud, and MariaDB
- Tailwind CSS for responsive UI
- Flash messages to show upload status

---

## 🧰 Tech Stack

- **Flask** (Python backend)
- **Nextcloud** (for file storage)
- **MariaDB** (used by Nextcloud)
- **Docker & Docker Compose**
- **Tailwind CSS** (UI)

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/hakim-az/mini-projet-cloud.git
cd mini-projet-cloud
```

### 2. Create a `.env` file

Create a `.env` file in the root directory with the following variables:

```env
NEXTCLOUD_URL=http://nextcloud:80/remote.php/webdav
NEXTCLOUD_USER=nc_user
NEXTCLOUD_PASSWORD=nc_pass
```

> Make sure the `NEXTCLOUD_URL` matches the internal Docker hostname (`nextcloud`) and WebDAV endpoint.

---

## 🐳 Using Docker

### 1. Build and start the stack

```bash
docker-compose up --build
```

- Flask app will be available at: `http://localhost:5000`
- Nextcloud will be available at: `http://localhost:8080`

### 2. Initial Nextcloud Setup

Open `http://localhost:8080` in your browser and:

- Create the admin account (you can skip DB setup—it’s already configured via `docker-compose`)
- Login to your Nextcloud dashboard

---

## 🌐 Usage

1. Go to `http://localhost:5000`
2. Navigate to **NextCloud** page from the navbar
3. Choose a file and click **Upload**
4. A flash message will confirm success or failure

---

## 📂 Project Structure

```
├── app.py                 # Flask backend
├── Dockerfile             # Flask app Dockerfile
├── docker-compose.yml     # Multi-service setup (Flask, Nextcloud, MariaDB)
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html
│   ├── labs.html
│   └── nextcloud.html     # Upload form UI
└── .env                   # Env variables (excluded from version control)
```
---
## 🖼️ Screenshot support
## 🖼️ Screenshot support

### 1. App Pages

#### Home Page
![Home page](https://i.imgur.com/pjGacLh.png)
*Home page view of the app.*

#### Labs Page
![Labs page](https://i.imgur.com/pjGacLh.png)
*Labs page where you can explore different cloud concepts.*

#### Nextcloud Page
![Nextcloud page](https://i.imgur.com/pjGacLh.png)
*Nextcloud page where you can upload files to the cloud.*

---

## ✅ Notes

- Uploaded files are sent to Nextcloud via the [WebDAV API](https://docs.nextcloud.com/server/latest/user_manual/files/access_webdav.html).
- Flask logs and flash messages help trace upload status.
- Be sure to install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) before running the project.

---

## 🙌 Credits

Built by **A. Azzaz**  
Tailwind UI & Flask ❤️

---

## 📃 License

MIT License. Use freely.