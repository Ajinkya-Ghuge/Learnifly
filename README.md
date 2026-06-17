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
    App <-->|Queries Engine| RecModel
