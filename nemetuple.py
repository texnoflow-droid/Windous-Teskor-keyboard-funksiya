import asyncio

async def hisobla(son):
    print(f"{son} ning kvadrati hisoblanmoqda...")
    await asyncio.sleep(1)
    print(f"{son} kvadrati = {son**2}")



async def test():
    print(f"Test ishga tushdi")
    await asyncio.sleep(5)
    print(f"Test tugadi")


async def test2():
    print(f"Test2 ishga tushdi")
    await asyncio.sleep(0)
    print(f"Test2 tugadi")

async def main():
    # 3 ta vazifani parallel bajarish
    await asyncio.gather(
        hisobla(2),
        test(),
        test2()
    )

asyncio.run(main())