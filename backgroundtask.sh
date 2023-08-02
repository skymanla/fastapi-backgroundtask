#!/bin/bash
echo 'docker compose start'
docker-compose -f fastapi-backgroundtask.yml up -d --build
docker restart fastapi-backgroundtask
echo 'docker compose end'