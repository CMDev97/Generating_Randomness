

def read_user_input() -> str:
    return input()


def parse_binary(input_string: str) -> str:
    tmp = ""
    for i in input_string:
        if i == "1" or i == "0":
            tmp += i
    return tmp


def get_triads(input_string: str) -> dict:
    tmp = {}
    for i in range(0, len(input_string)-3):
        tmp_string = input_string[i:i+3]
        if tmp_string not in tmp:
            tmp[tmp_string] = (0, 0)
        if i+3 < len(input_string):
            zeros, ones = tmp[tmp_string]
            if input_string[i+3] == "1":
                tmp[tmp_string] = (zeros, ones+1)
            elif input_string[i+3] == "0":
                tmp[tmp_string] = (zeros+1, ones)
    return tmp


def print_input_instruction():
    print("Print a random string containing 0 or 1:")


def print_info(current_length: int, remaining: int):
    print(f"The current data length is {current_length}, {remaining} symbols left")


def print_final_result(final_result: str):
    print("Final data string:")
    print(final_result)


def read_test_string() -> any:
    while True:
        print("Print a random string containing 0 or 1:")
        input_string = input()
        if input_string == "enough":
            return None
        parsed = parse_binary(input_string)
        if len(parsed) > 3:
            return input_string


def get_binary_char_from_probability(base: str, probabilities: dict) -> str:
    zero, one = probabilities[base]
    return "0" if zero > one else "1"


def predictions_string(test_string: str, length: int, probabilities: dict) -> str:
    predicted = ""
    start_index = 0
    while len(predicted) < length:
        base_string = test_string[start_index:start_index+3]
        predicted = predicted + get_binary_char_from_probability(base_string, probabilities)
        start_index = start_index + 1
    return predicted


def guessed_binary_char(right_test: str, predicted: str) -> int:
    occurance = 0
    for i in range(len(predicted)):
        if predicted[i] == right_test[i]:
            occurance += 1
    return occurance


def percentage_guessed(counter: int, total: int):
    print(f"Computer guessed {counter} out of {total} symbols right ({counter/total*100:.2f} %)")


def calculate_loss_user(char_guessed: int, total: int) -> int:
    user_loss = total - char_guessed
    return char_guessed - user_loss


string_length = 0
final_string = ""
user_bill = 1000
print("Please provide AI some data to learn...")
while string_length < 100:
    print_info(string_length, 100 - string_length)
    print_input_instruction()
    tmp_string = read_user_input()
    parsed_string = parse_binary(tmp_string)
    final_string = final_string + parsed_string
    string_length = len(final_string)
print_final_result(final_string)
dictionary_triads = get_triads(final_string)

print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
print('Otherwise, you earn $1. Print "enough" to leave the game.')
print("Let's go!")

while True:
    test_user_string = read_test_string()
    if test_user_string is None:
        print("Game over!")
        break
    predicted_string = predictions_string(test_user_string, len(test_user_string)-3, dictionary_triads)
    print("predictions:")
    print(predicted_string)
    computer_guessed = guessed_binary_char(test_user_string[3:], predicted_string)
    max_length = len(test_user_string[3:])

    user_bill = user_bill - calculate_loss_user(computer_guessed, max_length)

    percentage_guessed(computer_guessed, max_length)
    print(f"Your balance is now ${user_bill}")

