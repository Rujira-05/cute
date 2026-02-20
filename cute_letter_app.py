import tkinter as tk
from tkinter import simpledialog
import random
import math

class CuteLetterApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw() # ซ่อนหน้าต่างหลักไว้ก่อนเพื่อถามชื่อ
        
        # 1. ถามชื่อเล่น
        self.name = simpledialog.askstring("Hello!", "ใส่ชื่อเล่นของคุณตรงนี้เลยยย 💕:")
        if not self.name:
            self.name = "คนน่ารัก"
            
        self.root.deiconify() # แสดงหน้าต่างหลัก
        self.root.title("Letter from Lisa 💌")
        self.root.geometry("600x600")
        self.root.configure(bg='#ffe6f2') # พื้นหลังสีชมพูพาสเทล
        
        # สร้าง Canvas สำหรับวาดรูป
        self.canvas = tk.Canvas(root, width=600, height=600, bg='#ffe6f2', highlightthickness=0)
        self.canvas.pack()
        
        # ตัวแปรสถานะ
        self.is_opened = False
        self.wiggle_offset = 0
        self.wiggle_direction = 1
        self.flowers = []
        
        # ข้อความหัวข้อ
        self.title_text = self.canvas.create_text(
            300, 100, 
            text=f"💌 มีจดหมายจาก ลิซ่า ถึง {self.name} 💌", 
            font=("Helvetica", 24, "bold"), fill="#ff4d94"
        )
        
        # กลุ่มของภาพซองจดหมาย
        self.envelope_items = []
        self.draw_envelope()
        
        # เริ่มแอนิเมชันซองดุ๊กดิ๊ก
        self.wiggle_envelope()
        
        # ตั้งค่าให้คลิกที่ Canvas แล้วจดหมายเปิด
        self.canvas.bind("<Button-1>", self.open_letter)

    def draw_envelope(self):
        # วาดตัวซองจดหมาย
        body = self.canvas.create_rectangle(200, 250, 400, 380, fill="#ffb3d9", outline="#ff66b3", width=3)
        # วาดฝาปิดซองจดหมาย (แบบปิด)
        self.flap_closed = self.canvas.create_polygon(200, 250, 300, 320, 400, 250, fill="#ff99cc", outline="#ff66b3", width=3)
        
        self.envelope_items.extend([body, self.flap_closed])

    def wiggle_envelope(self):
        if self.is_opened:
            return # หยุดดุ๊กดิ๊กถ้าเปิดแล้ว
        
        # ขยับซ้ายขวา
        move_x = self.wiggle_direction * 2
        for item in self.envelope_items:
            self.canvas.move(item, move_x, 0)
            
        self.wiggle_offset += move_x
        if abs(self.wiggle_offset) > 10:
            self.wiggle_direction *= -1 # สลับทิศทาง
            
        self.root.after(100, self.wiggle_envelope)

    def open_letter(self, event):
        # เช็คว่าคลิกโดนซองจดหมายหรือเปล่า และยังไม่ได้เปิดใช่ไหม
        if not self.is_opened:
            x, y = event.x, event.y
            if 150 <= x <= 450 and 200 <= y <= 400: # พื้นที่ซองโดยประมาณ
                self.is_opened = True
                
                # ลบฝาปิด
                self.canvas.delete(self.flap_closed)
                
                # วาดกระดาษจดหมายโผล่ขึ้นมา
                self.paper = self.canvas.create_rectangle(210, 180, 390, 380, fill="white", outline="#cccccc", width=2)
                self.message = self.canvas.create_text(
                    300, 280, 
                    text=f"สวัสดี {self.name}!\n\nขอให้วันนี้เป็นวันที่ดี\nสดใสเหมือนดอกไม้พวกนี้นะ\nยิ้มเยอะๆ ล่ะ 😊\n\nรัก,\nลิซ่า", 
                    font=("Helvetica", 14), fill="#333333", justify="center"
                )
                
                # วาดฝาเปิดซองจดหมาย (ชี้ขึ้น)
                self.flap_opened = self.canvas.create_polygon(200, 250, 300, 180, 400, 250, fill="#ffb3d9", outline="#ff66b3", width=3)
                
                # เอาฝาซองมาบังกระดาษด้านล่าง (จัดลำดับ Layer)
                self.canvas.tag_raise(self.flap_opened)
                
                # เริ่มแอนิเมชันดอกไม้พุ่ง
                self.burst_flowers()

    def burst_flowers(self):
        emojis = ['🌸', '🌺', '🌼', '🌷', '✨', '💖']
        for _ in range(40): # จำนวนดอกไม้
            char = random.choice(emojis)
            x, y = 300, 250 # จุดศูนย์กลางที่พุ่งออกมา (ปากซอง)
            
            # สุ่มมุมและความเร็ว
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(5, 15)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed - 5 # ลบ 5 เพื่อให้พุ่งขึ้นข้างบนมากกว่า
            
            # สร้างตัวอักษรดอกไม้
            item = self.canvas.create_text(x, y, text=char, font=("Arial", random.randint(16, 28)))
            self.flowers.append({'item': item, 'vx': vx, 'vy': vy, 'life': 100})
            
        self.animate_flowers()

    def animate_flowers(self):
        active_flowers = []
        for f in self.flowers:
            # ขยับดอกไม้
            self.canvas.move(f['item'], f['vx'], f['vy'])
            # เพิ่มแรงโน้มถ่วงให้ตกลงมา
            f['vy'] += 0.8
            f['life'] -= 1
            
            # ถ้ายังไม่หมดอายุขัย ให้เก็บไว้ทำแอนิเมชันต่อ
            if f['life'] > 0 and self.canvas.coords(f['item'])[1] < 700:
                active_flowers.append(f)
            else:
                self.canvas.delete(f['item'])
                
        self.flowers = active_flowers
        
        if self.flowers:
            self.root.after(30, self.animate_flowers)

if __name__ == "__main__":
    root = tk.Tk()
    app = CuteLetterApp(root)
    root.mainloop()