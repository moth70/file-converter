FROM python:3.13-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV EXIFTOOL_PATH=/usr/bin/exiftool
ENV FFMPEG_PATH=/usr/bin/ffmpeg

# Runtime dependency
RUN apt-get update && apt-get install -y ffmpeg exiftool python3-magic

ARG INSTALL_GIT=false
RUN if [ "$INSTALL_GIT" = "true" ]; then \
    apt-get install -y --no-install-recommends \
    git; \
    fi

# Cleanup
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY main.py /app/
COPY requirements.txt /app/
#RUN pip --no-cache-dir install \
#    /app/packages/markitdown[all] \
#    /app/packages/markitdown-sample-plugin
RUN pip install -r /app/requirements.txt

# Default USERID and GROUPID
ARG USERID=nobody
ARG GROUPID=nogroup

USER $USERID:$GROUPID

ENTRYPOINT [ "gunicorn","main:app", "-b", "0.0.0.0:8000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker" ]
