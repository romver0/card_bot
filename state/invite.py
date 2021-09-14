from aiogram.dispatcher.filters.state import StatesGroup, State


class Invite(StatesGroup):
   unique_id=State()
