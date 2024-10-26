# Real-Time Weather Monitoring Application

## Overview
A real-time weather monitoring application using the OpenWeatherMap API. The system retrieves weather data for major Indian cities, performs daily rollups, triggers alerts based on conditions, and stores data in a PostgreSQL database.

## Prerequisites
- Docker
- Docker Compose

## Setup
1. Clone the repository and navigate to the project folder.
2. Set the environment variable `OPENWEATHERMAP_API_KEY`.
3. Run the application:
   ```bash
   docker-compose up --build
