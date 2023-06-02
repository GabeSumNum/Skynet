PKG=fastapi/test

format: ## Apply formatting
	black ${PKG} -l 120
	isort ${PKG}

lint: ## Check linting
	black --check ${PKG} -l 120
	isort --check ${PKG}

.PHONY: test
test: ## Run pytest
	python3 -m pytest -s ${PKG}

.PHONY: test-detailed
test-detailed: ## Run verbose pytest
	python3 -m pytest -vv -s ${PKG}

clean: ## Clean working directories
	pip3 install pyclean
	pyclean .
	rm -rf __pycache__
	find . -type f -name '*.pyc' -delete


install: fastapi/requirements.txt ## Install requirements
	pip3 install -r fastapi/requirements.txt


.PHONY: help
help: ## Prompts help for every command
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
    awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@printf "\n"
	@echo "For more information please check the Makefile to know exactly what each target is doing."
