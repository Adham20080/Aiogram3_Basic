from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

album_builder = MediaGroupBuilder(caption="Apple iphone 14 pro max style")
album_builder.add(type="photo", media=FSInputFile("./img/ip1.webp")) # input local file
album_builder.add(type="photo", media=FSInputFile("./img/ip4.webp")) # input local file
album_builder.add(type="photo", media=FSInputFile("./img/ip2.jpg")) # input local file
album_builder.add(type="photo", media=FSInputFile("./img/ip3.jpg")) # input local file
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6") # input global file
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6") # input global file
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6") # input global file
album_builder.add_photo(media="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6") # input global file
# await message.answer_media_group(
#     # Не забудьте вызвать build()
#     media=album_builder.build()
# )
