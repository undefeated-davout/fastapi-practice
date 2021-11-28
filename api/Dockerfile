FROM python:3.10.0

RUN apt update && apt install -y \
    bash \
    curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# alias
RUN echo "alias ll='ls -lahF'" >> ~/.bashrc

# work directory
WORKDIR /share
COPY ./ /share/

# pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/bin/bash"]
