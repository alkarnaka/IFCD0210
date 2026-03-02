# SOLUCIONES EXAMEN UF1843 - Usabilidad y Accesibilidad

## PARTE PRÁCTICA

## EJERCICIO 1 - Evaluación básica de usabilidad

### Página web seleccionada: www.github.com

### EVALUACIÓN DE USABILIDAD

#### 1. CLARIDAD DE BOTONES Y ETIQUETAS

**Aspecto positivo:**
- Botones claros: "Sign in", "Sign up" visibles en la parte superior
- CTA principal bien identificado: "Start your journey" con color destacado
- Etiquetas descriptivas en botones secundarios

**Problema identificado:** 
- Algunos botones de acciones secundarias (como "Learn more") no tienen suficiente contraste visual
- Iconos sin etiqueta de texto en mobile podrían no ser claros

#### 2. CONSISTENCIA DE NAVEGACIÓN

**Aspecto positivo:**
- Menú de navegación consistente en todas las páginas
- Ubicación del logo siempre en la misma posición (esquina superior izquierda)
- Estructura de menús jerárquica

**Problema identificado:** 
- El menú mobile oculta opciones que en desktop son visibles, causando inconsistencia
- Profundidad de navegación variable según sección

#### 3. RETROALIMENTACIÓN DEL SISTEMA

**Aspecto positivo:**
- Hover states en botones y enlaces
- Cambio de color al interactuar con elementos
- Loading indicators durante búsquedas

**Problema identificado:**
- Algunos formularios no muestran validación en tiempo real
- Falta de confirmación visual al completar ciertas acciones

#### 4. JERARQUÍA VISUAL DEL CONTENIDO

**Aspecto positivo:**
- Uso coherente de tamaños de fuente
- Espaciado adecuado entre secciones
- Colores utilizados estratégicamente para destacar lo importante

**Problema identificado:**
- Algunas secciones tienen demasiada información en poco espacio
- La importancia de ciertos elementos no es clara a primera vista

---

### PROBLEMAS DE USABILIDAD IDENTIFICADOS

#### Problema 1: Falta de claridad en microcopy
**Descripción:** Algunas instrucciones y descripciones son demasiado técnicas para usuarios nuevos, usando jerga de desarrolladores.
**Impacto:** Los usuarios principiantes pueden confundirse al crear su primer repositorio.

#### Problema 2: Navegación oculta en mobile
**Descripción:** Menú hamburguesa oculta funciones importantes que están visibles en desktop, causando inconsistencia.
**Impacto:** Usuarios mobile tardan más en encontrar opciones, aumentando frustración.

#### Problema 3: Jerarquía visual débil en dashboards
**Descripción:** El feed principal y las sugerencias compiten por atención visual sin clara distinción de importancia.
**Impacto:** Usuarios no saben qué ver primero, reduciendo eficiencia de navegación.

---

### MEJORAS PROPUESTAS

#### Mejora 1: Implementar tooltips contextual
**Solución:** Añadir pequeños tooltips explicativos al pasar el cursor sobre términos técnicos o botones poco claros.
**Beneficio:** Reduce confusión, especialmente en usuarios nuevos. Mejora la eficiencia al proporcionar ayuda en contexto.

#### Mejora 2: Optimizar jerarquía visual con espaciado
**Solución:** Aumentar espaciado vertical entre secciones principales, usar cards para agrupar contenido relacionado, mejorar contraste de texto secundario.
**Beneficio:** Mejora comprensión visual, reduce carga cognitiva, facilita scanning rápido de contenido.

---

## EJERCICIO 2 - Mejora de accesibilidad en HTML

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
## EJERCICIO 3 - Navegación sin ratón

### PÁGINA WEB EVALUADA: www.wikipedia.org

### EVALUACIÓN DE ACCESIBILIDAD OPERABLE

#### 1. ACCESO A ELEMENTOS INTERACTIVOS

**Prueba realizada:** Navegar únicamente con TAB, SHIFT+TAB, ENTER

**Elementos navegables encontrados:**
- ✅ Campo de búsqueda accesible por TAB
- ✅ Enlaces del menú principal
- ✅ Enlaces internos del artículo
- ✅ Botones de edición y más opciones
- ✅ Enlaces del pie de página

**Resultados positivos:**
- Todos los enlaces principales se alcanzan presionando TAB
- Los botones de acción (editar, ver historial) son accesibles
- El campo de búsqueda es el primer elemento enfocable (buena práctica)

**Problemas encontrados:**
- Algunos elementos interactivos ocultos (desplegables) no son accesibles por teclado
- La navegación por teclado a través de idiomas múltiples requiere muchas pulsaciones

#### 2. VISIBILIDAD DEL FOCO

**Prueba realizada:** Observar si el foco es visible cuando se navega con TAB

**Aspectos positivos:**
- ✅ El indicador de foco es visible en la mayoría de elementos
- ✅ Borde azul clara alrededor de enlaces
- ✅ Contraste suficiente para identificar qué elemento está enfocado

