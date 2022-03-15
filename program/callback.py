from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 **هلا حب [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
🎗 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) انا روبوت لتشغيل الموسيقى والفيديو على منصة تليجرام!**

ℹ️ **لمعرفة اوامر هذا البوت اضغط على » الاوامر الاساسية!**

ℹ️ **لمعرفة طريقة تشغيل هذا البوت اضغط على » طريقة التشغيل!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضفني الى مجموعتك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("طريقة التشغيل", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("الاوامر الاساسية", callback_data="cbcmds"),
                    InlineKeyboardButton("المطور", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/IQTHON"
                    ),
                    InlineKeyboardButton(
                        "تحديثات البوت", url=f"https://t.me/TELETHONMUSIC"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ملاحظة مهمة جدأ", url="https://t.me/IQTHON"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ℹ️ **هذا هي طريقة تشغيل البوت:**

1.) **اولا, اضفني الى مجموعتك.**
2.) **بعد ذالك, قم بترقيتي كمسؤول.**
3.) **بعد ذالك اكتب, .تحديث لتحديث البيانات.**
3.) **اضف @{ASSISTANT_NAME} في مجموعتك او اكتب .انضم **
4.) **بعد اكمال كل شي قم بفتح محادثة صوتية واستمتع.**
5.) **بعض الاحيان, ستواجه مشاكل في التشغيل ماعليك فقط سوى كتابة الامر .تحديث**

ℹ️ ** اذ لم ينضم حساب المساعد اكتب .اطلع , وبعد ذالك اكتب .انضم**

ℹ️ بواسطة {BOT_NAME} 
- المطور : @LLL5L
- القناه : @IQTHON""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ℹ️ **مرحبا بك [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **مرحبا بك في قائمة الاوامر الاساسية يمكنك معرفة الاوامر عن طريق استخدام الازرار ادناة !**

ℹ️ بواسطة {BOT_NAME} 
- المطور : @LLL5L
- القناه : @IQTHON""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر المشرفين", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 اوامر الاعضاء", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 مرحبا بك هذا هي اوامر الاعضاء:

» .شغل - لتشغيل اغنية بالرد على ملف صوتي
» .تدفق - لتشغيل راديو بث مباشر
» .فيديو - بالرد على مقطع فيديو
» .مباشر - لبث مباشر من اليوتيوب
» .الانتضار - لاضهار قائمة الانتضار
» .ابحثلي - لتحميل فيديو من اليوتيوب
» .بحث - لتحميل اغنية من اليوتيوب
» .كلمات - لاضهار كلمات اغنية
» .رابط - لاضهار رابط اغنية

» .بنك - عرض حالة البوت بينغ
» .فحص - لاضهار حاله البوت ان يعمل او لا
» .الحاله - فحص البوت في المجموعة

ℹ️ بواسطة {BOT_NAME} 
- المطور : @LLL5L
- القناه : @IQTHON""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 مرحبا بك هذا هي اوامر المشرفين:

» .توقف - لايقاف الاغنية مؤقتا
» .استمرار - لاستمرار الاغنية المتوقفة
» .تخطي - لتخطي اغنية , فيديو
» .اوكف - لانتهاء تشغيل الموسيقى
» .كتم - لكتم حساب المساعد
» .افتح - لالغاء كتم حساب المساعد
» .اضبط `1-200` - لضبط حجم الصوت
» .تحديث - اعادة تشغيل وتحديث بيانات
» .انضم - دعوة حساب المساعد للمجموعة
» .اطلع - لخروج حساب مساعد من لمجموعة

ℹ️ __بواسطة {BOT_NAME} __
- المطور : @LLL5L
- القناه : @IQTHON""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 مرحبا بك يامطوري في اوامرك التالية:

» .امسح - تنظيف جميع الملفات الخام
» .حدث - تحديث البوت الى اخر اصدار
» .النظام - اضهار معلومات النظام
» .حدث - لتحديث البوت الى احدث اصدار
» .اعادة - اعادة تشغيل البوت
» .مغادرة كل المجموعات - لمغادرة حساب المساعد من كل المجموعات

ℹ️ __بواسطة {BOT_NAME} __
- المطور : @LLL5L
- القناه : @IQTHON""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("انت مستخدم محهول !\n\n» لاتستطيع استخدام البوت.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡وخر ايدك المشرف الوحيد الذي لديه صلاحية إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **اعدادات الاغنية** {query.message.chat.title}\n\n⏸ : ايقاف مؤقت\n▶️ : استمرار\n🔇 : كتم حساب المساعد\n🔊 : الغاء كتم حساب المساعد\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 اغلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ لايوجد شيئ مشتغل", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ابعد ايدك المشرف الوحيد الذي لديه صلاحية إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
