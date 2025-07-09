import subprocess
import time
from datetime import datetime


def run_step(desc: str, cmd: str) -> None:
    print(f'🟢 [{datetime.now():%Y-%m-%d %H:%M:%S}] 開始執行：{desc}')
    print(f'↪️ 指令：{cmd}')

    start_time = time.time()
    result = subprocess.run(cmd, shell=True)
    end_time = time.time()

    duration = end_time - start_time

    if result.returncode != 0:
        print(f'❌ [{desc}] 失敗 (耗時: {duration:.2f} 秒)\n')
        exit(1)

    print(f'✅ [{datetime.now():%Y-%m-%d %H:%M:%S}] 完成: {desc} (耗時: {duration:.2f} 秒)\n')


def main():
    steps = [
        ('scripts/build_database.py', f'python3 scripts/build_database.py'),
        ('scripts/build_view_table.py', f'python3 scripts/build_view_table.py')
    ]

    for desc, cmd in steps:
        run_step(desc, cmd)


if __name__ == '__main__':
    main()
