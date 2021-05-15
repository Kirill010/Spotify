import sys
import csv
import sqlite3
from PyQt5 import QtCore, QtMultimedia, uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QMainWindow, QVBoxLayout, QComboBox, \
    QHBoxLayout, QListWidgetItem, QListWidget, QLineEdit, QMessageBox
import hashlib


class Entr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 200, 200)
        self.setWindowTitle('Вход')

        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(
            'background-color: #474a51;'
        )
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self)

        self.layout1 = QHBoxLayout(self)

        self.login_lbl = QLabel('Логин', self)
        self.login_lbl.setStyleSheet("color: #fff;"
                                     "font-size: 14px;"
                                     )

        self.login = QLineEdit(self)
        self.login.setStyleSheet("color: #fff;"
                                 'border: 2px solid white;'
                                 'border-radius: 15px;'
                                 )

        self.layout1.addWidget(self.login_lbl)
        self.layout1.addWidget(self.login)

        self.layout2 = QHBoxLayout(self)

        self.password_lbl = QLabel('Пароль', self)
        self.password_lbl.setStyleSheet("color: #fff;"
                                        "font-size: 14px;"
                                        )

        self.password = QLineEdit(self)
        self.password.setStyleSheet("color: #fff;"
                                    'border: 2px solid white;'
                                    'border-radius: 15px;'
                                    )

        self.layout2.addWidget(self.password_lbl)
        self.layout2.addWidget(self.password)

        self.layout3 = QHBoxLayout(self)

        self.entr_btn = QPushButton('Войти', self)
        self.entr_btn.setStyleSheet("padding:4px;"
                                    "color: #fff;"
                                    "font-size: 14px;"
                                    "border-radius: 2px;"
                                    "border: 1px solid #3873d9;"
                                    "background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, "
                                    "stop: 0 #4287ff, stop: 1 #356ccc);"
                                    )
        self.entr_btn.clicked.connect(self.entrance)

        self.reg_btn = QPushButton('Зарегистрироваться', self)
        self.reg_btn.setStyleSheet("padding:4px;"
                                   "color: #fff;"
                                   "font-size: 14px;"
                                   "border-radius: 2px;"
                                   "border: 1px solid #3873d9;"
                                   "background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, "
                                   "stop: 0 #4287ff, stop: 1 #356ccc);"
                                   )
        self.reg_btn.clicked.connect(self.reg)

        self.layout3.addWidget(self.entr_btn)
        self.layout3.addWidget(self.reg_btn)

        self.main_layout.addLayout(self.layout1)
        self.main_layout.addLayout(self.layout2)
        self.main_layout.addLayout(self.layout3)

        self.central_widget.setLayout(self.main_layout)

    def reg(self):
        self.registration = Ui_signUp()
        self.registration.show()

    def entrance(self):
        login = self.login.text()
        password = self.password.text()
        if not login or not password:
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return
        db = 'login.db'
        con = sqlite3.connect(db)
        cur = con.cursor()
        try:
            result = cur.execute(f"""SELECT password FROM data_table WHERE login = '{login}' """).fetchone()
            if hashlib.sha1(bytes(password, encoding='utf-8')).hexdigest() == result[0]:
                self.win = GenreChoice()
                self.win.show()
            else:
                self.showMessageBox('Внимание!', 'Неправильное имя пользователя или пароль.')
        except TypeError:
            self.showMessageBox('Внимание!', 'Неправильное имя пользователя или пароль.')

    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


