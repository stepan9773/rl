build:
	@echo "Building container... 🪀"
	sudo docker build -t rl_app .
	@echo "Done 🪀"

run:
	@echo "Running container... 🪀"
	sudo docker run -p 8000:8000 -it rl_app
	@echo "Done 🪀"

install:
	@echo "Installing dependencies..."
	pipenv install Pipfile
	@echo "Done 🪀"

linter:
	@echo "Running black..."
	black --check .

	@echo "Running flake8... 🥎"
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude setting
	
	@echo "Running isort... 🥎"
	isort -c . --profile black
	
	@echo "Running bandit... 🥎"
	bandit -r .
	
	@echo "Done 🪀"
