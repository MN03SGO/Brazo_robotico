
# Brazo robotico con ROS

El objetivo es desarrollar un sistema robótico capaz de percibir su entorno mediante una cámara web, identificar objetos de colores, y manipularlos de forma inteligente. El robot podrá realizar dos tareas principales:

Modo de Clasificación: Si se coloca un cubo de un color específico en una base central (gris), el robot lo recogerá y lo moverá a la zona correspondiente a su color.

Modo de Apilamiento por Gestos: Al detectar un gesto específico con la mano (por ejemplo, el número "2"), el robot seleccionará un cubo al azar de los que ya están clasificados y lo apilará sobre otro cubo en la base central.

Este proyecto nace de la creatividad, las ganas de curiosear y de un video que me encontre (JAJAJA)

## Componentes usados (Posible a modificaciones)

-- Hardware 

**Laptop:** Lenovo ThinkBook con Debian 13.

**Cámara:** Logitech 720p

**Brazo Robótico:** Brazo casero con servos y chunches

-- Software

**OS:** Debian 13 "Trixie" .

**ROS 2 Jazzy Jalisco**

**Brazo Robótico:** Brazo casero con servos y chunches.

**Biblioteca de Visión:** OpenCV

**Herramientas:**Python, docker


## Estructura

```javascript
└[~/robot_cube_sorter]> tree -L 3

├── config
├── docker
│   ├── docker-compose.yaml
│   ├── Dockerfile
│   └── shared_data
├── docs
├── LICENSE
├── README.md
├── scripts
│   ├── setup.sh
│   └── test_camera.sh
└── src
    └── cube_sorter_package
        ├── config
        ├── cube_sorter_package
        ├── launch
        ├── package.xml
        ├── resource
        ├── setup.cfg
        ├── setup.py
        └── test

13 directories, 9 files
```


## Installation

Clonar el repositorio

```bash
  git clone https://github.com/MN03SGO/Brazo_robotico.git
 
```
Dependiendo en que directorio lo clonaste, cambiara tu manera de entrar a la carpeta. En mi caso en /home/sigaran/robot_cube_sorter

Si quieres observar la estructura ejecuta
```bash
  sudo apt install nala -y
  sudo nala install tree -L 3


├── config
├── docker
│   ├── docker-compose.yaml
│   ├── Dockerfile
│   └── shared_data
├── docs
├── LICENSE
├── README.md
├── scripts
│   ├── setup.sh
│   └── test_camera.sh
└── src
    └── cube_sorter_package
        ├── config
        ├── cube_sorter_package
        ├── launch
        ├── package.xml
        ├── resource
        ├── setup.cfg
        ├── setup.py
        └── test
```  
Paso para ejecutar contenedor y dar permiso chmod 
* Dar permisos  y ejecutar sript
```bash
chmod +x scripts/*.sh
./scripts/setup.sh
```
* Ir al directorio "docker" y ejecutar contenedor  
```bash
cd docker
docker compose up -d
```
* Entrar al contenedor y construir el paquete del proyecto
```bash
docker exec -it cube_sorter_robot bash
colcon build --packages-select cube_sorter_package
```
* Recargar el entorno
```bash
source install/setup.bash
```
* Ejecutar pruba de camara
```bash
ros2 run cube_sorter_package camera_node
--- LA SALIDA ESPERADA TIENE QUE SER ---
root@debian:/home/ros2_ws# ros2 run cube_sorter_package camera_node
[INFO] [1755406736.895908980] [camera_node]: Cámara configurada: 1280x720 @ 7fps
[INFO] [1755406736.896295733] [camera_node]: Nodo de cámara iniciado
```
```bash
ros2 topic echo /camera/image_raw --field header
```
