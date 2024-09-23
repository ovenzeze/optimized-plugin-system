import asyncio

def register():
    return "exec_better"

async def run(code: str, language: str, timeout: int = 60, max_retries: int = 3):
    # 简化版实现
    for _ in range(max_retries):
        try:
            if language == "python":
                return await asyncio.wait_for(exec_python(code), timeout)
            # 可以添加其他语言的支持
            else:
                raise ValueError(f"Unsupported language: {language}")
        except asyncio.TimeoutError:
            print(f"Execution timed out, retrying... ({_ + 1}/{max_retries})")
    raise TimeoutError(f"Execution failed after {max_retries} attempts")

async def exec_python(code):
    # 这里应该使用更安全的方法来执行代码
    return eval(code)

