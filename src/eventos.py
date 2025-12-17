from datetime import date, timedelta
 
def es_dia_festivo(fecha: date) -> bool:    
    """
    Función auxiliar que simula la verificación de días festivos.
    Parámetros:
        fecha: date: La fecha a verificar.
    Devuelve:
        bool: True si la fecha es un día festivo, False en caso contrario.
    """
    dias_festivos = {
        date(2026, 1, 1),   # Año Nuevo
        date(2026, 1, 6),   # Día de Reyes
        date(2026, 3, 19),  # San José
        date(2026, 5, 1),   # Día del Trabajo
        date(2026, 8, 15),  # Asunción de la Virgen
        date(2026, 10, 12), # Fiesta Nacional de España
        date(2026, 11, 1),  # Todos los Santos
        date(2026, 12, 6),  # Día de la Constitución
        date(2026, 12, 8),  # Inmaculada Concepción
        date(2026, 12, 25)  # Navidad
    }
    return fecha in dias_festivos

def es_dia_no_laborable(fecha: date) -> bool:
    if fecha.weekday() == 5 or fecha.weekday() == 6 or es_dia_festivo(fecha):
        return True
    else:
         return False

def calcular_siguiente_valida(fecha_anterior:date, intervalo_dias: int ) -> date:
    """
      Recibe la fecha de la última ocurrencia (fecha_anterior) y un intervalo en días 
      (número entero intervalo_dias). 
      Calcula la próxima fecha sumando el intervalo. Si la fecha resultante cae en un
        día no laborable, la función debe avanzar día a día hasta encontrar el siguiente
          día laborable, devolviendo esta fecha.
    """
   
    fecha_a_comprobar = fecha_anterior + timedelta(days=intervalo_dias)
    
    while es_dia_no_laborable(fecha_a_comprobar):
            fecha_a_comprobar = fecha_a_comprobar + timedelta(days=1) 
    return fecha_a_comprobar

def planificar_eventos(fecha_inicio: date, intervalo_dias: int, num_eventos: int) -> None:
    """
    Recibe una fecha_inicio para los eventos, un intervalo_dias (días entre cada dos eventos)
      y el número de eventos en total a planificar (número entero num_eventos). 
      Genera y muestra por pantalla las fechas para cada uno de los eventos. 
      Ten en cuenta que:
      - La planificación comienza con fecha_inicio. 
             Importante: si fecha_inicio cae en un día no laborable, 
             se debe ajustar al siguiente día laborable antes de contarla como el primer evento.
      - A partir de la primera fecha válida, cada evento subsiguiente se calcula utilizando la función
        calcular_siguiente_valida.
      - El formato de salida debe ser: "Evento X: YYYY-MM-DD".
    """
def planificar_eventos(fecha_inicio: date, intervalo_dias: int, num_eventos: int) -> None:
    
    # PASO 1: Ajustar la fecha inicial (NORMALIZACIÓN)
    # Si cae en festivo/finde, buscamos el primer día válido.
    # No imprimimos nada todavía, solo preparamos la fecha.
    while es_dia_no_laborable(fecha_inicio):
        # Avanzamos 1 día hasta encontrar un hueco
        fecha_inicio = fecha_inicio + timedelta(days=1)
        
    # PASO 2: Generar los eventos (BUCLE PRINCIPAL)
    # Ahora fecha_inicio es 100% segura un día laborable.
    eventos_asignados = 0
        
    while eventos_asignados < num_eventos:
        eventos_asignados += 1
        #Imprimimos el evento ACTUAL (que ya sabemos que es válido)
        print(f"Evento {eventos_asignados}: {fecha_inicio}")
        fecha_inicio = calcular_siguiente_valida(fecha_inicio, intervalo_dias)
# Descomenta para probar la función anterior
planificar_eventos(date(2026, 1, 1), 10, 5)
