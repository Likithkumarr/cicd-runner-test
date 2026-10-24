# 🚀 Local Self-Hosted Runner CI/CD Test Project

This is a self-contained test project created to test **GitHub Actions CI/CD** directly on your local machine using a **GitHub Self-Hosted Runner** (100% Free, No Credit Card, No Public IP required).

---

## 📁 What is in this project?
- `app.py`: A lightweight FastAPI service.
- `test_app.py`: Pytest automated unit tests (runs in Stage 1 CI).
- `Dockerfile`: Containerizes the FastAPI app.
- `docker-compose.yml`: Deploys the container on port `8000` (runs in Stage 2 CD).
- `.github/workflows/deploy.yml`: The CI/CD pipeline using `runs-on: self-hosted`.

---

## 🛠️ Step 1: Push this Project to a New GitHub Repository

1. Go to [github.com/new](https://github.com/new) and create a repository called:
   `cicd-runner-test` (Public or Private).
2. Open PowerShell in this folder and run:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit for CI/CD test"
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/cicd-runner-test.git
   git push -u origin main
   ```

---

## 🏃 Step 2: Register Your Local Machine as a GitHub Runner

1. In your GitHub repository, click **Settings** (top bar).
2. On the left sidebar, click **Actions** → **Runners**.
3. Click the green button **"New self-hosted runner"**.
4. Select **Runner image**: **Windows** (or Linux if you prefer WSL).
5. GitHub will show you a few commands under **Download** and **Configure**.
   Open a separate PowerShell window and run those exact commands:

   ```powershell
   # Example of what GitHub shows you (copy the exact commands from GitHub!):
   mkdir actions-runner; cd actions-runner
   Invoke-WebRequest -Uri <DOWNLOAD_URL> -OutFile actions-runner.zip
   Add-Type -AssemblyName System.IO.Compression.FileSystem
   [System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD\actions-runner.zip", "$PWD")
   ./config.cmd --url https://github.com/YOUR_USER/cicd-runner-test --token <YOUR_TOKEN>
   ```
   *(Press Enter to accept all default names when prompted during `./config.cmd`).*

6. Start the runner:
   ```powershell
   ./run.cmd
   ```
   You will see:
   `Listening for Jobs...` 🟢 (Your machine is now connected to GitHub!)

---

## 🎯 Step 3: Trigger the CI/CD Pipeline!

1. Make a small edit in `app.py` (e.g., change `"version": "1.0.0"` to `"version": "1.0.1"`).
2. Commit and push:
   ```powershell
   git add app.py
   git commit -m "Bump version to 1.0.1"
   git push origin main
   ```
3. Watch what happens:
   - Your local PowerShell runner will say: **`Running job: Run Unit Tests`**!
   - Pytest runs and passes.
   - Then it runs: **`Running job: Deploy Container to Local Server`**!
   - Docker container starts up automatically!
4. Open your browser and go to:
   `http://localhost:8000`
   You will see the live response from your automatically deployed Docker container!
