def main(HOSTS, COMMANDS):
    for host in HOSTS:
        for command in COMMANDS:
            if command != 'rm -rf /':
                print(f"На хосте {host} была выполнена команда {command}")
            else:
                print(f"На хосте {host} была попытка выполнить команду {command} , но процесс выполнения был аварийно остановлен.")
                break
        else:
            continue            
        break

def remove_space_symbols(COMMANDS):
    command_clear = []        
    for com in COMMANDS:
        if com[0] == ' ':
            command_clear.append(com.replace(' ', '', 1))
        else:
            command_clear.append(com)
    return command_clear

if __name__ == '__main__':
    ip_address = str(input().replace('[','').replace(']','').replace("'",'').replace(" ",''))
    execute_command = str(input().replace('[','').replace(']','').replace("'",""))
    HOSTS = list(map(str, ip_address.split(',')))
    COMMANDS = list(map(str, execute_command.split(',')))
    
    main(HOSTS, remove_space_symbols(COMMANDS))