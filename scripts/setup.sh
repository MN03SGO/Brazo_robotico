echo  "Configuracion de Robot MINED"

if ! command -v docker &> /dev/null; then 
    echo "Docker necesota instalarse "
    exit 1 
fi
#canara 
fi [ ! -c /dev/video0]; then
    echo "Camara no encontrada en /dev/video0"
    exit 1
fi 
echo "docker instalado"
echo "camara detectedada" 
#configuracion de x11
echo"Permisos configurados de X11"
xhost +local:docker

echo"Imagen de docker"
docker compose build

echo ".SH completado"
echo "Inciar docker: docker compose up -d"
echo "Para ingresar: docker exect -it cube_sorter_robot bash"
