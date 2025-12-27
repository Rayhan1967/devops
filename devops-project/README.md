# DevOps Project - Complete CI/CD Pipeline

Proyek DevOps lengkap dengan semua tools dan best practices untuk modern software development dan deployment.

## 📋 Daftar Isi

- [Fitur](#fitur)
- [Struktur Proyek](#struktur-proyek)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Usage](#usage)
- [CI/CD Pipeline](#cicd-pipeline)
- [Monitoring](#monitoring)
- [Infrastructure as Code](#infrastructure-as-code)
- [Contributing](#contributing)

## ✨ Fitur

- ✅ **CI/CD Pipeline** dengan GitHub Actions
- ✅ **Containerization** dengan Docker & Docker Compose
- ✅ **Orchestration** dengan Kubernetes (K8s)
- ✅ **Infrastructure as Code** dengan Terraform
- ✅ **Configuration Management** dengan Ansible
- ✅ **Monitoring** dengan Prometheus & Grafana
- ✅ **Load Balancing** dengan Nginx
- ✅ **Auto-scaling** dengan Kubernetes HPA
- ✅ **Security Scanning** dengan Trivy
- ✅ **Code Quality** dengan Linters & Formatters
- ✅ **Testing** dengan pytest & coverage
- ✅ **Git Hooks** dengan pre-commit

## 📁 Struktur Proyek

```
devops-project/
├── app/                      # Application code
│   ├── main.py              # Flask application
│   ├── requirements.txt     # Python dependencies
│   └── tests/               # Unit tests
│       └── test_app.py
├── kubernetes/              # Kubernetes manifests
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── configmap.yaml
│   └── secret.yaml
├── terraform/               # Infrastructure as Code
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── ansible/                 # Configuration Management
│   ├── playbook.yml
│   ├── inventory.ini
│   └── templates/
├── monitoring/              # Monitoring configs
│   ├── prometheus/
│   └── grafana/
├── nginx/                   # Nginx configuration
│   └── nginx.conf
├── .github/
│   └── workflows/          # CI/CD pipelines
│       ├── ci.yml
│       └── cd.yml
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── Makefile               # Common tasks
├── .pre-commit-config.yaml # Git hooks
└── README.md              # This file
```

## 🔧 Prerequisites

Sebelum memulai, pastikan Anda telah menginstall:

- **Python 3.11+**
- **Docker & Docker Compose**
- **Kubernetes CLI (kubectl)**
- **Terraform >= 1.0**
- **Ansible >= 2.9**
- **Make** (opsional, untuk menggunakan Makefile)
- **Git**

### Install Dependencies

```bash
# Python dependencies
pip install -r app/requirements.txt
pip install pytest pytest-cov flake8 pylint black isort

# Pre-commit hooks
pip install pre-commit
pre-commit install
```

## 🚀 Quick Start

### 1. Development dengan Docker Compose

```bash
# Build dan jalankan semua services
make docker-run

# Atau menggunakan docker-compose langsung
docker-compose up -d

# Lihat logs
make docker-logs

# Stop services
make docker-stop
```

Aplikasi akan tersedia di:
- **App**: http://localhost:5000
- **Nginx**: http://localhost:80
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin123)

### 2. Testing

```bash
# Run semua tests
make test

# Run dengan coverage
cd app && pytest tests/ -v --cov=. --cov-report=html
```

### 3. Code Quality

```bash
# Format code
make format

# Lint code
make lint
```

### 4. Build Docker Image

```bash
# Build image
make docker-build

# Build dengan tag tertentu
docker build -t devops-app:v1.0.0 .
```

## 🛠 Teknologi yang Digunakan

### Application Stack
- **Python 3.11** - Programming language
- **Flask** - Web framework
- **Gunicorn** - WSGI HTTP Server
- **PostgreSQL** - Relational database
- **Redis** - Caching & session storage

### DevOps Tools

#### Containerization
- **Docker** - Container runtime
- **Docker Compose** - Multi-container orchestration

#### Orchestration
- **Kubernetes** - Container orchestration
  - Deployments
  - Services
  - Ingress
  - HPA (Horizontal Pod Autoscaler)
  - ConfigMaps & Secrets

#### CI/CD
- **GitHub Actions** - Continuous Integration/Deployment
  - Automated testing
  - Security scanning
  - Docker image building
  - Kubernetes deployment

#### Infrastructure as Code
- **Terraform** - Cloud infrastructure provisioning
  - AWS EKS cluster
  - VPC & Networking
  - RDS database
  - Security groups

#### Configuration Management
- **Ansible** - Server configuration & deployment
  - Automated server setup
  - Application deployment
  - Service management

#### Monitoring & Observability
- **Prometheus** - Metrics collection
- **Grafana** - Visualization & dashboards
- **Nginx** - Reverse proxy & load balancer

#### Security
- **Trivy** - Container vulnerability scanning
- **Pre-commit hooks** - Code quality checks
- **Linters** - Code analysis

## 📖 Usage

### Makefile Commands

Proyek ini dilengkapi dengan Makefile untuk memudahkan operasi umum:

```bash
make help              # Tampilkan semua commands
make install           # Install dependencies
make test              # Run tests
make lint              # Run linters
make format            # Format code
make docker-build      # Build Docker image
make docker-run        # Run dengan Docker Compose
make docker-stop       # Stop Docker Compose
make k8s-deploy        # Deploy ke Kubernetes
make k8s-delete        # Delete dari Kubernetes
make terraform-init    # Initialize Terraform
make terraform-plan    # Plan Terraform changes
make terraform-apply   # Apply Terraform changes
make ansible-deploy    # Deploy dengan Ansible
make clean             # Clean temporary files
```

### Docker Commands

```bash
# Build image
docker build -t devops-app:latest .

# Run container
docker run -p 5000:5000 devops-app:latest

# Run dengan environment variables
docker run -p 5000:5000 -e ENVIRONMENT=production devops-app:latest
```

### Kubernetes Commands

```bash
# Deploy semua resources
kubectl apply -f kubernetes/

# Check status
kubectl get all -n devops-app

# View logs
kubectl logs -f deployment/devops-app -n devops-app

# Scale deployment
kubectl scale deployment/devops-app --replicas=5 -n devops-app

# Delete semua resources
kubectl delete -f kubernetes/
```

### Terraform Commands

```bash
# Initialize
cd terraform
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy
```

### Ansible Commands

```bash
# Deploy dengan Ansible
cd ansible
ansible-playbook -i inventory.ini playbook.yml

# Check syntax
ansible-playbook -i inventory.ini playbook.yml --syntax-check

# Dry run
ansible-playbook -i inventory.ini playbook.yml --check
```

## 🔄 CI/CD Pipeline

### Continuous Integration (CI)

Pipeline CI dijalankan pada setiap push dan pull request:

1. **Lint** - Code quality checks (Black, isort, Flake8, Pylint)
2. **Test** - Unit tests dengan coverage
3. **Security Scan** - Vulnerability scanning dengan Trivy
4. **Build** - Build Docker image
5. **Deploy Staging** - Auto-deploy ke staging environment

### Continuous Deployment (CD)

Pipeline CD dijalankan pada tags atau manual trigger:

1. **Deploy** - Deploy ke production/staging
2. **Smoke Tests** - Verify deployment
3. **Notifications** - Send deployment status

Workflow files:
- `.github/workflows/ci.yml` - CI pipeline
- `.github/workflows/cd.yml` - CD pipeline

## 📊 Monitoring

### Prometheus

- **URL**: http://localhost:9090
- **Targets**: Application, Node Exporter, Redis, PostgreSQL
- **Alert Rules**: CPU, Memory, Error Rate

### Grafana

- **URL**: http://localhost:3000
- **Username**: admin
- **Password**: admin123
- **Dashboards**: Pre-configured dashboards for application metrics

### Access Monitoring

```bash
# Start monitoring stack
make monitoring-up

# View Prometheus
open http://localhost:9090

# View Grafana
open http://localhost:3000
```

## ☁️ Infrastructure as Code

### Terraform

Infrastructure didefinisikan dengan Terraform untuk AWS:

- **EKS Cluster** - Kubernetes cluster
- **VPC** - Virtual Private Cloud
- **Subnets** - Public & Private subnets
- **RDS** - PostgreSQL database
- **Security Groups** - Network security
- **IAM Roles** - Access control

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

## 🔐 Security

### Security Best Practices

- ✅ Non-root user di Docker containers
- ✅ Secrets management dengan Kubernetes Secrets
- ✅ Security scanning dengan Trivy
- ✅ HTTPS dengan TLS certificates
- ✅ Network policies
- ✅ Resource limits di Kubernetes

### Secrets Management

**PENTING**: Jangan commit secrets ke repository!

- Gunakan Kubernetes Secrets untuk production
- Gunakan environment variables untuk development
- Gunakan secret management tools (AWS Secrets Manager, HashiCorp Vault)

## 📝 Environment Variables

```bash
ENVIRONMENT=production
APP_VERSION=1.0.0
DEBUG=false
PORT=5000
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://host:6379/0
```

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Development Workflow

1. Install pre-commit hooks: `pre-commit install`
2. Create feature branch
3. Make changes
4. Run tests: `make test`
5. Format code: `make format`
6. Commit (pre-commit hooks will run automatically)
7. Push and create PR

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- DevOps Team

## 🙏 Acknowledgments

- All open-source tools and libraries used in this project
- DevOps community for best practices and guidelines

## 📞 Support

Untuk pertanyaan atau bantuan:
- Create an issue di GitHub
- Check documentation
- Contact DevOps team

---

**Happy DevOps! 🚀**

