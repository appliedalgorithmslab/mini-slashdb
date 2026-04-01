# mini-slashdb

A lightweight Python backend that exposes relational database resources through REST-style endpoints using FastAPI and SQLAlchemy. This project also demonstrates how backend APIs integrate with frontend applications in a full-stack web architecture.

## Why this project exists

This project demonstrates a simplified database-to-API layer: mapping relational tables and relationships into clean HTTP endpoints with filtering, validation, and JSON responses.

## Features

- Resource-oriented REST endpoints
- SQLAlchemy ORM models for relational data
- Query-parameter filtering
- Nested resource routes
- FastAPI request/response validation
- Modular backend architecture
- Basic API testing with pytest

## Example endpoints

- GET /users
- GET /users?email=alice@example.com
- GET /users/{user_id}
- POST /users
- GET /orders
- POST /orders
- GET /users/{user_id}/orders

## Architecture

- db.py — database setup
- models.py — ORM models
- schemas.py — API schemas
- routes/ — endpoints
- services/ — business logic
- tests/ — test suite

## Tech stack

Python, FastAPI, SQLAlchemy, SQLite, pytest

## Run locally

pip install -r requirements.txt  
uvicorn app.main:app --reload

## Run tests

pytest
