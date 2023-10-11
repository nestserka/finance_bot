import datetime
import telebot
import os
from telebot import TeleBot, types
import logging 
import category
from datetime import date, timedelta
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
bot = telebot.TeleBot(BOT_API_TOKEN)

data_handler_mapping = {
    'register': handler_category,
    'total': select_records_last_7_days,
    'income': handler_income,
    'saving': handler_saving,
    'fixed_expenditure': handler_fixed_expenditure,
    'food_expenses': handler_food_expenses,
    'pocket_money': handler_pocket_money,
    'clothing': handler_clothing,
    'animals': handler_animals,
    'self_emprov': handler_self_emprov,
    'family_celebration': handler_family_celebration,
    'traveling': handler_traveling,
    'health': handler_health,
    'daily_supply': handler_daily_supply
}



@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    total = types.InlineKeyboardButton("금액 확인", callback_data='total')
    register = types.InlineKeyboardButton('등록', callback_data='register')
    markup.add(total, register)
    bot.send_message(message.chat.id, '안녕하세요, 유진, 총 금액을 확인하시겠습니까, 아니면 신규 비용을 등록하시겠습니까?', reply_markup=markup)
    
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            handler_function = data_handler_mapping.get(call.data)
            if handler_function:
                save_user_choice(call.message, call.data)
                handler_function(call.message)
    except Exception as e:
        logger.error(repr(e))

def save_user_choice(message, maincategory):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    query = "INSERT INTO expense (maincategory) VALUES (?)"
    values = (maincategory,)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

def handler_category(message): 
    bot.send_message(message.chat.id, '대분류 선택헤주세요', reply_markup=category.maincategory)
    

def handler_income(message): 
    bot.send_message(message.chat.id, '수입의 소분류 선택헤주세요', reply_markup=category.incomecategory)
    bot.register_next_step_handler(message, write_date)
 
def handler_saving(message): 
    bot.send_message(message.chat.id, '저축의 소분류 선택헤주세요', reply_markup=category.savingcategory)
    bot.register_next_step_handler(message, write_date)


def handler_fixed_expenditure(message): 
    bot.send_message(message.chat.id, '고정지출의 소분류 선택헤주세요', reply_markup=category.fixedcategory)
    bot.register_next_step_handler(message, write_date)
    
    
def handler_food_expenses(message): 
    bot.send_message(message.chat.id, '식비의 소분류 선택헤주세요', reply_markup=category.foodcategory)
    bot.register_next_step_handler(message, write_date)
    
    
def  handler_pocket_money(message): 
    bot.send_message(message.chat.id, '용돈의 소분류 선택헤주세요', reply_markup=category.pocketcategory)
    bot.register_next_step_handler(message, write_date)
    
    
def handler_clothing(message): 
    bot.send_message(message.chat.id, '의복/미용의 소분류 선택헤주세요', reply_markup=category.clothingcategory)
    bot.register_next_step_handler(message, write_date)


def handler_self_emprov(message): 
    bot.send_message(message.chat.id, '자기계발의 소분류 선택헤주세요', reply_markup=category.selfcategory)
    bot.register_next_step_handler(message, write_date)
    
    
def handler_animals(message): 
    bot.send_message(message.chat.id, '동물의 소분류 선택헤주세요', reply_markup=category.animalscategory)
    bot.register_next_step_handler(message, write_date)
    
    
def handler_family_celebration(message): 
    bot.send_message(message.chat.id, '경조사의 소분류 선택헤주세요', reply_markup=category.familycategory)
    bot.register_next_step_handler(message, write_date)


def handler_traveling(message): 
    bot.send_message(message.chat.id, '여행의 소분류 선택헤주세요', reply_markup=category.travellingcategory)
    bot.register_next_step_handler(message, write_date)
    
    
def handler_health(message): 
    bot.send_message(message.chat.id, '건강의 소분류 선택헤주세요', reply_markup=category.healthcategory)
    bot.register_next_step_handler(message, write_date)


