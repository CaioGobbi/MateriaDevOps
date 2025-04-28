import pandas as pd
import pytest

# Carregar os arquivos para os testes
personal_data = pd.read_parquet('personal_data.parquet')
experimental_data = pd.read_parquet('experimental_data.parquet')

def test_personal_data_columns():
    """Testa se personal_data tem todas as colunas esperadas."""
    expected_columns = {"person_id", "gender", "age", "profession"}
    assert expected_columns.issubset(personal_data.columns)

def test_experimental_data_columns():
    """Testa se experimental_data tem todas as colunas esperadas."""
    expected_columns = {"experiment_id", "person_id", "sleep_hours", "sleep_quality", "stress_level", "steps"}
    assert expected_columns.issubset(experimental_data.columns)

def test_age_range():
    """Testa se todas as idades estão entre 0 e 120 anos."""
    assert personal_data["age"].between(0, 120).all()

def test_sleep_hours_positive():
    """Testa se todas as horas de sono são maiores que zero."""
    assert (experimental_data["sleep_hours"] > 0).all()

def test_relationship_between_tables():
    """Testa se todas as pessoas no experimental_data existem no personal_data."""
    assert experimental_data["person_id"].isin(personal_data["person_id"]).all()
