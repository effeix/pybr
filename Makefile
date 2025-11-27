.PHONY: clean build publish test

clean:
	@echo "🧹 Cleaning artifacts..."
	rm -rf dist/ build/ *.egg-info .pytest_cache/ .ruff_cache/
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "_version.py" -delete
	@echo "✨ Clean."

build: clean
	@echo "📦 Building package..."
	uv build

test:
	@echo "🧪 Running tests..."
	uv run pytest

publish: build
	@echo "🚀 Publishing..."
	uv publish