
echo "=== Test de Cámara ==="

# Verificar cámara en host
if [ -c /dev/video0 ]; then
    echo "Cámara detectada en host"
else
    echo "No se detecta cámara en /dev/video0"
    exit 1
fi

# carga basica con OpenCV
python3 -c "
import cv2
import sys

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Error: No se puede abrir la cámara')
    sys.exit(1)

ret, frame = cap.read()
if ret:
    h, w = frame.shape[:2]
    print(f'Cámara funcionando: {w}x{h}')
else:
    print('Error: No se puede capturar frame')
    sys.exit(1)

cap.release()
print('Test de cámara completado')
"