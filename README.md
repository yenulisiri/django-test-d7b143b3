# Django Test Project

Auto-generated Django project with comprehensive testing.

## Test Status

![Django Tests](https://github.com/yenulisiri/django-test-d7b143b3/actions/workflows/django-tests.yml/badge.svg)

## Automated Testing

This repository includes automated testing via GitHub Actions that runs:

- Django unit tests on every push and pull request
- Code linting and formatting checks
- Test coverage reporting
- Django deployment checks

### Test Results

You can view the latest test results by clicking the badge above or visiting the Actions tab at:
https://github.com/yenulisiri/django-test-d7b143b3/actions

### Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test --verbosity=2
```
