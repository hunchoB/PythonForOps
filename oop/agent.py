class MetricsAgent():
    """Агент сбора метрик"""
    
    def __init__(self, server_ip: str, server_key: str, get_metrics_timeout: int, timeout_push_events: int):
        """Конструктор

        Args:
            server_ip (str): IP адрес сервера, с которого собираем метрики
            server_key (str): Ключ для подключения к серверу
            get_metrics_timeout (int): Период сбора метрик(в секундах)
            timeout_push_events (int): Периодом отправки событий на сервер сбора событий (в секундах)
        """
        self.__server_ip = server_ip
        self.__server_key = server_key
        self.__get_metrics_timeout = get_metrics_timeout
        self.__timeout_push_events = timeout_push_events
        self.counter_call_agent = 0
        self.counter_get_events = 0
        
        
    def get_events(self):
        """
        Собираем события
        :return:
        """
        print(f"Cобытия сервера {self.__server_ip} собраны. Следующий сбор через {self.__get_metrics_timeout} секунд")
        self.counter_call_agent += 1
        self.counter_get_events += 1
        
    
    def push_events_to_the_metrics_server(self):
        """
        Отправляем события на удаленный сервер
        :return:
        """
        print(f"Cобытия сервера {self.__server_ip} собраны отправлены на сервер сбора метрик. Следующиая отправка через {self.__timeout_push_events} секунд")
        self.counter_call_agent += 1

        
    def reset_agent_cash(self):
        """
        Очищаем кэш агента сбора метрик
        :return:
        """
        print(f"Метод сборки событий был вызван {self.counter_call_agent} раз")
        self.counter_call_agent = 0
        print(f"Кеш агента был очищен. Сейчас его значение равно {self.counter_call_agent}")
        
        
    def get_info_about_count_got_events(self):
        """
        Получаем информацию о том, сколько событий было собрано
        :return:
        """
        print(f"С сервера {self.__server_ip} собрано {self.counter_get_events} событий")
        


def main():
    agent_one = MetricsAgent("192.168.0.1", "keykeykey", 5, 10)
    agent_one.get_events()
    agent_one.get_events()
    agent_one.get_events()
    agent_one.push_events_to_the_metrics_server()
    # agent_one.reset_agent_cash()
    agent_one.get_info_about_count_got_events()


if __name__ == '__main__':
    main()
    