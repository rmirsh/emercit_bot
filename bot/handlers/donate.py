from aiogram import Router, types, F
from aiogram.filters import Command

router = Router()


@router.message(Command("donate"))
async def cmd_donate(message: types.Message):
    """Donate to the project.

    This function sends a message to the user with a link to the project's
    donation page.

    Args:
        message (types.Message): The message object triggering the command.
    """
    await message.answer(
        "Спасибо большое за ваш донат 🙏\n"
        "Ваша поддержка помогает мне развивать бота и добавлять новые функции.\n"
        "Если у вас есть предложения или вопросы, пишите [мне](tg://user?id=446913605)"
        "в любое время.\n\n"
        "Отправить пожертвование можно на карту Сбербанка:\n"
        "```2202 2061 1476 2706```",
        reply_markup=types.ReplyKeyboardRemove(),
    )
