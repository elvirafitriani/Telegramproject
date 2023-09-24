import os
from PIL import Image
import pytesseract
from telegram.ext import Updater, MessageHandler, Filters

# Fungsi untuk mengonversi foto menjadi teks
def convert_photo_to_text(update, context):
    # Mendapatkan objek foto dari pesan yang diterima
    photo = update.message.photo[-1].get_file()

    # Mendownload foto ke direktori lokal
    photo_path = 'photo' + photo.file_path.split('.')[-1]
    photo.download(photo_path)

    # Menggunakan Tesseract untuk mengonversi foto menjadi teks
    extracted_text = pytesseract.image_to_string(Image.open(photo_path))

    # Mengirimkan hasil teks ke pengguna melalui bot Telegram
    update.message.reply_text(extracted_text)

    # Menghapus foto setelah selesai
    os.remove(photo_path)

# Fungsi untuk menangani pesan yang mengandung foto
def handle_photo(update, context):
    # Memeriksa apakah pesan mengandung foto
    if update.message.photo:
        convert_photo_to_text(update, context)

# Fungsi utama untuk menjalankan bot Telegram
def main():
    # Menginisialisasi objek Updater dengan token bot Telegram Anda
    updater = Updater('6454566033:AAG_bT2gHQ7qVDAQTuDNneGfnzHEH3fGl_M', use_context=True)

    # Mendapatkan objek Dispatcher dari updater
    dp = updater.dispatcher

    # Menambahkan handler untuk pesan yang mengandung foto
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))

    # Memulai bot
    updater.start_polling()

    # Menjaga bot berjalan hingga dihentikan secara manual
    updater.idle()

# Memanggil fungsi utama untuk menjalankan bot
if __name__ == '__main__':
    main()
