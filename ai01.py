
import sys
import random
from dataclasses import dataclass
from typing import List, Optional, Tuple
from PyQt6.QtCore import Qt, QSize, QSortFilterProxyModel, QRegularExpression, pyqtSignal
from PyQt6.QtGui import QAction, QIcon, QStandardItem, QStandardItemModel, QRegularExpressionValidator
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QPushButton,
    QLabel,
    QTableView,
    QHeaderView,
    QAbstractItemView,
    QToolButton,
    QLineEdit,
    QFormLayout,
    QDialog,
    QDialogButtonBox,
    QMessageBox,
    QComboBox,
    QSpinBox,
    QDoubleSpinBox,
    QFrame,
    QSizePolicy,
    QScrollArea,
    QStyle,
    QSplitter,
    QGraphicsDropShadowEffect,
)
# Matplotlib embedding
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# ----------- Theme Manager ------------------------------------
class ThemeManager:
    LIGHT = "light"
    DARK = "dark"
    
    def __init__(self):
        self.current_theme = self.LIGHT
        self._subscribers = []
    
    def subscribe(self, callback):
        """Subscribe to theme changes"""
        self._subscribers.append(callback)
    
    def set_theme(self, theme: str):
        """Set the current theme and notify subscribers"""
        if theme in [self.LIGHT, self.DARK]:
            self.current_theme = theme
            for callback in self._subscribers:
                callback(theme)
    
    def get_theme(self) -> str:
        return self.current_theme
    
    def toggle_theme(self):
        """Toggle between light and dark themes"""
        new_theme = self.DARK if self.current_theme == self.LIGHT else self.LIGHT
        self.set_theme(new_theme)
    
    def get_stylesheet(self) -> str:
        """Get the stylesheet for the current theme"""
        if self.current_theme == self.DARK:
            return self._dark_stylesheet()
        else:
            return self._light_stylesheet()
    
    def _light_stylesheet(self) -> str:
        return """
        QMainWindow { background: #f8fafc; }
        /* Sidebar */
        #Sidebar {
            background: #0f172a;
            border-right: 1px solid #0b1220;
        }
        #Brand {
            color: #e2e8f0;
            font-size: 16px;
            font-weight: 600;
            padding: 6px 8px;
        }
        #SidebarFooter {
            color: #94a3b8;
            font-size: 12px;
            padding: 6px 8px;
        }
        #SidebarButton {
            background: transparent;
            color: #cbd5e1;
            border: none;
            text-align: left;
            padding: 10px 12px;
            border-radius: 8px;
        }
        #SidebarButton:hover {
            background: #1e293b;
            color: #e2e8f0;
        }
        #SidebarButton:checked {
            background: #334155;
            color: #ffffff;
        }
        #ThemeToggleButton {
            background: #334155;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 8px 12px;
            margin: 8px 0px;
            font-weight: 600;
            font-size: 13px;
        }
        #ThemeToggleButton:hover {
            background: #475569;
        }
        /* Headings */
        #H1 {
            font-size: 22px;
            font-weight: 700;
            color: #0f172a;
        }
        /* General text elements */
        QLabel {
            color: #0f172a;
        }
        /* Cards */
        #Card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
        }
        #CardTitle {
            font-size: 14px;
            font-weight: 600;
            color: #0f172a;
        }
        #CardSubtitle {
            font-size: 24px;
            font-weight: 700;
            color: #111827;
        }
        /* Primary buttons */
        #PrimaryButton {
            background: #4f46e5;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            padding: 6px 14px;
        }
        #PrimaryButton:hover {
            background: #4338ca;
        }
        #PrimaryButton:pressed {
            background: #3730a3;
        }
        QPushButton {
            border-radius: 10px;
            padding: 6px 12px;
            color: #0f172a;
        }
        /* Inputs */
        QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 6px 8px;
            color: #0f172a;
        }
        QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {
            border: 1px solid #4f46e5;
        }
        /* Table */
        #Table {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            gridline-color: #e5e7eb;
            alternate-background-color: #f8fafc;
        }
        QHeaderView::section {
            background: #f1f5f9;
            color: #0f172a;
            padding: 8px;
            border: none;
            border-bottom: 1px solid #e2e8f0;
        }
        QTableView {
            selection-background-color: #e0e7ff;
            selection-color: #111827;
            color: #0f172a;
        }
        QTableView::item {
            color: #0f172a;
        }
        /* Dialog */
        #Dialog {
            background: #ffffff;
        }
        QDialog > QVBoxLayout > * {
            font-size: 14px;
            color: #0f172a;
        }
        QDialogButtonBox QPushButton {
            background: #4f46e5;
            color: #ffffff;
            border: none;
            padding: 6px 12px;
            border-radius: 8px;
        }
        QDialogButtonBox QPushButton:hover { background: #4338ca; }
        /* Status Bar */
        QStatusBar {
            background: #f1f5f9;
            color: #0f172a;
            border-top: 1px solid #e2e8f0;
        }
        /* Additional text elements */
        QFormLayout QLabel {
            color: #0f172a;
        }
        QSpinBox, QDoubleSpinBox {
            color: #0f172a;
        }
        """
    
    def _dark_stylesheet(self) -> str:
        return """
        QMainWindow { background: #0f172a; }
        /* Sidebar */
        #Sidebar {
            background: #020617;
            border-right: 1px solid #1e293b;
        }
        #Brand {
            color: #e2e8f0;
            font-size: 16px;
            font-weight: 600;
            padding: 6px 8px;
        }
        #SidebarFooter {
            color: #64748b;
            font-size: 12px;
            padding: 6px 8px;
        }
        #SidebarButton {
            background: transparent;
            color: #94a3b8;
            border: none;
            text-align: left;
            padding: 10px 12px;
            border-radius: 8px;
        }
        #SidebarButton:hover {
            background: #1e293b;
            color: #cbd5e1;
        }
        #SidebarButton:checked {
            background: #334155;
            color: #ffffff;
        }
        #ThemeToggleButton {
            background: #475569;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 8px 12px;
            margin: 8px 0px;
        }
        #ThemeToggleButton:hover {
            background: #64748b;
        }
        /* Headings */
        #H1 {
            font-size: 22px;
            font-weight: 700;
            color: #f1f5f9;
        }
        /* Cards */
        #Card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 14px;
        }
        #CardTitle {
            font-size: 14px;
            font-weight: 600;
            color: #e2e8f0;
        }
        #CardSubtitle {
            font-size: 24px;
            font-weight: 700;
            color: #f8fafc;
        }
        /* Primary buttons */
        #PrimaryButton {
            background: #6366f1;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            padding: 6px 14px;
        }
        #PrimaryButton:hover {
            background: #5855eb;
        }
        #PrimaryButton:pressed {
            background: #4f46e5;
        }
        QPushButton {
            border-radius: 10px;
            padding: 6px 12px;
        }
        /* Inputs */
        QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
            background: #334155;
            border: 1px solid #475569;
            border-radius: 8px;
            padding: 6px 8px;
            color: #f1f5f9;
        }
        QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {
            border: 1px solid #6366f1;
        }
        /* Table */
        #Table {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            gridline-color: #475569;
            alternate-background-color: #0f172a;
            color: #f1f5f9;
        }
        QHeaderView::section {
            background: #334155;
            color: #e2e8f0;
            padding: 8px;
            border: none;
            border-bottom: 1px solid #475569;
        }
        QTableView {
            selection-background-color: #3730a3;
            selection-color: #ffffff;
        }
        /* Dialog */
        #Dialog {
            background: #1e293b;
        }
        QDialog > QVBoxLayout > * {
            font-size: 14px;
        }
        QDialogButtonBox QPushButton {
            background: #6366f1;
            color: #ffffff;
            border: none;
            padding: 6px 12px;
            border-radius: 8px;
        }
        QDialogButtonBox QPushButton:hover { background: #5855eb; }
        /* Status Bar */
        QStatusBar {
            background: #334155;
            color: #e2e8f0;
            border-top: 1px solid #475569;
        }
        """

