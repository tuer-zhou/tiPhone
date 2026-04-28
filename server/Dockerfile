FROM python:3.10-alpine

#RUN pip install -U pdm

#ENV PDM_CHECK_UPDATE=false

COPY pyproject.toml pdm.lock requirements.txt /project/
COPY src/ /project/src

WORKDIR /project/
#RUN pdm lock
#RUN pdm install --check --prod --no-editable
RUN pip install -r requirements.txt

WORKDIR /project/src/tiphone_server
CMD ["fastapi", "run"]