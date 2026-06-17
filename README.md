# 🚀 Learnifly - Gamified EdTech Platform

Learnifly is an interactive, gamified EdTech platform designed to transform traditional learning into an engaging, rewarding experience. By combining a Flask-driven web architecture with an intelligent content recommendation engine, the platform adapts to user performance while keeping engagement high through XP tracking, progress milestones, and dynamic dashboards.

---

## 🏗️ System Architecture

Learnifly uses a modular Model-View-Controller (MVC) pattern. The Flask application acts as the central controller, routing frontend requests, managing user sessions, and interfacing with the machine learning recommendation logic to serve personalized content.

```mermaid
graph TD
    subgraph Client_Side [Client Side / UI Layer]
        UI[HTML5 / CSS3 / JavaScript]
    end

    subgraph Backend_Flask [Flask Server / Control Layer]
        App{app.py}
        Templates[Jinja2 Templates]
        Static[Static Assets: JS/CSS]
    end

    subgraph ML_Engine [Intelligence & Gamification Layer]
        RecModel[rec_model.py]
        Cache[__pycache__]
    end

    UI <-->|HTTP Requests / Responses| App
    App -->|Renders Data to| Templates
    App -->|Serves| Static
    App <-->|Queries Engine| RecModel# Learnifly

sequenceDiagram
    autonumber
    actor User as Student / User
    participant App as Flask Backend (app.py)
    participant ML as Rec Engine (rec_model.py)
    participant DB as Session / Database Storage

    User->>App: Visit Landing Page (home.html)
    
    alt Account Creation
        User->>App: Submits Signup Details (signup.html)
        App->>DB: Persist User Profile & Initialize Stats (XP=0)
    else Existing User
        User->>App: Submits Credentials (login.html)
        App->>DB: Validate User Authenticity
    end
    
    DB-->>App: Authentication Successful
    App->>ML: Fetch Customized Content Paths (UserID, Current Streak)
    ML-->>App: Return Tailored Gamified Modules & Badges
    App->>User: Render Active Dashboard (profile.html with Recs)

login flask/
│
├── __pycache__/          # Compiled Python bytecode
│   └── rec_model.cpython-312.pyc
│
├── static/               # Frontend Assets & Client-Side Scripts
│   ├── images/           # Gamified assets (badges, levels, achievement icons)
│   ├── profile.css       # Layout styles for the student dashboard
│   ├── script.js         # Interactive UI handlers (animations, progress bar calculations)
│   └── style.css         # Global typography, color variables, and application themes
│
├── templates/            # Jinja2 Production Templates
│   ├── home.html         # Public landing page with product features
│   ├── login.html        # Secure user authentication portal
│   ├── profile.html      # Gamified user dashboard (tracks progress, streaks, & recommendations)
│   └── signup.html       # Onboarding and registration page
│
├── app.py                # Main Application Driver (Routing, Controllers & Sessions)
├── rec_model.py          # Recommendation Algorithm & Gamification Metric Rules
└── requirements.txt      # Project Python Dependencies


⚡ Quick Start & Deployment
Follow these steps to spin up your local development environment.

Prerequisites
Python 3.12+ installed on your host system.

Installation & Setup
Navigate to the workspace directory:

Bash
cd "login flask"
Initialize a localized environment:

Bash
python -m venv venv
Activate the virtual environment:

On Windows:

Bash
.\venv\Scripts\activate
On macOS/Linux:

Bash
source venv/bin/activate
Install necessary dependencies:

Bash
pip install -r requirements.txt
Launch the development server:

Bash
python app.py
Access the application:
Open your preferred browser and go to: http://127.0.0.1:5000/
