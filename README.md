# Simple Task Management Application

A modern, full-stack task management application built with FastAPI (backend) and Vue.js 3 (frontend).

## Features

### User Features
- ✅ User authentication (register/login)
- ✅ Create, read, update, delete tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Task filtering and sorting
- ✅ Responsive design for mobile devices

### Admin Features
- ✅ View all users' tasks
- ✅ User management
- ✅ Task statistics and overview
- ✅ Advanced filtering options

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Reliable relational database
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migrations
- **JWT** - Authentication tokens
- **Pydantic** - Data validation

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **TypeScript** - Type-safe JavaScript
- **Pinia** - State management
- **Vue Router** - Client-side routing
- **Axios** - HTTP client
- **Vite** - Build tool

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 20+ (for local development)

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd simple-task-management
```

2. Start the application:
```bash
docker-compose up -d
```

3. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Local Development

1. Backend setup:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2. Frontend setup:
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
simple-task-management/
├── backend/
│   ├── app/
│   │   ├── api/           # API routes
│   │   ├── core/          # Configuration
│   │   ├── crud/          # Database operations
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   └── main.py        # FastAPI app
│   ├── alembic/           # Database migrations
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/    # Vue components
│   │   ├── views/         # Page components
│   │   ├── store/         # Pinia stores
│   │   ├── services/      # API services
│   │   └── router/        # Vue Router
│   └── package.json
├── docker-compose.yml
└── README.md
```

## API Documentation

The API documentation is available at http://localhost:8000/docs when the backend is running.

### Key Endpoints

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user
- `GET /tasks` - Get user's tasks
- `POST /tasks` - Create new task
- `PUT /tasks/{id}` - Update task
- `PATCH /tasks/{id}/status` - Toggle task status
- `DELETE /tasks/{id}` - Delete task
- `GET /admin/tasks` - Get all tasks (admin only)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License 