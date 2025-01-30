import pyautogui
import pygetwindow as gw
import time
import os

def open_notepad_and_write():
    """Abre el Bloc de notas, se asegura de que la ventana esté activa, escribe un texto y lo guarda correctamente."""
    
    # Abrir Notepad en Windows
    os.system("start notepad.exe")
    time.sleep(2)  # Esperar a que abra

    # Buscar la ventana de Notepad y activarla
    notepad_window = None
    for window in gw.getWindowsWithTitle("Bloc de notas"):  # Para Windows en español
        notepad_window = window
        break

    if notepad_window:
        notepad_window.activate()
        time.sleep(1)
        
        # Hacer clic en una posición segura dentro de Notepad para asegurar el foco
        pyautogui.click(notepad_window.left + 100, notepad_window.top + 100)
        time.sleep(1)

        # Escribir mensaje
        pyautogui.write("¡Hola! Esto es una automatización con Python y FastAPI.", interval=0.1)
        time.sleep(1)

        # Guardar archivo (Ctrl + S)
        pyautogui.hotkey("ctrl", "s")
        time.sleep(2)

        # Asegurarnos de que la ventana del 'Guardar como' esté activa
        save_as_window = None
        for window in gw.getWindowsWithTitle("Guardar como"):  # Cambiar según el idioma de tu sistema
            save_as_window = window
            break
        
        if save_as_window:
            save_as_window.activate()  # Traer el cuadro de "Guardar como" al frente
            time.sleep(1)
            
            # Escribir el nombre del archivo
            pyautogui.write("archivo_automatizado.txt", interval=0.1)
            time.sleep(1)

            # Confirmar el guardado
            pyautogui.press("enter")
            time.sleep(1)
            
            return "Tarea completada: Se abrió Notepad, se escribió el mensaje y se guardó."

        else:
            return "Error: No se pudo encontrar la ventana de 'Guardar como'."
    
    else:
        return "Error: No se pudo encontrar la ventana de Notepad."
