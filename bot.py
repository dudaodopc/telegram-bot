import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# ================== TOKEN ==================

TOKEN = os.getenv("BOT_TOKEN")

# ================== TEXTOS ==================

QUEM_SOMOS_TEXT = (
    "🏦 *FETRADER*\n\n"
    "Somos uma comunidade focada em *criptomoedas*, "
    "*análise técnica profissional* e *educação financeira*.\n\n"
    "📊 Nosso foco é:\n"
    "• Operações conscientes\n"
    "• Gestão de risco\n"
    "• Disciplina e consistência\n\n"
    "⚠️ Não prometemos lucro fácil.\n"
    "📈 Trabalhamos com probabilidade e método."
)

VIP_TEXT = (
    "📈 *VIP CRIPTO*\n\n"
    "Ao entrar no VIP você recebe:\n\n"
    "✅ Sinais em tempo real\n"
    "✅ Análises detalhadas\n"
    "✅ Gestão de risco aplicada\n"
    "✅ Acompanhamento contínuo\n\n"
    "🚀 Ideal para quem busca evolução real no mercado."
)

PLANOS_TEXT = (
    "💰 *PLANOS DISPONÍVEIS*\n\n"
    "🔹 Plano Mensal\n"
    "🔹 Plano Trimestral\n"
    "🔹 Plano Anual\n\n"
    "📩 Para valores e condições,\n"
    "clique em *Suporte*."
)

ANALISES_TEXT = (
    "📊 *ANÁLISES DE MERCADO*\n\n"
    "Nossas análises são baseadas em:\n\n"
    "📌 Tendência\n"
    "📌 Estrutura de mercado\n"
    "📌 Volume e contexto\n\n"
    "❌ Sem achismo\n"
    "✔️ Apenas técnica"
)

SUPORTE_TEXT = (
    "📞 @fabriciatraderr\n\n"
    "Para atendimento personalizado,\n"
    "entre em contato com um administrador.\n\n"
    "🕐 Atendimento em horário comercial."
)

# ================== MENU ==================

def main_menu():
    keyboard = [
        [InlineKeyboardButton("ℹ️ Quem Somos", callback_data="quem_somos")],
        [InlineKeyboardButton("📈 VIP Cripto", callback_data="vip")],
        [InlineKeyboardButton("💰 Planos", callback_data="planos")],
        [InlineKeyboardButton("📊 Análises", callback_data="analises")],
        [InlineKeyboardButton("📞 Suporte", callback_data="suporte")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ================== START ==================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 *Bem-vindo à FETRADER!*\n\n"
        "Escolha uma opção abaixo:",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# ================== HANDLER DO MENU ==================

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "quem_somos":
        await query.edit_message_text(
            QUEM_SOMOS_TEXT,
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    elif query.data == "vip":
        await query.edit_message_text(
            VIP_TEXT,
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    elif query.data == "planos":
        await query.edit_message_text(
            PLANOS_TEXT,
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    elif query.data == "analises":
        await query.edit_message_text(
            ANALISES_TEXT,
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    elif query.data == "suporte":
        await query.edit_message_text(
            SUPORTE_TEXT,
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

# ================== MAIN ==================

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))

    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
