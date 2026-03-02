

# EJERCICIO 2 - JAVASCRIPT: Control de consumo eléctrico

### Problema
Analizar el consumo eléctrico de una semana y devolver:
1. Número de días con consumo alto (> 30 kWh)
2. Consumo total de la semana
3. Día con menor consumo

### Solución

```javascript
/**
 * Función para analizar el consumo eléctrico diario
 * @param {Array<number>} consumos - Array con consumo en kWh de cada día
 * @returns {Array<number>} [días_altos, total, mínimo]
 */
function analizarConsumo(consumos) {
    // Validación de entrada
    if (!Array.isArray(consumos) || consumos.length === 0) {
        return null; // O lanzar un error
    }

    // 1. Contar días con consumo alto (> 30 kWh)
    const diasAltos = consumos.filter(kwh => kwh > 30).length;

    // 2. Calcular consumo total
    const consumoTotal = consumos.reduce((acumulado, kwh) => acumulado + kwh, 0);

    // 3. Encontrar el mínimo consumo
    const consumoMinimo = Math.min(...consumos);

    // Retornar array con los resultados
    return [diasAltos, consumoTotal, consumoMinimo];
}

// ============================================
// PRUEBAS
// ============================================

// Datos de ejemplo del examen
const consumos = [28, 35, 22, 40, 31, 18, 25];
const resultado = analizarConsumo(consumos);

console.log('Consumos diarios:', consumos);
console.log('Resultado:', resultado);
console.log('');

// Desglose del resultado
console.log('--- ANÁLISIS DE RESULTADOS ---');
console.log('Días con consumo alto (>30 kWh):', resultado[0]); // 3
console.log('  → Días: ', consumos.map((c, i) => c > 30 ? `Día ${i+1}: ${c}kWh` : null).filter(x => x));

console.log('Consumo total de la semana:', resultado[1], 'kWh'); // 199
console.log('Consumo mínimo:', resultado[2], 'kWh'); // 18

console.log('');
console.log('✓ Resultado esperado: [3, 199, 18]');
console.log('✓ Resultado obtenido:', resultado);
console.log('✓ Test:', JSON.stringify(resultado) === JSON.stringify([3, 199, 18]) ? 'PASADO ✓' : 'FALLIDO ✗');
```


## EJERCICIO 3 - USABILIDAD Y ACCESIBILIDAD: Mejora de accesibilidad

### Código Original:
```html
<img src="grafico.png"> 
<button>X</button>
```

### Problemas encontrados:
1. ❌ Imagen sin texto alternativo (inaccesible para ciegos)
2. ❌ Botón con texto críptico "X" (confuso para lectores de pantalla)
3. ❌ Falta de semántica clara

---

### Código Mejorado - Versión Básica:

```html
<!-- Imagen accesible con alt descriptivo -->
<img src="grafico.png" alt="Gráfico de análisis de datos trimestral">

<!-- Botón accesible con aria-label -->
<button type="button" aria-label="Cerrar diálogo">
  <span aria-hidden="true">&times;</span>
</button>
```

### Código Mejorado - Versión Avanzada:

```html
<!-- Estructura con más contexto y semántica -->
<div class="dialog-container" role="dialog" 
     aria-labelledby="dialog-title" 
     aria-modal="true">
  
  <!-- Título del diálogo con ID para aria-labelledby -->
  <h2 id="dialog-title">Análisis de Datos</h2>
  
  <!-- Imagen con más contexto semántico -->
  <figure>
    <img src="grafico.png" 
         alt="Gráfico de análisis de datos trimestral con comparativa Q1 vs Q2 vs Q3">
    <figcaption>Análisis de ventas: Trimestres 1 a 3 de 2024</figcaption>
  </figure>
  
  <!-- Botón cerrar con mejores prácticas -->
  <button type="button" 
          aria-label="Cerrar diálogo de análisis" 
          class="close-btn"
          onclick="cerrarDialogo()">
    <span aria-hidden="true">&times;</span>
  </button>
</div>
```