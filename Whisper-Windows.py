import whisper

model = whisper.load_model("large")
print("Ingrese una ruta de archivo que quiera trasncribir: ")
inputFilePath = input()
print("Ingrese una ruta de salida para el archivo de texto transcribido: ")
outputFilePath = input()
# inputFilePath = "C:\\Users\\Hernan\\OneDrive\\Hduarte\\01 - Estudios\\Intercambio\\3 - Práctica Profesionalizante III Entrevista\\Entrevistas\\Entrevista 1\\Entrevista 1.mp4"
# outputFilePath = "C:\\Users\\Hernan\\OneDrive\\Hduarte\\01 - Estudios\\Intercambio\\3 - Práctica Profesionalizante III Entrevista\\Entrevistas\\Entrevista 1\\Entrevista 1.txt"
result = model.transcribe(inputFilePath, verbose = False)
archi = open (outputFilePath,"w")
archi.write(result["text"])  
archi.close()

print(result["text"])

