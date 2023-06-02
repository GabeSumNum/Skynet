#!/bin/bash

cd /app/src && alembic upgrade head
python /app/src/main.py
