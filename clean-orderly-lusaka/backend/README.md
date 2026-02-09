# Clean & Orderly Lusaka

A civic tech platform for identifying and tracking urban issues in sanitation, traffic, and city management across Lusaka.

## About

Instead of just complaining about urban problems, report and track them. Clean & Orderly Lusaka lets citizens document issues, visualize problem areas on a map, and monitor resolution progress — turning civic concern into actionable data.

**Mission:** Transform urban management through community-driven data collection and transparent issue tracking.

## Features

- **Issue Reporting** — Submit sanitation, traffic, or infrastructure problems with photos
- **Interactive Map** — Visualize reported issues across Lusaka neighborhoods  
- **Status Tracking** — Follow issue resolution from reported to resolved
- **Data Dashboard** — View statistics and trends in urban management

## Tech Stack

### Backend
- Django — Python web framework
- Django REST Framework — API development
- PostgreSQL — Database
- Redis — Caching

### Frontend
- Next.js — React framework
- Tailwind CSS — Styling
- Leaflet/Mapbox — Interactive maps

### Deployment
- Docker — Containerization
- Nginx — Web server
- Gunicorn — WSGI server

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL 14+
- Git

### Installation

1. **Clone the repository**
   \\\ash
   git clone https://github.com/Suwilamji/clean-orderly-lusaka.git
   cd clean-orderly-lusaka
   \\\

2. **Set up Backend**
   \\\ash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   \\\

3. **Set up Frontend**
   \\\ash
   cd ../frontend
   npm install
   npm run dev
   \\\

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Project Structure

\\\
clean-orderly-lusaka/
├── backend/          # Django API server
│   ├── config/      # Django settings
│   ├── reports/     # Issue reporting app
│   ├── manage.py
│   └── requirements.txt
├── frontend/        # Next.js web interface
│   ├── pages/       # Next.js pages
│   ├── components/  # React components
│   ├── styles/      # CSS/Tailwind
│   └── package.json
├── docs/            # Documentation
├── README.md        # This file
└── .gitignore       # Git ignore rules
\\\

## Civic Context

Clean & Orderly Lusaka addresses:
- **Sanitation** — Overflowing bins, illegal dumping, drainage issues
- **Traffic** — Congestion, road damage, missing signage  
- **Urban Management** — Street lighting, public space maintenance, infrastructure

By documenting issues systematically, we create data that can:
1. Inform municipal planning
2. Prioritize resource allocation
3. Measure improvement over time
4. Engage citizens in urban stewardship

## Team

- **Suwilanji Sinyangwe** — Project Lead & Full-Stack Development
- **Contributors Welcome** — Join us in building civic tech for Lusaka

## Contact

- **Phone**: +86 1850 7916 548
- **Email**: sinyangwesuwilanji530@gmail.com
- **GitHub**: [@Suwilamji](https://github.com/Suwilamji)

## License

Open for community use and collaboration.
