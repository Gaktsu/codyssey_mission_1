import os
from datetime import datetime

# 데이터 저장 파일
DATA_FILE = "attendance.csv"

def add_attendance(date, name):
    """출석 기록 추가 (핵심 기능)"""
    attendance = load_attendance()
    record = f"{date},{name}"
    
    # 중복 확인
    if record in attendance:
        print(f"⚠️  이미 기록되어 있습니다: {date} - {name}")
        return
    
    attendance.append(record)
    save_attendance(attendance)
    print(f"✅ 출석 기록됨: {date} - {name}")

def show_attendance():
    """출석 목록 보기 (핵심 기능)"""
    attendance = load_attendance()
    
    if not attendance:
        print("📋 기록된 출석이 없습니다.")
        return
    
    print("\n" + "=" * 40)
    print("📋 출석 목록")
    print("="*40)
    for i, record in enumerate(attendance, 1):
        date, name = record.split(',')
        print(f"{i}. {date} - {name}")
    print("=" * 40 + "\n")

def load_attendance():
    """저장된 출석 데이터 불러오기 (부가 기능)"""
    if not os.path.exists(DATA_FILE):
        return []
    
    attendance = []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:  # 빈 줄 무시
                attendance.append(line)
    return attendance

def save_attendance(attendance):
    """출석 데이터 저장하기 (부가 기능)"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        for record in attendance:
            f.write(record + '\n')

def main():
    """메인 메뉴"""
    while True:
        print("\n🎯 출석부 프로그램")
        print("1. 출석 기록하기")
        print("2. 출석 목록 보기")
        print("3. 종료")
        
        choice = input("선택 (1-3): ").strip()
        
        if choice == '1':
            date = input("날짜 입력 (YYYY-MM-DD): ").strip()
            name = input("이름 입력: ").strip()
            
            if date and name:
                add_attendance(date, name)
            else:
                print("⚠️  날짜와 이름을 모두 입력해주세요.")
        
        elif choice == '2':
            show_attendance()
        
        elif choice == '3':
            print("👋 프로그램을 종료합니다.")
            break
        
        else:
            print("⚠️  1-3 중에서 선택해주세요.")

if __name__ == "__main__":
    main()