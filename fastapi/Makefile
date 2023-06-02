PKG=src

format: ## Applies linter formatting to code
	black ${PKG} -l 120
	isort ${PKG} -l 120 --profile black

lint: ## Checks for linting errors
	black --check ${PKG} -l 120
	isort --check ${PKG} -l 120 --profile black

.PHONY: test
test:
	python3 -m pytest -s ${PKG}/tests

.PHONY: test-detailed
test-detailed:
	python3 -m pytest -vv -s ${PKG}/tests

clean: ## Cleans the current directory of all generated python files
	pip3 install pyclean
	pyclean .
	rm -rf __pycache__
	find . -type f -name '*.pyc' -delete

install: requirements.txt ## Installs all requirements
	pip3 install -r requirements.txt


typecheck:
	mypy ${PKG}

test-cov: ## Produces the test coverage report
	python3 -m pytest tests --cov=./${PKG} --cov-report xml

# Alembic Related Actions
migrate: ## Creates a new migration, requires arg message="message" describing the migration
	docker-compose exec -w /app/src fastapi alembic revision --autogenerate -m $(message)

apply-migrate: ## Applies all migrations to the docker container running the fastapi
	docker-compose exec -w /app/src fastapi alembic upgrade head

.PHONY: help
help: ## Prompts help for every command
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
    awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@printf "\n"
	@echo "For more information please check the Makefile to know exactly what each target is doing."
# Uncomment below to build Sphinx docs

# build-docs:
# 	cd docs && make html && cd ..

# open-docs: build-docs
# 	open docs/_build/html/index.html
