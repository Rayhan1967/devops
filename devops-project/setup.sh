#!/bin/bash

# DevOps Project Setup Script
# This script sets up the development environment

set -e

echo "🚀 Setting up DevOps Project..."

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker is not installed. Some features may not work."
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "⚠️  Docker Compose is not installed. Some features may not work."
fi

echo -e "${BLUE}📦 Installing Python dependencies...${NC}"
cd app
pip install -r requirements.txt
pip install pytest pytest-cov flake8 pylint black isort
cd ..

echo -e "${BLUE}🔧 Setting up pre-commit hooks...${NC}"
if command -v pre-commit &> /dev/null; then
    pip install pre-commit
    pre-commit install
    echo -e "${GREEN}✅ Pre-commit hooks installed${NC}"
else
    echo "⚠️  pre-commit not found. Installing..."
    pip install pre-commit
    pre-commit install
fi

echo -e "${BLUE}📝 Creating environment file...${NC}"
if [ ! -f .env ]; then
    cp env.example .env
    echo -e "${GREEN}✅ Created .env file from env.example${NC}"
    echo "⚠️  Please edit .env file with your configuration"
else
    echo "⚠️  .env file already exists, skipping..."
fi

echo -e "${BLUE}🐳 Building Docker image...${NC}"
if command -v docker &> /dev/null; then
    docker build -t devops-app:latest .
    echo -e "${GREEN}✅ Docker image built successfully${NC}"
else
    echo "⚠️  Docker not available, skipping Docker build"
fi

echo -e "${GREEN}✨ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "  1. Edit .env file with your configuration"
echo "  2. Run 'make test' to run tests"
echo "  3. Run 'make docker-run' to start the application"
echo "  4. Run 'make help' to see all available commands"
echo ""
echo "Happy coding! 🎉"

