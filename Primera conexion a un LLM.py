import os

if os.getenv('VSCODE_RESOLVING_ENVIRONMENT'):
    print("El código se está ejecutando en el entorno de Visual Studio Code.")
else:
    print("El código no se está ejecutando en el entorno de Visual Studio Code.")

env_name = os.getenv('VIRTUAL_ENV')
if env_name:
    print(f"El entorno virtual actual es: {os.path.basename(env_name)}")
else:
    print("No se está utilizando un entorno virtual.")