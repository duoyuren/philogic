import os

def update_scss_tags():
    # 獲取當前目錄下所有 .scss 文件
    files = [f for f in os.listdir('.') if f.endswith('.scss')]
    
    if not files:
        print("未找到任何 .scss 文件。")
        return

    processed_count = 0
    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # 執行替換：將 rules 標籤改為 defaults 標籤
            # 使用 replace 確保精確匹配
            if '/*-- scss:rules --*/' in content:
                new_content = content.replace('/*-- scss:rules --*/', '/*-- scss:defaults --*/')
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"  [成功] 已修改標籤: {filename}")
                processed_count += 1
            else:
                print(f"  [跳過] 未發現目標標籤: {filename}")

        except Exception as e:
            print(f"  [錯誤] 處理 {filename} 時發生異常: {e}")

    print(f"\n任務結束。共修改了 {processed_count} 個文件。")

if __name__ == "__main__":
    print(">>> 開始將 SCSS 標籤從 rules 切換至 defaults...")
    update_scss_tags()
