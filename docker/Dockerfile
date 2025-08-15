
FROM osrf/ros:humble-desktop-full

# sistema depedencias
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

# dependencias py
RUN pip3 install \
    setuptools \
    mediapipe==0.10.7 \
    imutils \
    scipy

# ROS
ENV ROS_WS=/home/ros2_ws
RUN mkdir -p $ROS_WS/src

# entorno ROS
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source $ROS_WS/install/setup.bash" >> ~/.bashrc || true

# Configurar directorio
WORKDIR $ROS_WS

# Comando por defecto
CMD ["bash", "-l"]
