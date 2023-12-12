from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QTableWidget, QMessageBox, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
import mysql.connector

class AssetManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Asset Management")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("icon.png"))

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Memanggil Database
        self.db_connection = self.connect_to_database()

        # Memanggil ID
        self.init_ui()

    # Koneksi ke Database
    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                database="aset_management"
            )
            return connection
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    # Tampilan Window
    def init_ui(self):
        self.id_barang_label = QLabel("ID Asset:")
        self.edit_id_barang = QLineEdit(self)

        self.Nama_Barang_label = QLabel("Nama Barang:")
        self.edit_Nama_Barang = QLineEdit(self)

        self.Tanggal_Registrasi_label = QLabel("Tanggal Registrasi:")
        self.edit_Tanggal_Registrasi = QLineEdit(self)

        self.Harga_Barang_label = QLabel("Harga Barang:")
        self.edit_Harga_Barang = QLineEdit(self)

        self.Penanggung_Jawab_label = QLabel("Penanggung Jawab:")
        self.edit_Penanggung_Jawab = QLineEdit(self)

        self.Lokasi_label = QLabel("Lokasi:")
        self.edit_Lokasi = QLineEdit(self)

        self.button_submit = QPushButton("Save", self)
        # Memaggil Fungsi Save
        self.button_submit.clicked.connect(self.save)

        self.button_list = QPushButton("List Barang", self)
        self.button_list.clicked.connect(self.read_data)

        # Add Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_list)
        self.layout.addWidget(self.id_barang_label)
        self.layout.addWidget(self.edit_id_barang)
        self.layout.addWidget(self.Nama_Barang_label)
        self.layout.addWidget(self.edit_Nama_Barang)
        self.layout.addWidget(self.Tanggal_Registrasi_label)
        self.layout.addWidget(self.edit_Tanggal_Registrasi)
        self.layout.addWidget(self.Harga_Barang_label)
        self.layout.addWidget(self.edit_Harga_Barang)
        self.layout.addWidget(self.Penanggung_Jawab_label)
        self.layout.addWidget(self.edit_Penanggung_Jawab)
        self.layout.addWidget(self.Lokasi_label)
        self.layout.addWidget(self.edit_Lokasi)
        self.layout.addWidget(self.button_submit)
        

        self.table_widget = QTableWidget(self)
        self.layout.addWidget(self.table_widget)

        self.central_widget.setLayout(self.layout)

    # Membuat Fungsi Save ####################################################
    def save(self):
        id_barang = self.edit_id_barang.text()
        Nama_Barang = self.edit_Nama_Barang.text()
        Tanggal_Registrasi = self.edit_Tanggal_Registrasi.text()
        Harga_Barang = self.edit_Harga_Barang.text()
        Penanggung_Jawab = self.edit_Penanggung_Jawab.text()
        Lokasi = self.edit_Lokasi.text()

        # Validasi data
        if not id_barang:
            QMessageBox.information(self, "Info Bosqu", "ID barang harus diisi!")
            # print("ID barang harus diisi!")
            return

        if not Nama_Barang:
            QMessageBox.information(self, "Info Bosqu", "Nama barang harus diisi!")
            # print("")
            return
        
        if not Tanggal_Registrasi:
            QMessageBox.information(self, "Info Bosqu", "Tanggal Registrasi harus diisi!")
            return
        
        if not Harga_Barang:
            QMessageBox.information(self, "Info Bosqu", "Harga Barang harus diisi!")
            return
        
        if not Penanggung_Jawab:
            QMessageBox.information(self, "Info Bosqu", "Penagngung Jawab harus diisi!")
            return
        
        if not Lokasi:
            QMessageBox.information(self, "Info Bosqu", "Lokasi harus diisi!")
            return
        
        
        # Proses penyimpanan data
        connection = self.connect_to_database()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tb_barang (id_barang, Nama_Barang, Tanggal_Registrasi, Harga_Barang, Penanggung_Jawab, Lokasi)"
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (id_barang, Nama_Barang, Tanggal_Registrasi, Harga_Barang, Penanggung_Jawab, Lokasi),
        )
        connection.commit()
        # Pesan sukses
        QMessageBox.information(self, "Info Bosqu", "Data berhasil disimpan!")
    # End Fungsi Save ################################################################################

    # Membuat Fungsi Read ############################################################################
    # def read_data(self):
    #     try:
    #         connection = self.connect_to_database()
    #         cursor = connection.cursor()

    #         # Execute SQL query to retrieve data from tb_barang
    #         cursor.execute("SELECT id_barang, Nama_Barang, Tanggal_Registrasi, Harga_Barang, Penanggung_Jawab, Lokasi FROM tb_barang")
    #         data = cursor.fetchall()

    #         # Display data in the table widget
    #         self.table_widget.setRowCount(len(data))
    #         self.table_widget.setColumnCount(len(data[0]))

    #         for row_num, row_data in enumerate(data):
    #             for col_num, col_data in enumerate(row_data):
    #                 item = QTableWidgetItem(str(col_data))
    #                 self.table_widget.setItem(row_num, col_num, item)
    #                 self.table_widget.setHorizontalHeaderLabels([
    #                     "ID Asset", 
    #                     "Nama Barang", 
    #                     "Tanggal Registrasi", 
    #                     "Harga Barang",
    #                     "Penanggung Jawab",
    #                     "Lokasi"
    #                     ])

    #     except mysql.connector.Error as err:
    #         print("Error: {}".format(err))
    #         self.button_submit = QPushButton("Save", self)
    #         # Memaggil Fungsi Save
    #         self.button_submit.clicked.connect(self.save)
    def read_data(self):
        try:
            connection = self.connect_to_database()
            cursor = connection.cursor()

            # Execute SQL query to retrieve data from tb_barang
            cursor.execute("SELECT id_barang, Nama_Barang, Tanggal_Registrasi, Harga_Barang, Penanggung_Jawab, Lokasi FROM tb_barang")
            data = cursor.fetchall()

            # Display data in the table widget
            self.table_widget.setRowCount(len(data))
            self.table_widget.setColumnCount(len(data[0]))

            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.table_widget.setItem(row_num, col_num, item)

                # Add "Edit" button
                edit_button = QPushButton("Edit", self)
                edit_button.clicked.connect(lambda _, row=row_num: self.edit_data(row))
                self.table_widget.setCellWidget(row_num, len(row_data), edit_button)

                # Add "Delete" button
                delete_button = QPushButton("Delete", self)
                delete_button.clicked.connect(lambda _, row=row_num: self.delete_data(row))
                self.table_widget.setCellWidget(row_num, len(row_data) + 1, delete_button)

            # Set headers
            self.table_widget.setHorizontalHeaderLabels([
                "ID Asset", 
                "Nama Barang", 
                "Tanggal Registrasi", 
                "Harga Barang",
                "Penanggung Jawab",
                "Lokasi",
                "Edit",
                "Delete"
            ])

        except mysql.connector.Error as err:
            print("Error: {}".format(err))

    # Membuat Fungsi Edit
    def edit_data(self, row):
        # Implement edit logic here
        print(f"Editing data in row {row}")

    # Membuat Fungsi Delete
    def delete_data(self, row):
        # Implement delete logic here
        print(f"Deleting data in row {row}")

if __name__ == "__main__":
    app = QApplication([])
    window = AssetManagementApp()
    window.show()
    app.exec()
