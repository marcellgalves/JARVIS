from core import JarvisCore


jarvis = JarvisCore()
print("JARVIS iniciado. ")

while True:
    message:str = input("Você: ")
    if(message == "/exit"):
        print("JARVIS encerrado.")  
        break
    print(jarvis.process_message(message))

   