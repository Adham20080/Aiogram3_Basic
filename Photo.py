from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

album_builder = MediaGroupBuilder(caption="Apple iphone 14 pro max style")
album_builder.add(type="photo", media=FSInputFile("image_from_pc.jpg"))
album_builder.add_photo(media="https://images.app.goo.gl/6faejXkHcnCcw37s8")
album_builder.add_photo(media="https://images.app.goo.gl/cQw9iKqvmg6euYva9")
album_builder.add_photo(media="https://images.app.goo.gl/x4hBA1Nxa69kk15h9")
album_builder.add_photo(media="https://images.app.goo.gl/W9SkjvnwBDcgnKeP8")
# await message.answer_media_group(
#     # Не забудьте вызвать build()
#     media=album_builder.build()
# )
