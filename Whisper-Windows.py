import whisper

model = whisper.load_model("large")
result = model.transcribe("C:\\Users\\Hernan\\OneDrive\\Hduarte\\01 - Estudios\\Intercambio\\3 - Práctica Profesionalizante III Entrevista\\Entrevistas\\Entrevista 2\\Entrevista 2.mp4")
archi = open ("C:\\Users\\Hernan\\OneDrive\\Hduarte\\01 - Estudios\\Intercambio\\3 - Práctica Profesionalizante III Entrevista\\Entrevistas\\Entrevista 2\\Entrevista 2.txt","w")
archi.write(result["text"])  
archi.close() 
print(result["text"])

