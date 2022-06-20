import time


def parse_resourses_info(raw_input_resourses: str):
    resourses_usage = {}

    for resourse_info in raw_input_resourses.split(";"):
        resourse_info = resourse_info[1:-1]
        resourse_info = resourse_info.split(",", 1)
        resourse_id = resourse_info[0]
        details = [] if len(resourse_info) == 3 else resourse_info[-1].split(",")
        
        resourses_usage.setdefault(resourse_id, []).append(details)
    
    return resourses_usage

    
        


def parse_command_name(raw_input_data: str):
    commands = {}

    for command_name_info in raw_input_data.split("$"):
        command_name, command_resourse_info = command_name_info.split("|")
        commands[command_name] = parse_resourses_info(command_resourse_info)
        print(commands)
        time.sleep(3)


def main():
    input_data = input()
    parse_command_name(input_data)

    

if __name__ == '__main__':
    main()
    
# syndicate virtual markets
# facilitate best-of-breed channels
# seize efficient experiences
# cultivate one-to-one schemas