class Ui_signUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 200, 200)
        self.setWindowTitle('Регистрация')

        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(
            'background-color: #474a51;'
        )
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self)

        self.layout1 = QHBoxLayout(self)

        self.login_lbl = QLabel('Логин', self)
        self.login_lbl.setStyleSheet("color: #fff;"
                                     "font-size: 14px;"
                                     )

        self.login = QLineEdit(self)
        self.login.setStyleSheet("color: #fff;"
                                 'border: 2px solid white;'
                                 'border-radius: 15px;'
                                 )

        self.layout1.addWidget(self.login_lbl)
        self.layout1.addWidget(self.login)

        self.layout2 = QHBoxLayout(self)

        self.password_lbl = QLabel('Пароль', self)
        self.password_lbl.setStyleSheet("color: #fff;"
                                        "font-size: 14px;"
                                        )

        self.password = QLineEdit(self)
        self.password.setStyleSheet("color: #fff;"
                                    'border: 2px solid white;'
                                    'border-radius: 15px;'
                                    )
        self.layout2.addWidget(self.password_lbl)
        self.layout2.addWidget(self.password)

        self.layout3 = QHBoxLayout(self)

        self.reg_btn = QPushButton('Зарегистрироваться', self)
        self.reg_btn.setStyleSheet("padding:4px;"
                                   "color: #fff;"
                                   "font-size: 14px;"
                                   "border-radius: 2px;"
                                   "border: 1px solid #3873d9;"
                                   "background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, "
                                   "stop: 0 #4287ff, stop: 1 #356ccc);"
                                   )
        self.reg_btn.clicked.connect(self.insertData)
        self.layout3.addWidget(self.reg_btn)

        self.main_layout.addLayout(self.layout1)
        self.main_layout.addLayout(self.layout2)
        self.main_layout.addLayout(self.layout3)

        self.central_widget.setLayout(self.main_layout)

    def insertData(self):
        login = self.login.text()
        password = self.password.text()
        if not login or not password:
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return
        db = 'login.db'
        con = sqlite3.connect(db)
        cur = con.cursor()
        result = cur.execute(f"""SELECT login FROM data_table WHERE login = '{login}' """).fetchone()
        if not result:
            # в бд хранится хеш
            password = hashlib.sha1(bytes(password, encoding='utf-8')).hexdigest()
            cur.execute(f"""INSERT INTO data_table (login, password) VALUES('{login}', '{password}') """)
            con.commit()
            con.close()
            self.close()
        else:
            msg = QMessageBox.information(self, 'Внимание!', 'Пользоватеть с таким именем уже зарегистрирован.')


