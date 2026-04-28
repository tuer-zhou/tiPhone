FROM python:3.12

RUN pip install -U pdm

ENV PDM_CHECK_UPDATE=false

COPY pyproject.toml pdm.lock
COPY src/

RUN pdm install --check --prod --no-editable

WORKDIR src/tiphone_server
CMD ["fastapi", "run"]