from aiogram import Dispatcher

from loader import dp
from .IsAdmin import AdminFilter
from .IsGroup import IsGroup
from .IsPrivate import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)