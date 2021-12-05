FROM python:3.10.0-slim-bullseye

RUN apt update && apt install --no-install-recommends -y \
    bash \
    curl \
    default-mysql-client \
    gcc \
    libmariadb-dev\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN echo "alias ll='ls -lahF'" >> ~/.bashrc

WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/app/src

EXPOSE 8000

CMD ["/bin/bash"]
