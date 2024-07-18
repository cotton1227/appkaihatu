import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QLineEdit, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt, QSize

class Menu:
    def __init__(self, name):
        self.name = name
    
    def edit(self, new_name):
        self.name = new_name

class DailyMeals:
    def __init__(self):
        self.breakfast = None
        self.lunch = None
        self.dinner = None

class WeeklySchedule:
    def __init__(self):
        self.days = {
            "月曜日": DailyMeals(),
            "火曜日": DailyMeals(),
            "水曜日": DailyMeals(),
            "木曜日": DailyMeals(),
            "金曜日": DailyMeals(),
            "土曜日": DailyMeals(),
            "日曜日": DailyMeals(),
        }
    
    def assign_menu(self, day, meal_time, menu):
        if day in self.days:
            if meal_time == "朝食":
                self.days[day].breakfast = menu
            elif meal_time == "昼食":
                self.days[day].lunch = menu
            elif meal_time == "夕食":
                self.days[day].dinner = menu
            else:
                print("無効な食事時間です。")
        else:
            print("無効な曜日です。")
    
    def reset_schedule(self):
        for day in self.days.values():
            day.breakfast = None
            day.lunch = None
            day.dinner = None

class MealPlanningApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menus = []
        self.schedule = WeeklySchedule()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("2116綿貫大希")
        self.setGeometry(100, 100, 360, 640)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        central_widget.setStyleSheet("background-color: #FFFFFF;")

        layout = QGridLayout()
        central_widget.setLayout(layout)
        
        title = QLabel("ランダム食事アプリ")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #222222;
            margin-bottom: 20px;
            text-align: center;
        """)
        title.setAlignment(Qt.AlignCenter)  # Set alignment for the title
        layout.addWidget(title, 0, 0, 1, 3)  # Span across 3 columns
        
        menu_label = QLabel("メニュー管理")
        menu_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #444444;
            margin-bottom: 10px;
        """)
        layout.addWidget(menu_label, 1, 0, 1, 3)  # Span across 3 columns
        
        self.menu_entry = QLineEdit()
        self.menu_entry.setStyleSheet("""
            font-size: 24px;
            background-color: #c9d2d7;
            padding: 10px;
            border: 1px solid #cccccc;
            border-radius: 10px;
            margin-bottom: 10px;
        """)
        layout.addWidget(self.menu_entry, 2, 0, 1, 3)  # Span across 3 columns
        
        add_menu_button = self.create_button("追加")
        layout.addWidget(add_menu_button, 3, 0)
        add_menu_button.clicked.connect(self.add_menu)
        
        edit_menu_button = self.create_button("編集")
        layout.addWidget(edit_menu_button, 3, 1)
        edit_menu_button.clicked.connect(self.edit_menu)
        
        delete_menu_button = self.create_button("削除")
        layout.addWidget(delete_menu_button, 3, 2)
        delete_menu_button.clicked.connect(self.delete_menu)
        
        display_menu_button = self.create_button("表示")
        layout.addWidget(display_menu_button, 4, 0)
        display_menu_button.clicked.connect(self.display_menus)
        
        reset_menu_button = self.create_button("リセット")
        layout.addWidget(reset_menu_button, 4, 1)
        reset_menu_button.clicked.connect(self.reset_menus)
        
        schedule_label = QLabel("スケジュール管理")
        schedule_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #444444;
            margin-top: 20px;
            margin-bottom: 10px;
        """)
        layout.addWidget(schedule_label, 5, 0, 1, 3)  # Span across 3 columns
        
        assign_meals_button = self.create_button("メニューを割り当て")
        assign_meals_button.setFixedWidth(330)
        layout.addWidget(assign_meals_button, 6, 0, 1, 3)  # Span across 3 columns
        assign_meals_button.clicked.connect(self.assign_meals_randomly)
        
        display_schedule_button = self.create_button("スケジュールを表示")
        display_schedule_button.setFixedWidth(330)
        layout.addWidget(display_schedule_button, 7, 0, 1, 3)  # Span across 3 columns
        display_schedule_button.clicked.connect(self.display_schedule)
    
    def create_button(self, text):
        button = QPushButton(text)
        button.setFixedSize(QSize(100, 100))  # ボタンの固定サイズを設定
    
    # ボタンごとに異なる背景色を設定する例
        if text == "追加":
            button.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    padding: 10px;
                    background-color: #df4d69;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
                QPushButton:hover {
                    background-color: #c5445e;  /* ホバー時の色 */
                }
                QPushButton:pressed {
                    background-color: #ac3e54;  /* 押下時の色 */
                }
            """)
        elif text == "編集":
            button.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    padding: 10px;
                    background-color: #dba059; 
                    color: white;
                    border: none;
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
                QPushButton:hover {
                    background-color: #b8874c;
                }
                QPushButton:pressed {
                    background-color: #a27744;
                }
            """)

        elif text == "削除":
            button.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    padding: 10px;
                    background-color: #c8682c;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
                QPushButton:hover {
                    background-color: #b8632e;
                }
                QPushButton:pressed {
                    background-color: #9c5326;
                }
            """)

        elif text == "表示":
            button.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    padding: 10px;
                    background-color: #dba059; 
                    color: white;
                    border: none;
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
                QPushButton:hover {
                    background-color: #b8874c;
                }
                QPushButton:pressed {
                    background-color: #a27744;
                }
            """)

        elif text == "リセット":
            button.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    padding: 10px;
                    background-color: #c8682c;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
                QPushButton:hover {
                    background-color: #b8632e;
                }
                QPushButton:pressed {
                    background-color: #9c5326;
                }
            """)

        else:
            # デフォルトのスタイルシート（他のボタンにも適用される）
            button.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    padding: 10px;
                    background-color: #0f8eae;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    margin-bottom: 10px;
                }
                QPushButton:hover {
                    background-color: #0d7791;
                }
                QPushButton:pressed {
                    background-color: #0d667d;
                }
            """)
        return button

    
    def add_menu(self):
        name = self.menu_entry.text().strip()
        if not name:
            QMessageBox.critical(self, "エラー", "メニュー名を入力してください。")
            return
        
        menu = Menu(name)
        self.menus.append(menu)
        QMessageBox.information(self, "成功", f"メニュー '{name}' を追加しました。")
        self.menu_entry.clear()
    
    def edit_menu(self):
        if not self.menus:
            QMessageBox.critical(self, "エラー", "編集するメニューがありません。")
            return
        
        menu_names = [menu.name for menu in self.menus]
        choice, ok = QInputDialog.getItem(self, "メニュー編集", "編集するメニューを選択してください：", menu_names, 0, False)
        
        if ok and choice:
            for menu in self.menus:
                if menu.name == choice:
                    new_name, ok = QInputDialog.getText(self, "メニュー編集", f"'{choice}' の新しい名前を入力してください：")
                    if ok and new_name:
                        menu.edit(new_name)
                        QMessageBox.information(self, "成功", f"メニュー '{choice}' を '{new_name}' に変更しました。")
                    return
            
            QMessageBox.critical(self, "エラー", f"メニュー '{choice}' が見つかりません。")
    
    def delete_menu(self):
        if not self.menus:
            QMessageBox.critical(self, "エラー", "削除するメニューがありません。")
            return
        
        menu_names = [menu.name for menu in self.menus]
        choice, ok = QInputDialog.getItem(self, "メニュー削除", "削除するメニューを選択してください：", menu_names, 0, False)
        
        if ok and choice:
            for menu in self.menus:
                if menu.name == choice:
                    self.menus.remove(menu)
                    QMessageBox.information(self, "成功", f"メニュー '{choice}' を削除しました。")
                    return
            
            QMessageBox.critical(self, "エラー", f"メニュー '{choice}' が見つかりません。")
    
    def display_menus(self):
        if self.menus:
            menus_str = "\n".join([menu.name for menu in self.menus])
            QMessageBox.information(self, "登録されたメニュー", menus_str)
        else:
            QMessageBox.information(self, "メニューなし", "登録されたメニューがありません。")
    
    def reset_menus(self):
        self.menus = []
        QMessageBox.information(self, "成功", "メニューをリセットしました。")
    
    def assign_meals_randomly(self):
        if not self.menus:
            QMessageBox.warning(self, "エラー", "メニューが登録されていません。")
            return
        
        self.schedule.reset_schedule()
        
        days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
        meal_times = ["朝食", "昼食", "夕食"]
        
        for day in days:
            for meal_time in meal_times:
                random_menu = random.choice(self.menus)
                self.schedule.assign_menu(day, meal_time, random_menu)
        
        QMessageBox.information(self, "成功", "週の食事がランダムに割り当てられました。")
    
    def display_schedule(self):
        schedule_str = ""
        for day, meals in self.schedule.days.items():
            schedule_str += f"{day}:\n"
            schedule_str += f"  朝食: {meals.breakfast.name if meals.breakfast else '未割り当て'}\n"
            schedule_str += f"  昼食: {meals.lunch.name if meals.lunch else '未割り当て'}\n"
            schedule_str += f"  夕食: {meals.dinner.name if meals.dinner else '未割り当て'}\n"
        
        QMessageBox.information(self, "週間スケジュール", schedule_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MealPlanningApp()
    ex.show()
    sys.exit(app.exec_())
