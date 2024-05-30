# Key-Value Store Project

## Overview
This project is a simple key-value store implemented using Django, with Celery for asynchronous task processing and Redis as the message broker and backend for Celery.

## Features
- CRUD operations for key-value pairs
- TTL (Time to Live) feature for key-value pairs
- Soft delete functionality
- Scheduled batch deletion of expired key-value pairs using Celery and Redis

## Prerequisites
- Python 3.x
- Redis
- PostgreSQL (optional, depending on your database choice)

## Installation

### Clone the Repository
```bash
git clone https://github.com/ShaktidharK1997/ShaktiKV.git
cd keyvalue-store
