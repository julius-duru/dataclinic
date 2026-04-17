import streamlit as st
import pandas as pd

TITLE = "Docker Containers: Concepts, Installation, Commands, Debugging & Security"
CATEGORY = "devops"
KEYWORDS = ["docker", "containers", "virtual machines", "devops", "container security", "docker commands", "debugging", "containerization"]


def show():

    st.title("🐳 Docker Containers: Comprehensive Guide")
    st.caption("Category: devops | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        Docker has revolutionized how we build, ship, and run applications. This guide covers everything from 
        core concepts to hands‑on commands, debugging techniques, and security best practices – all with 
        practical code examples.
        
        **What you'll learn:**
        - What Docker containers are and how they work
        - Docker vs traditional virtual machines
        - Installation on Linux (Ubuntu) and overview for macOS/Windows
        - Essential Docker commands (images, containers, networks, volumes)
        - Debugging failing or misbehaving containers
        - Securing containers in production
        """
    )

    # ============================================
    # SECTION 1: DOCKER CONTAINERS
    # ============================================
    st.header("1. What Are Docker Containers?")
    
    st.write(
        """
        A **Docker container** is a standard unit of software that packages code and all its dependencies 
        (libraries, system tools, runtime, settings). Containers run in isolated user spaces on a shared 
        host operating system kernel, making them lightweight and fast.
        
        **Key characteristics:**
        - **Isolation** – Processes, filesystems, and network stacks are separated using Linux namespaces.
        - **Resource control** – CPU, memory, disk I/O limited via cgroups.
        - **Portability** – Same container runs identically on a laptop, test server, or production.
        - **Immutable infrastructure** – Containers are built from images and never modified; changes require rebuilding the image.
        
        **How a container works**  
        A container is an instance of a **Docker image** – a read‑only template with layered filesystem changes. 
        When you run an image, Docker adds a thin writable layer on top (copy‑on‑write).
        """
    )

    st.subheader("Container vs Image")
    st.code(
        """
        # An image is a static template
        docker pull nginx:latest
        
        # A container is a running instance of that image
        docker run -d --name web nginx:latest
        """,
        language="bash"
    )

    st.divider()

    # ============================================
    # SECTION 2: DOCKER VS VIRTUAL MACHINES
    # ============================================
    st.header("2. Docker Containers vs Virtual Machines")
    
    st.write(
        """
        Both provide isolation, but at different levels of the technology stack. The table below highlights 
        the key differences.
        """
    )

    comparison_data = {
        "Feature": ["Isolation level", "Guest OS", "Startup time", "Size", "Resource overhead", "Security", "Use case"],
        "Docker Container": [
            "Process‑level (shared OS kernel)",
            "Uses host OS kernel (e.g., Linux)",
            "Milliseconds to seconds",
            "MB (app + dependencies)",
            "Very low",
            "Kernel isolation – potential attack surface",
            "Microservices, CI/CD, dev‑prod parity"
        ],
        "Virtual Machine": [
            "Full hardware virtualization (Hypervisor)",
            "Each VM runs a complete guest OS",
            "Minutes",
            "GB (entire OS)",
            "High (memory, CPU, disk)",
            "Stronger isolation (hardware‑enforced)",
            "Running different OS families, strong isolation"
        ]
    }
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)

    st.markdown(
        """
        **When to choose what?**  
        - **Containers** – high density, fast deployment, all apps on same OS kernel.  
        - **VMs** – need different OS families (e.g., Windows + Linux) or strict security boundaries.
        """
    )

    st.divider()

    # ============================================
    # SECTION 3: DOCKER INSTALLATION
    # ============================================
    st.header("3. Docker Installation")
    
    st.write(
        """
        Below are instructions for **Ubuntu 22.04/24.04 LTS** (most common for servers).  
        For macOS or Windows, install **Docker Desktop** from [docker.com](https://docker.com).  
        All commands may need `sudo` unless your user is in the `docker` group.
        """
    )

    st.subheader("3.1 Installing on Ubuntu")
    st.code(
        """
        # Update package index and install prerequisites
        sudo apt update
        sudo apt install -y ca-certificates curl

        # Add Docker's official GPG key
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc

        # Add the repository to Apt sources
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

        # Install Docker Engine, CLI, and containerd
        sudo apt update
        sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        """,
        language="bash"
    )

    st.subheader("3.2 Post‑installation Steps")
    st.code(
        """
        # Start and enable Docker daemon
        sudo systemctl enable docker --now

        # Add your user to the docker group (to run without sudo)
        sudo usermod -aG docker $USER
        # Log out and back in, or run: newgrp docker

        # Verify installation
        docker run hello-world
        """,
        language="bash"
    )

    st.subheader("3.3 Docker Desktop (macOS/Windows)")
    st.write(
        """
        1. Download Docker Desktop from the official website.  
        2. Install using the standard wizard (enable Hyper‑V on Windows, or use WSL2).  
        3. After installation, open a terminal and run `docker version` to confirm.
        """
    )

    st.divider()

    # ============================================
    # SECTION 4: ESSENTIAL DOCKER COMMANDS
    # ============================================
    st.header("4. Essential Docker Commands")
    
    st.write("Hands‑on reference with practical examples. Assume Docker is installed and the daemon is running.")

    st.subheader("4.1 Working with Images")
    commands_images = pd.DataFrame({
        "Command": [
            "`docker pull <td>`",
            "`docker images`",
            "`docker build -t <name> .`",
            "`docker rmi <td>`"
        ],
        "Description": [
            "Download an image from a registry (e.g., Docker Hub)",
            "List locally stored images",
            "Build an image from a Dockerfile in the current directory",
            "Remove an image"
        ]
    })
    st.dataframe(commands_images, use_container_width=True)
    st.code(
        """
        # Example: pull and inspect an Ubuntu image
        docker pull ubuntu:22.04
        docker images
        docker rmi ubuntu:22.04
        """,
        language="bash"
    )

    st.subheader("4.2 Running and Managing Containers")
    commands_containers = pd.DataFrame({
        "Command": [
            "`docker run <td>`",
            "`docker run -it <td> bash`",
            "`docker run -d --name myapp <td>`",
            "`docker ps`",
            "`docker ps -a`",
            "`docker stop <container>`",
            "`docker rm <container>`",
            "`docker logs <container>`"
        ],
        "Description": [
            "Create and start a container",
            "Interactive terminal",
            "Detached mode (background)",
            "List running containers",
            "List all containers (including stopped)",
            "Gracefully stop a container",
            "Remove a stopped container",
            "View stdout/stderr logs"
        ]
    })
    st.dataframe(commands_containers, use_container_width=True)
    st.code(
        """
        # Run a simple nginx web server
        docker run -d -p 8080:80 --name mynginx nginx
        curl localhost:8080

        # Stop and remove
        docker stop mynginx
        docker rm mynginx
        """,
        language="bash"
    )

    st.subheader("4.3 Container Lifecycle Examples")
    st.code(
        """
        # Run a temporary busybox container that prints "Hello" and exits
        docker run --rm busybox echo Hello

        # Run an interactive Ubuntu container with a shell
        docker run -it --name ubuntu-test ubuntu:22.04 /bin/bash
        # Inside the container: apt update && apt install -y vim
        # Type 'exit' to stop the container

        # Re‑start the stopped container (filesystem changes persist)
        docker start -ai ubuntu-test
        """,
        language="bash"
    )

    st.subheader("4.4 Advanced Commands")
    st.code(
        """
        # Run a command inside a running container
        docker exec -it <container> bash

        # Copy files into/out of a container
        docker cp <src> <container>:<dest>

        # Create a new image from a container’s changes (not recommended for production)
        docker commit <container> <newimage>

        # Display detailed metadata (network, volumes, state)
        docker inspect <container>

        # Follow log output
        docker logs --tail 100 -f <container>
        """,
        language="bash"
    )

    st.divider()

    # ============================================
    # SECTION 5: DEBUGGING A CONTAINER
    # ============================================
    st.header("5. Debugging a Container")
    
    st.write(
        """
        When a container fails to start, crashes, or behaves unexpectedly, use these systematic debugging techniques.
        """
    )

    st.subheader("5.1 Check Logs – First Step")
    st.code(
        """
        docker logs <container>
        docker logs --tail 50 --timestamps <container>
        docker logs -f <container>   # follow live output
        """,
        language="bash"
    )

    st.subheader("5.2 Investigate a Running Container")
    st.code(
        """
        # Get an interactive shell (if the container has /bin/bash)
        docker exec -it <container> /bin/bash
        # or /bin/sh for minimal images

        # Check running processes
        docker exec <container> ps aux

        # View environment variables
        docker exec <container> env

        # Inspect filesystem (e.g., config files, application logs)
        docker exec <container> cat /var/log/app.log
        """,
        language="bash"
    )

    st.subheader("5.3 Inspect a Non‑Running Container")
    st.code(
        """
        # Examine exit code and last logs
        docker ps -a
        docker logs <container>

        # Override the entrypoint to get a shell and investigate
        docker run -it --entrypoint /bin/sh <td>
        """,
        language="bash"
    )

    st.subheader("5.4 Using `docker events` and `docker inspect`")
    st.code(
        """
        # Stream real‑time events from the Docker daemon
        docker events --filter event=stop

        # Low‑level details
        docker inspect <container> | jq '.[0].State'   # State, exit code, error
        docker inspect <container> | jq '.[0].Config'  # Entrypoint, Cmd, Env
        """,
        language="bash"
    )

    st.subheader("5.5 Debugging Resource Issues")
    st.code(
        """
        # Real‑time CPU/mem/net/IO
        docker stats <container>

        # Check if container was OOM‑killed
        docker inspect <container> | jq '.[0].State.OOMKilled'
        """,
        language="bash"
    )

    st.subheader("5.6 Network Debugging")
    st.code(
        """
        # Create a network
        docker network create mynet

        # Run two containers on that network
        docker run -d --net mynet --name app1 nginx
        docker run -it --net mynet --name app2 alpine sh

        # Inside app2:
        ping app1
        wget -qO- http://app1:80
        """,
        language="bash"
    )

    st.subheader("5.7 Debugging Example: Broken Node.js App")
    st.code(
        """
        # Build and run (fails)
        docker build -t myapp .
        docker run --name test myapp   # exits

        # Inspect logs
        docker logs test   # shows missing module error

        # Override entrypoint to get a shell
        docker run -it --entrypoint /bin/sh myapp

        # Inside container:
        ls -la
        cat package.json
        npm install   # manually run install
        node index.js # test manually
        """,
        language="bash"
    )

    st.divider()

    # ============================================
    # SECTION 6: SECURING A CONTAINER
    # ============================================
    st.header("6. Securing a Docker Container")
    
    st.write(
        """
        Security is a shared responsibility: the daemon, the host, the container runtime, and the image. 
        Follow these best practices to harden your containers.
        """
    )

    st.subheader("6.1 Keep Host and Docker Updated")
    st.code(
        """
        sudo apt update && sudo apt upgrade -y   # Linux
        sudo systemctl restart docker
        """,
        language="bash"
    )

    st.subheader("6.2 Use Official and Minimal Base Images")
    st.code(
        """
        # Example: multi‑stage build with distroless
        FROM node:20-alpine AS builder
        WORKDIR /app
        COPY package*.json .
        RUN npm ci --only=production

        FROM gcr.io/distroless/nodejs20-debian12
        COPY --from=builder /app /app
        WORKDIR /app
        CMD ["index.js"]
        """,
        language="dockerfile"
    )

    st.subheader("6.3 Run Containers as Non‑Root User")
    st.code(
        """
        FROM ubuntu:22.04
        RUN useradd -m -u 1000 appuser
        USER appuser
        WORKDIR /home/appuser
        COPY --chown=appuser:appuser . .
        CMD ["python", "app.py"]
        """,
        language="dockerfile"
    )
    st.code(
        """
        # At runtime
        docker run --user 1000:1000 myapp
        """,
        language="bash"
    )

    st.subheader("6.4 Drop Unnecessary Capabilities")
    st.code(
        """
        # Drop ALL, then add only needed capabilities
        docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp
        """,
        language="bash"
    )

    st.subheader("6.5 Use Security Profiles: Seccomp & AppArmor")
    st.code(
        """
        # Apply custom seccomp profile
        docker run --security-opt seccomp=/path/to/custom.json myapp

        # Disable seccomp (not recommended for production)
        docker run --security-opt seccomp=unconfined myapp
        """,
        language="bash"
    )

    st.subheader("6.6 Limit Resources (Prevent DoS)")
    st.code(
        """
        docker run -d --name web \\
          --memory="512m" \\
          --memory-swap="1g" \\
          --cpus="1.5" \\
          --pids-limit=100 \\
          nginx
        """,
        language="bash"
    )

    st.subheader("6.7 Read‑only Root Filesystem")
    st.code(
        """
        docker run -d --read-only -v /tmp --tmpfs /run myapp
        """,
        language="bash"
    )
    st.code(
        """
        # Docker Compose example
        services:
          app:
            image: myapp
            read_only: true
            tmpfs:
              - /tmp
              - /run
        """,
        language="yaml"
    )

    st.subheader("6.8 Use User Namespaces (Remap Root)")
    st.code(
        """
        # Edit /etc/docker/daemon.json
        {
          "userns-remap": "default"
        }
        sudo systemctl restart docker
        """,
        language="json"
    )

    st.subheader("6.9 Secure the Docker Daemon Socket")
    st.write("Never mount `/var/run/docker.sock` into untrusted containers. Use authorization plugins if needed.")

    st.subheader("6.10 Image Scanning and Signing")
    st.code(
        """
        # Scan image for vulnerabilities (requires Docker Scout)
        docker scan <td>

        # Enable Docker Content Trust
        export DOCKER_CONTENT_TRUST=1
        docker push myuser/myimage:latest
        """,
        language="bash"
    )

    st.subheader("6.11 Network Security")
    st.code(
        """
        # Isolated internal network
        docker network create --internal secure_net
        docker run --net secure_net --name db mongo
        """,
        language="bash"
    )

    st.subheader("6.12 Secrets Management")
    st.write(
        "Never embed secrets in images or environment variables. Use Docker secrets (Swarm mode) or external stores like HashiCorp Vault."
    )

    st.subheader("6.13 Example: Secured Nginx Container")
    st.code(
        """
        docker run -d \\
          --name secure-nginx \\
          --cap-drop=ALL \\
          --cap-add=NET_BIND_SERVICE \\
          --read-only \\
          --tmpfs /var/cache/nginx:rw,noexec,nosuid,size=100M \\
          --tmpfs /var/run:rw,noexec,nosuid,size=1M \\
          --user 101:101 \\
          --security-opt=no-new-privileges:true \\
          nginx:1.25-alpine
        """,
        language="bash"
    )

    st.divider()

    # ============================================
    # SECTION 7: PUTTING IT ALL TOGETHER
    # ============================================
    st.header("7. Sample Secure Application")
    
    st.write("A minimal Python Flask app with a security‑hardened Dockerfile.")

    st.subheader("7.1 Project Structure")
    st.code(
        """
        my_secure_app/
        ├── app.py
        ├── requirements.txt
        └── Dockerfile
        """,
        language="text"
    )

    st.subheader("7.2 app.py")
    st.code(
        """
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def hello():
            return "Hello from a secure container!"

        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=8000)
        """,
        language="python"
    )

    st.subheader("7.3 requirements.txt")
    st.code("flask==3.0.0", language="text")

    st.subheader("7.4 Dockerfile (Secure Multi‑stage)")
    st.code(
        """
        FROM python:3.12-slim AS builder
        WORKDIR /app
        COPY requirements.txt .
        RUN pip install --no-cache-dir -r requirements.txt

        FROM gcr.io/distroless/python3
        COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
        COPY --from=builder /usr/local/bin /usr/local/bin
        COPY app.py /app/app.py
        WORKDIR /app
        USER nonroot:nonroot
        CMD ["app.py"]
        """,
        language="dockerfile"
    )

    st.subheader("7.5 Build and Run with Security Options")
    st.code(
        """
        docker build -t secure-flask .
        docker run -d \\
          --name flask-app \\
          --cap-drop=ALL \\
          --cap-add=NET_BIND_SERVICE \\
          --read-only \\
          --pids-limit=50 \\
          --memory=128m \\
          --security-opt=no-new-privileges:true \\
          -p 8000:8000 \\
          secure-flask
        """,
        language="bash"
    )

    st.divider()

    # ============================================
    # SUMMARY TABLE & BEST PRACTICES
    # ============================================
    st.header("8. Summary: Docker Best Practices")
    
    summary_data = {
        "Area": [
            "Images", 
            "Runtime", 
            "Networking", 
            "Secrets", 
            "Debugging"
        ],
        "Best Practice": [
            "Use minimal base images (Alpine, distroless); pin versions; scan for CVEs",
            "Run as non‑root; drop capabilities; set resource limits; use read‑only rootfs",
            "Use user‑defined bridge networks; avoid `--network host`; block unnecessary ports",
            "Never embed secrets; use Docker secrets or Vault; mount secrets as files",
            "Always check `docker logs` first; use `docker exec` for live inspection; override entrypoint for dead containers"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)

    st.markdown(
        """
        **Final takeaways**  
        - Docker containers are lightweight, portable, and fast – ideal for microservices and CI/CD.  
        - Understand the differences from VMs to choose the right isolation level.  
        - Master essential commands (`run`, `exec`, `logs`, `inspect`, `ps`) for daily work.  
        - Debug systematically: logs → exec → inspect → override entrypoint.  
        - Apply defense in depth: non‑root, dropped caps, read‑only FS, resource limits, and regular updates.
        """
    )

    st.divider()
    st.caption("© 2025 – Complete guide to Docker containers. All code examples are ready to use.")