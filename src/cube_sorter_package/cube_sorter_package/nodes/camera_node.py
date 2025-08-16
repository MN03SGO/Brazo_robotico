import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import threading
import time

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        
        # Parámetros configurables
        self.declare_parameter('camera_id', 0)
        self.declare_parameter('width', 1280)
        self.declare_parameter('height', 720)
        self.declare_parameter('fps', 30)
        
        # Obtener parámetros
        camera_id = self.get_parameter('camera_id').value
        width = self.get_parameter('width').value
        height = self.get_parameter('height').value
        fps = self.get_parameter('fps').value
        
        # Publisher para imágenes
        self.image_pub = self.create_publisher(Image, 'camera/image_raw', 10)
        
        # Bridge OpenCV-ROS
        self.bridge = CvBridge()
        
        # Inicializar cámara
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            self.get_logger().error(f"No se pudo abrir la cámara {camera_id}")
            return
            
        # Configurar cámara
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)
        
        # Verificar configuración
        actual_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        actual_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        actual_fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        
        self.get_logger().info(f"Cámara configurada: {actual_width}x{actual_height} @ {actual_fps}fps")
        
        # Timer para capturar frames
        timer_period = 1.0 / fps
        self.timer = self.create_timer(timer_period, self.capture_and_publish)
        
        self.get_logger().info("Nodo de cámara iniciado")
    
    def capture_and_publish(self):
        """Capturar frame y publicar"""
        try:
            ret, frame = self.cap.read()
            if not ret:
                self.get_logger().warn("No se pudo capturar frame")
                return
            
            # Convertir a mensaje ROS
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'camera_frame'
            
            # Publicar
            self.image_pub.publish(msg)
            
        except Exception as e:
            self.get_logger().error(f'Error en captura: {str(e)}')
    
    def destroy_node(self):
        """Limpiar recursos"""
        if hasattr(self, 'cap'):
            self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    
    try:
        node = CameraNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if 'node' in locals():
            node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()