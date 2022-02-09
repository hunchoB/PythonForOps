#TODO: Q

if __name__ == '__main__':
    # platform = "K8s"
    # atomic_unit = "POD"
    # what_about_kubernetes = "Минимальной единицей является"
    # what_about_kubernetes = (f"Минимальной единицей {platform.replace('8', 'ubernete')} является {atomic_unit.lower()}")
    # print(what_about_kubernetes)
    # free_ram_amount = 200  # Количество свободной оперативной памяти в облачном кластере в мегабайтах
    # app_replicas = 2 # Количество реплик приложения
    # has_ram_overdraft = True # Есть ли возможность использовать дополнительную оперативную память при исчерпании лимита
    # balance = 9000  # Баланс лицевого счета в местной валюте
    # is_fail_safe = (app_replicas * 150 <= free_ram_amount) or (has_ram_overdraft and balance >= 8000)
    # print((app_replicas * 150 <= free_ram_amount) or (has_ram_overdraft and balance >= 8000))
    basic_courses = ("Docker", "Ansible", "Ceph")
    advanced_courses = ("Kubernetes База", "Kubernetes Мега")

    print((basic_courses + advanced_courses)[1::3])