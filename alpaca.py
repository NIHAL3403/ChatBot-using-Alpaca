import re
import datetime
import long_responses as long
import alpaca_trade_api as alpaca

api = alpaca.REST('<YOUR_API_KEY>', '<YOUR_SECRET_KEY>', base_url='https://paper-api.alpaca.markets')
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    # Additional responses
    response('That\'s interesting!', ['interesting'], single_response=True)
    response('Tell me more!', ['tell', 'more'], required_words=['tell', 'more'])
    response('How can I help you?', ['help'], single_response=True)
    response('Let\'s chat!', ['chat'], single_response=True)

    # Responses to specific queries
    response('Data structures are a way of organizing and storing data to enable efficient access and modification.', ['data', 'structures'], required_words=['data', 'structures'])
    response('To print "Hello, World!" in Python, you can use the following code: print("Hello, World!")', ['print', 'hello', 'world', 'python'], required_words=['print', 'hello', 'world', 'python'])

    # New responses for additional queries
    response(datetime.datetime.now().strftime("The current time is %I:%M %p."), ['what', 'time', 'is', 'it'], required_words=[ 'time', 'is', 'it'])
    response('Sure! I can help answer questions, provide information, and even tell jokes.', ['tell', 'me', 'about', 'your', 'features'], required_words=['tell', 'me', 'about', 'your', 'features'])
    response('Certainly! What type of cuisine are you interested in?', ['recommend', 'a', 'good', 'restaurant'], required_words=['recommend', 'a', 'good', 'restaurant'])
    response('Sure thing! Here are the top headlines for today...', ['show', 'me', 'the', 'latest', 'news', 'headlines'], required_words=['show', 'me', 'the', 'latest', 'news', 'headlines'])
    response('You\'re welcome!', ['thank', 'you'], single_response=True)
    response('Glad I could assist!', ['helpful', 'thanks'], single_response=True)
    response("My day has been pretty good, thank you for asking. How about you?", ['how', 'was', 'your', 'day'], required_words=['how', 'was', 'your', 'day'])
    response("I don't have a favorite color, but I can appreciate them all!", ['favorite', 'color'], required_words=['favorite', 'color'])
    # Additional responses
    response('That sounds intriguing!', ['intriguing'], single_response=True)
    response('Please elaborate!', ['elaborate'], required_words=['elaborate'])
    response('How may I assist you today?', ['assist', 'today'], required_words=['assist', 'today'])
    response('Let\'s have a conversation!', ['conversation'], single_response=True)

    # Responses to specific queries
    response('Algorithms are step-by-step procedures or formulas for solving problems.', ['algorithms'],
             required_words=['algorithms'])
    response('Machine learning is a subset of artificial intelligence that allows systems to learn from data.',
             ['machine', 'learning'], required_words=['machine', 'learning'])
    response('You can deploy a website using various web hosting services like AWS, Google Cloud, or Heroku.',
             ['deploy', 'website'], required_words=['deploy', 'website'])
    response(
        'Virtual reality (VR) is a simulated experience that can be similar to or completely different from the real world.',
        ['virtual', 'reality'], required_words=['virtual', 'reality'])

    # New responses for additional queries
    response('The stock market is a place where stocks, bonds, and other securities are bought and sold.',
             ['stock', 'market'], required_words=['stock', 'market'])
    response('Cloud computing refers to the delivery of computing services over the internet.', ['cloud', 'computing'],
             required_words=['cloud', 'computing'])
    response('Blockchain is a decentralized and distributed digital ledger technology.', ['blockchain'],
             required_words=['blockchain'])
    response('Artificial intelligence (AI) is the simulation of human intelligence processes by machines.',
             ['artificial', 'intelligence'], required_words=['artificial', 'intelligence'])

    # More responses to specific queries
    response(
        'Natural language processing (NLP) is a field of artificial intelligence that deals with the interaction between computers and humans using natural language.',
        ['natural', 'language', 'processing'], required_words=['natural', 'language', 'processing'])
    response('Python is a high-level, interpreted programming language known for its simplicity and readability.',
             ['python'], required_words=['python'])
    response(
        'JavaScript is a versatile scripting language primarily used for enhancing web pages and web applications.',
        ['javascript'], required_words=['javascript'])
    response('Data science involves extracting insights and knowledge from structured and unstructured data.',
             ['data', 'science'], required_words=['data', 'science'])

    # Additional responses for specific queries
    response(
        'Cybersecurity encompasses practices, technologies, and processes designed to protect computers, networks, and data from attack, damage, or unauthorized access.',
        ['cybersecurity'], required_words=['cybersecurity'])
    response(
        'Mobile applications (apps) are software programs designed to run on mobile devices like smartphones and tablets.',
        ['mobile', 'applications'], required_words=['mobile', 'applications'])
    response(
        'An API (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications.',
        ['api'], required_words=['api'])
    response(
        'Responsive web design is an approach to web design that makes web pages render well on a variety of devices and window or screen sizes.',
        ['responsive', 'web', 'design'], required_words=['responsive', 'web', 'design'])

    # Even more responses for specific queries
    response(
        'Big data refers to large and complex datasets that cannot be easily processed using traditional data processing applications.',
        ['big', 'data'], required_words=['big', 'data'])
    response(
        'Open-source software is software with its source code made available and licensed with a license that allows modifications and redistribution.',
        ['open-source', 'software'], required_words=['open-source', 'software'])
    response(
        'User experience (UX) design focuses on enhancing user satisfaction by improving the usability, accessibility, and pleasure provided in the interaction with a product.',
        ['user', 'experience', 'design'], required_words=['user', 'experience', 'design'])
    response(
        'User interface (UI) design focuses on the visual and interactive elements of a product, such as buttons, icons, and layout.',
        ['user', 'interface', 'design'], required_words=['user', 'interface', 'design'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Bot: ' + get_response(input('User: ')))