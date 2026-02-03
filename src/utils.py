"""
utils.py
Funções utilitárias genéricas (I/O).
"""

import json
from pathlib import Path
from typing import Any, Dict


def read_json(path: str) -> Dict[str, Any]:
    """Lê um arquivo JSON e retorna um dicionário Python."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_text(path: str, text: str) -> None:
    """Escreve texto em um arquivo, criando diretórios se necessário."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def write_json(path: str, data: Dict[str, Any]) -> None:
    """Escreve um dicionário como JSON formatado."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )