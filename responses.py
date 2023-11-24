def handle_responses(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`this is a help message you can modify.`"