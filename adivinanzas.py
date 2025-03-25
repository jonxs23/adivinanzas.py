import random

#LISTA DE ADIVINANZAS Y RESPUESTAS
adivinanzas =[
    ("blanca por dentro, verde por fuera. si quieres que te lo diga, espera.","pera"),
    ("oro parece, plata no es . quien no lo adivine , bien tonto es.", "platano"),
    ("largo, largo como un tren , tiene  dientes y no es un pez.","peine"),
    ("tiene alas y no vuela, tiene ojos y no ve , tiene agua y no la bebe.","pez"),
    ("es mas  larga que la vida, mas corta que un suspiro, sin ella no hay alegria, y en la voz cobra sentido.", "la palabra")
]
puntos = 10

while 0 < puntos < 100:
    adivinanza, respuesta = random.choice(adivinanzas) #elegimos una pregunta al azar
    print(f"❓) {adivinanza}")
    respuesta_usuario = input("tu respuesta:")
    
    if respuesta_usuario == respuesta: 
        puntos += 10 #sumar puntos si es correcto
        print("✔ ¡correcto! + 10 puntos .")
    else:
        puntos -= 10 # restar puntos si es incorrecto
        print(f"✖ incorrecto. la respuesta era:{respuesta}. -10 puntos.")
        
print(f"🎯 puntos actuales: {puntos}\n")

if puntos >= 100:
    print("🎉 ¡felicidades, ganaste!🎉")
else:
    print("💀 perdiste, vuelve a intentarlo.💀")
        