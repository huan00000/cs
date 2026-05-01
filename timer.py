import time
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(content):
    with open("time_log.txt", "a", encoding="utf-8") as f:
        f.write(content + "\n")

if __name__ == "__main__":
    start_timestamp = time.time()
    t1 = get_current_time()
    log1 = f"【程序启动】当前时间：{t1}"
    print(log1)
    write_log(log1)

    # 5小时59分 单位秒
    wait_5h59m = 5 * 3600 + 59 * 60
    time.sleep(wait_5h59m)

    t2 = get_current_time()
    log2 = f"【5小时59分后】当前时间：{t2}"
    print(log2)
    write_log(log2)

    time.sleep(50)

    t3 = get_current_time()
    log3 = f"【再加50秒后】当前时间：{t3}"
    print(log3)
    write_log(log3)

    print("【进入1分钟每秒计时阶段】")
    write_log("【进入1分钟每秒计时阶段】")
    for sec in range(60):
        run_time = time.time() - start_timestamp
        log_txt = f"第{sec+1}秒，已运行时长：{run_time:.2f} 秒"
        print(log_txt)
        write_log(log_txt)
        time.sleep(1)

    end_log = "【所有流程完成，程序结束】"
    print(end_log)
    write_log(end_log)
