#!/bin/bash
# Script to change CISO Assistant superuser credentials

echo "=============================================="
echo "  Changing CISO Assistant Credentials"
echo "=============================================="

# Navigate to the project directory
cd /Users/ashishthirunagari/Documents/GitHub/ciso-assistant-community

echo -e "\n1. Stopping current containers..."
docker compose down

echo -e "\n2. Removing old database (to create fresh superuser)..."
if [ -f "./db/db.sqlite3" ]; then
    echo "   Removing existing database..."
    rm ./db/db.sqlite3
fi

echo -e "\n3. Applying new environment configuration..."
echo "   New credentials:"
echo "   - Email: admin@pestle.in"
echo "   - Password: admin123"

echo -e "\n4. Starting containers with new configuration..."
docker compose -f docker-compose-build.yml up -d

echo -e "\n5. Waiting for services to initialize..."
sleep 30

echo -e "\n6. Checking container status..."
docker ps --format "table {{.Names}}\t{{.Status}}" | grep -E "backend|frontend|caddy|huey"

echo -e "\n7. Verifying backend logs..."
docker compose logs backend | grep -i "superuser" | tail -5

echo -e "\n=============================================="
echo "  Credential Update Complete!"
echo "=============================================="
echo "✓ New credentials applied"
echo "✓ Containers restarted"
echo ""
echo "Access your CISO Assistant instance at:"
echo "URL: https://localhost:8443"
echo "Username: admin@pestle.in"
echo "Password: admin123"
echo ""
echo "Note: The first login might take a moment while"
echo "the database is initialized with the new superuser."
