from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

album_builder = MediaGroupBuilder(caption="Apple iphone 14 pro max style")
album_builder.add(type="photo", media=FSInputFile("./img/ip1.webp"))
album_builder.add(type="photo", media=FSInputFile("./img/ip4.webp"))
album_builder.add(type="photo", media=FSInputFile("./img/ip2.jpg"))
album_builder.add(type="photo", media=FSInputFile("./img/ip3.jpg"))
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6")
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6")
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6")
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6")
# await message.answer_media_group(
#     # Не забудьте вызвать build()
#     media=album_builder.build()
# )
