
from os import environ
from typing import Text
import telegram
import logging
import random
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, updater, ConversationHandler
from flask import Flask
TOKEN = '1964203815:AAFREBYZiXTYHesgJUhKVHVgT1zwadCm32Y'

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# START, SEND_DOCUMENT = range(2)
#--------------------------------------------------------------------------------------------------------------------------------------#
Alabama = [205, 251, 256, 334, 938]
Alaska = [907]
Arizona = [480, 520, 602, 623, 928]
Arkansas = [479, 501, 870]
California = [209, 213, 279, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 628,
                650, 657, 661, 669, 707, 714, 747, 760, 805, 818, 820, 831, 858, 909, 916, 925, 949, 951]
Colorado = [303, 719, 720, 970]
Connecticut = [203, 475, 860, 959]
Delaware = [302]
Florida = [239, 305, 321, 352, 386, 407, 561, 727,
           754, 772, 786, 813, 850, 863, 904, 941, 954]
Georgia = [229, 404, 470, 478, 678, 706, 762, 770, 912]
Hawaii = [808]
Idaho = [208, 986]
Illinois = [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872]
Indiana = [219, 260, 317, 463, 574, 765, 812, 930]
Iowa = [319, 515, 563, 641, 712]
Kansas = [316, 620, 785, 913]
Kentucky = [270, 364, 502, 606, 859]
Louisiana = [225, 318, 337, 504, 985]
Maine = [207]
Maryland = [240, 301, 410, 443, 667]
Massachusetts = [339, 351, 413, 508, 617, 774, 781, 857, 978]
Michigan = [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989]
Minnesota = [218, 320, 507, 612, 651, 763, 952]
Mississippi = [228, 601, 662, 769]
Missouri = [314, 417, 573, 636, 660, 816]
Montana = [406]
Nebraska = [308, 402, 531]
Nevada = [702, 725, 775]
New_Hampshire = [603]
New_Jersey = [201, 551, 609, 640, 732, 848, 856, 862, 908, 973]
New_Mexico = [505, 575]
New_York = [212, 315, 332, 347, 516, 518, 585, 607, 631,
            646, 680, 716, 718, 838, 845, 914, 917, 929, 934]
North_Carolina = [252, 336, 704, 743, 828, 910, 919, 980, 984]
North_Dakota = [701]
Ohio = [216, 220, 234, 330, 380, 419, 440, 513, 567, 614, 740, 937]
Oklahoma = [405, 539, 580, 918]
Oregon = [458, 503, 541, 971]
Pennsylvania = [215, 223, 267, 272, 412,
                445, 484, 570, 610, 717, 724, 814, 878]
Rhode_Island = [401]
South_Carolina = [803, 843, 854, 864]
South_Dakota = [605]
Tennessee = [423, 615, 629, 731, 865, 901, 931]
Texas = [210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682,
         713, 726, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979]
Utah = [385, 435, 801]
Vermont = [802]
Virginia = [276, 434, 540, 571, 703, 757, 804]
Washington = [206, 253, 360, 425, 509, 564]
Washington_DC = [	202]
West_Virginia = [304, 681]
Wisconsin = [	262, 414, 534, 608, 715, 920]
Wyoming = [307]

#--------------------------------------------------------------------------------------------------------------------------------------#
total = int(10000)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'select state u want to generate numbers ex : FL ,CA')

def total_number(update, context):
    user_input = update.message.text
    update.message.reply_text("do_something(user_input)")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def generate_number(zip_state):
    range_start = 10**(7-1)
    range_end = (10**7)-1
    with open(f"{total}_numbers generated.txt", "w") as file:
        for i in range(total):
            d = str(random.randint(range_start, range_end))
            g = random.choice(zip_state)
            file.write(f"+{1}{g}{d}\n")
    file.close()


def send_txt_file(update, context):
    """Send a document."""
    update.message.reply_text(
        'downloading text file')
    doc_file = open(f"{total}_numbers generated.txt", 'rb')
    chat_id = update.effective_chat.id
    context.bot.sendDocument(chat_id, doc_file)


