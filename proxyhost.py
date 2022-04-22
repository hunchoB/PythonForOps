# TODO:нужно осуществить 1000 обращений
# TODO:Из списка прокси необходимо составить очередь использования прокси
# TODO:если обращение было с использованием прокси, то такая прокси ставится в конец очереди и будет использована заново при следующем цикле использования
# TODO:При любой попытке использования прокси нужно вывести сообщение (вне зависимости от того, будет ли она удалена из очереди)
# TODO:После завершения работы программы необходимо вывести на экран число оставшихся в очереди прокси.
import re
from collections import Counter, deque

def main(proxy_hosts):
    
    ban_list =[]
    clear_proxy_list = []
    
    #FIXME:  Исправить говноцикл
    for proxy_host in proxy_hosts:
        ban_number = re.findall(r'\d+', proxy_host)
        for n in ban_number:
            num = int(n)
            if (num % 3 == 0) or (num % 8 == 0):
                ban_list.append(proxy_host)
                print(f"Обращение при помощи прокси {proxy_host}")
            else:
                clear_proxy_list.append(proxy_host)
    #FIXME:  Исправить говноцикл 
    
    clear_proxy_deque = deque(clear_proxy_list)
    used_proxy_counter = Counter()
    for call_count in range(0,1000):
        # print(f"call {call_count}")
        used_proxy = clear_proxy_deque.popleft()
        print(f"Было осуществлено обращение к ресурсу при помощи прокси {used_proxy}")
        used_proxy_counter[used_proxy] += 1
        clear_proxy_deque.append(used_proxy)
    
    print(used_proxy_counter)



if __name__ == '__main__':
    proxy_list = ["proxyhost1.slurm.io", "proxyhost2.slurm.io", "proxyhost3.slurm.io", "proxyhost4.slurm.io", "proxyhost5.slurm.io", "proxyhost6.slurm.io", "proxyhost7.slurm.io", "proxyhost8.slurm.io", "proxyhost9.slurm.io","proxyhost10.slurm.io","proxyhost11.slurm.io","proxyhost12.slurm.io","proxyhost13.slurm.io","proxyhost14.slurm.io","proxyhost15.slurm.io","proxyhost16.slurm.io","proxyhost17.slurm.io","proxyhost18.slurm.io","proxyhost19.slurm.io"]
    main(proxy_list)