class GenreChoice(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GenreChoice.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Выбор жанра')
        self.centralwidget.setStyleSheet(
            'background-color: #474a51;'
        )

        db = 'login.db'
        con = sqlite3.connect(db)
        cur = con.cursor()
        # в бд хранится строка с любимыми песнями
        result = cur.execute(f"""SELECT songs FROM data_table WHERE login = '{win.login.text()}' """).fetchone()[0]
        con.close()

        if not result:
            self.lst = []
        else:
            self.lst = [el.split('  ') for el in result.split(',')]

        # проверка на то, что открыты ли любимые песни
        self.fsongs = None

        self.choose_genres()

        self.search_btn.setStyleSheet("padding:4px;"
                                      "color: #fff;"
                                      "font-size: 14px;"
                                      "border-radius: 2px;"
                                      "border: 1px solid #3873d9;"
                                      "background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, "
                                      "stop: 0 #4287ff, stop: 1 #356ccc);"
                                      )
        self.search_btn.clicked.connect(self.search)

        self.favourite_btn.clicked.connect(self.favourite)
        self.favourite_btn.setStyleSheet("padding:4px;"
                                         "color: #fff;"
                                         "font-size: 14px;"
                                         "border-radius: 2px;"
                                         "border: 1px solid #3873d9;"
                                         "background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, "
                                         "stop: 0 #4287ff, stop: 1 #356ccc);"
                                         )

        self.genre_combobox.setStyleSheet("padding:4px;"
                                          "color: #fff;"
                                          "font-size: 14px;"
                                          "border-radius: 2px;"
                                          "border: 2px solid #3873d9;"
                                          )

        self.label.setStyleSheet("color: #fff;"
                                 "font-size: 14px;"
                                 )

    def search(self):
        songs = Songs(self, self.genre_combobox.currentText())
        songs.show()

    def choose_genres(self):
        db = 'music_db.db'
        con = sqlite3.connect(db)
        cur = con.cursor()
        result = cur.execute("""SELECT genre FROM genres""").fetchall()
        self.genre_combobox.addItems([el[0] for el in result])
        con.close()

    def favourite(self):
        self.fsongs = FavouriteSongs(self, self.lst)
        self.fsongs.show()


class FavouriteSongs(QMainWindow):
    def __init__(self, parent, lst):
        super().__init__(parent)
        self.tracks = lst
        self.initUI()

    def initUI(self):
        # любимые песни записываются в csv файл
        with open('songs.csv', encoding="utf8", mode='w') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for el in self.tracks:
                writer.writerow(f'{el[0]} - {el[1]}')

        self.setWindowTitle('Любимые песни')
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(
            'background-color: #474a51;'
        )
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self)

        self.lst = QListWidget(self)
        self.layout.addWidget(self.lst)

        self.songs()

    def songs(self):
        self.btns = {}

        for el in self.tracks:
            track_name, artist, track, image = el
            btn = QPushButton(self)
            self.btns[btn] = [track_name, artist, track, image]

            probel1 = 10
            probel2 = 90 - len(track_name)
            probel3 = 90 - len(artist)

            btn.setText(probel1 * ' ' + f'{track_name}' + probel2 * ' ' + '\n' + probel1 * ' ' + f'{artist}' +
                        probel3 * ' ')

            btn.setMinimumHeight(30)
            btn.setIcon(QIcon(image))
            btn.setIconSize(QSize(50, 50))
            btn.clicked.connect(self.click)
            btn.setStyleSheet("padding:4px;"
                              "color: #fff;"
                              "font-size: 14px;"
                              "border-radius: 2px;"
                              "border: 1px solid #3873d9;"
                              "background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, "
                              "stop: 0 #4287ff, stop: 1 #356ccc);"
                              )
            item = QListWidgetItem()
            self.lst.addItem(item)
            self.lst.setItemWidget(item, btn)
            item.setSizeHint(btn.sizeHint())

        self.central_widget.setLayout(self.layout)

    def click(self):
        self.song = Song(self, self.btns[self.sender()])
        self.song.show()

    def closeEvent(self, event):
        win.win.fsongs = None


class Songs(QMainWindow):
    def __init__(self, parent, genre):
        super().__init__(parent)
        self.genre = genre
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Песни')
        self.setGeometry(500, 200, 500, 500)
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(
            'background-color: #474a51;'
        )
        self.setCentralWidget(self.central_widget)

        self.con = sqlite3.connect('music_db.db')
        cur = self.con.cursor()
        self.result = cur.execute(
            """SELECT track_name, artist, track, image FROM tracks WHERE genre = (SELECT id FROM genres 
            WHERE genre = ?)""",
            (self.genre,)).fetchall()

        self.layout = QVBoxLayout(self)
        self.lst = QListWidget(self)
        self.layout.addWidget(self.lst)
        self.songs()

    def songs(self):
        self.btns = {}

        # песни записываются в QListWidget
        for el in self.result:
            track_name, artist, track, image = el
            btn = QPushButton(self)
            self.btns[btn] = [track_name, artist, track, image]

            probel1 = 10
            probel2 = 90 - len(track_name)
            probel3 = 90 - len(artist)

            btn.setText(probel1 * ' ' + f'{track_name}' + probel2 * ' ' + '\n' + probel1 * ' ' + f'{artist}' +
                        probel3 * ' ')

            btn.setMinimumHeight(30)
            # у песни есть картинка с обложки альбома
            btn.setIcon(QIcon(image))
            btn.setIconSize(QSize(50, 50))
            # при нажатии на кнопку с песней открывается окно с возможностью воспроизвести песню
            btn.clicked.connect(self.click)
            btn.setStyleSheet("padding:4px;"
                              "color: #fff;"
                              "font-size: 14px;"
                              "border-radius: 2px;"
                              "border: 1px solid #3873d9;"
                              "background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, "
                              "stop: 0 #4287ff, stop: 1 #356ccc);"
                              )
            item = QListWidgetItem()
            self.lst.addItem(item)
            self.lst.setItemWidget(item, btn)
            item.setSizeHint(btn.sizeHint())

        self.central_widget.setLayout(self.layout)

    def click(self):
        song = Song(self, self.btns[self.sender()])
        song.show()

    def closeEvent(self, event):
        self.con.close()