# Global theme manager instance
theme_manager = ThemeManager()

# ----------- Data Models (simple in-memory stubs) --------------
@dataclass
class Product:
    name: str
    brand: str
    price: float
    stock: int

@dataclass
class Customer:
    name: str
    phone: str
    email: str
    total_purchases: int

# ----------- Shared Widgets and Utilities ----------------------
class Card(QWidget):
    def __init__(self, title: str, subtitle: str = "", parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setObjectName("Card")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(6)
        self.title_label = QLabel(title)
        self.title_label.setObjectName("CardTitle")
        self.subtitle_label = QLabel(subtitle)
        self.subtitle_label.setObjectName("CardSubtitle")
        layout.addWidget(self.title_label)
        layout.addWidget(self.subtitle_label)
        # Subtle shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(22)
        shadow.setOffset(0, 8)
        shadow.setColor(Qt.GlobalColor.black)
        shadow.setEnabled(False) # keep disabled for performance; enable if desired
        self.setGraphicsEffect(shadow)

class FigureCard(QWidget):
    def __init__(self, title: str, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setObjectName("Card")
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(12)
        self.title_label = QLabel(title)
        self.title_label.setObjectName("CardTitle")
        outer.addWidget(self.title_label)
        # Matplotlib Figure
        self.figure = Figure(figsize=(5, 3), tight_layout=True)
        self.canvas = FigureCanvasQTAgg(self.figure)
        outer.addWidget(self.canvas)
        
        # Subscribe to theme changes to update chart styling
        theme_manager.subscribe(self.on_theme_changed)
    
    def on_theme_changed(self, theme: str):
        """Update chart styling when theme changes"""
        self.update_chart_theme()
    
    def update_chart_theme(self):
        """Update the chart colors based on current theme"""
        theme = theme_manager.get_theme()
        if theme == theme_manager.DARK:
            # Dark theme colors
            self.figure.patch.set_facecolor('#1e293b')
            for ax in self.figure.axes:
                ax.set_facecolor('#1e293b')
                ax.tick_params(colors='#e2e8f0')
                ax.xaxis.label.set_color('#e2e8f0')
                ax.yaxis.label.set_color('#e2e8f0')
                ax.title.set_color('#f1f5f9')
                ax.spines['bottom'].set_color('#475569')
                ax.spines['top'].set_color('#475569')
                ax.spines['left'].set_color('#475569')
                ax.spines['right'].set_color('#475569')
                ax.grid(True, alpha=0.2, color='#475569')
        else:
            # Light theme colors
            self.figure.patch.set_facecolor('#ffffff')
            for ax in self.figure.axes:
                ax.set_facecolor('#ffffff')
                ax.tick_params(colors='#0f172a')
                ax.xaxis.label.set_color('#0f172a')
                ax.yaxis.label.set_color('#0f172a')
                ax.title.set_color('#0f172a')
                ax.spines['bottom'].set_color('#e2e8f0')
                ax.spines['top'].set_color('#e2e8f0')
                ax.spines['left'].set_color('#e2e8f0')
                ax.spines['right'].set_color('#e2e8f0')
                ax.grid(True, alpha=0.3, color='#e2e8f0')
        
        self.canvas.draw_idle()

# ----------- Sidebar ------------------------------------------
class Sidebar(QFrame):
    menuSelected = pyqtSignal(int)
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setObjectName("Sidebar")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.setMinimumWidth(220)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 16, 12, 16)
        layout.setSpacing(6)
        self.btn_group: List[QPushButton] = []
        # App branding
        brand = QLabel("📱 Mobile Shop Admin")
        brand.setObjectName("Brand")
        brand.setWordWrap(True)
        layout.addWidget(brand)
        layout.addSpacing(12)
        # Buttons
        self.addButton("🏠 Dashboard", 0, layout)
        self.addButton("📦 Products", 1, layout)
        self.addButton("👥 Customers", 2, layout)
        self.addButton("📊 Analytics", 3, layout)
        self.addButton("⚙️ Settings", 4, layout)
        
        # Theme toggle button
        layout.addSpacing(16)
        self.theme_toggle_btn = QPushButton("🌙 Dark Mode")
        self.theme_toggle_btn.setObjectName("ThemeToggleButton")
        self.theme_toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.theme_toggle_btn.setToolTip("Toggle between light and dark themes (Ctrl+T)")
        self.theme_toggle_btn.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_toggle_btn)
        
        layout.addStretch(1)
        # Footer
        foot = QLabel("v1.0.0")
        foot.setObjectName("SidebarFooter")
        layout.addWidget(foot, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        # Select default
        if self.btn_group:
            self.btn_group[0].setChecked(True)
        
        # Subscribe to theme changes to update button text
        theme_manager.subscribe(self.on_theme_changed)

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        theme_manager.toggle_theme()
    
    def on_theme_changed(self, theme: str):
        """Update button text when theme changes"""
        if theme == theme_manager.DARK:
            self.theme_toggle_btn.setText("☀️ Light Mode")
        else:
            self.theme_toggle_btn.setText("🌙 Dark Mode")

    def addButton(self, text: str, page_index: int, layout: QVBoxLayout):
        btn = QPushButton(text)
        btn.setObjectName("SidebarButton")
        btn.setCheckable(True)
        btn.setAutoExclusive(True)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.clicked.connect(lambda: self.menuSelected.emit(page_index))
        btn.setMinimumHeight(42)
        layout.addWidget(btn)
        self.btn_group.append(btn)

# ----------- Pages --------------------------------------------
class DashboardPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(16)
        header = QLabel("Overview")
        header.setObjectName("H1")
        outer.addWidget(header)
        # Cards grid
        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        outer.addLayout(cards_row)
        total_sales = Card("Total Sales", "$124,320")
        total_sales.setMinimumHeight(100)
        total_orders = Card("Orders", "2,136")
        total_orders.setMinimumHeight(100)
        total_customers = Card("Customers", "856")
        total_customers.setMinimumHeight(100)
        cards_row.addWidget(total_sales)
        cards_row.addWidget(total_orders)
        cards_row.addWidget(total_customers)
        # Scroll filler
        filler = QWidget()
        filler.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        outer.addWidget(filler)

class ProductDialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None, product: Optional[Product] = None):
        super().__init__(parent)
        self.setWindowTitle("Product")
        self.setObjectName("Dialog")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        form = QFormLayout()
        form.setSpacing(8)
        self.name_edit = QLineEdit()
        self.brand_edit = QLineEdit()
        self.price_edit = QDoubleSpinBox()
        self.price_edit.setMaximum(1_000_000)
        self.price_edit.setPrefix("$ ")
        self.price_edit.setDecimals(2)
        self.stock_edit = QSpinBox()
        self.stock_edit.setMaximum(1_000_000)
        form.addRow("Name", self.name_edit)
        form.addRow("Brand", self.brand_edit)
        form.addRow("Price", self.price_edit)
        form.addRow("Stock", self.stock_edit)
        layout.addLayout(form)
        buttons = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        self.button_box = QDialogButtonBox(buttons)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)
        if product:
            self.name_edit.setText(product.name)
            self.brand_edit.setText(product.brand)
            self.price_edit.setValue(product.price)
            self.stock_edit.setValue(product.stock)

    def get_product(self) -> Product:
        return Product(
            name=self.name_edit.text().strip(),
            brand=self.brand_edit.text().strip(),
            price=float(self.price_edit.value()),
            stock=int(self.stock_edit.value()),
        )

class ProductsPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.products: List[Product] = self.seed_products()
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(12)
        header_row = QHBoxLayout()
        header_row.setSpacing(8)
        title = QLabel("Products")
        title.setObjectName("H1")
        header_row.addWidget(title)
        header_row.addStretch(1)
        self.add_btn = QPushButton("Add")
        self.edit_btn = QPushButton("Edit")
        self.delete_btn = QPushButton("Delete")
        for b in (self.add_btn, self.edit_btn, self.delete_btn):
            b.setObjectName("PrimaryButton")
            b.setMinimumHeight(34)
        header_row.addWidget(self.add_btn)
        header_row.addWidget(self.edit_btn)
        header_row.addWidget(self.delete_btn)
        outer.addLayout(header_row)
        # Table
        self.model = QStandardItemModel(0, 4, self)
        self.model.setHorizontalHeaderLabels(["Name", "Brand", "Price", "Stock"])
        self.table = QTableView()
        self.table.setObjectName("Table")
        self.table.setModel(self.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        outer.addWidget(self.table)
        self.refresh_table()
        # Connections
        self.add_btn.clicked.connect(self.add_product)
        self.edit_btn.clicked.connect(self.edit_selected_product)
        self.delete_btn.clicked.connect(self.delete_selected_product)

    def seed_products(self) -> List[Product]:
        brands = ["Apple", "Samsung", "Xiaomi", "Oppo", "Vivo", "Google"]
        sample = []
        for i in range(18):
            brand = random.choice(brands)
            name = f"{brand} Model {random.randint(1, 30)}"
            price = round(random.uniform(199, 1499), 2)
            stock = random.randint(0, 250)
            sample.append(Product(name=name, brand=brand, price=price, stock=stock))
        return sample

    def refresh_table(self):
        self.model.setRowCount(0)
        for p in self.products:
            self.append_product_to_model(p)

    def append_product_to_model(self, product: Product):
        row = [
            QStandardItem(product.name),
            QStandardItem(product.brand),
            QStandardItem(f"${product.price:,.2f}"),
            QStandardItem(str(product.stock)),
        ]
        for item in row:
            item.setEditable(False)
        self.model.appendRow(row)

    def get_selected_row_index(self) -> Optional[int]:
        indexes = self.table.selectionModel().selectedRows()
        if not indexes:
            return None
        return indexes[0].row()

    def add_product(self):
        dlg = ProductDialog(self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            product = dlg.get_product()
            if not product.name or not product.brand:
                QMessageBox.warning(self, "Invalid", "Name and Brand are required.")
                return
            self.products.append(product)
            self.append_product_to_model(product)

    def edit_selected_product(self):
        row_idx = self.get_selected_row_index()
        if row_idx is None:
            QMessageBox.information(self, "Select a row", "Please select a product to edit.")
            return
        current = self.products[row_idx]
        dlg = ProductDialog(self, current)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            edited = dlg.get_product()
            if not edited.name or not edited.brand:
                QMessageBox.warning(self, "Invalid", "Name and Brand are required.")
                return
            self.products[row_idx] = edited
            # Update model row
            self.model.setItem(row_idx, 0, QStandardItem(edited.name))
            self.model.setItem(row_idx, 1, QStandardItem(edited.brand))
            self.model.setItem(row_idx, 2, QStandardItem(f"${edited.price:,.2f}"))
            self.model.setItem(row_idx, 3, QStandardItem(str(edited.stock)))
            for c in range(4):
                self.model.item(row_idx, c).setEditable(False)

    def delete_selected_product(self):
        row_idx = self.get_selected_row_index()
        if row_idx is None:
            QMessageBox.information(self, "Select a row", "Please select a product to delete.")
            return
        name = self.products[row_idx].name
        confirm = QMessageBox.question(self, "Delete", f"Delete product '{name}'?")
        if confirm == QMessageBox.StandardButton.Yes:
            del self.products[row_idx]
            self.model.removeRow(row_idx)

class CustomersFilterProxy(QSortFilterProxyModel):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.search_text = ""
        self.min_purchases = 0

    def set_search_text(self, text: str):
        self.search_text = text.lower().strip()
        self.invalidateFilter()

    def set_min_purchases(self, value: int):
        self.min_purchases = value
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row: int, source_parent) -> bool:
        # Columns: Name, Phone, Email, Total Purchases
        model = self.sourceModel()
        name_idx = model.index(source_row, 0, source_parent)
        phone_idx = model.index(source_row, 1, source_parent)
        email_idx = model.index(source_row, 2, source_parent)
        total_idx = model.index(source_row, 3, source_parent)
        name = model.data(name_idx) or ""
        phone = model.data(phone_idx) or ""
        email = model.data(email_idx) or ""
        try:
            total = int(model.data(total_idx) or 0)
        except ValueError:
            total = 0
        if total < self.min_purchases:
            return False
        if not self.search_text:
            return True
        blob = f"{name} {phone} {email}".lower()
        return self.search_text in blob

class CustomersPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.customers: List[Customer] = self.seed_customers()
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(12)
        header = QLabel("Customers")
        header.setObjectName("H1")
        outer.addWidget(header)
        # Filters row
        filters = QHBoxLayout()
        filters.setSpacing(8)
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Search name, phone, email...")
        self.search_edit.setClearButtonEnabled(True)
        filters.addWidget(QLabel("Search"))
        filters.addWidget(self.search_edit, 3)
        self.min_purchases = QSpinBox()
        self.min_purchases.setRange(0, 1_000_000)
        self.min_purchases.setValue(0)
        filters.addWidget(QLabel("Min purchases"))
        filters.addWidget(self.min_purchases, 1)
        filters.addStretch(1)
        outer.addLayout(filters)
        # Table with proxy
        self.model = QStandardItemModel(0, 4, self)
        self.model.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Total Purchases"])
        self.proxy = CustomersFilterProxy(self)
        self.proxy.setSourceModel(self.model)
        self.table = QTableView()
        self.table.setObjectName("Table")
        self.table.setModel(self.proxy)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        outer.addWidget(self.table)
        self.refresh_table()
        # Connect filters
        self.search_edit.textChanged.connect(self.proxy.set_search_text)
        self.min_purchases.valueChanged.connect(self.proxy.set_min_purchases)

    def seed_customers(self) -> List[Customer]:
        first = ["Alex", "Taylor", "Jordan", "Morgan", "Sam", "Riley", "Casey", "Jamie", "Devin", "Avery"]
        last = ["Lee", "Kim", "Patel", "Singh", "Garcia", "Nguyen", "Brown", "Johnson", "Lopez", "Martinez"]
        sample = []
        for _ in range(40):
            name = f"{random.choice(first)} {random.choice(last)}"
            phone = f"+1 {random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"
            email = f"{name.lower().replace(' ','.')}@example.com"
            total = random.randint(0, 50)
            sample.append(Customer(name=name, phone=phone, email=email, total_purchases=total))
        return sample

    def refresh_table(self):
        self.model.setRowCount(0)
        for c in self.customers:
            row = [
                QStandardItem(c.name),
                QStandardItem(c.phone),
                QStandardItem(c.email),
                QStandardItem(str(c.total_purchases)),
            ]
            for item in row:
                item.setEditable(False)
            self.model.appendRow(row)

class AnalyticsPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(16)
        header = QLabel("Analytics")
        header.setObjectName("H1")
        outer.addWidget(header)
        # Two charts side by side
        charts_row = QHBoxLayout()
        charts_row.setSpacing(16)
        outer.addLayout(charts_row)
        self.sales_card = FigureCard("Monthly Sales")
        self.brands_card = FigureCard("Best-Selling Brands Share")
        charts_row.addWidget(self.sales_card)
        charts_row.addWidget(self.brands_card)
        self.render_charts()
        
        # Apply initial theme to charts
        self.sales_card.update_chart_theme()
        self.brands_card.update_chart_theme()
        
        filler = QWidget()
        filler.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        outer.addWidget(filler)

    def render_charts(self):
        # Bar chart for monthly sales
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        sales = [random.randint(40, 160) for _ in months]
        self.sales_card.figure.clear()
        ax = self.sales_card.figure.add_subplot(111)
        bars = ax.bar(months, sales, color="#4F46E5")
        ax.set_ylabel("Units Sold")
        ax.set_title("Sales per Month")
        ax.grid(axis="y", linestyle="--", alpha=0.3)
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f"{height}", (bar.get_x() + bar.get_width() / 2, height),
                        ha="center", va="bottom", fontsize=8)
        self.sales_card.canvas.draw_idle()
        # Pie chart for brand share
        brands = ["Apple", "Samsung", "Xiaomi", "Oppo", "Vivo", "Google"]
        values = [random.randint(5, 30) for _ in brands]
        self.brands_card.figure.clear()
        bx = self.brands_card.figure.add_subplot(111)
        wedges, texts, autotexts = bx.pie(
            values, labels=brands, autopct="%1.1f%%", startangle=140, pctdistance=0.8
        )
        for w in wedges:
            w.set_edgecolor("#ffffff")
        bx.set_aspect("equal")
        self.brands_card.canvas.draw_idle()

class SettingsPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(12)
        header = QLabel("Settings")
        header.setObjectName("H1")
        outer.addWidget(header)
        
        # Current theme display
        theme_info = QLabel(f"Current Theme: {theme_manager.get_theme().title()}")
        theme_info.setObjectName("CardSubtitle")
        theme_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer.addWidget(theme_info)
        
        card = QFrame()
        card.setObjectName("Card")
        form_wrap = QVBoxLayout(card)
        form_wrap.setContentsMargins(16, 16, 16, 16)
        form_wrap.setSpacing(8)
        form = QFormLayout()
        form.setSpacing(8)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"])
        self.theme_combo.setCurrentText(theme_manager.get_theme().title())
        self.density_combo = QComboBox()
        self.density_combo.addItems(["Comfortable", "Compact"])
        form.addRow("Theme", self.theme_combo)
        form.addRow("Density", self.density_combo)
        form_wrap.addLayout(form)
        
        # Connect theme selection
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        
        outer.addWidget(card)
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        outer.addWidget(spacer)
        
        # Subscribe to theme changes to update combo box
        theme_manager.subscribe(self.on_theme_manager_changed)
        
        # Store reference to theme info label for updates
        self.theme_info_label = theme_info
    
    def on_theme_changed(self, theme_text: str):
        """Handle theme selection change"""
        if theme_text == "Dark":
            theme_manager.set_theme(theme_manager.DARK)
        else:
            theme_manager.set_theme(theme_manager.LIGHT)
    
    def on_theme_manager_changed(self, theme: str):
        """Update combo box when theme changes externally"""
        if theme == theme_manager.DARK:
            self.theme_combo.setCurrentText("Dark")
        else:
            self.theme_combo.setCurrentText("Light")
        
        # Update theme info label
        if hasattr(self, 'theme_info_label'):
            self.theme_info_label.setText(f"Current Theme: {theme.title()}")

