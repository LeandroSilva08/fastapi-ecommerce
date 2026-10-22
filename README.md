# Scalable E-Commerce Platform

## Overview

A scalable e-commerce backend built using Python, FastAPI and a microservices architecture.

## Architecture

The project follows a microservices architecture, with independently deployable services organized within a single Git repository (monorepo).

Each service is responsible for a specific business domain.

## Microservices

| Service | Responsibility |
| --- | --- |
| User Service | User registration, authentication and profiles |
| Product Service | Product catalog, categories and inventory |
| Cart Service | Shopping cart management |
| Order Service | Order creation and lifecycle |
| Payment Service | Payment processing and transaction status |
| Notification Service | Order confirmation and notifications |

## Planned Technology Stack

- Python and FastAPI
- PostgreSQL
- Redis
- RabbitMQ
- Docker and Docker Compose
- Pytest
- GitHub Actions

## Current Progress

Phase 1: Project setup and initial User Service health endpoint.

## Local Development

### Install dependencies

`pip install -r requirements-dev.txt`

### Run User Service

From `services/users`:

`uvicorn app.main:app --reload --port 8001`

### Run tests

From `services/users`:

`python -m pytest tests -v`

## Roadmap

- [ ] User authentication
- [ ] Product catalog
- [ ] Shopping cart
- [ ] Order management
- [ ] Payment processing
- [ ] Event-driven notifications
- [ ] Containerization
- [ ] CI/CD
- [ ] Monitoring and scalability
