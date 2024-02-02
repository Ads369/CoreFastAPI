define set-default-container
	ifndef c
	c = web
	else ifeq (${c},all)
	override c=
	endif
endef

# Подключаем аргументы
.PHONY: test 


set-container:
	$(eval $(call set-default-container))
build:
	docker-compose -f docker-compose.dev.yml build
up:
	docker-compose -f docker-compose.dev.yml up -d
down:
	docker-compose -f docker-compose.dev.yml down
logs: set-container
	docker-compose -f docker-compose.dev.yml logs --tail=10 -f $(c)
restart: set-container
	docker-compose -f docker-compose.dev.yml restart $(c)
exec: set-container
	docker-compose -f docker-compose.dev.yml exec $(c) /bin/bash
test: set-container
	docker-compose -f docker-compose.dev.yml run --rm $(c) python -m pytest $(filter-out $@,$(MAKECMDGOALS))
compile-reqs: set-container
	docker-compose -f docker-compose.dev.yml run --rm $(c) bash -c 'pip install pip-tools && pip-compile'
pip-compile:
	pip-compile --output-file=requirements.txt requirements.in
pip-compile-dev:
	pip-compile --output-file=requirements.txt requirements-dev.in
pre-commit: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'pre-commit run --all-files'