# Shorten Links

## Description

A full-stack URL shortening application that transforms long URLs into shortened, shareable links. This project consists of a Django REST API backend and a Vue.js frontend, providing a clean and intuitive interface for URL shortening.

### Features
- Transform long URLs into shortened links
- Clean and responsive user interface
- RESTful API backend
- Docker containerization for easy deployment
- ESLint integration for code quality
- Comprehensive testing setup
- Error handling and user feedback

### Technology Stack
- **Backend**: Django 5.0.4 with Django REST Framework
- **Frontend**: Vue.js 3.4 with Vite
- **Containerization**: Docker and Docker Compose
- **Testing**: Vitest for frontend testing
- **Code Quality**: ESLint with Standard configuration

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
   ```bash
   git clone git@github.com:ihleonel/shorten-links.git
   cd shorten-links
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - **Frontend**: http://localhost:5173
   - **Backend API**: http://localhost:8000

4. To stop the application:
   ```bash
   docker-compose down
   ```

### Development Mode

The Docker Compose setup includes volume mounts for live code reloading during development:
- Backend changes are reflected automatically
- Frontend changes trigger hot module replacement

## Todo
- [x] Add eslint
- [x] Add test
- [x] Add funcionalities
- [x] Add styles
- [x] Add django
- [x] Dockering this application
- [x] Feedback errors
