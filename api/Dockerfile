FROM python:3.10.0

RUN apt install -y \
  bash \
  curl \
  wget \
  && apt clean

# alias
RUN echo "alias ll='ls -lahF'" >> ~/.bashrc

# work directory
WORKDIR /share
COPY ./ /share/

# pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/bin/bash"]
