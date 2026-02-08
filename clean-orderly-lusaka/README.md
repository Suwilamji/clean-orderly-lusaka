# Clean & Orderly Lusaka

A civic tech platform for identifying and tracking urban issues in sanitation, traffic, and city management.

## Project Goals

- **Identify Problem Areas**: Crowdsource data on sanitation issues, traffic congestion, and urban management challenges
- **Promote Civic Engagement**: Provide a neutral platform for citizens to report and track civic issues
- **Data-Driven Insights**: Generate actionable data for community organizations and local authorities
- **Transparent Tracking**: Allow public monitoring of reported issues and their resolution status

## Technology Stack

### Backend
- **Django** (Python) - REST API
- **Django REST Framework** - API development
- **PostgreSQL** - Database
- **Redis** - Caching (optional)

### Frontend
- **Next.js** (React) - Web interface
- **Tailwind CSS** - Styling
- **Leaflet/Mapbox** - Interactive maps
- **Axios** - API communication

### DevOps
- **Docker** - Containerization
- **Nginx** - Web server
- **Gunicorn** - WSGI server

## Getting Started

### Prerequisites
- Python 3.9+ and pip
- Node.js 18+ and npm/yarn
- PostgreSQL 14+
- Git

### Installation

#### 1. Clone the repository
\\\ash
git clone https://github.com/Suwilamji/clean-orderly-lusaka.git
cd clean-orderly-lusaka
\\\

#### 2. Set up Backend (Django)
\\\ash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# Edit .env with your database settings

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
\\\

#### 3. Set up Frontend (Next.js)
\\\ash
cd ../frontend
npm install
cp .env.local.example .env.local
# Edit .env.local with your API URL

npm run dev
\\\

#### 4. Access the application
- Backend API: http://localhost:8000
- Frontend: http://localhost:3000
- Admin panel: http://localhost:8000/admin

## Features

### Phase 1
- [x] Django REST API setup
- [x] Next.js frontend structure
- [ ] User authentication (JWT)
- [ ] Issue reporting form
- [ ] Interactive map with markers

### Phase 2
- [ ] Photo upload for issues
- [ ] Issue status tracking
- [ ] Email/SMS notifications
- [ ] Admin dashboard

### Future
- [ ] Mobile app (React Native)
- [ ] Real-time updates (WebSockets)
- [ ] Data analytics dashboard
- [ ] Public API for developers

## Database Schema (PostgreSQL)

\\\sql
-- Example tables
-- Users, Issues, Categories, Comments, StatusUpdates
\\\

## Contributing

We welcome contributions! Please see \CONTRIBUTING.md\ for guidelines.

1. Fork the repository
2. Create a feature branch (\git checkout -b feature/improvement\)
3. Commit changes (\git commit -m 'Add some improvement'\)
4. Push to branch (\git push origin feature/improvement\)
5. Open a Pull Request

## Contact

**Project Lead**: Suwilanji Sinyangwe
- **Phone**: +86 1850 7916 548
- **Email**: sinyangwesuwilanji530@gmail.com
- **GitHub**: [@Suwilamji](https://github.com/Suwilamji)

## License

This project is open for community use and collaboration.
