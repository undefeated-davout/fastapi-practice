# 実行用
FROM node:16.13.1-bullseye-slim as runner

RUN apt update && apt install -y \
    bash \
    curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN echo "alias ll='ls -lahF'" >> ~/.bashrc

RUN npm install -g npm@8.1.4

WORKDIR /opt/app/src

EXPOSE 3000
EXPOSE 9229

CMD ["/bin/bash"]
