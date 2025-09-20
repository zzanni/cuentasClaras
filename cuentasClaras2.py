'''
cantidad=int(input("Cuántas personas son?: "))
lista1=[]
total=0

for i in range(cantidad):
    nombre=input("Ingrese el nombre: ")
    importe=int(input("Ingrese el importe: "))
    total+=importe
    elemento=[nombre, importe]
    lista1.append(elemento)
    
print(lista1)

print("El total del asado es de $"+str(total))

resultado=total/cantidad

print("Cada persona debe abonar $"+ str(resultado))

for i in range(cantidad):
    if resultado < lista1[i][1]:
        print(lista1[i][0]+" recibirá "+ str(lista1[i][1] - resultado))
    elif resultado > lista1[i][1]:
        print(lista1[i][0]+" devolverá "+ str(lista1[i][1] - resultado))
    elif resultado == lista1[i][1]:
        print(lista1[i][0]+" entregó el valor exacto.")

'''

#-------------------- otra forma de hacerlo -------------------
'''
import csv

# Solicitar cantidad de personas
cantidad = int(input("¿Cuántas personas son?: "))
personas = []
total = 0

# Ingreso de datos
for _ in range(cantidad):
    nombre = input("Ingrese el nombre: ")
    importe = float(input("Ingrese el importe aportado: $"))
    personas.append({"nombre": nombre, "importe": round(importe, 2)})
    total += importe

# Cálculo del promedio
promedio = round(total / cantidad, 2)

# Mostrar resumen
print("\n📋 Resumen de aportes:")
for p in personas:
    print(f"- {p['nombre']} aportó ${p['importe']}")

print(f"\n💰 Total del asado: ${round(total, 2)}")
print(f"💸 Cada persona debe abonar: ${promedio}\n")

# Cálculo de ajustes
for p in personas:
    diferencia = round(p["importe"] - promedio, 2)
    if diferencia > 0:
        print(f"✅ {p['nombre']} recibirá ${diferencia}")
    elif diferencia < 0:
        print(f"⚠️ {p['nombre']} debe devolver ${abs(diferencia)}")
    else:
        print(f"👌 {p['nombre']} aportó el monto justo.")

# Guardar en archivo CSV
with open("asado.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["Nombre", "Importe", "Ajuste"]
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for p in personas:
        diferencia = round(p["importe"] - promedio, 2)
        ajuste = (
            f"Recibe ${diferencia}" if diferencia > 0
            else f"Debe ${abs(diferencia)}" if diferencia < 0
            else "Monto justo"
        )
        writer.writerow({"Nombre": p["nombre"], "Importe": p["importe"], "Ajuste": ajuste})

print("\n📁 Los datos se guardaron en el archivo 'asado.csv'. ¡Listo para compartir!")

'''
#-------------------- otra forma de hacerlo -------------------
'''
#cantidad = int(input("Cuántas personas son?: "))
lista1 = []
total = 0

for i in range(cantidad):
    nombre = input("Ingrese el nombre: ")
    importe = int(input("Ingrese el importe: "))
    total += importe
    elemento = [nombre, importe]
    lista1.append(elemento)
   
print(lista1)
print("El total del asado es de $" + str(total))
resultado = total / cantidad
print("Cada persona debe abonar $" + str(round(resultado, 2)))

# Listas para manejar las transacciones
acreedores = []  # Personas que deben recibir dinero
deudores = []    # Personas que deben pagar dinero

print("\n--- BALANCE INDIVIDUAL ---")
# Calcular quién debe recibir y quién debe pagar
for i in range(cantidad):
    diferencia = lista1[i][1] - resultado
    if diferencia > 0:  # Pagó de más, debe recibir
        acreedores.append([lista1[i][0], round(diferencia, 2)])
        print(f"{lista1[i][0]} recibirá ${round(diferencia, 2)}")
    elif diferencia < 0:  # Pagó de menos, debe pagar
        deudores.append([lista1[i][0], round(abs(diferencia), 2)])
        print(f"{lista1[i][0]} debe agregar ${round(abs(diferencia), 2)}")
    else:  # Pagó exacto
        print(f"{lista1[i][0]} entregó el valor exacto.")

print("\n--- TRANSACCIONES ESPECÍFICAS ---")

# Realizar las transacciones
acreedor_idx = 0
deudor_idx = 0

while acreedor_idx < len(acreedores) and deudor_idx < len(deudores):
    acreedor = acreedores[acreedor_idx]
    deudor = deudores[deudor_idx]
    
    # Determinar cuánto se transfiere
    monto_transferencia = min(acreedor[1], deudor[1])
    
    print(f"{deudor[0]} le debe dar ${round(monto_transferencia, 2)} a {acreedor[0]}")
    
    # Actualizar los montos
    acreedor[1] -= monto_transferencia
    deudor[1] -= monto_transferencia
    
    # Si el acreedor ya recibió todo lo suyo, pasar al siguiente
    if acreedor[1] == 0:
        acreedor_idx += 1
    
    # Si el deudor ya pagó todo lo suyo, pasar al siguiente
    if deudor[1] == 0:
        deudor_idx += 1
'''
#-------------------- otra forma de hacerlo  para android-------------------
'''
cantidad = int(input("Cuántas personas son?: "))
lista1 = []
total = 0

for i in range(cantidad):
    nombre = input("Ingrese el nombre: ")
    importe = int(input("Ingrese el importe: "))
    total += importe
    elemento = [nombre, importe]
    lista1.append(elemento)
   
print(lista1)
print("El total del asado es de $" + str(total))
resultado = total / cantidad
print("Cada persona debe abonar $" + str(round(resultado, 2)))

# Listas para manejar las transacciones
acreedores = []  # Personas que deben recibir dinero
deudores = []    # Personas que deben pagar dinero

print("\n--- BALANCE INDIVIDUAL ---")
# Calcular quién debe recibir y quién debe pagar
for i in range(len(lista1)):  # ← AQUÍ ESTÁ EL CAMBIO CLAVE
    diferencia = lista1[i][1] - resultado
    if diferencia > 0:  # Pagó de más, debe recibir
        acreedores.append([lista1[i][0], round(diferencia, 2)])
        print(f"{lista1[i][0]} recibirá ${round(diferencia, 2)}")
    elif diferencia < 0:  # Pagó de menos, debe pagar
        deudores.append([lista1[i][0], round(abs(diferencia), 2)])
        print(f"{lista1[i][0]} debe Pagar ${round(abs(diferencia), 2)}")
    else:  # Pagó exacto
        print(f"{lista1[i][0]} entregó el valor exacto.")

print("\n--- Quien Paga a Quien ? ---")

# Realizar las transacciones
acreedor_idx = 0
deudor_idx = 0

while acreedor_idx < len(acreedores) and deudor_idx < len(deudores):
    acreedor = acreedores[acreedor_idx]
    deudor = deudores[deudor_idx]
    
    # Determinar cuánto se transfiere
    monto_transferencia = min(acreedor[1], deudor[1])
    
    print(f"{deudor[0]} debe darle ${round(monto_transferencia, 2)} a {acreedor[0]}")
    
    # Actualizar los montos
    acreedor[1] -= monto_transferencia
    deudor[1] -= monto_transferencia
    
    # Si el acreedor ya recibió todo lo suyo, pasar al siguiente
    if acreedor[1] == 0:
        acreedor_idx += 1
    
    # Si el deudor ya pagó todo lo suyo, pasar al siguiente
    if deudor[1] == 0:
        deudor_idx += 1
'''#-------------------- otra forma de hacerlo -------------------
'''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuentas Claras - División de Gastos</title>
    
    <!-- PWA Meta Tags -->
    <meta name="theme-color" content="#667eea">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="CuentasClaras">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            backdrop-filter: blur(10px);
        }

        .header {
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            padding: 30px;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            position: relative;
            z-index: 2;
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
            position: relative;
            z-index: 2;
        }

        .content {
            padding: 40px;
        }

        .step {
            margin-bottom: 30px;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 0.6s forwards;
        }

        .step:nth-child(2) { animation-delay: 0.2s; }
        .step:nth-child(3) { animation-delay: 0.4s; }
        .step:nth-child(4) { animation-delay: 0.6s; }

        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .step h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.3rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .step-number {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1rem;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }

        .input-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }

        input[type="number"], input[type="text"] {
            width: 100%;
            padding: 15px 20px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 1rem;
            transition: all 0.3s ease;
            background: white;
        }

        input[type="text"] {
            text-transform: uppercase;
        }

        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }

        .btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 16px 32px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }

        .btn:active {
            transform: translateY(-1px);
        }

        .btn-secondary {
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            box-shadow: 0 6px 20px rgba(255, 107, 107, 0.3);
        }

        .btn-secondary:hover {
            box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
        }

        .personas-container {
            display: none;
        }

        .persona-card {
            background: linear-gradient(135deg, #f8f9fa, #ffffff);
            border: 2px solid #e9ecef;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .persona-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2, #ff6b6b, #feca57);
            background-size: 300% 300%;
            animation: gradientShift 3s ease infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .persona-card:hover {
            border-color: #667eea;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transform: translateY(-5px);
        }

        .persona-inputs {
            display: flex;
            gap: 20px;
            align-items: end;
        }

        .persona-inputs > div {
            flex: 1;
        }

        .resultado {
            display: none;
            background: linear-gradient(135deg, #f8f9fa, #ffffff);
            border-radius: 20px;
            padding: 35px;
            margin-top: 35px;
            border: 3px solid #e9ecef;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        }

        .resultado h2 {
            color: #333;
            margin-bottom: 25px;
            text-align: center;
            font-size: 2rem;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .balance-section, .transacciones-section {
            margin-bottom: 30px;
        }

        .balance-section h3, .transacciones-section h3 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.4rem;
            border-bottom: 3px solid #e9ecef;
            padding-bottom: 12px;
            position: relative;
        }

        .balance-section h3::after, .transacciones-section h3::after {
            content: '';
            position: absolute;
            bottom: -3px;
            left: 0;
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }

        .balance-item {
            padding: 15px 20px;
            margin-bottom: 12px;
            border-radius: 12px;
            font-weight: 500;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .balance-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }

        .balance-item:hover::before {
            left: 100%;
        }

        .recibe {
            background: linear-gradient(135deg, #d4edda, #c3e6cb);
            color: #155724;
            border-left: 5px solid #28a745;
            box-shadow: 0 4px 15px rgba(40, 167, 69, 0.2);
        }

        .debe {
            background: linear-gradient(135deg, #f8d7da, #f5c6cb);
            color: #721c24;
            border-left: 5px solid #dc3545;
            box-shadow: 0 4px 15px rgba(220, 53, 69, 0.2);
        }

        .exacto {
            background: linear-gradient(135deg, #d1ecf1, #bee5eb);
            color: #0c5460;
            border-left: 5px solid #17a2b8;
            box-shadow: 0 4px 15px rgba(23, 162, 184, 0.2);
        }

        .transaccion {
            background: linear-gradient(135deg, #ffffff, #f8f9fa);
            border: 3px solid #667eea;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 15px;
            text-align: center;
            font-weight: 600;
            color: #333;
            font-size: 1.1rem;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
            transition: all 0.3s ease;
        }

        .transaccion:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.25);
        }

        .total-info {
            text-align: center;
            padding: 25px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
        }

        .total-info::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: float 8s ease-in-out infinite;
        }

        .total-info h3 {
            font-size: 1.6rem;
            margin-bottom: 12px;
            position: relative;
            z-index: 2;
        }

        .total-info p {
            font-size: 1.2rem;
            position: relative;
            z-index: 2;
        }

        .hidden {
            display: none;
        }

        .install-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            color: white;
            border: none;
            padding: 15px 20px;
            border-radius: 50px;
            font-weight: 600;
            box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @media (max-width: 768px) {
            .container {
                margin: 10px;
                border-radius: 15px;
            }
            
            .content {
                padding: 25px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .persona-inputs {
                flex-direction: column;
                gap: 15px;
            }

            .resultado {
                padding: 25px;
            }

            .install-button {
                bottom: 15px;
                right: 15px;
                padding: 12px 16px;
                font-size: 0.9rem;
            }
        }

        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255,255,255,.3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🍖 Cuentas Claras</h1>
            <p>División Justa de Gastos Para tu Asado o Reunion</p>
        </div>

        <div class="content">
            <div class="step">
                <h3><span class="step-number">1</span> ¿Cuántas Personas Participaran Hoy?</h3>
                <div class="input-group">
                    <label for="cantidad">Número de Personas:</label>
                    <input type="number" id="cantidad" min="2" max="20" placeholder="Ej: 5">
                </div>
                <button class="btn" onclick="crearFormulario(this)">Siguiente</button>
            </div>

            <div class="step personas-container" id="personasContainer">
                <h3><span class="step-number">2</span> Ingresa los Datos de Cada Persona</h3>
                <div id="personasForm"></div>
                <button class="btn btn-secondary" onclick="calcularDivision(this)">Calcular División</button>
            </div>

            <div class="resultado" id="resultado">
                <h2>📊 Resultados de la División</h2>
                <div id="resultadoContent"></div>
                <button class="btn" onclick="reiniciar()" style="margin-top: 25px; width: 100%;">🔄 Nueva División</button>
            </div>
        </div>
    </div>

    <script>
        let personas = [];

        function mostrarLoading(button) {
            const originalText = button.innerHTML;
            button.innerHTML = '<span class="loading"></span> Procesando...';
            button.disabled = true;
            
            setTimeout(() => {
                button.innerHTML = originalText;
                button.disabled = false;
            }, 800);
        }

        function crearFormulario(button) {
            const cantidad = parseInt(document.getElementById('cantidad').value);
            
            if (!cantidad || cantidad < 2) {
                alert('Por favor ingresa un número válido de personas (mínimo 2)');
                return;
            }

            if (cantidad > 20) {
                alert('Máximo 20 personas por división');
                return;
            }

            mostrarLoading(button);

            setTimeout(() => {
                const container = document.getElementById('personasForm');
                container.innerHTML = '';

                for (let i = 0; i < cantidad; i++) {
                    const personaCard = document.createElement('div');
                    personaCard.className = 'persona-card';
                    personaCard.style.animationDelay = `${i * 0.1}s`;
                    personaCard.innerHTML = `
                        <div class="persona-inputs">
                            <div>
                                <label>👤 Nombre:</label>
                                <input type="text" id="nombre${i}" placeholder="Ej: JUAN" required oninput="this.value = this.value.toUpperCase()">
                            </div>
                            <div>
                                <label>💰 Importe gastado ($):</label>
                                <input type="number" id="importe${i}" min="0" step="0.01" placeholder="0.00" required>
                            </div>
                        </div>
                    `;
                    container.appendChild(personaCard);
                }

                document.getElementById('personasContainer').style.display = 'block';
                document.getElementById('personasContainer').scrollIntoView({ behavior: 'smooth' });
            }, 800);
        }

        function calcularDivision(button) {
            const cantidad = parseInt(document.getElementById('cantidad').value);
            personas = [];
            let total = 0;
            let hasErrors = false;

            // Recopilar y validar datos
            for (let i = 0; i < cantidad; i++) {
                const nombre = document.getElementById(`nombre${i}`).value.trim().toUpperCase();
                const importeInput = document.getElementById(`importe${i}`);
                const importe = parseFloat(importeInput.value) || 0;

                if (!nombre) {
                    alert(`Por favor ingresa el nombre de la persona ${i + 1}`);
                    document.getElementById(`nombre${i}`).focus();
                    return;
                }

                if (importe < 0) {
                    alert('Los importes no pueden ser negativos');
                    importeInput.focus();
                    return;
                }

                personas.push({ nombre, importe });
                total += importe;
            }

            if (total === 0) {
                alert('El total no puede ser 0. Ingresa al menos un gasto.');
                return;
            }

            mostrarLoading(button);

            setTimeout(() => {
                // Calcular división
                const promedio = total / cantidad;
                const acreedores = [];
                const deudores = [];

                let resultadoHTML = `
                    <div class="total-info">
                        <h3>💰 Total: $${total.toLocaleString('es-AR', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</h3>
                        <p>Cada persona debe: $${promedio.toLocaleString('es-AR', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</p>
                    </div>

                    <div class="balance-section">
                        <h3>📋 Balance Individual</h3>
                `;

                personas.forEach(persona => {
                    const diferencia = persona.importe - promedio;
                    if (Math.abs(diferencia) < 0.01) {
                        resultadoHTML += `<div class="balance-item exacto">✅ <strong>${persona.nombre}</strong> entregó el valor exacto</div>`;
                    } else if (diferencia > 0) {
                        acreedores.push({ nombre: persona.nombre, monto: diferencia });
                        resultadoHTML += `<div class="balance-item recibe">💵 <strong>${persona.nombre}</strong> recibirá $${diferencia.toLocaleString('es-AR', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>`;
                    } else {
                        deudores.push({ nombre: persona.nombre, monto: Math.abs(diferencia) });
                        resultadoHTML += `<div class="balance-item debe">💸 <strong>${persona.nombre}</strong> debe agregar $${Math.abs(diferencia).toLocaleString('es-AR', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>`;
                    }
                });

                resultadoHTML += '</div>';

                // Calcular transacciones específicas
                if (acreedores.length > 0 && deudores.length > 0) {
                    resultadoHTML += `
                        <div class="transacciones-section">
                            <h3>🔄 Transacciones Específicas</h3>
                    `;

                    let acreedorIdx = 0;
                    let deudorIdx = 0;

                    while (acreedorIdx < acreedores.length && deudorIdx < deudores.length) {
                        const acreedor = acreedores[acreedorIdx];
                        const deudor = deudores[deudorIdx];
                        const montoTransferencia = Math.min(acreedor.monto, deudor.monto);

                        resultadoHTML += `
                            <div class="transaccion">
                                💳 <strong>${deudor.nombre}</strong> le debe dar <strong>$${montoTransferencia.toLocaleString('es-AR', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</strong> a <strong>${acreedor.nombre}</strong>
                            </div>
                        `;

                        acreedor.monto -= montoTransferencia;
                        deudor.monto -= montoTransferencia;

                        if (acreedor.monto < 0.01) acreedorIdx++;
                        if (deudor.monto < 0.01) deudorIdx++;
                    }

                    resultadoHTML += '</div>';
                } else {
                    resultadoHTML += '<div class="balance-item exacto" style="text-align: center; font-size: 1.2rem; margin-top: 20px;">🎉 ¡Todas las cuentas están perfectamente balanceadas!</div>';
                }

                document.getElementById('resultadoContent').innerHTML = resultadoHTML;
                document.getElementById('resultado').style.display = 'block';
                document.getElementById('resultado').scrollIntoView({ behavior: 'smooth' });
            }, 800);
        }

        function reiniciar() {
            document.getElementById('cantidad').value = '';
            document.getElementById('personasContainer').style.display = 'none';
            document.getElementById('resultado').style.display = 'none';
            document.getElementById('personasForm').innerHTML = '';
            personas = [];
            
            document.querySelector('.container').scrollIntoView({ behavior: 'smooth' });
        }

        // Eventos de teclado
        document.getElementById('cantidad').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                document.querySelector('.btn').click();
            }
        });

        // PWA Service Worker
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('./sw.js')
                    .then(function(registration) {
                        console.log('SW registered: ', registration);
                    }, function(registrationError) {
                        console.log('SW registration failed: ', registrationError);
                    });
            });
        }

        // PWA Install Prompt
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            
            const installButton = document.createElement('button');
            installButton.className = 'install-button';
            installButton.innerHTML = '📱 Instalar App';
            
            installButton.addEventListener('click', () => {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then((choiceResult) => {
                    if (choiceResult.outcome === 'accepted') {
                        console.log('User accepted the install prompt');
                        installButton.remove();
                    }
                    deferredPrompt = null;
                });
            });
            
            document.body.appendChild(installButton);
        });

        // Animaciones adicionales
        window.addEventListener('load', function() {
            document.body.style.opacity = '0';
            document.body.style.transform = 'translateY(20px)';
            document.body.style.transition = 'all 0.6s ease';
            
            setTimeout(() => {
                document.body.style.opacity = '1';
                document.body.style.transform = 'translateY(0)';
            }, 100);
        });
    </script>
</body>
</html>
'''

#-------------------- forma basica de hacerlo -------------------

