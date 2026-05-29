FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel

RUN python -m pip install --no-cache-dir \
    torch==2.3.1 \
    torchvision==0.18.1 \
    torchaudio==2.3.1

RUN python -m pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    jupyter \
    transformers \
    datasets \
    accelerate \
    safetensors \
    flask \
    requests \
    huggingface_hub \
    nano \
    build-essential \
    curl \
    wget \
    tmux \
    htop \
    unzip \
    python3-venv

VOLUME ["/workspace", "/models"]

EXPOSE 8888
EXPOSE 5000

CMD ["python"]
