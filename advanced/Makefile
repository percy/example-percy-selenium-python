VENV=.venv/bin
REQUIREMENTS=requirements.txt

$(VENV):
	python3 -m venv .venv
	$(VENV)/python3 -m pip install --upgrade pip

$(VENV)/.deps: $(REQUIREMENTS) | $(VENV)
	$(VENV)/pip install -r $(REQUIREMENTS)
	touch $(VENV)/.deps

.PHONY: venv install clean test test-advanced test-advanced-ci

venv install: $(VENV)/.deps

clean:
	rm -rf .venv .pytest_cache __pycache__ tests/__pycache__ advanced-requests.json

# Local run against a real PERCY_TOKEN.
test test-advanced: install
	npx --no-install percy exec -- $(VENV)/python3 -m pytest tests/ -v

# CI run in --testing mode + capture requests file.
test-advanced-ci: install
	PERCY_TOKEN=fake_token npx --no-install percy exec --testing -- bash -c '\
		$(VENV)/python3 -m pytest tests/ -v; \
		ec=$$?; \
		curl -fsS http://localhost:5338/test/requests > advanced-requests.json || true; \
		exit $$ec'
