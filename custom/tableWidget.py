from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(TableWidget, self).__init__(parent=parent)
        self.mainwindow = parent
        self.setShowGrid(True)  # 显示网格
        self.setAlternatingRowColors(True)  # 隔行显示颜色
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().sectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().sectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setStretchLastSection(True)
        self.setFocusPolicy(Qt.NoFocus)

    def signal_connect(self):
        for spinbox in self.findChildren(QSpinBox):
            spinbox.valueChanged.connect(self.update_item)
        for doublespinbox in self.findChildren(QDoubleSpinBox):
            doublespinbox.valueChanged.connect(self.update_item)
        for combox in self.findChildren(QComboBox):
            combox.currentIndexChanged.connect(self.update_item)
        for checkbox in self.findChildren(QCheckBox):
            checkbox.stateChanged.connect(self.update_item)

    def update_item(self):
        param = self.get_params()
        self.mainwindow.useListWidget.currentItem().update_params(param)
        self.mainwindow.update_image()

    def update_params(self, param=None):
        for key in param.keys():
            box = self.findChild(QWidget, name=key)
            if isinstance(box, QSpinBox) or isinstance(box, QDoubleSpinBox):
                box.setValue(param[key])
            elif isinstance(box, QComboBox):
                box.setCurrentIndex(param[key])
            elif isinstance(box, QCheckBox):
                box.setChecked(param[key])

    def get_params(self):
        param = {}
        for spinbox in self.findChildren(QSpinBox):
            param[spinbox.objectName()] = spinbox.value()
        for doublespinbox in self.findChildren(QDoubleSpinBox):
            param[doublespinbox.objectName()] = doublespinbox.value()
        for combox in self.findChildren(QComboBox):
            param[combox.objectName()] = combox.currentIndex()
        for combox in self.findChildren(QCheckBox):
            param[combox.objectName()] = combox.isChecked()
        return param


class GrayingTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(GrayingTableWidget, self).__init__(parent=parent)


class FilterTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(FilterTabledWidget, self).__init__(parent=parent)

        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['mean filter', 'Gaussian filter', 'median filter'])
        self.kind_comBox.setObjectName('kind')

        self.ksize_spinBox = QSpinBox()
        self.ksize_spinBox.setObjectName('ksize')
        self.ksize_spinBox.setMinimum(1)
        self.ksize_spinBox.setSingleStep(2)

        self.setColumnCount(2)
        self.setRowCount(2)
        self.setItem(0, 0, QTableWidgetItem('type'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('nuclear size'))
        self.setCellWidget(1, 1, self.ksize_spinBox)

        self.signal_connect()


class MorphTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(MorphTabledWidget, self).__init__(parent=parent)

        self.op_comBox = QComboBox()
        self.op_comBox.addItems(['Corrosion operation', 'Inflation operation', 'openoperation', 'closeopeation', 'gradientoperation', 'tophatoperation', 'blackhatoperation'])
        self.op_comBox.setObjectName('op')

        self.ksize_spinBox = QSpinBox()
        self.ksize_spinBox.setMinimum(1)
        self.ksize_spinBox.setSingleStep(2)
        self.ksize_spinBox.setObjectName('ksize')

        self.kshape_comBox = QComboBox()
        self.kshape_comBox.addItems(['square', 'circle', 'oval'])
        self.kshape_comBox.setObjectName('kshape')

        self.setColumnCount(2)
        self.setRowCount(3)
        self.setItem(0, 0, QTableWidgetItem('type'))
        self.setCellWidget(0, 1, self.op_comBox)
        self.setItem(1, 0, QTableWidgetItem('nuclearsize'))
        self.setCellWidget(1, 1, self.ksize_spinBox)
        self.setItem(2, 0, QTableWidgetItem('nuclearshape'))
        self.setCellWidget(2, 1, self.kshape_comBox)
        self.signal_connect()


class GradTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(GradTabledWidget, self).__init__(parent=parent)

        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['Sobel算子', 'Scharr算子', 'Laplacian算子'])
        self.kind_comBox.setObjectName('kind')

        self.ksize_spinBox = QSpinBox()
        self.ksize_spinBox.setMinimum(1)
        self.ksize_spinBox.setSingleStep(2)
        self.ksize_spinBox.setObjectName('ksize')

        self.dx_spinBox = QSpinBox()
        self.dx_spinBox.setMaximum(1)
        self.dx_spinBox.setMinimum(0)
        self.dx_spinBox.setSingleStep(1)
        self.dx_spinBox.setObjectName('dx')

        self.dy_spinBox = QSpinBox()
        self.dy_spinBox.setMaximum(1)
        self.dy_spinBox.setMinimum(0)
        self.dy_spinBox.setSingleStep(1)
        self.dy_spinBox.setObjectName('dy')

        self.setColumnCount(2)
        self.setRowCount(4)

        self.setItem(0, 0, QTableWidgetItem('type'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('nuclearsize'))
        self.setCellWidget(1, 1, self.ksize_spinBox)
        self.setItem(2, 0, QTableWidgetItem('xdirection'))
        self.setCellWidget(2, 1, self.dx_spinBox)
        self.setItem(3, 0, QTableWidgetItem('ydirection'))
        self.setCellWidget(3, 1, self.dy_spinBox)

        self.signal_connect()


class ThresholdTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(ThresholdTableWidget, self).__init__(parent=parent)

        self.thresh_spinBox = QSpinBox()
        self.thresh_spinBox.setObjectName('thresh')
        self.thresh_spinBox.setMaximum(255)
        self.thresh_spinBox.setMinimum(0)
        self.thresh_spinBox.setSingleStep(1)

        self.maxval_spinBox = QSpinBox()
        self.maxval_spinBox.setObjectName('maxval')
        self.maxval_spinBox.setMaximum(255)
        self.maxval_spinBox.setMinimum(0)
        self.maxval_spinBox.setSingleStep(1)

        self.method_comBox = QComboBox()
        self.method_comBox.addItems(['binary thresholding', 'reversebinarythreshold', 'truncation thresholding', 'Threshold to 0', 'Dethreshold to 0', 'Otsus method'])
        self.method_comBox.setObjectName('method')

        self.setColumnCount(2)
        self.setRowCount(3)

        self.setItem(0, 0, QTableWidgetItem('type'))
        self.setCellWidget(0, 1, self.method_comBox)
        self.setItem(1, 0, QTableWidgetItem('threshold'))
        self.setCellWidget(1, 1, self.thresh_spinBox)
        self.setItem(2, 0, QTableWidgetItem('maximum value'))
        self.setCellWidget(2, 1, self.maxval_spinBox)

        self.signal_connect()


class EdgeTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(EdgeTableWidget, self).__init__(parent=parent)

        self.thresh1_spinBox = QSpinBox()
        self.thresh1_spinBox.setMinimum(0)
        self.thresh1_spinBox.setMaximum(255)
        self.thresh1_spinBox.setSingleStep(1)
        self.thresh1_spinBox.setObjectName('thresh1')

        self.thresh2_spinBox = QSpinBox()
        self.thresh2_spinBox.setMinimum(0)
        self.thresh2_spinBox.setMaximum(255)
        self.thresh2_spinBox.setSingleStep(1)
        self.thresh2_spinBox.setObjectName('thresh2')

        self.setColumnCount(2)
        self.setRowCount(2)

        self.setItem(0, 0, QTableWidgetItem('Threshold 1'))
        self.setCellWidget(0, 1, self.thresh1_spinBox)
        self.setItem(1, 0, QTableWidgetItem('threshold 2'))
        self.setCellWidget(1, 1, self.thresh2_spinBox)
        self.signal_connect()


class ContourTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(ContourTableWidget, self).__init__(parent=parent)

        self.bbox_comBox = QComboBox()
        self.bbox_comBox.addItems(['normal contour', 'circumscribed rectangle', 'Minimum circumscribed rectangle', 'minimum circumcircle'])
        self.bbox_comBox.setObjectName('bbox')

        self.mode_comBox = QComboBox()
        self.mode_comBox.addItems(['outline', 'List of contours', 'Outer profile and inner hole', 'Outline Hierarchy Tree'])
        self.mode_comBox.setObjectName('mode')

        self.method_comBox = QComboBox()
        self.method_comBox.addItems(['no approximation', 'easy approximation'])
        self.method_comBox.setObjectName('method')

        self.setColumnCount(2)
        self.setRowCount(3)

        self.setItem(0, 0, QTableWidgetItem('轮廓模式'))
        self.setCellWidget(0, 1, self.mode_comBox)
        self.setItem(1, 0, QTableWidgetItem('轮廓近似'))
        self.setCellWidget(1, 1, self.method_comBox)
        self.setItem(2, 0, QTableWidgetItem('边界模式'))
        self.setCellWidget(2, 1, self.bbox_comBox)
        self.signal_connect()


class EqualizeTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(EqualizeTableWidget, self).__init__(parent=parent)
        self.red_checkBox = QCheckBox()
        self.red_checkBox.setObjectName('red')
        self.red_checkBox.setTristate(False)
        self.blue_checkBox = QCheckBox()
        self.blue_checkBox.setObjectName('blue')
        self.blue_checkBox.setTristate(False)
        self.green_checkBox = QCheckBox()
        self.green_checkBox.setObjectName('green')
        self.green_checkBox.setTristate(False)

        self.setColumnCount(2)
        self.setRowCount(3)

        self.setItem(0, 0, QTableWidgetItem('R通道'))
        self.setCellWidget(0, 1, self.red_checkBox)
        self.setItem(1, 0, QTableWidgetItem('G通道'))
        self.setCellWidget(1, 1, self.green_checkBox)
        self.setItem(2, 0, QTableWidgetItem('B通道'))
        self.setCellWidget(2, 1, self.blue_checkBox)
        self.signal_connect()


class HoughLineTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(HoughLineTableWidget, self).__init__(parent=parent)

        self.thresh_spinBox = QSpinBox()
        self.thresh_spinBox.setMinimum(0)
        self.thresh_spinBox.setSingleStep(1)
        self.thresh_spinBox.setObjectName('thresh')

        self.min_length_spinBox = QSpinBox()
        self.min_length_spinBox.setMinimum(0)
        self.min_length_spinBox.setSingleStep(1)
        self.min_length_spinBox.setObjectName('min_length')

        self.max_gap_spinbox = QSpinBox()
        self.max_gap_spinbox.setMinimum(0)
        self.max_gap_spinbox.setSingleStep(1)
        self.max_gap_spinbox.setObjectName('max_gap')

        self.setColumnCount(2)
        self.setRowCount(3)

        self.setItem(0, 0, QTableWidgetItem('交点阈值'))
        self.setCellWidget(0, 1, self.thresh_spinBox)
        self.setItem(1, 0, QTableWidgetItem('最小长度'))
        self.setCellWidget(1, 1, self.min_length_spinBox)
        self.setItem(2, 0, QTableWidgetItem('最大间距'))
        self.setCellWidget(2, 1, self.max_gap_spinbox)
        self.signal_connect()


class LightTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(LightTableWidget, self).__init__(parent=parent)

        self.alpha_spinBox = QDoubleSpinBox()
        self.alpha_spinBox.setMinimum(0)
        self.alpha_spinBox.setMaximum(3)
        self.alpha_spinBox.setSingleStep(0.1)
        self.alpha_spinBox.setObjectName('alpha')

        self.beta_spinbox = QSpinBox()
        self.beta_spinbox.setMinimum(0)
        self.beta_spinbox.setSingleStep(1)
        self.beta_spinbox.setObjectName('beta')

        self.setColumnCount(2)
        self.setRowCount(2)

        self.setItem(0, 0, QTableWidgetItem('alpha'))
        self.setCellWidget(0, 1, self.alpha_spinBox)
        self.setItem(1, 0, QTableWidgetItem('beta'))
        self.setCellWidget(1, 1, self.beta_spinbox)
        self.signal_connect()


class GammaITabelWidget(TableWidget):
    def __init__(self, parent=None):
        super(GammaITabelWidget, self).__init__(parent=parent)
        self.gamma_spinbox = QDoubleSpinBox()
        self.gamma_spinbox.setMinimum(0)
        self.gamma_spinbox.setSingleStep(0.1)
        self.gamma_spinbox.setObjectName('gamma')

        self.setColumnCount(2)
        self.setRowCount(1)

        self.setItem(0, 0, QTableWidgetItem('gamma'))
        self.setCellWidget(0, 1, self.gamma_spinbox)
        self.signal_connect()