# ----------- Main Window --------------------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mobile Shop Admin Dashboard")
        self.resize(1200, 800)
        # Central layout with splitter for responsive behavior
        central = QWidget()
        central_layout = QHBoxLayout(central)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(0)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setChildrenCollapsible(False)
        central_layout.addWidget(splitter)
        # Sidebar
        self.sidebar = Sidebar()
        splitter.addWidget(self.sidebar)
        # Pages container
        self.stack = QStackedWidget()
        splitter.addWidget(self.stack)
        # Pages
        self.dashboard_page = DashboardPage()
        self.products_page = ProductsPage()
        self.customers_page = CustomersPage()
        self.analytics_page = AnalyticsPage()
        self.settings_page = SettingsPage()
        self.stack.addWidget(self.dashboard_page) # 0
        self.stack.addWidget(self.products_page) # 1
        self.stack.addWidget(self.customers_page) # 2
        self.stack.addWidget(self.analytics_page) # 3
        self.stack.addWidget(self.settings_page) # 4
        # Initial sizes
        splitter.setSizes([240, 960])
        self.setCentralWidget(central)
        # Routing
        self.sidebar.menuSelected.connect(self.stack.setCurrentIndex)
        # Menu bar (optional actions)
        self.setup_menu()
        
        # Subscribe to theme changes and apply initial theme
        theme_manager.subscribe(self.apply_theme)
        self.apply_theme(theme_manager.get_theme())
        
        # Setup status bar with theme indicator
        self.setup_status_bar()

    def setup_menu(self):
        bar = self.menuBar()
        file_menu = bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        view_menu = bar.addMenu("View")
        dash_action = QAction("Dashboard", self)
        dash_action.triggered.connect(lambda: self.stack.setCurrentIndex(0))
        view_menu.addAction(dash_action)
        
        # Theme toggle action
        theme_action = QAction("Toggle Theme", self)
        theme_action.triggered.connect(theme_manager.toggle_theme)
        theme_action.setShortcut("Ctrl+T")
        theme_action.setToolTip("Switch between light and dark themes")
        view_menu.addAction(theme_action)

    def setup_status_bar(self):
        """Setup status bar with theme indicator"""
        self.statusBar().showMessage("Ready")
        self.theme_label = QLabel()
        self.statusBar().addPermanentWidget(self.theme_label)
        self.update_theme_indicator()
        
        # Subscribe to theme changes to update indicator
        theme_manager.subscribe(self.on_theme_changed_for_status)
    
    def on_theme_changed_for_status(self, theme: str):
        """Update status bar theme indicator"""
        self.update_theme_indicator()
    
    def update_theme_indicator(self):
        """Update the theme indicator in status bar"""
        theme = theme_manager.get_theme()
        if theme == theme_manager.DARK:
            self.theme_label.setText("🌙 Dark Mode")
        else:
            self.theme_label.setText("☀️ Light Mode")
    
    def apply_theme(self, theme: str):
        """Apply the selected theme to the application"""
        self.setStyleSheet(theme_manager.get_stylesheet())

# ----------- App bootstrap ------------------------------------
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()