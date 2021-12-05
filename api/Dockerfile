# ビルド用
FROM python:3.10.0-bullseye as builder

WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip install --no-cache-dir -r requirements.txt

# 実行用
FROM python:3.10.0-slim-bullseye as runner
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

RUN apt update && apt install --no-install-recommends -y \
    bash \
    curl \
    default-mysql-client \
    gcc \
    libmariadb-dev\
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN echo "alias ll='ls -lahF'" >> ~/.bashrc

WORKDIR /opt/app/src

# 実行環境でalembicコマンドを使用するため
RUN pip install --no-cache-dir alembic

EXPOSE 8000

CMD ["/bin/bash"]
