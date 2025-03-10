from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QTimer, Qt
import sys
import time
import math

class RelogioAnalogico(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relógio Analógico - PyQt5")
        self.setGeometry(100, 100, 500, 500)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Atualiza a cada segundo

    def paintEvent(self, event):
        # Configurar o QPainter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Configurações básicas
        centro_x, centro_y = 250, 250
        raio = 200

        # Desenhar o mostrador do relógio
        painter.setPen(QPen(Qt.black, 7, Qt.SolidLine))
        painter.drawEllipse(centro_x - raio, centro_y - raio, 2 * raio, 2 * raio)

        # Adicionar números no mostrador
        for i in range(12):
            angulo = math.radians(i * 30 - 90)
            x_numero = centro_x + 0.75 * raio * math.cos(angulo)
            y_numero = centro_y + 0.75 * raio * math.sin(angulo)
            painter.drawText(int(x_numero - 10), int(y_numero + 10), f"{i if i != 0 else 12}")

        # Obter a hora atual
        hora, minuto, segundo = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec

        # Calcular os ângulos para os ponteiros
        angulo_hora = math.radians((hora % 12) * 30 - 90 + (minuto / 2))
        angulo_minuto = math.radians(minuto * 6 - 90)
        angulo_segundo = math.radians(segundo * 6 - 90)

        # Desenhar os ponteiros
        self.desenhar_ponteiro(painter, centro_x, centro_y, 0.5 * raio, angulo_hora, Qt.black, 7)
        self.desenhar_ponteiro(painter, centro_x, centro_y, 0.7 * raio, angulo_minuto, Qt.black, 5)
        self.desenhar_ponteiro(painter, centro_x, centro_y, 0.9 * raio, angulo_segundo, Qt.red, 2)

    def desenhar_ponteiro(self, painter, x, y, tamanho, angulo, cor, largura):
        x_fim = x + tamanho * math.cos(angulo)
        y_fim = y + tamanho * math.sin(angulo)
        painter.setPen(QPen(cor, largura, Qt.SolidLine))
        painter.drawLine(x, y, int(x_fim), int(y_fim))

# Configurar a aplicação PyQt5
app = QApplication(sys.argv)
janela = RelogioAnalogico()
janela.show()
sys.exit(app.exec_())
