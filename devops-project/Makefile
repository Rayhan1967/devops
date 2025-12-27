.PHONY: help install test lint format docker-build docker-run docker-stop k8s-deploy k8s-delete terraform-init terraform-plan terraform-apply terraform-destroy ansible-deploy clean

# Variables
APP_NAME=devops-app
DOCKER_IMAGE=devops-app:latest
NAMESPACE=devops-app
TERRAFORM_DIR=terraform
ANSIBLE_DIR=ansible

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install Python dependencies
	cd app && pip install -r requirements.txt
	cd app && pip install pytest pytest-cov flake8 pylint black isort

test: ## Run tests
	cd app && pytest tests/ -v --cov=. --cov-report=term --cov-report=html

lint: ## Run linters
	cd app && flake8 . --max-line-length=120
	cd app && pylint app/
	cd app && black --check .
	cd app && isort --check-only .

format: ## Format code
	cd app && black .
	cd app && isort .

docker-build: ## Build Docker image
	docker build -t $(DOCKER_IMAGE) .

docker-run: ## Run application with Docker Compose
	docker-compose up -d

docker-stop: ## Stop Docker Compose services
	docker-compose down

docker-logs: ## View Docker Compose logs
	docker-compose logs -f app

k8s-deploy: ## Deploy to Kubernetes
	kubectl apply -f kubernetes/namespace.yaml
	kubectl apply -f kubernetes/configmap.yaml
	kubectl apply -f kubernetes/secret.yaml
	kubectl apply -f kubernetes/deployment.yaml
	kubectl apply -f kubernetes/service.yaml
	kubectl apply -f kubernetes/ingress.yaml
	kubectl apply -f kubernetes/hpa.yaml

k8s-delete: ## Delete Kubernetes resources
	kubectl delete -f kubernetes/ --ignore-not-found=true

k8s-logs: ## View Kubernetes logs
	kubectl logs -f deployment/devops-app -n $(NAMESPACE)

k8s-status: ## Check Kubernetes deployment status
	kubectl get all -n $(NAMESPACE)

terraform-init: ## Initialize Terraform
	cd $(TERRAFORM_DIR) && terraform init

terraform-plan: ## Plan Terraform changes
	cd $(TERRAFORM_DIR) && terraform plan

terraform-apply: ## Apply Terraform changes
	cd $(TERRAFORM_DIR) && terraform apply

terraform-destroy: ## Destroy Terraform infrastructure
	cd $(TERRAFORM_DIR) && terraform destroy

terraform-validate: ## Validate Terraform configuration
	cd $(TERRAFORM_DIR) && terraform validate

terraform-fmt: ## Format Terraform files
	cd $(TERRAFORM_DIR) && terraform fmt -recursive

ansible-deploy: ## Deploy with Ansible
	cd $(ANSIBLE_DIR) && ansible-playbook -i inventory.ini playbook.yml

ansible-check: ## Check Ansible playbook syntax
	cd $(ANSIBLE_DIR) && ansible-playbook -i inventory.ini playbook.yml --syntax-check

clean: ## Clean temporary files
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	rm -rf .terraform
	rm -f terraform.tfstate terraform.tfstate.backup

security-scan: ## Run security scans
	docker run --rm -v $(PWD):/app -w /app aquasec/trivy fs .
	cd app && safety check || true

monitoring-up: ## Start monitoring stack
	docker-compose -f docker-compose.monitoring.yml up -d

monitoring-down: ## Stop monitoring stack
	docker-compose -f docker-compose.monitoring.yml down

all: install test lint docker-build ## Run all checks and build

