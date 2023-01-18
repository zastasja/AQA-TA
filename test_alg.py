import builtins
import alg
import mock


""" POSITIVE TESTS """
def test_number_over_seven():
    with mock.patch.object(builtins, 'input', lambda: '8'):
        print(alg.number_over_seven())
        assert alg.number_over_seven() == "Привет"
#
# def test_name_checker():
#     with mock.patch.object(builtins, 'input', lambda: 'Вячеслав'):
#         assert alg.name_checker() == "Привет, Вячеслав"
#
# def test_aliquote_to_3():
#     with mock.patch.object(builtins, 'input', lambda: '0 2 3 4 6 9 10'):
#         assert alg.aliquote_to_3() == "3 6 9"