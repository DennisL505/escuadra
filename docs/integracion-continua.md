# Guía de Integración Continua (CI/CD)

Este documento explica el funcionamiento de nuestro pipeline de Integración y Despliegue Continuo (CI/CD), detallando cómo fluye el código en el repositorio, los flujos de trabajo automatizados disponibles y los procedimientos de ingeniería para resolver problemas cuando las validaciones fallen.

## Workflows disponibles

El proyecto cuenta con tres flujos de trabajo automatizados en la ruta `.github/workflows/`:

| Nombre | Cuándo se activa (Trigger) | Qué hace |
|---|---|---|
| `Python CI` (`ci.yml`) | Ante cualquier `push` o `pull_request` en **cualquier rama** del repositorio (`"**"`). | Configura un entorno matriz con Python 3.10, 3.11 y 3.12. Ejecuta el linter `ruff` para análisis estático y corre la suite de pruebas unitarias con `pytest`. |
| `Security scan` (`security.yml`) | Al realizar un `push` directo en la rama `dev` o al abrir un `pull_request` apuntando a `main`. | Utiliza GitHub CodeQL para realizar un análisis estático de seguridad (SAST) buscando vulnerabilidades específicas en el código escrito en JavaScript/TypeScript. |
| `Deploy` (`deploy.yml`) | Al hacer un `push` (o un merge de PR aprobado) en la rama `main`. | Funciona como un *placeholder* preparatorio para el despliegue automático. Actualmente solo imprime un mensaje de confirmación en la consola. |

## Flujo de un PR

El ciclo de vida estándar de cualquier contribución al código sigue esta secuencia de pasos:

```text
1. 💻 Crear rama de trabajo local (siempre partiendo desde 'dev').
2. 🛠️ Realizar cambios en el código y guardar los estados mediante commits.
3. ⬆️ Subir (push) la rama local hacia el repositorio remoto en GitHub.
4. 🔄 Abrir un Pull Request (PR) en GitHub apuntando hacia la rama 'dev'.
5. 🤖 GitHub Actions intercepta el PR y ejecuta de forma automática el pipeline de CI.
6. 🚦 Evaluación del CI:
   - ❌ Si el CI falla: El autor debe inspeccionar logs, corregir en su máquina y hacer un nuevo push.
   - ✅ Si el CI pasa: El PR queda habilitado y bloqueado a la espera de aprobación humana.
7. 👁️ Revisión de código (Code Review) obligatoria por parte de los compañeros de equipo.
8. 🔀 Fusión (merge) del PR aprobado hacia la rama 'dev'.