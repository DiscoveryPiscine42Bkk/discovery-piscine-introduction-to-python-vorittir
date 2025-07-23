from typing import List
from collections import defaultdict

class Task:
    def __init__(self, name: str, date: str, task_type: str):
        self.name = name
        self.date = date
        self.task_type = task_type

    def __str__(self):
        return f"{self.date} - {self.name} (Type {self.task_type})"

class SmartFarmTaskOrganizer:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, name: str, date: str, task_type: str):
        task = Task(name, date, task_type)
        self.tasks.append(task)
        print("\n✅ เพิ่มงานสำเร็จ")

    def show_all_tasks(self):
        print("\n📋 รายการงานทั้งหมด:")
        if not self.tasks:
            print("△ ยังไม่มีงานในรายการ")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def delete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"\n🗑️ ลบงาน: {removed.name} แล้ว")
        else:
            print("❌ ไม่พบงานในลำดับที่ระบุ")

    def summarize_tasks_by_type(self):
        summary = defaultdict(int)
        for task in self.tasks:
            summary[task.task_type] += 1

        print("\n📊 สรุปจำนวนงานแต่ละประเภท:")
        if not summary:
            print("△ ยังไม่มีงานในระบบ")
        else:
            for task_type, count in summary.items():
                print(f"- Type {task_type}: {count} งาน")

def display_menu():
    print("\n====== Smart Farm Task Organizer ======")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def main():
    organizer = SmartFarmTaskOrganizer()

    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ").strip()

        if choice == "1":
            name = input("📝 ชื่องาน: ")
            date = input("📅 วันที่ (dd/mm/yyyy): ")
            task_type = input("📌 ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ").strip().split()[-1]  # เก็บตัวอักษรสุดท้าย เช่น Type A
            organizer.add_task(name, date, task_type)

        elif choice == "2":
            organizer.show_all_tasks()

        elif choice == "3":
            organizer.show_all_tasks()
            if organizer.tasks:
                try:
                    index = int(input("❗ ลำดับของงานที่ต้องการลบ: ")) - 1
                    organizer.delete_task(index)
                except ValueError:
                    print("❌ กรุณากรอกตัวเลขให้ถูกต้อง")

        elif choice == "4":
            organizer.summarize_tasks_by_type()

        elif choice == "5":
            print("\n👋 ขอบคุณที่ใช้โปรแกรม Smart Farm!")
            break

        else:
            print("❌ กรุณาเลือกเมนูระหว่าง 1 ถึง 5 เท่านั้น")

if __name__ == "__main__":
    main()