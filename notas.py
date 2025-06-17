import json
from datetime import datetime
import os

ARCHIVO = "notas.json"


def cargar_notas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_notas(notas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(notas, f, indent=4, ensure_ascii=False)


def agregar_nota():
    titulo = input("Título de la nota: ")
    categoria = input("Categoría: ")
    contenido = input("Contenido: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    nota = {
        "titulo": titulo,
        "categoria": categoria,
        "contenido": contenido,
        "fecha": fecha
    }

    notas = cargar_notas()
    notas.append(nota)
    guardar_notas(notas)
    print("✅ Nota guardada con éxito.\n")


def ver_notas():
    notas = cargar_notas()
    if not notas:
        print("❌ No hay notas aún.\n")
        return
    for nota in notas:
        print(f"📝 {nota['titulo']} ({nota['categoria']}) - {nota['fecha']}")
        print(f"   {nota['contenido']}\n")


def menu():
    while True:
        print("\n--- Notitas Cool ---")
        print("1. Agregar nota")
        print("2. Ver notas")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            ver_notas()
        elif opcion == "3":
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción no válida.\n")


if __name__ == "__main__":
    menu()
