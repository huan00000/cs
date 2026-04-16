import subprocess
import os

def generate_prompt(
    code_dir: str = "./你的代码目录",  # 你要扫描的代码文件夹
    output_file: str = "prompt.txt"   # 输出文件
):
    """
    使用 code2prompt 生成 AI 提示词（Python 封装版）
    """
    # 二进制文件路径（Ubuntu 编译后位置）
    binary_path = "./code2prompt-main/target/release/code2prompt"

    # 检查二进制是否存在
    if not os.path.exists(binary_path):
        print("❌ 未找到编译后的 code2prompt，请先执行：cargo build --release")
        return

    # 构建命令（和原命令完全等价）
    cmd = [
        binary_path,
        code_dir,
        "--output",
        output_file
    ]

    try:
        print(f"✅ 开始扫描目录：{code_dir}")
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        print(f"✅ 生成成功！输出文件：{output_file}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ 运行失败：{e.stderr}")
        return False


# ==================== 直接运行 ====================
if __name__ == "__main__":
    # 你只需要改这里！
    代码目录 = "./test_code"    # 你的代码文件夹
    输出文件 = "prompt.txt"     # 输出文件名

    generate_prompt(code_dir=代码目录, output_file=输出文件)
