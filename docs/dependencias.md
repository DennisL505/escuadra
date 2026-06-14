# Dependencias del Proyecto

## Dependencias de Producción

Estas dependencias son gestionadas en el archivo `requirements.txt`
| Dependencia | Versión | Propósito | ¿Crítica? | ¿Puede eliminarse? | Documentación |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **FastAPI** | 0.115.0 | Framework principal para la construcción y diseño de las APIs REST del proyecto. | Sí | No | [FastAPI Docs](https://fastapi.tiangolo.com) |
| **Uvicorn** | 0.30.0 | Servidor ASGI de alta velocidad para ejecutar y desplegar la aplicación FastAPI. | Sí | No | [Uvicorn Docs](https://www.uvicorn.org) |
| **Requests** | 2.32.3 | Biblioteca para realizar solicitudes HTTP y consumo de servicios o APIs externas. | No | No, requerida para integraciones externas. | [Requests Docs](https://requests.readthedocs.io) |

---

## Dependencias de Desarrollo

Estas dependencias son gestionadas en el archivo `requirements-dev.txt`.

| Dependencia | Versión | Propósito | ¿Crítica? | ¿Puede eliminarse? | Documentación |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Pytest** | 8.3.0 | Framework para la creación, organización y ejecución de pruebas unitarias e de integración. | Sí | No | [Pytest Docs](https://docs.pytest.org) |
| **Black** | 24.4.0 | Formateador de código determinista para asegurar la consistencia del estilo PEP 8 en el proyecto. | No | Sí, pero afectaría la estandarización del código. | [Black Docs](https://black.readthedocs.io) |

---

## Política de Dependencias

Antes de agregar una nueva dependencia al proyecto se deben cumplir estrictamente los siguientes criterios:

1. Verificar que no exista una solución ya disponible en la biblioteca estándar de Python.
2. Revisar el mantenimiento y soporte del proyecto.
3. Evaluar riesgos de seguridad.
4. Justificar claramente su uso.
5. Documentar propósito y versión.
6. Mantener actualizadas las dependencias