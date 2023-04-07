import openai  # pip install openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table
import config
import pyowm
from os import system
import datetime


conversation_file = open("conversation.txt", "a")  # 1. Crear archivo
ciudad = "Monteria"
def main():
    openai.api_key = config.GPT_KEY
    owm = pyowm.OWM(config.OPW_KEY)
    now = datetime.datetime.now()

    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']
    status = w.get_status()


    print("💬 [bold green] PyGPT [/bold green]")
    print(f"🕥 [bold blue] {now.strftime('%H:%M:%S')} [/bold blue]")

    if "rain" in status.lower():
        print (f" Se encuentra lloviendo 🌧️⛈️🌧️ en {location} y la temperatura es de {temperature}°C")
    elif "cloud" in status.lower():
        print (f"EL clima esta nublado 🌥️🌥️🌥️ en {location} y la temperatura es de {temperature}°C")
    elif "sun" in status.lower():
        print (f"El clima es soleado 🌞 en {location} y la temperatura es de {temperature}°C")
    else:
        print (f"El clima de {location} es {status} y la temperatura es de {temperature}°C")

    table = Table("Comando", "Descripción")
    table.add_row("/exit", "Salir de la aplicación")
    table.add_row("/new", "Crear una nueva conversación")
    table.add_row("/clear", "Limpiar la Consola")

    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    
    while True:

        content = __prompt()

        if content == "/new":
            print("🆕 Nueva conversación creada")

             # 2. Guardar conversación anterior en archivo
            conversation_file.write(str(messages))
            conversation_file.write("\n\n\n\n\n\n\n\n\n\n\n")  # separador
            conversation_file.flush()

            messages = [context]
            content = __prompt()
        
        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

        if content =="/clear":
            system("clear")
            print("💬 [bold green] PyGPT [/bold green]")
            print(f"🕥 [bold blue] {now.strftime('%H:%M:%S')} [/bold blue]")
            if "rain" in status.lower():
                print (f" Se encuentra lloviendo 🌧️⛈️🌧️ en {location} y la temperatura es de {temperature}°C")
            elif "cloud" in status.lower():
                print (f"EL clima esta nublado 🌥️🌥️🌥️ en {location} y la temperatura es de {temperature}°C")
            elif "sun" in status.lower():
                print (f"El clima es soleado 🌞 en {location} y la temperatura es de {temperature}°C")
            else:
                print (f"El clima de {location} es {status} y la temperatura es de {temperature}°C")

            print(table)
            

location = (ciudad) 


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "/exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            conversation_file.close()  # cerrar archivo de conversación
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)