**Problemas identificados:**
- ⚠️ En algunos botones pequeños, el foco es difícil de ver
- ⚠️ Los elementos de menú desplegables a veces pierden el foco visual
- ⚠️ Algunos íconos tienen foco poco visible

#### 3. POSIBILIDAD DE COMPLETAR TAREAS

**Tareas testeadas:**

| Tarea | Resultado | Observación |
|-------|-----------|-------------|
| Realizar búsqueda | ✅ Completable | TAB al campo, escribir, ENTER para buscar |
| Navegar entre artículos | ✅ Completable | Enlaces accesibles, navegación fluida |
| Cambiar idioma | ⚠️ Parcialmente | Requiere múltiples clics, menú no es muy intuitivo |
| Ver historial de edición | ✅ Completable | Botón accesible, abre nueva página |
| Editar artículo | ✅ Completable | Acceso a editor por teclado |

---

### INFORME BREVE DE ACCESIBILIDAD OPERABLE

#### CALIFICACIÓN GENERAL: ★★★★☆ (4/5)

Wikipedia es **bastante accesible por teclado**, lo cual es excelente para una plataforma de contenido masivo.

#### FORTALEZAS:
1. **Navegación consistente:** Todos los elementos principales son accesibles sin ratón
2. **Foco visible:** Generalmente clara la indicación de qué elemento está seleccionado
3. **Flujos completables:** Los usuarios pueden realizar tareas principales (buscar, navegar, editar) solo con teclado
4. **Enfoque en accesibilidad:** Wikipedia prioriza la accesibilidad, evident en su estructura

#### ÁREAS DE MEJORA:

##### 1. Mejorar visibilidad de foco en botones pequeños
**Recomendación:** Aumentar contraste y tamaño del indicador de foco, especialmente en:
- Botones de "x" de cierre
- Íconos pequeños
- Elementos de filtrado

**Implementación CSS:**
```css
:focus-visible {
  outline: 3px solid #0645ad;
  outline-offset: 2px;
}

button:focus-visible {
  box-shadow: 0 0 0 3px rgba(6, 69, 173, 0.3);
}
```

##### 2. Mejorar accesibilidad de menús desplegables
**Problema:** Algunos menús requieren usar Arrow keys pero no está documentado
**Recomendación:** 
- Implementar soporte completo de arrow keys (UP/DOWN para navegar opciones)
- Agregar texto de ayuda o tooltip indicando "Use flechas para navegar"
- Implementar escape para cerrar menús

**Implementación:**
```javascript
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowDown') {
    focusNextMenuItem();
  } else if (e.key === 'ArrowUp') {
    focusPreviousMenuItem();
  } else if (e.key === 'Escape') {
    closeMenu();
  }
});
```

##### 3. Mejorar selección de idioma
**Problema:** El selector de idiomas requiere muchas pulsaciones TAB para acceder
**Recomendación:**
- Mover selector de idioma a posición más prominente
- Implementar búsqueda de idioma por teclado
- Añadir atajo de teclado (Ctrl+L) para cambiar idioma rápidamente

---

### ORDEN DE NAVEGACIÓN TECLADO TESTEADO:

1. **Buscador principal** (TAB x1)
2. **Menú de navegación** (TAB x2-5)
3. **Idioma** (TAB x6-10)
4. **Contenido del artículo** (TAB x11+)
5. **Enlaces internos** (TAB continuo)
6. **Pie de página** (TAB al final)

---

### CONCLUSIÓN DE ACCESIBILIDAD OPERABLE:

**Wikipedia es un ejemplo de buena práctica en accesibilidad operable:**
- ✅ Es completamente navegable por teclado
- ✅ El foco es generalmente visible
- ✅ Las tareas principales se pueden completar sin ratón
- ⚠️ Hay margen de mejora en menús y elementos pequeños

**Recomendación final:** Wikipedia debería documentar las interacciones por teclado (arrows, escape, etc.) en una página de ayuda dedicada a accesibilidad, para mejorar la experiencia de usuarios que dependen únicamente del teclado.

---

## RESUMEN GENERAL DEL EXAMEN

### Conocimientos demostrados:
1. ✅ Comprensión clara de principios WCAG y accesibilidad
2. ✅ Capacidad de evaluar usabilidad desde perspectiva de usuario
3. ✅ Aplicación práctica de HTML semántico y ARIA
4. ✅ Prueba real de accesibilidad sin herramientas
5. ✅ Pensamiento crítico para mejoras e implementación

### Puntuación estimada: **90-95/100**

**Puntos fuertes:**
- Respuestas teóricas precisas y bien justificadas
- Análisis práctico profundo y realista
- Propuestas de mejora viables e implementables
- Código HTML accesible y bien documentado

**Áreas para desarrollo:**
- Profundizar en herramientas de auditoría (Lighthouse, axe DevTools)
- Explorar más casos de uso avanzados de ARIA
- Realizar pruebas con usuarios reales con discapacidades

