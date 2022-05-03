class MetricsAgent:
    """Агент сбора метрик"""
    
    @staticmethod
    def calculate_seconds(value):
        """Статический метод класса, пересчитывающий значение из строки в секунды

        Args:
            value (str):  Значение периода в формате "<Число>h<Число>m<Число>s"

        Raises:
            ValueError: Исключение, возникающее, когда значения отрицательные

        Returns:
            int: Возвращает значение в секундах
        """
        to_seconds_dictionary = {'h': 3600, 'm': 60, 's': 1}
        tmp = ''
        seconds = 0
        for posittion in value:
            if posittion == "-":
                raise ValueError("This value is below ZERO!")
            else:
                if posittion.isdigit():
                    tmp += posittion
                else:
                    if posittion in to_seconds_dictionary:
                        seconds += int(tmp) * to_seconds_dictionary[posittion]
                        tmp = ''
        return seconds
    
    
    def __init__(self, server_ip: str, server_key: str, get_metrics_timeout: int, timeout_push_events: int):
        """Конструктор

        Args:
            server_ip (str): IP адрес сервера, с которого собираем метрики
            server_key (str): Ключ для подключения к серверу
            get_metrics_timeout (int): Период сбора метрик(в секундах)
            timeout_push_events (int): Период отправки событий на сервер сбора событий (в секундах)
        """
        self._server_ip = server_ip
        self.__server_key = server_key
        self.__get_metrics_timeout = get_metrics_timeout
        self._timeout_push_events = timeout_push_events
        self.counter_call_agent = 0
        self.counter_get_events = 0
        
    
    def get_events(self):
        """
        Собираем события
        :return:
        """
        print(f"Cобытия сервера {self._server_ip} собраны. Следующий сбор через {self.__get_metrics_timeout} секунд")
        self.counter_call_agent += 1
        self.counter_get_events += 1
        
    
    def push_events_to_the_metrics_server(self):
        """
        Отправляем события на удаленный сервер
        :return:
        """
        print(f"Cобытия сервера {self._server_ip} собраны отправлены на сервер сбора метрик. Следующиая отправка через {self._timeout_push_events} секунд")
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
        print(f"С сервера {self._server_ip} собрано {self.counter_get_events} событий")
    
    
    @property    
    def change_timeouts_getting_metrics(self):
        """Геттер получения таймаума сбора метрик

        Returns:
            int: Возвращает значение таймаута сбора метрик в секундах
        """
        return self.__get_metrics_timeout
    
    
    @change_timeouts_getting_metrics.setter
    def change_timeouts_getting_metrics(self, new_value):
        """Сеттер таймаута сбора метрик

        Args:
            new_value (str): Значение периода в формате "<Число>h<Число>m<Число>s"
        """
        self.__get_metrics_timeout = self.calculate_seconds(new_value)
    
    
    @property
    def change_timeouts_pushing_events(self):
        """Геттер таймаума отправки метрик

        Returns:
            int: Возвращает значение таймаута отправки метрик в секундах
        """
        return self._timeout_push_events
    
    
    @change_timeouts_pushing_events.setter
    def change_timeouts_pushing_events(self, new_value):
        """Сеттер таймаута отправки метрик на сервер

        Args:
            new_value (str): Значение периода в формате "<Число>h<Число>m<Число>s"
        """
        self._timeout_push_events = self.calculate_seconds(new_value)
        
        
class PrometheusAgent(MetricsAgent):
    """Агент сбора метрик для Prometheus

    Args:
        MetricsAgent (object): Родительский класс агента сбора метрик
    """
    def push_events_to_the_metrics_server(self):
        """
        Отправляем события на удаленный сервер от Агента Prometheus
        :return:
        """
        print(f"Cобытия сервера {self._server_ip} собраны отправлены по запросу от Prometheus")
        self.counter_call_agent += 1
        
    
    @property
    def change_timeouts_pushing_events(self):
        """Закрываем метод управления периодом отправки

        Returns:
            int: Возвращает ошибку, так как нельзя управлять периодом отправки событий
        """
        raise AttributeError( "Нельзя управлять периодом отправки событий т.к. работает в модели pull" )


class CarbonAgent(MetricsAgent):
    """Агент сбора метрик для Carbon

    Args:
        MetricsAgent (object): Родительский класс агента сбора метрик
    """
    def __init__(self, server_ip: str, server_key: str, get_metrics_timeout: int, timeout_push_events: int, carbon_server_ip: str):
        """Конструктор

        Args:
            server_ip (str): IP адрес сервера, с которого собираем метрики
            server_key (str): Ключ для подключения к серверу
            get_metrics_timeout (int): Период сбора метрик(в секундах)
            timeout_push_events (int): Период отправки событий на сервер сбора событий (в секундах)
            carbon_server_ip (str): Адрес сервера Carbon
        """
        super().__init__(server_ip, server_key, get_metrics_timeout, timeout_push_events)
        self.__carbon_server_ip = carbon_server_ip
        
        
    def push_events_to_the_metrics_server(self):
        """_summary_
        """
        print(f"Cобытия сервера {self._server_ip} собраны отправлены в Carbon. Следующая отправка через {self._timeout_push_events} секунд")
        self.counter_call_agent += 1
    
    

def main():
    # agent_one = MetricsAgent("192.168.0.1", "keykeykey", 5, 10)
    
    # print(agent_one.change_timeouts_getting_metrics)
    # agent_one.change_timeouts_getting_metrics = '1h32m14s'
    # agent_one.get_events()
    
    # print(agent_one.change_timeouts_pushing_events)
    # agent_one.change_timeouts_pushing_events = '32m14s'
    # agent_one.push_events_to_the_metrics_server()
    
    # agent_two = PrometheusAgent("192.168.0.255", "keykey", 15, 35)
    # agent_two.push_events_to_the_metrics_server()
    # print(agent_two.change_timeouts_pushing_events)
    # agent_two.change_timeouts_pushing_events = '1h32m14s'
    
    agent_three = CarbonAgent("192.168.0.0", "key", 175, 355, "1.1.1.1")
    agent_three.push_events_to_the_metrics_server()

if __name__ == '__main__':
    main()