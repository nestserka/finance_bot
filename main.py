import telebot
from telebot import TeleBot, types
import logging 
import category
from datetime import date

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


bot = telebot.TeleBot("5844191574:AAHunAoovc85hKgT6cvNpXyiEouSHxhexRQ")


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    total = types.InlineKeyboardButton("Total", callback_data='total')
    register = types.InlineKeyboardButton('등록', callback_data='register')
    markup.add(total, register)
    bot.send_message(message.chat.id, '안녕하세요, 유진, 총 금액을 확인하시겠습니까, 아니면 신규 비용을 등록하시겠습니까?', reply_markup=markup)
    
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'register':
                handler_category(call.message)
            elif call.data == 'total':
               pass
            elif call.data == 'income':
                handler_income(call.message)
            elif call.data == 'saving':
                handler_saving(call.message)
            elif call.data == 'fixed_expenditure':
                handler_fixed_expenditure(call.message)
            elif call.data == 'food_expenses':
                handler_food_expenses(call.message)
            elif call.data == 'pocket_money':
                handler_pocket_money(call.message)
            elif call.data == 'clothing':
                handler_clothing(call.message)
            elif call.data == 'animals':
                handler_animals(call.message)
            elif call.data == 'self_emprov':
                handler_self_emprov(call.message)
            elif call.data == 'family_celebration':
                handler_family_celebration(call.message)
            elif call.data == 'traveling':
                handler_traveling(call.message)
            elif call.data == 'health':
                handler_health(call.message)
            elif call.data == 'daily_supply':
                handler_daily_supply(call.message)
    except Exception as e:
        logger.error(repr(e))



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
    
def write_date(message):
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
    print('date', d1)
    type_information(message)

def handle_datefromuser(message):
    todayDate = message.text.strip()
    if validate_date(todayDate):
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
    bot.register_next_step_handler(message,add_price)

def add_price(message):
    bot.send_message(message.chat.id, "가격 등록 주세요")
    bot.register_next_step_handler(message,finish_data)
    
def finish_data(message):
    bot.send_message(message.chat.id, "감사합니다 정보가 저장되었습니다")
    handle_start(message)
        
    
bot.polling(none_stop=True)