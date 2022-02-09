if __name__ == '__main__':
    # language = "Python"
    # position = "Ops"
    # print(f"Изучить {language} " , end="")
    # if "o" in language.lower() and not "g" in language:
    #     print("намного проще", end="")
    # else:
    #     print("проще", end=" ")
    # print(", чем сопромат")
    branch_name = input()
    is_test_completed = int(input())
    coverage_count = int(input())
    approve_count = int(input())
    is_test_coverage_ok = is_test_completed and coverage_count > 5
    is_test_approve = is_test_completed and coverage_count <= 5 and approve_count > 3

    if branch_name.lower() in ("development", "staging"):
        if is_test_coverage_ok or is_test_approve:
            print(f"Внимание! Код из {branch_name} отправлен в релиз!")
        else:
            print(f"Код из {branch_name} с результатами тесты: {is_test_completed}, coverage: {coverage_count}, approve: {approve_count} в релиз не попадает.")
    else:
        print(f"В ветке {branch_name} непроверенный код, пропускаем")
