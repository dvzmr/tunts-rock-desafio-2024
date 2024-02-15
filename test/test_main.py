import pytest

from main import get_student_status


@pytest.mark.parametrize(
    'student_entry_approved, expected',
    [
        (['1', 'Felipe', '2', '60', '80', '90'], ['Aprovado', '0']),
        (['2', 'David', '2', '100', '100', '100'], ['Aprovado', '0']),
        (['3', 'Rodrigo', '1', '70', '70', '70'], ['Aprovado', '0']),
    ],
)
def test_get_student_status_approved(student_entry_approved, expected):
    assert get_student_status(student_entry_approved, 10) == expected


@pytest.mark.parametrize(
    'student_entry_reproved, expected',
    [
        (['4', 'Fernando', '2', '50', '50', '47'], ['Reprovado', '0']),
        (['5', 'Tiago', '2', '30', '25', '10'], ['Reprovado', '0']),
        (['6', 'Samira', '1', '0', '0', '0'], ['Reprovado', '0']),
    ],
)
def test_get_student_status_reproved(student_entry_reproved, expected):
    assert get_student_status(student_entry_reproved, 10) == expected


@pytest.mark.parametrize(
    'student_entry_final_approval, expected',
    [
        (['7', 'Shirley', '2', '70', '70', '67'], ['Exame Final', '31']),
        (['8', 'Andreia', '2', '55', '55', '60'], ['Exame Final', '43']),
        (['9', 'Pedro', '1', '50', '50', '49'], ['Exame Final', '50']),
    ],
)
def test_get_student_status_reproved_final(
    student_entry_final_approval, expected
):
    assert get_student_status(student_entry_final_approval, 10) == expected


@pytest.mark.parametrize(
    'student_entry_absent_reproving, expected',
    [
        (
            ['10', 'Matheus', '4', '100', '100', '100'],
            ['Reprovado por Falta', '0'],
        ),
        (['11', 'Lucas', '3', '40', '60', '70'], ['Reprovado por Falta', '0']),
        (['12', 'Carla', '5', '0', '0', '0'], ['Reprovado por Falta', '0']),
    ],
)
def test_get_student_status_absent_reproving(
    student_entry_absent_reproving, expected
):
    assert get_student_status(student_entry_absent_reproving, 10) == expected
