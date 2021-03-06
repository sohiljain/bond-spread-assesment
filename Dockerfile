# Copyright (c) 2020 Databot Inc. All rights reserved.
# @author Sohil Jain

FROM python:3.7-stretch
WORKDIR /submission

RUN apt-get update
RUN pip install pipenv
RUN pipenv install --skip-lock
ENV PYTHONPATH "${PYTONPATH}:/submission"

ENTRYPOINT ["/submission/run.sh"]
