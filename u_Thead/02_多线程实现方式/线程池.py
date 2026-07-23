from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def work_task(idx, sleep_t):
    print(f"任务{idx} 开始执行")
    time.sleep(sleep_t)
    return f"任务{idx} 结果值"

if __name__ == "__main__":
    # max_workers：最大并发线程数，IO密集可设20~100
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = []
        # 提交5个任务，池内最多同时3个线程运行
        for i in range(5):
            fut = pool.submit(work_task, i, i * 0.5)
            futures.append(fut)

        # 方式1：按提交顺序获取结果（阻塞）
        # for f in futures:
        #     print(f.result())

        # 方式2：任务完成立刻返回，无序，适合爬虫
        for future in as_completed(futures):
            try:
                res = future.result(timeout=3)  # 超时3秒抛异常
                print("已完成：", res)
            except Exception as e:
                print("任务异常：", e)
    # with代码块结束自动调用pool.shutdown(wait=True)，等待所有线程结束
    print("线程池全部任务执行完毕")