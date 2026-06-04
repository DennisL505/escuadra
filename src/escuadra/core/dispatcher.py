"""
Despachador de comandos que mapea subcomandos a funciones ejecutables
consultando dinámicamente al registry.
"""

import sys
from escuadra.core import registry


def dispatch(subcommand: str) -> int:
    """
    Despacha un subcomando a su función ejecutable correspondiente.

    Args:
        subcommand: Nombre del subcomando a ejecutar.

    Returns:
        Código de salida entero (0 para éxito).

    Examples:
        >>> dispatch("convert")
        Ejecutando conversión...
        0
        >>> dispatch("desconocido")
        Error: subcomando desconocido 'desconocido'
        1
    """
    # Obtenemos el diccionario de herramientas registradas y buscamos el comando
    tools = registry.get_tools()
    handler = tools.get(subcommand)

    if handler is None:
        print(
            f"Error: subcomando desconocido '{subcommand}'",
            file=sys.stderr,
        )
        return 1

    try:
        return handler()
    except (ImportError, ModuleNotFoundError):
        print(
            "Error: El módulo solicitado no está disponible o no existe.",
            file=sys.stderr,
        )
        return 1