def handler_daily_supply(message): 
    bot.send_message(message.chat.id, '생활용품의 소분류 선택헤주세요', reply_markup=category.dailysupplycategory)
    bot.register_next_step_handler(message, write_date)


def get_previous_id():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    query = "SELECT MAX(id) FROM expense"
    cursor.execute(query)
    result = cursor.fetchone()
    previous_id = result[0] if result[0] is not None else 0

    cursor.close()
    conn.close()

    return previous_id
    
def write_date(message):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    previous_id = get_previous_id()
    user_choice = message.text
    query = "UPDATE expense SET subcategory = ? WHERE id = ?"
    values = (user_choice, previous_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    todaydate = types.KeyboardButton('오늘')
    directinput = types.KeyboardButton('직접 입력')
    keyboard.add(todaydate, directinput)
    bot.send_message(message.chat.id, "날짜 입력해주세요. 예: DD/MM", reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_date_choice)  

def handle_date_choice(message):
    if message.text == '오늘':
        handle_todaydate(message)
    elif message.text == '직접 입력':
        bot.send_message(message.chat.id, '날짜를 직접 입력해주세요. 예: DD/MM')
        bot.register_next_step_handler(message, handle_datefromuser)

def handle_todaydate(message):
    today = date.today()
    d1 = today.strftime("%d/%m")
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    previous_id = get_previous_id()
    query = "UPDATE expense SET date = ? WHERE id = ?"
    values = (d1, previous_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    type_information(message)

def handle_datefromuser(message):
    todayDate = message.text.strip()
    if validate_date(todayDate):
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        previous_id = get_previous_id()
        query = "UPDATE expense SET date = ? WHERE id = ?"
        values = (todayDate, previous_id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        type_information(message)
    else:
        bot.send_message(message.chat.id, '유진, 형식을 다시 확인해주세요: DD/MM (12/03)')
        bot.register_next_step_handler(message, handle_datefromuser)


def validate_date(todayDate):
    try:
        day, month = map(int,todayDate.split('/'))
        if day < 1 or day > 31 or month < 1 or month > 12:
            return False
        return True
    except:
        return False
    
def type_information(message):
    bot.send_message(message.chat.id, "내용을 정리해서 거기에 짧게 요약한 걸 적어 주세요")
    getInfo = message.text
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    previous_id = get_previous_id()
    query = "UPDATE expense SET info = ? WHERE id = ?"
    values = (getInfo, previous_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    bot.register_next_step_handler(message,add_price)

def add_price(message):
    bot.send_message(message.chat.id, "가격 등록 주세요")
    getInfo = message.text
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    previous_id = get_previous_id()
    query = "UPDATE expense SET info = ? WHERE id = ?"
    values = (getInfo, previous_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    bot.register_next_step_handler(message,finish_data)
    
def finish_data(message):
    price = message.text
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    previous_id = get_previous_id()
    query = "UPDATE expense SET price = ? WHERE id = ?"
    values = (price, previous_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    bot.send_message(message.chat.id, "감사합니다 정보가 저장되었습니다")
    handle_start(message)

def select_records_last_7_days(message):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    end_date = date.today()

    start_date = end_date - timedelta(days=7)
    start_month_day = start_date.strftime('%d-%m')
    end_month_day = end_date.strftime('%d-%m')

    query = "SELECT date, info, price, maincategory, subcategory FROM expense WHERE SUBSTR(date, 1, 5) BETWEEN ? AND ?"
    cursor.execute(query, (start_month_day, end_month_day))
    records = cursor.fetchall()
    message_text = "최근 7일 이내의 기록:\n"
    for record in records:
        message_text += f"날짜: {record[0]}, 내용: {record[1]}, 금액: {record[2]}, 대분류: {record[3]}, 소분류: {record[4]}\n"
    bot.send_message(message.chat.id, text=message_text)  # Replace `bot` with your Telegram bot instance

    cursor.close()
    conn.close()
        
    
bot.polling(none_stop=True)
