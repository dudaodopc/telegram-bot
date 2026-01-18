import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

# ---------- MENU PRINCIPAL ----------
def main_menu():
    keyboard = [
        [InlineKeyboardButton("ℹ️ Quem Somos", callback_data="quem_somos")],
        [InlineKeyboardButton("📈 VIP Cripto", callback_data="vip")],
        [InlineKeyboardButton("💰 Planos", callback_data="planos")],
        [InlineKeyboardButton("📊 Análises", callback_data="analises")],
        [InlineKeyboardButton("📞 Suporte", callback_data="suporte")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bem-vindo!\n\nEscolha uma opção abaixo:",
        reply_markup=main_menu()
    )

# ---------- HANDLER DO MENU ----------
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "quem_somos":
        text = (
            "ℹ️ *Quem Somos*\n\n"
            "Somos um projeto focado em criptomoedas,\n"
            "análises técnicas e educação financeira."
        )

    elif query.data == "vip":
        text = "📈 *VIP Cripto*\n\nSinais, análises e acompanhamento."

    elif query.data == "planos":
        text = (
            "💰 *Planos Disponíveis*\n\n"
            "• Mensal\n"
            "• Trimestral\n"
            "• Vitalício"
        )

    elif query.data == "analises":
        text = "📊 As análises são enviadas diariamente no grupo VIP."

    elif query.data == "suporte":
        text = "📞 Suporte: @seuuser"

    else:
        text = "Opção inválida."

    await query.edit_message_text(
        text=text,
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# ---------- MAIN ----------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))

    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
