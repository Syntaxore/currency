from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from ..States.states import UserData
from ..CurrencyAPI.currency import Currency

currency = Currency()

router = Router()

@router.callback_query(F.data == "conv")
async def conv(q: CallbackQuery, state: FSMContext):
    await q.answer()
    text = "💵 Введи данные для конвертации в таком формате (Валюта1:Валюта2:Сумма)\n\nПример: USD:RUB:10"
    await state.set_state(UserData.data)
    await q.message.edit_text(text)

@router.message(UserData.data)
async def conv_state(message: Message, state: FSMContext):
    await state.update_data(user_input=message.text)
    user_data = await state.get_data()
    try:
        value0, value1, amount = user_data["user_input"].split(":")
        data = currency.get_pair(value0, value1, float(amount))

        if "error" in data:
            await message.answer(f"Ошибка API: {data['error']}")
        else:
            result = data["conversion_result"]
            await message.answer(f"Результат: {result} {value1}")
    except Exception as e:
        await message.answer(f"Ошибка формата. Введи: USD:RUB:10")
    finally:
        await state.clear()