class Song(QMainWindow):
    def __init__(self, parent, track):
        self.track_name, self.artist, self.track, self.image = self.lst = track
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.artist + ' - ' + self.track_name)
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet(
            'background-color: #474a51;'
        )
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self)

        self.layout1 = QVBoxLayout(self)
        self.pixmap = QPixmap(self.image)
        self.image1 = QLabel(self)
        self.image1.setPixmap(self.pixmap)
        self.layout1.addWidget(self.image1)

        self.load_mp3(self.track)

        self.layout2 = QHBoxLayout(self)
        self.playBtn = QPushButton(self)
        # включить песню
        self.playBtn.clicked.connect(self.player.play)
        self.playBtn.setIcon(QIcon('images/zapusk.png'))
        self.playBtn.setIconSize(QSize(25, 25))
        self.playBtn.setStyleSheet("padding:4px;"
                                   "color: #fff;"
                                   "font-size: 14px;"
                                   "border-radius: 7px;"
                                   "border: 2px solid #3873d9;"
                                   )
        self.layout2.addWidget(self.playBtn)

        self.pauseBtn = QPushButton(self)
        # поставить на паузу
        self.pauseBtn.clicked.connect(self.player.pause)
        self.pauseBtn.setIcon(QIcon('images/pause.png'))
        self.pauseBtn.setIconSize(QSize(25, 25))
        self.pauseBtn.setStyleSheet("padding:4px;"
                                    "color: #fff;"
                                    "font-size: 14px;"
                                    "border-radius: 7px;"
                                    "border: 2px solid #3873d9;"
                                    )
        self.layout2.addWidget(self.pauseBtn)

        self.add_btn = QPushButton(self)
        self.add_btn.clicked.connect(self.add)
        if self.lst in win.win.lst:
            # если песня есть в любимых сердечко красное
            self.add_btn.setIcon(QIcon('images/add_red.png'))
        else:
            self.add_btn.setIcon(QIcon('images/add_black.png'))
        self.add_btn.setIconSize(QSize(25, 25))
        self.add_btn.setStyleSheet("padding:4px;"
                                   "color: #fff;"
                                   "font-size: 14px;"
                                   "border-radius: 7px;"
                                   "border: 2px solid #3873d9;"
                                   )
        self.layout2.addWidget(self.add_btn)

        self.main_layout.addLayout(self.layout1)
        self.main_layout.addLayout(self.layout2)
        self.central_widget.setLayout(self.main_layout)

    def load_mp3(self, filename):
        # загрузка песни
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def add(self):
        lst = [self.track_name, self.artist, self.track, self.image]
        db = 'login.db'
        con = sqlite3.connect(db)
        cur = con.cursor()
        result = cur.execute(f'''SELECT songs FROM data_table WHERE login = '{win.login.text()}' ''').fetchone()[0]

        if lst not in win.win.lst:
            win.win.lst.append(lst)
            lst = '  '.join(lst)
            if not result:
                result = lst
            else:
                result += ',' + lst
            self.add_btn.setIcon(QIcon('images/add_red.png'))
        else:
            win.win.lst.remove(lst)
            result = ', '.join(['  '.join(el) for el in win.win.lst])
            self.add_btn.setIcon(QIcon('images/add_black.png'))
        cur.execute('''UPDATE data_table SET songs = ? WHERE login = ? ''', (result, win.login.text()))
        con.commit()
        con.close()

    def closeEvent(self, event):
        if win.win.fsongs:
            # если открыт список с любимыми песнями и пользователь удалил песню из любимых, список обновляется
            win.win.fsongs.lst.clear()
            win.win.fsongs.tracks = win.win.lst
            win.win.fsongs.songs()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Entr()
    win.show()

    sys.excepthook = except_hook
    sys.exit(app.exec())