def echo(update, context):
    """Echo the user message."""
    text = update.message.text
    print(text)
    if text.upper() == 'FL':
        generate_number(Florida)
        send_txt_file(update, context)
    elif text.upper() == 'CA':
        generate_number(California)
        send_txt_file(update, context)
    elif text.upper() == 'AL':
        generate_number(Alabama)
        send_txt_file(update, context)
    elif text.upper() == 'AK':
        generate_number(Alaska)
        send_txt_file(update, context)
    elif text.upper() == 'AZ':
        generate_number(Arizona)
        send_txt_file(update, context)
    elif text.upper() == 'AR':
        generate_number(Arkansas)
        send_txt_file(update, context)
    elif text.upper() == 'CO':
        generate_number(Colorado)
        send_txt_file(update, context)
    elif text.upper() == 'CT':
        generate_number(Connecticut)
        send_txt_file(update, context)
    elif text.upper() == 'DE':
        generate_number(Delaware)
        send_txt_file(update, context)
    elif text.upper() == 'FL':
        generate_number(Florida)
        send_txt_file(update, context)
    elif text.upper() == 'GA':
        generate_number(Georgia)
        send_txt_file(update, context)
    elif text.upper() == 'HI':
        generate_number(Hawaii)
        send_txt_file(update, context)
    elif text.upper() == 'ID':
        generate_number(Idaho)
        send_txt_file(update, context)
    elif text.upper() == 'IL':
        generate_number(Illinois)
        send_txt_file(update, context)  
    elif text.upper() == 'IN':
        generate_number(Indiana)
        send_txt_file(update, context)
    elif text.upper() == 'IA':
        generate_number(Iowa)
        send_txt_file(update, context)
    elif text.upper() == 'KS':
        generate_number(Kansas)
        send_txt_file(update, context)
    elif text.upper() == 'KY':
        generate_number(Kentucky)
        send_txt_file(update, context)
    elif text.upper() == 'LA':
        generate_number(Louisiana)
        send_txt_file(update, context)
    elif text.upper() == 'ME':
        generate_number(Maine)
        send_txt_file(update, context)
    elif text.upper() == 'MD':
        generate_number(Maryland)
        send_txt_file(update, context)
    elif text.upper() == 'MA':
        generate_number(Massachusetts)
        send_txt_file(update, context)
    elif text.upper() == 'MI':
        generate_number(Michigan)
        send_txt_file(update, context)
    elif text.upper() == 'MN':
        generate_number(Minnesota)
        send_txt_file(update, context)
    elif text.upper() == 'MS':
        generate_number(Mississippi)
        send_txt_file(update, context)
    elif text.upper() == 'MO':
        generate_number(Missouri)
        send_txt_file(update, context)
    elif text.upper() == 'MT':
        generate_number(Montana)
        send_txt_file(update, context)
    elif text.upper() == 'NE':
        generate_number(Nebraska)
        send_txt_file(update, context)
    elif text.upper() == 'NV':
        generate_number(Nevada)
        send_txt_file(update, context)
    elif text.upper() == 'NH':
        generate_number(New_Hampshire)
        send_txt_file(update, context)
    elif text.upper() == 'NJ':
        generate_number(New_Jersey)
        send_txt_file(update, context)
    elif text.upper() == 'NM':
        generate_number(New_Mexico)
        send_txt_file(update, context)
    elif text.upper() == 'NY':
        generate_number(New_York)
        send_txt_file(update, context)
    elif text.upper() == 'NC':
        generate_number(North_Carolina)
        send_txt_file(update, context)
    elif text.upper() == 'ND':
        generate_number(North_Dakota)
        send_txt_file(update, context)
    elif text.upper() == 'OH':
        generate_number(Ohio)
        send_txt_file(update, context)
    elif text.upper() == 'OK':
        generate_number(Oklahoma)
        send_txt_file(update, context)
    elif text.upper() == 'OR':
        generate_number(Oregon)
        send_txt_file(update, context)
    elif text.upper() == 'PA':
        generate_number(Pennsylvania)
        send_txt_file(update, context)
    elif text.upper() == 'RI':
        generate_number(Rhode_Island)
        send_txt_file(update, context)
    elif text.upper() == 'SC':
        generate_number(South_Carolina)
        send_txt_file(update, context)
    elif text.upper() == 'SD':
        generate_number(South_Dakota)
        send_txt_file(update, context)
    elif text.upper() == 'TN':
        generate_number(Tennessee)
        send_txt_file(update, context)
    elif text.upper() == 'TX':
        generate_number(Texas)
        send_txt_file(update, context)
    elif text.upper() == 'UT':
        generate_number(Utah)
        send_txt_file(update, context)
    elif text.upper() == 'VT':
        generate_number(Vermont)
        send_txt_file(update, context)
    elif text.upper() == 'VA':
        generate_number(Virginia)
        send_txt_file(update, context)
    elif text.upper() == 'WA':
        generate_number(Washington)
        send_txt_file(update, context)
    elif text.upper() == 'WV':
        generate_number(West_Virginia)
        send_txt_file(update, context)
    elif text.upper() == 'WI':
        generate_number(Wisconsin)
        send_txt_file(update, context)
    elif text.upper() == 'WY':
        generate_number(Wyoming)
        send_txt_file(update, context)
    else:
        update.message.reply_text(
            'Please enter a valid state')



def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on delifferent commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, echo, pass_user_data=True))
   # dp.add_handler(CommandHandler("download",
    #               send_txt_file))

    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('start', start)],
    #     states={
    #         0: [MessageHandler(Filters.text, echo)],
    #         1: [MessageHandler(Filters.document, send_txt_file, pass_user_data=True)],

    #     },
    #     fallbacks=[CommandHandler('ok', start)]

    # )

    # # log all errors
    # dp.add_handler(conv_handler)
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

@app.route("/")
def hello():
    main()
    return "Hello World!"

    
if __name__ == '__main__':
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True,threaded=True)
    #main()
