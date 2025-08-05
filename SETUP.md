# Development Setup Guide

This guide will help you set up the Task Management Application for development.

## Prerequisites

- Docker and Docker Compose
- Node.js 20+ (for local frontend development)
- Python 3.11+ (for local backend development)

## Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd simple-task-management
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Initialize the database**
   ```bash
   docker-compose exec backend python init_database.py
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Demo Credentials

After initialization, you can use these demo accounts:

- **Admin User**: admin@example.com / admin123
- **Regular User**: user@example.com / user123

## Local Development Setup

### Backend Development

1. **Set up Python environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set environment variables**
   ```bash
   export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/task_management"
   export SECRET_KEY="your-secret-key-for-development"
   ```

3. **Start PostgreSQL** (if not using Docker)
   ```bash
   # Using Docker for database only
   docker run -d --name postgres \
     -e POSTGRES_DB=task_management \
     -e POSTGRES_USER=postgres \
     -e POSTGRES_PASSWORD=postgres \
     -p 5432:5432 \
     postgres:15-alpine
   ```

4. **Initialize database**
   ```bash
   python init_database.py
   ```

5. **Start the backend server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Development

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server**
   ```bash
   npm run dev
   ```

3. **Access the frontend**
   - http://localhost:3000

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user

### Tasks
- `GET /api/v1/tasks` - Get user's tasks
- `POST /api/v1/tasks` - Create new task
- `GET /api/v1/tasks/{id}` - Get specific task
- `PUT /api/v1/tasks/{id}` - Update task
- `PATCH /api/v1/tasks/{id}/status` - Toggle task status
- `DELETE /api/v1/tasks/{id}` - Delete task

### Admin (Admin users only)
- `GET /api/v1/admin/users` - Get all users
- `GET /api/v1/admin/tasks` - Get all tasks

## Development Workflow

1. **Backend changes**: The FastAPI server will automatically reload when you make changes to Python files.

2. **Frontend changes**: The Vite dev server will hot-reload when you make changes to Vue files.

3. **Database changes**: If you modify models, you'll need to recreate the database or add proper migrations.

## Testing

### Backend Tests
```bash
cd backend
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Troubleshooting

### Common Issues

1. **Database connection errors**
   - Ensure PostgreSQL is running
   - Check DATABASE_URL environment variable
   - Verify database credentials

2. **CORS errors**
   - Ensure the backend is running on the correct port
   - Check CORS configuration in `app/main.py`

3. **Frontend build errors**
   - Clear node_modules and reinstall: `rm -rf node_modules && npm install`
   - Check TypeScript configuration

4. **Docker issues**
   - Stop all containers: `docker-compose down`
   - Remove volumes: `docker-compose down -v`
   - Rebuild: `docker-compose up --build`

### Logs

View logs for specific services:
```bash
# Backend logs
docker-compose logs backend

# Frontend logs
docker-compose logs frontend

# Database logs
docker-compose logs postgres
```

## Production Deployment

For production deployment, consider:

1. **Environment variables**: Set proper SECRET_KEY and DATABASE_URL
2. **Database**: Use a managed PostgreSQL service
3. **Frontend**: Build and serve static files
4. **Backend**: Use a production WSGI server like Gunicorn
5. **Reverse proxy**: Use Nginx for SSL termination and static file serving
6. **Monitoring**: Add logging and monitoring solutions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License 