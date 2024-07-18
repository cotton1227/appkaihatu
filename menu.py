import tkinter as tk
from tkinter import messagebox, font, simpledialog

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

class MealPlanningApp:
    def __init__(self, root):
        self.menus = []
        self.schedule = WeeklySchedule()
        self.root = root
        self.root.title("2116綿貫大希")
        self.root.geometry("360x640")
        
        # カラーパレットの定義
        self.bg_color = "#FFFCD2"
        self.text_color = "#FF6900"
        self.button_color = "#FF6900"
        self.button_text_color = "#FFFFFF"
        self.accent_color = "#FF6900"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
    
    def create_widgets(self):
        main_font = font.Font(family="Yu Gothic Medium", size=14, weight="bold")
        title_font = font.Font(family="Yu Gothic Medium", size=18, weight="bold")
        deka_font = font.Font(family="Yu Gothic Medium", size=30, weight="bold")
        
        # タイトル
        title_label = tk.Label(self.root, text="ランダム食事アプリ", font=deka_font, bg=self.bg_color, fg=self.text_color)
        title_label.pack(pady=20)
        
        # メニュー管理フレーム
        menu_frame = tk.Frame(self.root, bg=self.bg_color)
        menu_frame.pack(pady=10, padx=20, fill=tk.X)
        
        menu_label = tk.Label(menu_frame, text="メニュー管理", font=main_font, bg=self.bg_color, fg=self.text_color)
        menu_label.pack(pady=5)
        
        self.menu_entry = tk.Entry(menu_frame, font=main_font, width=20)
        self.menu_entry.pack(pady=5, fill=tk.X)
        
        add_menu_button = tk.Button(menu_frame, text="メニューを追加", command=self.add_menu, font=main_font, 
                                    bg=self.button_color, fg=self.button_text_color, activebackground=self.accent_color)
        add_menu_button.pack(pady=5, fill=tk.X)
        
        edit_menu_button = tk.Button(menu_frame, text="メニューを編集", command=self.edit_menu, font=main_font, 
                                     bg=self.button_color, fg=self.button_text_color, activebackground=self.accent_color)
        edit_menu_button.pack(pady=5, fill=tk.X)
        
        delete_menu_button = tk.Button(menu_frame, text="メニューを削除", command=self.delete_menu, font=main_font, 
                                       bg=self.button_color, fg=self.button_text_color, activebackground=self.accent_color)
        delete_menu_button.pack(pady=5, fill=tk.X)
        
        display_menu_button = tk.Button(menu_frame, text="メニューを表示", command=self.display_menus, font=main_font, 
                                        bg=self.button_color, fg=self.button_text_color, activebackground=self.accent_color)
        display_menu_button.pack(pady=5, fill=tk.X)
        
        reset_menu_button = tk.Button(menu_frame, text="メニューをリセット", command=self.reset_menus, font=main_font, 
                                      bg=self.button_color, fg=self.button_text_color, activebackground=self.accent_color)
        reset_menu_button.pack(pady=5, fill=tk.X)
        
        # スケジュール管理フレーム
        schedule_frame = tk.Frame(self.root, bg=self.bg_color)
        schedule_frame.pack(pady=10, padx=20, fill=tk.X)
        
        schedule_label = tk.Label(schedule_frame, text="スケジュール管理", font=main_font, bg=self.bg_color, fg=self.text_color)
        schedule_label.pack(pady=5)
        
        assign_meals_button = tk.Button(schedule_frame, text="1週間の食事をランダムに割り当て", command=self.assign_meals_randomly, font=main_font, 
                                        bg=self.accent_color, fg=self.button_text_color, activebackground=self.button_color)
        assign_meals_button.pack(pady=5, fill=tk.X)
        
        display_schedule_button = tk.Button(schedule_frame, text="週間スケジュールを表示", command=self.display_schedule, font=main_font, 
                                            bg=self.button_color, fg=self.button_text_color, activebackground=self.accent_color)
        display_schedule_button.pack(pady=5, fill=tk.X)

    def add_menu(self):
        name = self.menu_entry.get().strip()
        if not name:
            messagebox.showerror("エラー", "メニュー名を入力してください。")
            return
    
        menu = Menu(name)
        self.menus.append(menu)
        messagebox.showinfo("成功", f"メニュー '{name}' を追加しました。")
        self.menu_entry.delete(0, tk.END)
    
    def edit_menu(self):
        if not self.menus:
            messagebox.showerror("エラー", "編集するメニューがありません。")
            return
        
        menu_names = [menu.name for menu in self.menus]
        choice = simpledialog.askstring("メニュー編集", "編集するメニューを選択してください：\n" + "\n".join(menu_names))
        
        if choice:
            for menu in self.menus:
                if menu.name == choice:
                    new_name = simpledialog.askstring("メニュー編集", f"'{choice}' の新しい名前を入力してください：")
                    if new_name:
                        menu.edit(new_name)
                        messagebox.showinfo("成功", f"メニュー '{choice}' を '{new_name}' に変更しました。")
                    return
            
            messagebox.showerror("エラー", f"メニュー '{choice}' が見つかりません。")
    
    def delete_menu(self):
        if not self.menus:
            messagebox.showerror("エラー", "削除するメニューがありません。")
            return
        
        menu_names = [menu.name for menu in self.menus]
        choice = simpledialog.askstring("メニュー削除", "削除するメニューを選択してください：\n" + "\n".join(menu_names))
        
        if choice:
            for menu in self.menus:
                if menu.name == choice:
                    self.menus.remove(menu)
                    messagebox.showinfo("成功", f"メニュー '{choice}' を削除しました。")
                    return
            
            messagebox.showerror("エラー", f"メニュー '{choice}' が見つかりません。")
    
    def display_menus(self):
        if self.menus:
            menus_str = "\n".join([menu.name for menu in self.menus])
            messagebox.showinfo("登録されたメニュー", menus_str)
        else:
            messagebox.showinfo("メニューなし", "登録されたメニューがありません。")
    
    def reset_menus(self):
        self.menus = []
        messagebox.showinfo("成功", "メニューをリセットしました。")
    
    def assign_meals_randomly(self):
        if not self.menus:
            messagebox.showwarning("エラー", "メニューが登録されていません。")
            return
        
        self.schedule.reset_schedule()
        
        days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
        meal_times = ["朝食", "昼食", "夕食"]
        
        for day in days:
            for meal_time in meal_times:
                random_menu = random.choice(self.menus)
                self.schedule.assign_menu(day, meal_time, random_menu)
        
        messagebox.showinfo("成功", "週の食事がランダムに割り当てられました。")
    
    def display_schedule(self):
        schedule_str = ""
        for day, meals in self.schedule.days.items():
            schedule_str += f"{day}:\n"
            schedule_str += f"  朝食: {meals.breakfast.name if meals.breakfast else '未割り当て'}\n"
            schedule_str += f"  昼食: {meals.lunch.name if meals.lunch else '未割り当て'}\n"
            schedule_str += f"  夕食: {meals.dinner.name if meals.dinner else '未割り当て'}\n"
        
        messagebox.showinfo("週間スケジュール", schedule_str)

# アプリの実行
if __name__ == "__main__":
    root = tk.Tk()
    app = MealPlanningApp(root)
    root.mainloop()
