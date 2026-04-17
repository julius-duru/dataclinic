import streamlit as st

TITLE = "Build a Real Working Flask + MySQL + Docker Project"
CATEGORY = "docker"
KEYWORDS = ["flask", "mysql", "docker", "docker-compose", "github", "web development"]


def show():
    st.title(" Build a Real Working GitHub Project: Flask + MySQL + Docker")
    st.caption(f"Category: {CATEGORY} | Level: Intermediate")
    st.markdown("---")

    st.write("""
    In this tutorial, you will create a fully containerized web application using **Flask** (Python), **MySQL**, and **Docker**.  
    The final project can be pushed to GitHub and run anywhere with Docker installed.  
    You will learn:
    - Structuring a Flask + MySQL app
    - Writing a Dockerfile and `docker-compose.yml`
    - Persisting database data with Docker volumes
    - Connecting application and database containers via a custom network
    - Running and testing the application locally
    - Pushing the project to a GitHub repository
    """)

    # ============================================
    # SECTION 1: PROJECT OVERVIEW
    # ============================================
    st.header(" Project Overview")
    st.code("""
flask-mysql-docker/
├── app/
│   └── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── init.sql
└── README.md
    """, language="text")

    st.write("""
    - **app/app.py** – Main Flask application with database integration.
    - **requirements.txt** – Python dependencies.
    - **Dockerfile** – Instructions to build the Flask app image.
    - **docker-compose.yml** – Orchestrates Flask and MySQL containers.
    - **.env.example** – Template for environment variables (database credentials).
    - **init.sql** – Optional initial database schema.
    - **README.md** – Documentation for your GitHub repo.
    """)

    # ============================================
    # SECTION 2: APPLICATION CODE
    # ============================================
    st.header(" Step 1: Write the Flask Application")

    st.subheader("app/app.py")
    st.code("""
import os
import mysql.connector
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Database configuration from environment variables
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'root'),
    'database': os.environ.get('DB_NAME', 'mydb')
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Simple HTML template
HTML_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Flask + MySQL Docker Demo</title></head>
<body>
    <h1>Messages</h1>
    <ul>
        {% for msg in messages %}
            <li>{{ msg[1] }}</li>
        {% endfor %}
    </ul>
    <form method="post">
        <input type="text" name="message" placeholder="New message" required>
        <button type="submit">Add</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        message = request.form['message']
        cursor.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
        conn.commit()
        return redirect(url_for('index'))

    cursor.execute("SELECT id, content FROM messages ORDER BY id DESC")
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string(HTML_TEMPLATE, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    """, language="python")

    st.subheader("requirements.txt")
    st.code("""
flask==3.0.0
mysql-connector-python==8.2.0
    """, language="text")

    # ============================================
    # SECTION 3: DATABASE INITIALIZATION
    # ============================================
    st.header(" Step 2: Database Initialisation Script")
    st.write("Create `init.sql` – this will be automatically run when the MySQL container starts for the first time.")

    st.code("""
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO messages (content) VALUES ('Hello from Docker!'), ('Flask + MySQL is awesome');
    """, language="sql")

    # ============================================
    # SECTION 4: DOCKER FILES AND COMPOSE
    # ============================================
    st.header(" Step 3: Containerize the Application")

    st.subheader("Dockerfile")
    st.code("""
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

ENV FLASK_APP=app/app.py
EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
    """, language="dockerfile")

    st.subheader("docker-compose.yml")
    st.code("""
version: '3.8'

services:
  db:
    image: mysql:8.0
    container_name: flask_mysql_db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    ports:
      - "3306:3306"   # optional, for external DB tools
    volumes:
      - mysql_data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      timeout: 20s
      retries: 10

  web:
    build: .
    container_name: flask_web
    restart: unless-stopped
    environment:
      DB_HOST: db
      DB_USER: ${MYSQL_USER}
      DB_PASSWORD: ${MYSQL_PASSWORD}
      DB_NAME: ${MYSQL_DATABASE}
    ports:
      - "5000:5000"
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - ./app:/app   # bind mount for live development (optional)

volumes:
  mysql_data:
    """, language="yaml")

    st.subheader(".env")
    st.code("""
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=mydb
MYSQL_USER=root
MYSQL_PASSWORD=root
    """, language="bash")
    st.write("**Important:** Copy `.env` to `.env` and change passwords before deploying.")

    # ============================================
    # SECTION 5: RUN LOCALLY WITH DOCKER COMPOSE
    # ============================================
    st.header(" Step 4: Build and Run the Project Locally")
    st.code("""
# 1. Clone or create the project folder
mkdir flask-mysql-docker && cd flask-mysql-docker

# 2. Create all the files as shown above (app/, requirements.txt, Dockerfile, etc.)

# 3. Copy .env to .env and edit credentials
cp .env.example .env

# 4. Start the containers
docker compose up -d

# 5. Check logs
docker compose logs -f

# 6. Open your browser at http://localhost:5000

# 7. Stop and remove containers (data remains in volume)
docker compose down

# 8. Remove everything including database volume (all data lost)
docker compose down -v
    """, language="bash")

    st.write("""
    **Verification:**  
    - The Flask app should be accessible on `http://localhost:5000`.  
    - It displays existing messages and allows adding new ones.  
    - Data persists across container restarts thanks to the `mysql_data` volume.
    """)

    # ============================================
    # SECTION 6: DEBUGGING TIPS
    # ============================================
    st.header("🐛 Debugging Common Issues")
    st.markdown("""
    - **App cannot connect to database**  
      Check environment variables: `docker exec flask_web env | grep DB_`  
      Test connectivity: `docker exec flask_web ping db`
    
    - **MySQL container fails to start**  
      Look at logs: `docker logs flask_mysql_db`  
      Ensure the `.env` file exists and contains valid values.
    
    - **Port 5000 already in use**  
      Change the host port in `docker-compose.yml` (e.g., `"5001:5000"`).
    
    - **Changes in code not reflected**  
      The bind mount `- ./app:/app` enables live reload. Restart the web container if needed: `docker compose restart web`.
    """)

    # ============================================
    # SECTION 7: PUSHING TO GITHUB
    # ============================================
    st.header(" Step 5: Push the Project to GitHub")
    st.write("""
    After confirming everything works locally, share your project on GitHub.  
    **Important:** Never commit `.env` or any file containing secrets.
    """)

    st.subheader("Create a .gitignore file")
    st.code("""
.env
__pycache__/
*.pyc
*.log
    """, language="text")

    st.subheader("Git commands to initialise and push")
    st.code("""
# Inside your project folder
git init
git add .
git commit -m "Initial commit: Flask + MySQL Docker app"

# Create a repository on GitHub (without README, .gitignore)
git remote add origin https://github.com/your-username/flask-mysql-docker.git
git branch -M main
git push -u origin main
    """, language="bash")

    st.write("""
    Your repository is now live. Anyone can clone it and run `docker compose up -d` to start the same application.
    """)

    # ============================================
    # SECTION 8: PRODUCTION CONSIDERATIONS
    # ============================================
    st.header(" Production Hardening (Optional)")
    st.markdown("""
    For a real deployment, apply these improvements:
    - **Use a non‑root user** inside the Flask container.
    - **Drop all Linux capabilities** except `NET_BIND_SERVICE`.
    - **Set `read_only: true`** and use `tmpfs` for `/tmp`.
    - **Limit resources** (CPU, memory) in `docker-compose.yml`.
    - **Use a reverse proxy** (like Nginx) in front of Flask.
    - **Store secrets in Docker secrets** (Swarm) or a vault.
    - **Add healthchecks** to the web service.
    - **Scan images** with Trivy or Docker Scout.
    """)

    # ============================================
    # SECTION 9: CONCLUSION
    # ============================================
    st.header(" Conclusion")
    st.write("""
    You have built a complete, containerised Flask + MySQL application that can be run anywhere Docker is available.  
    The project is ready to be shared on GitHub, deployed to a VPS, or integrated into a CI/CD pipeline.
    
    **Next steps:**
    - Add more features (user authentication, API endpoints).
    - Deploy to a cloud provider (AWS ECS, Google Cloud Run, Azure Container Instances).
    - Set up GitHub Actions to automatically build and push the Docker image.
    """)

    st.divider()
    st.caption("© 2026 – Real working Flask + MySQL + Docker project. Use it as a template for your own applications.")

