# Contributing to DevOps Project

Terima kasih telah tertarik untuk berkontribusi pada proyek ini! 🎉

## Cara Berkontribusi

### 1. Fork & Clone

```bash
# Fork repository di GitHub, kemudian clone
git clone https://github.com/YOUR_USERNAME/devops-project.git
cd devops-project
```

### 2. Setup Development Environment

```bash
# Install dependencies
make install

# Install pre-commit hooks
pre-commit install

# Setup environment variables
cp env.example .env
# Edit .env sesuai kebutuhan
```

### 3. Create Feature Branch

```bash
git checkout -b feature/amazing-feature
# atau
git checkout -b fix/bug-description
```

### 4. Make Changes

- Buat perubahan yang diperlukan
- Pastikan code mengikuti style guide
- Tambahkan tests untuk fitur baru
- Update documentation jika diperlukan

### 5. Test Your Changes

```bash
# Run tests
make test

# Run linters
make lint

# Format code
make format

# Run pre-commit hooks
pre-commit run --all-files
```

### 6. Commit Changes

```bash
git add .
git commit -m "feat: add amazing feature"
# atau
git commit -m "fix: resolve bug description"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 7. Push & Create Pull Request

```bash
git push origin feature/amazing-feature
```

Kemudian buat Pull Request di GitHub dengan deskripsi yang jelas.

## Development Guidelines

### Code Style

- Follow PEP 8 untuk Python code
- Gunakan Black untuk formatting
- Gunakan isort untuk import sorting
- Maximum line length: 120 characters

### Testing

- Tulis tests untuk semua fitur baru
- Maintain code coverage > 80%
- Tests harus dapat dijalankan secara independen

### Documentation

- Update README.md jika menambah fitur besar
- Dokumentasikan fungsi dan class dengan docstrings
- Update CHANGELOG.md untuk perubahan penting

### Pull Request Process

1. Pastikan semua tests pass
2. Pastikan code quality checks pass
3. Request review dari maintainers
4. Address review comments
5. Setelah approved, maintainer akan merge

## Questions?

Jika ada pertanyaan, silakan buat issue di GitHub atau hubungi maintainers.

Terima kasih atas kontribusinya! 🙏

