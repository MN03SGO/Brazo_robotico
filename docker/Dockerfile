# Archivo: docker/Dockerfile
FROM osrf/ros:humble-desktop-full

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-opencv \
    python3-numpy \
    libopencv-dev \
    v4l-utils \
    usbutils \
    nano \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python específicas
RUN pip3 install \
    mediapipe==0.10.7 \
    imutils \
    scipy

# Configurar workspace ROS
ENV ROS_WS=/home/ros2_ws
RUN mkdir -p $ROS_WS/src

# Configurar entorno ROS
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source $ROS_WS/install/setup.bash" >> ~/.bashrc || true

# Configurar directorio de trabajo
WORKDIR $ROS_WS

# Comando por defecto
CMD ["bash", "-l"]
